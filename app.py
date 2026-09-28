"""Vigila la carpeta de Descargas y muestra cada archivo nuevo, resumido por Claude, en una página local."""

import json
import os
import threading
import time
import uuid
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from flask import Flask, jsonify, render_template, send_file  # noqa: E402
from watchdog.events import FileSystemEventHandler  # noqa: E402
from watchdog.observers import Observer  # noqa: E402

import analyzer  # noqa: E402

WATCH_FOLDER = Path(os.getenv("WATCH_FOLDER") or Path.home() / "Downloads").expanduser()
PORT = int(os.getenv("PORT", "5000"))
DATA_FILE = Path(__file__).parent / "historial.json"

# Archivos temporales que crean los navegadores mientras la descarga está en curso.
TEMP_SUFFIXES = {".crdownload", ".part", ".tmp", ".download", ".partial"}

app = Flask(__name__)
lock = threading.Lock()
seen_paths: set[str] = set()


def load_history() -> list[dict]:
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return []


history = load_history()


def save_history() -> None:
    DATA_FILE.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")


def update_entry(entry_id: str, **changes) -> None:
    with lock:
        for entry in history:
            if entry["id"] == entry_id:
                entry.update(changes)
                break
        save_history()


def wait_until_complete(path: Path, timeout: float = 120) -> bool:
    """Espera a que el archivo deje de crecer (descarga terminada)."""
    last_size = -1
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            size = path.stat().st_size
        except FileNotFoundError:
            return False
        if size == last_size and size > 0:
            return True
        last_size = size
        time.sleep(1)
    return path.exists()


def process(path: Path) -> None:
    if not wait_until_complete(path):
        return

    entry = {
        "id": uuid.uuid4().hex,
        "nombre": path.name,
        "ruta": str(path),
        "tipo": analyzer.file_kind(path),
        "tamano": path.stat().st_size,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "analizando",
        "resumen": "",
    }
    with lock:
        history.insert(0, entry)
        save_history()
    print(f"[+] Nueva descarga: {path.name} — analizando con Claude...")

    try:
        summary = analyzer.analyze(path)
        update_entry(entry["id"], estado="listo", resumen=summary)
        print(f"[✓] Listo: {path.name}")
    except Exception as exc:  # noqa: BLE001 — mostramos cualquier error en la página
        update_entry(entry["id"], estado="error", resumen=str(exc))
        print(f"[x] Error con {path.name}: {exc}")


def handle(path_str: str) -> None:
    path = Path(path_str)
    if path.suffix.lower() in TEMP_SUFFIXES or path.name.startswith((".", "~$")):
        return
    with lock:
        if path_str in seen_paths:
            return
        seen_paths.add(path_str)
    threading.Thread(target=process, args=(path,), daemon=True).start()


class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            handle(event.src_path)

    def on_moved(self, event):
        # Chrome descarga como "archivo.crdownload" y al terminar lo renombra.
        if not event.is_directory:
            handle(event.dest_path)


@app.route("/")
def index():
    return render_template("index.html", carpeta=str(WATCH_FOLDER))


@app.route("/api/archivos")
def api_files():
    with lock:
        return jsonify(history)


@app.route("/api/archivos/<entry_id>/ver")
def view_file(entry_id):
    with lock:
        entry = next((e for e in history if e["id"] == entry_id), None)
    if not entry or not Path(entry["ruta"]).exists():
        return "Archivo no encontrado", 404
    return send_file(entry["ruta"])


@app.route("/api/archivos/<entry_id>/reanalizar", methods=["POST"])
def reanalyze(entry_id):
    with lock:
        entry = next((e for e in history if e["id"] == entry_id), None)
    if not entry or not Path(entry["ruta"]).exists():
        return jsonify({"error": "Archivo no encontrado"}), 404
    update_entry(entry_id, estado="analizando", resumen="")

    def run():
        try:
            update_entry(entry_id, estado="listo", resumen=analyzer.analyze(Path(entry["ruta"])))
        except Exception as exc:  # noqa: BLE001
            update_entry(entry_id, estado="error", resumen=str(exc))

    threading.Thread(target=run, daemon=True).start()
    return jsonify({"ok": True})


@app.route("/api/archivos/<entry_id>", methods=["DELETE"])
def delete_entry(entry_id):
    with lock:
        history[:] = [e for e in history if e["id"] != entry_id]
        save_history()
    return jsonify({"ok": True})


def main():
    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit("Falta ANTHROPIC_API_KEY. Copiá .env.example a .env y poné tu clave.")
    if not WATCH_FOLDER.is_dir():
        raise SystemExit(f"La carpeta a vigilar no existe: {WATCH_FOLDER}")

    observer = Observer()
    observer.schedule(DownloadHandler(), str(WATCH_FOLDER), recursive=False)
    observer.start()
    print(f"Vigilando: {WATCH_FOLDER}")
    print(f"Abrí http://localhost:{PORT} en tu navegador")
    try:
        app.run(host="127.0.0.1", port=PORT, debug=False)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
