"""Mudanza de un vault de Obsidian a la carpeta Trabajo/.

Uso:
    python scripts/migrar_obsidian.py RUTA_AL_VAULT            # muestra el plan (no copia nada)
    python scripts/migrar_obsidian.py RUTA_AL_VAULT --aplicar  # copia los archivos

RUTA_AL_VAULT puede ser una carpeta o un .zip del vault.

Cada nota .md se clasifica por su ruta original y su contenido según REGLAS
(la primera que coincide gana). Lo que no coincide va a Trabajo/_inbox/.
Los adjuntos (imágenes, PDF) van junto a las notas en una carpeta adjuntos/.
No se pisa ningún archivo existente: si el nombre ya existe se agrega un sufijo.
"""

import argparse
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

DESTINO = Path(__file__).resolve().parent.parent / "Trabajo"

# (destino relativo a Trabajo/, palabras clave). Orden = prioridad: lo más
# específico (productos) antes que lo general (ecosistemas).
REGLAS = [
    ("Amazon/Kina", ["kina"]),
    ("Amazon/Avie", ["avie"]),
    ("Amazon/_comun", ["amazon", "fba", "asin", "seller central", "ppc", "acos", "helium"]),
    ("Etsy/_comun", ["etsy"]),
    ("Paginas-Web/_comun", ["shopify", "wordpress", "dtc", "dominio", "landing", "web"]),
]

IGNORAR = {".obsidian", ".trash", ".git"}
ADJUNTOS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".csv", ".xlsx"}


def clasificar(ruta_rel: Path, texto: str) -> str:
    # Gana la regla más específica (orden de REGLAS); dentro de cada regla se
    # mira primero la ruta (carpetas + nombre) y después el contenido.
    ruta, cuerpo = str(ruta_rel).lower(), texto.lower()
    for destino, claves in REGLAS:
        for fuente in (ruta, cuerpo):
            if any(re.search(rf"\b{re.escape(c)}\b", fuente) for c in claves):
                return destino
    return "_inbox"


def destino_libre(ruta: Path, reservados: set) -> Path:
    candidato, n = ruta, 2
    while candidato.exists() or candidato in reservados:
        candidato = ruta.with_name(f"{ruta.stem} ({n}){ruta.suffix}")
        n += 1
    reservados.add(candidato)
    return candidato


def migrar(vault: Path, aplicar: bool) -> None:
    archivos = [
        p for p in vault.rglob("*")
        if p.is_file() and not IGNORAR & set(p.relative_to(vault).parts)
    ]
    notas = [p for p in archivos if p.suffix.lower() == ".md"]
    adjuntos = [p for p in archivos if p.suffix.lower() in ADJUNTOS]

    plan, reservados, conteo = [], set(), {}
    for nota in notas:
        rel = nota.relative_to(vault)
        carpeta = clasificar(rel, nota.read_text(encoding="utf-8", errors="ignore"))
        conteo[carpeta] = conteo.get(carpeta, 0) + 1
        plan.append((nota, destino_libre(DESTINO / carpeta / nota.name, reservados)))

    # Un adjunto va a la carpeta de la primera nota que lo menciona ([[img.png]] o ![](img.png)).
    destino_de = {}
    for nota, dest in plan:
        texto = nota.read_text(encoding="utf-8", errors="ignore")
        for adj in adjuntos:
            if adj.name in texto and adj not in destino_de:
                destino_de[adj] = dest.parent / "adjuntos"
    for adj in adjuntos:
        carpeta = destino_de.get(adj, DESTINO / "_inbox" / "adjuntos")
        plan.append((adj, destino_libre(carpeta / adj.name, reservados)))

    for origen, dest in plan:
        print(f"{origen.relative_to(vault)}  ->  {dest.relative_to(DESTINO.parent)}")
    print("\nNotas por carpeta:")
    for carpeta, n in sorted(conteo.items()):
        print(f"  {carpeta}: {n}")
    print(f"  adjuntos: {len(adjuntos)}")

    if not aplicar:
        print("\nPlan solamente. Corré de nuevo con --aplicar para copiar.")
        return
    for origen, dest in plan:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origen, dest)
    print(f"\nCopiados {len(plan)} archivos a {DESTINO}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("vault", type=Path, help="carpeta o .zip del vault de Obsidian")
    parser.add_argument("--aplicar", action="store_true", help="copiar de verdad (por defecto solo muestra el plan)")
    args = parser.parse_args()

    if not args.vault.exists():
        sys.exit(f"No existe: {args.vault}")
    if args.vault.suffix.lower() == ".zip":
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(args.vault) as z:
                z.extractall(tmp)
            migrar(Path(tmp), args.aplicar)
    else:
        migrar(args.vault, args.aplicar)


if __name__ == "__main__":
    main()
