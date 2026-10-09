# REFLEX — Protocolo DELTA-FIRST y fuentes

> Los archivos fuente (CSV de Amazon, Helium) viven en el vault **PROYECTOS 100K** (`90_INBOX/MASTER_IMPORTS/AMAZON/SOURCES/`) y en Descargas, no en esta carpeta.

## DELTA-FIRST (regla permanente desde 15-sep)

```
LAST VERIFIED BASELINE → NEW DATA ONLY → CALCULATE DELTA → FLAG MATERIAL CHANGES → DECIDE
```
**Nunca:** día nuevo → re-analizar todo el histórico.

El histórico completo se reabre **sólo** por: (1) contradicción entre fuentes · (2) anomalía material · (3) cambio de estrategia · (4) Santi pide auditoría completa.

### Umbrales de materialidad

| Métrica | Se reporta si |
|---|---|
| Spend / día | **±15 %** |
| CPC | **±10 %** |
| CVR | **±20 % relativo** |
| ACoS / TACoS | **±5 puntos** |
| Rank orgánico core | **±3 posiciones** |
| Precio propio o de competidor | **cualquier cambio** |
| Rating / reviews de competidor | **±0,1 / ±10 %** |
| BSR de competidor | **±25 %** |
| Contribución / día | **±US$ 10** |

Por debajo del umbral: no se menciona.

### Reglas de procesamiento
- Los CSV crudos **se procesan con código (python/pandas), nunca leyendo filas**. Al modelo le llegan agregados.
- Un export nuevo se compara contra el último dato y **sólo el delta entra al contexto**.
- Si un dominio no cambió: **`NO ANALYSIS`**.
- Al cerrar una revisión se actualiza `ESTADO.md` con fecha y valores nuevos; no se crea un archivo por día.

### Formato de una revisión
```
WHAT CHANGED
ANOMALIES
ACTION REQUIRED
NO ACTION
```
Sin recapitular el histórico.

## Fuentes primarias (en PROYECTOS 100K)

| Archivo | Ventana | Qué contiene |
|---|---|---|
| `SP_search_term_report_REFLEX_2026-08-01_2026-09-03.csv` | W1 · 34 d | 1.672 filas, 1.357 términos, 110 campañas. Economía por término |
| `REFLEX_TARGETING_BIDS_EXPORT_2026-09-07.csv` | W2 | 2.620 filas. Pujas, presupuestos, targets. Sin placements ni negativos |
| `REFLEX_SP_SEARCH_TERM_DAILY_2026-08-08_2026-09-06.xlsx` | W4 · 30 d | Única fuente con evolución diaria de PPC |
| `REFLEX_BUSINESS_REPORT_DAILY_2026-04-10_2026-09-04.csv` | 148 d | Sesiones, unidades, CVR, ASP diarios. Contiene la ruptura del 19→20 ago |
| `REFLEX_BUSINESS_REPORT_BY_ASIN_2026-09-07.csv` | ventana sin declarar | Unidades y precio por ASIN |
| `REFLEX_TRANSACCIONES_2026-08-16_2026-09-08.csv` | W7 | Settlement. Valida la fórmula de fees |
| `Transacciones … 1_5_2026 a 16_9_2026.csv` | 1-may → 16-sep | Contiene el removal order |
| `REFLEX_NEGATIVE_CANDIDATES.csv` | W1 | 79 términos ≥US$3 y cero órdenes (no ejecutar sin revisar) |
| Helium 10 Keyword Tracker R46 / QW5 | 30-ago · 10-sep · 15-sep | Ranks orgánicos. `>96`/`>306` = posición, no ausencia |

## Lo que todavía no existe y hay que bajar de Amazon
1. **Informe de inventario FBA por ASIN** (bloqueante #1)
2. Removal Order Detail 01/09 → hoy
3. Bulk Operations export (placements y negativos)
4. Export del listing con backend e Item Highlights
5. Returns report / Voice of the Customer (causa del 19→20 ago)
