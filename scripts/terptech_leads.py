"""Limpia y prioriza una exportación de Google Maps (Outscraper, Apify u otra) de smoke shops.

Uso:
    python scripts/terptech_leads.py ENTRADA.csv [SALIDA.csv]

Salida por defecto: TERPTECH/mayoristas/leads.csv
- Se queda sólo con smoke / tobacco / vape / head shops.
- Saca duplicados (por email, sitio web o teléfono) y los cerrados.
- Calcula `popularidad` (0-4) según rating y reseñas, y el `tier` (A/B/C).
- Arma `detalle_real`, el dato verificado para personalizar el primer mail.
Nunca manda nada: sólo prepara la lista.
"""
import csv
import re
import sys
from pathlib import Path

SALIDA_DEFAULT = Path("TERPTECH/mayoristas/leads.csv")
RUBROS = re.compile(r"smoke|tobacco|vape|vapor|head ?shop|cbd|hookah|cigar", re.I)
EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)

# Nombres de columna habituales en las distintas exportaciones de Google Maps
ALIAS = {
    "nombre": ["name", "title", "business_name"],
    "rubro": ["category", "type", "categories", "categoryName", "subtypes"],
    "ciudad": ["city"],
    "estado_us": ["state", "us_state", "state_code"],
    "direccion": ["full_address", "address", "street"],
    "telefono": ["phone", "phone_number", "phoneUnformatted"],
    "web": ["site", "website", "url"],
    "email": ["email", "email_1", "emails", "email_address"],
    "rating": ["rating", "totalScore", "stars"],
    "resenas": ["reviews", "reviews_count", "reviewsCount", "user_ratings_total"],
    "instagram": ["instagram", "company_instagram"],
    "cerrado": ["business_status", "permanentlyClosed", "closed"],
}

COLUMNAS = [
    "tier", "popularidad", "nombre", "rubro", "ciudad", "estado_us", "direccion", "telefono",
    "web", "email", "instagram", "rating", "resenas", "detalle_real",
    "etapa", "toques", "ultimo_contacto", "respuestas", "puntaje_muestra", "notas",
]


def campo(fila, clave):
    for alias in ALIAS[clave]:
        for col, valor in fila.items():
            if col and col.strip().lower() == alias.lower() and valor:
                return valor.strip()
    return ""


def numero(texto):
    try:
        return float(str(texto).replace(",", ""))
    except ValueError:
        return 0.0


def popularidad(rating, resenas):
    puntos = 0
    if rating >= 4.3:
        puntos += 1
    if resenas >= 50:
        puntos += 1
    if resenas >= 150:
        puntos += 1
    if resenas >= 400:
        puntos += 1
    return puntos


def normalizar(fila):
    lead = {c: campo(fila, c) for c in ALIAS}
    lead["email"] = lead["email"].split(",")[0].strip().lower()
    if lead["email"] and not EMAIL.match(lead["email"]):
        lead["email"] = ""
    rating, resenas = numero(lead["rating"]), int(numero(lead["resenas"]))
    lead["popularidad"] = popularidad(rating, resenas)
    lead["tier"] = "A" if lead["popularidad"] >= 3 else "B" if lead["popularidad"] >= 2 else "C"
    if rating and resenas:
        lead["detalle_real"] = f"{lead['nombre']} has {rating:.1f} stars from {resenas} reviews in {lead['ciudad'] or 'town'}"
    else:
        lead["detalle_real"] = f"{lead['nombre']} came up as a go-to shop in {lead['ciudad'] or 'your area'}"
    lead.update(etapa="nuevo", toques="0", ultimo_contacto="", respuestas="0", puntaje_muestra="", notas="")
    return lead


def procesar(entrada, salida):
    with open(entrada, newline="", encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))

    vistos, leads = set(), []
    descartes = {"rubro": 0, "cerrado": 0, "duplicado": 0}
    for fila in filas:
        lead = normalizar(fila)
        if not RUBROS.search(f"{lead['rubro']} {lead['nombre']}"):
            descartes["rubro"] += 1
            continue
        if re.search(r"closed|true", lead["cerrado"], re.I) and not re.search(r"operational", lead["cerrado"], re.I):
            descartes["cerrado"] += 1
            continue
        claves = {k for k in (lead["email"], lead["web"].lower().rstrip("/"), re.sub(r"\D", "", lead["telefono"])) if k}
        if claves & vistos:
            descartes["duplicado"] += 1
            continue
        vistos |= claves
        leads.append(lead)

    leads.sort(key=lambda l: (-l["popularidad"], -int(numero(l["resenas"]))))
    salida.parent.mkdir(parents=True, exist_ok=True)
    with open(salida, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNAS, extrasaction="ignore")
        w.writeheader()
        w.writerows(leads)

    con_email = sum(1 for l in leads if l["email"])
    por_tier = {t: sum(1 for l in leads if l["tier"] == t) for t in "ABC"}
    print(f"Entrada: {len(filas)} filas · descartes: {descartes}")
    print(f"Leads: {len(leads)} · con email: {con_email} · tiers: {por_tier}")
    print(f"Guardado en {salida}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    procesar(Path(sys.argv[1]), Path(sys.argv[2]) if len(sys.argv) > 2 else SALIDA_DEFAULT)
