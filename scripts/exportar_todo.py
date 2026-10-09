"""Junta todo el trabajo (carpetas de producto + Trabajo/) en un solo Markdown (foto del momento, para pasarlo a otra sesión).

Uso: python scripts/exportar_todo.py [SALIDA]   (por defecto Trabajo/_inbox/TODO_TRABAJO_<fecha>.md)
"""

import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TRABAJO = RAIZ
IGNORAR = {".git", "scripts", "templates"}
FUERA = {"README.md"}  # README de la app de descargas
PRIMERO = ["CLAUDE.md", "ESTADO.md"]  # dentro de cada carpeta, estos van antes que el resto


def orden(p: Path):
    rel = p.relative_to(TRABAJO)
    nombre = rel.name
    return (str(rel.parent) != ".", str(rel.parent).lower(),
            PRIMERO.index(nombre) if nombre in PRIMERO else len(PRIMERO), nombre.lower())


def main() -> None:
    salida = Path(sys.argv[1]) if len(sys.argv) > 1 else TRABAJO / "Trabajo" / "_inbox" / f"TODO_TRABAJO_{date.today()}.md"
    archivos = sorted(
        (p for p in TRABAJO.rglob("*") if p.is_file() and p.suffix in {".md", ".csv"}
         and not IGNORAR & set(p.relative_to(TRABAJO).parts) and str(p.relative_to(TRABAJO)) not in FUERA
         and p.resolve() != salida.resolve() and not p.name.startswith("TODO_TRABAJO_")),
        key=orden,
    )
    partes = [
        f"# TODO TRABAJO — foto del {date.today()}",
        "",
        "> Archivo generado con `scripts/exportar_todo.py`: junta en uno solo todos los archivos de trabajo del repo.",
        "> **No editar acá.** La versión que manda es cada archivo en su carpeta; esto es sólo para leer o pasar a otra sesión.",
        "> Cada sección empieza con `## 📄 <ruta>` = el archivo original.",
        "",
        "## Índice",
        *[f"- `{p.relative_to(TRABAJO)}`" for p in archivos],
        "",
    ]
    for p in archivos:
        texto = p.read_text(encoding="utf-8").rstrip()
        if p.suffix == ".csv":
            texto = f"```csv\n{texto}\n```"
        partes += ["---", "", f"## 📄 `{p.relative_to(TRABAJO)}`", "", texto, ""]
    salida.write_text("\n".join(partes) + "\n", encoding="utf-8")
    print(f"{len(archivos)} archivos → {salida.relative_to(RAIZ)} ({salida.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
