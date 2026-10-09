"""Cola de envíos de TerpTech: decide a quién le toca el próximo mail y registra lo enviado.

Regla de Santi (2026-10-08): primero el toque 1 a TODA la lista; recién después el toque 2 al primero,
y así hasta 6 toques por tienda o hasta vender el stock.

Uso:
    python scripts/terptech_cola.py siguiente [N]              -> próximos N leads (default 10) en JSON
    python scripts/terptech_cola.py enviado EMAIL THREAD_ID    -> suma 1 toque y guarda el hilo
    python scripts/terptech_cola.py etapa EMAIL ETAPA [NOTA]   -> respondio / calificado / baja / descartado / ...
    python scripts/terptech_cola.py resumen                    -> embudo y avance
"""
import csv
import json
import sys
from datetime import date, datetime
from pathlib import Path

LEADS = Path("TERPTECH/mayoristas/leads.csv")
MAX_TOQUES = 6
DIAS_ENTRE_TOQUES = 3
# Etapas en las que la secuencia automática se frena (la conversación sigue a mano o terminó)
FUERA_DE_COLA = {"respondio", "calificando", "calificado", "muestra_ofrecida", "muestra_enviada",
                 "pedido", "cliente", "baja", "descartado", "rebote"}
CAMPOS_EXTRA = ["toques", "ultimo_contacto", "thread_id", "etapa", "notas"]


def leer():
    with open(LEADS, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    campos = list(filas[0].keys()) if filas else []
    for c in CAMPOS_EXTRA:
        if c not in campos:
            campos.append(c)
    for f_ in filas:
        for c in CAMPOS_EXTRA:
            f_.setdefault(c, "")
        f_["toques"] = f_["toques"] or "0"
        f_["etapa"] = f_["etapa"] or "nuevo"
    return filas, campos


def guardar(filas, campos):
    with open(LEADS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)


def dias_desde(fecha):
    if not fecha:
        return 999
    return (date.today() - datetime.strptime(fecha, "%Y-%m-%d").date()).days


def siguiente(n):
    filas, _ = leer()
    candidatos = [
        f for f in filas
        if f.get("email") and f["etapa"] not in FUERA_DE_COLA
        and int(f["toques"]) < MAX_TOQUES and dias_desde(f["ultimo_contacto"]) >= DIAS_ENTRE_TOQUES
    ]
    # Menos toques primero (así la lista entera recibe el toque 1 antes que nadie reciba el 2),
    # y dentro del mismo toque, el contacto más viejo primero.
    candidatos.sort(key=lambda f: (int(f["toques"]), f["ultimo_contacto"] or "0000"))
    salida = [{k: f.get(k, "") for k in ("nombre", "email", "ciudad", "estado_us", "tipo", "detalle_real",
                                          "toques", "thread_id")} | {"toque_a_enviar": int(f["toques"]) + 1}
              for f in candidatos[:n]]
    print(json.dumps(salida, ensure_ascii=False, indent=1))


def buscar(filas, email):
    for f in filas:
        if f.get("email", "").lower() == email.lower():
            return f
    sys.exit(f"No existe {email} en {LEADS}")


def enviado(email, thread_id):
    filas, campos = leer()
    f = buscar(filas, email)
    f["toques"] = str(int(f["toques"]) + 1)
    f["ultimo_contacto"] = date.today().isoformat()
    f["thread_id"] = thread_id or f["thread_id"]
    if f["etapa"] == "nuevo":
        f["etapa"] = "contactado"
    guardar(filas, campos)
    print(f"{email}: toque {f['toques']}")


def etapa(email, nueva, nota=""):
    filas, campos = leer()
    f = buscar(filas, email)
    f["etapa"] = nueva
    if nota:
        f["notas"] = (f["notas"] + " | " if f["notas"] else "") + f"{date.today()}: {nota}"
    guardar(filas, campos)
    print(f"{email}: {nueva}")


def resumen():
    filas, _ = leer()
    con_email = [f for f in filas if f.get("email")]
    por_etapa, por_toque = {}, {}
    for f in con_email:
        por_etapa[f["etapa"]] = por_etapa.get(f["etapa"], 0) + 1
        por_toque[f["toques"]] = por_toque.get(f["toques"], 0) + 1
    enviados = sum(int(f["toques"]) for f in con_email)
    print(f"Leads con email: {len(con_email)} · mails enviados en total: {enviados}")
    print("Por etapa:", dict(sorted(por_etapa.items())))
    print("Por cantidad de toques:", dict(sorted(por_toque.items())))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "siguiente":
        siguiente(int(args[0]) if args else 10)
    elif cmd == "enviado":
        enviado(args[0], args[1] if len(args) > 1 else "")
    elif cmd == "etapa":
        etapa(args[0], args[1], " ".join(args[2:]))
    elif cmd == "resumen":
        resumen()
    else:
        sys.exit(__doc__)
