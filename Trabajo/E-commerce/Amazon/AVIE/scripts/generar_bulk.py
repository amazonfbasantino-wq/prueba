"""Genera el archivo masivo (bulk) de Amazon Ads para crear las campañas de campanas-octubre.csv.
Uso (desde la carpeta AVIE): python scripts/generar_bulk.py  -> AVIE_OCT_bulk_carga.xlsx
"""
import csv, openpyxl

H = ['Product','Entity','Operation','Campaign ID','Ad Group ID','Portfolio ID','Ad ID','Keyword ID','Product Targeting ID',
     'Campaign Name','Ad Group Name','Start Date','End Date','Targeting Type','State','Daily Budget','SKU',
     'Ad Group Default Bid','Bid','Keyword Text','Native Language Keyword','Native Language Locale','Match Type',
     'Bidding Strategy','Placement','Percentage','Product Targeting Expression']
SKU, INICIO = 'avie 011', '20261009'
# campaña: (USD/día, tipo, puja por defecto, % extra primera posición)
# Nivel 1 de la escalera (plan-octubre-expansion.md §2): 55 USD/día nuevas + 5 de SP-(Substitutes) y SP-(CloseMatch) = 60
CAMPS = {'AVIE_OCT_EMPUJE_EX': (20, 'Manual', 0.90, 60), 'AVIE_OCT_PROBADAS_EX': (12, 'Manual', 0.85, 30),
         'AVIE_OCT_QUICKWIN_EX': (10, 'Manual', 0.75, 0), 'AVIE_OCT_RIVALES_EX': (3, 'Manual', 0.60, 0),
         'AVIE_OCT_ASIN': (4, 'Manual', 0.65, 0), 'AVIE_OCT_DESCUBRIR_PH': (3, 'Manual', 0.55, 0),
         'AVIE_OCT_AUTO_COSECHA': (3, 'Auto', 0.40, 0)}
import sys
SOLO = sys.argv[1:]  # ej.: python scripts/generar_bulk.py AVIE_OCT_EMPUJE_EX  -> sólo esas campañas
AUTO = {'Coincidencia cercana (close match)': 'close-match', 'Coincidencia amplia (loose match)': 'loose-match',
        'Sustitutos (substitutes)': 'substitutes', 'Complementos (complements)': 'complements'}
MATCH = {'Exacta': 'exact', 'Frase': 'phrase', 'Negativa exacta': 'negativeExact', 'Negativa frase': 'negativePhrase'}

filas = list(csv.DictReader(open('campanas-octubre.csv', encoding='utf-8')))
out = []

def fila(**kw):
    r = dict.fromkeys(H, ''); r.update(Product='Sponsored Products', Operation='Create'); r.update(kw)
    out.append([r[h] for h in H])

for c, (budget, tipo, puja, top) in CAMPS.items():
    if SOLO and c not in SOLO:
        continue
    ag = c.lower()
    base = {'Campaign ID': c, 'Ad Group ID': ag, 'State': 'enabled'}
    fila(Entity='Campaign', **{'Campaign ID': c, 'Campaign Name': c, 'Start Date': INICIO, 'Targeting Type': tipo,
                              'State': 'enabled', 'Daily Budget': budget, 'Bidding Strategy': 'Dynamic bids - down only'})
    if top:
        fila(Entity='Bidding Adjustment', **{'Campaign ID': c, 'Placement': 'Placement Top', 'Percentage': top})
    fila(Entity='Ad Group', **base, **{'Ad Group Name': ag, 'Ad Group Default Bid': puja})
    fila(Entity='Product Ad', **base, SKU=SKU)
    for r in filas:
        if r['Campaña'] != c:
            continue
        k, m, b = r['Keyword o ASIN'], r['Concordancia'], r['Puja inicial USD']
        if m in ('Exacta', 'Frase'):
            fila(Entity='Keyword', **base, Bid=b, **{'Keyword Text': k, 'Match Type': MATCH[m]})
        elif m in ('Negativa exacta', 'Negativa frase'):
            fila(Entity='Negative Keyword', **base, **{'Keyword Text': k, 'Match Type': MATCH[m]})
        elif m == 'Producto (ASIN)':
            fila(Entity='Product Targeting', **base, Bid=b, **{'Product Targeting Expression': f'asin="{k}"'})
        elif m == 'ASIN negativo':
            fila(Entity='Negative Product Targeting', **base, **{'Product Targeting Expression': f'asin="{k}"'})
        elif m == 'Automática':
            fila(Entity='Product Targeting', **base, Bid=b, **{'Product Targeting Expression': AUTO[k]})
        elif m == 'Automática (pausada)':
            fila(Entity='Product Targeting', **{**base, 'State': 'paused'}, Bid=puja, **{'Product Targeting Expression': AUTO[k]})

wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'Sponsored Products Campaigns'
ws.append(H)
for o in out:
    ws.append(o)
nombre = 'AVIE_OCT_bulk_' + ('_'.join(x.replace('AVIE_OCT_', '').lower() for x in SOLO) if SOLO else 'carga') + '.xlsx'
wb.save(nombre)
print(f'{len(out)} filas -> {nombre}')
