# REFLEX — Ventas y conversión por ventana

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep · W4 8-ago→6-sep · W5 8–19 vs 20–30 ago · W6 reportes agencia 14-jul→21-ago · W7 settlement 16-ago→8-sep · W8 24-ago→15-sep · W9 Helium 30-ago/10-sep/15-sep · Wx sin declarar. **Las ventanas no se suman entre sí.** Etiquetas: VERIFIED · CALCULATED · INFERRED · UNKNOWN · CONFLICT.

## 5 · VENTAS Y CONVERSIÓN — POR VENTANA

### 5.1 W1 · 2026-08-01 → 2026-09-03 (34 días) — SRC-014 + SRC-018

| Métrica | Total cuenta |
|---|---:|
| Unidades vendidas | **653** `VERIFIED` |
| Revenue | **US$ 12.946,49** `VERIFIED` |
| Precio medio realizado | **US$ 19,83** `CALCULATED` |
| Sesiones | 3.450 · Unit Session % **18,93 %** `VERIFIED` |
| Fees Amazon (653 × 7,87) | −5.139,11 `CALCULATED` |
| COGS (653 × 5,94) | −3.878,82 `CALCULATED` |
| Contribución pre-PPC | **+4.035,54** (@19,99) / **+3.928,56** (@19,83) `CALCULATED` |
| Marketing (spend + fee 10 %) | **−5.607,72** `CALCULATED` |
| **RESULTADO NETO** | **−US$ 1.572,18** (@19,99) / **−US$ 1.679,16** (@19,83) `CALCULATED` |
| TACoS | 39,38 % · **43,31 %** con agencia `CALCULATED` |
| PPC % de unidades / revenue | 69,68 % / 69,12 % `CALCULATED` |
| Contribución neta por unidad | **−US$ 2,41 / −US$ 2,57** `CALCULATED` |

**Revenue y unidades por ASIN en W1: `UNKNOWN`** — declarado expresamente. El Business Report por ASIN cubre otra ventana (Wx).

### 5.2 Wx · ventana NO DECLARADA (~30 d entre 02/08 y 02/09) — Business Report por ASIN

> ⚠️ **No se suma a W1.** `CONFLICT` **C-29** abierto: la ventana exacta de este export es `UNKNOWN`.

| | **R46** | **QW5** | TOTAL |
|---|---:|---:|---:|
| Sesiones | 1.424 | 1.666 | 3.090 |
| Unidades | **304** (51,5 %) | 286 (48,5 %) | 590 |
| Ventas | 6.270,97 | 5.370,15 | 11.641,12 |
| **Precio medio** | **20,63** | **18,78** | 19,73 |
| **Unit Session %** | **21,35 %** | 17,17 % | 19,09 % |
| Buy Box | 100,00 % | 99,95 % | — |
| − Fees Amazon | −2.392,48 | −2.250,82 | — |
| − COGS | −1.805,76 | −1.698,84 | — |
| = Contribución pre-PPC | **+2.072,73** | **+1.420,49** | — |
| − Marketing `ESTIMATE` | −2.462,35 | −3.145,37 | — |
| **Resultado neto `ESTIMATE`** | **−389,62** | **−1.724,88** | — |

El ad spend por ASIN aquí es `ESTIMATE`: reparto 43,91 % / 56,09 % tomado de W1.

**Hallazgo `VERIFIED`: los dos ASINs se venden a precios distintos.** R46 20,63 · QW5 18,78 · brecha US$ 1,85.

### 5.3 W5 · ruptura de conversión del 19→20 de agosto — SRC-018

| Métrica | 8–19 ago → 20–30 ago |
|---|---|
| Sesiones | **+3,5 %** (otra medición: +12,3 %) |
| Unidades | **−28,1 %** |
| **CVR total** | **22,57 % → 15,68 % (−30,5 %)** |
| CVR de pago | −26,6 % |
| Línea de base previa | 22,72 % las tres semanas anteriores |
| ASP | −6,2 % / −7,2 % |
| Buy Box | 100 % / 99,95 % |

**Hipótesis descartadas `VERIFIED`:** pérdida de Buy Box · caída de tráfico · subida de precio · cambio de mix de tráfico pago.
**Qué cambió ese día: `UNKNOWN`.** Es el hueco más caro del expediente.
Costo estimado de la caída de conversión: **≈ US$ 4.470/mes** `CALCULATED` — casi el doble que todo el problema de PPC junto.

### 5.4 W7 · settlement 2026-08-16 → 2026-09-08 (24 días, 599 transacciones)

| Línea | Importe |
|---|---:|
| Ventas brutas (cargos por producto) | +10.998,43 |
| Devoluciones promocionales | −122,09 |
| Otros ajustes | +178,02 |
| Tarifas de Amazon sobre pedidos | −4.409,31 |
| Reembolsos a clientes (neto, 26 devoluciones) | −510,11 |
| Liquidaciones | +9,51 |
| **= Ingreso neto de Amazon** | **+6.144,45** |
| Almacenamiento FBA | −295,38 |
| Devolución de inventario | −78,96 |
| Eliminación de inventario | −1,68 |
| Suscripción Seller Central | −39,99 |
| **= Antes de publicidad** | **+5.728,44** |
| Publicidad facturada (7 cargos) | −3.367,05 |
| Fee de agencia 10 % | −336,71 |
| **= Neto Amazon + marketing** | **+2.024,68** |
| COGS (542 u × 5,94) | −3.219,48 |
| **RESULTADO NETO DE CAJA** | **−US$ 1.194,80** · **−US$ 2,20 / u** |

**Mix de precios realizados (W7)** `VERIFIED`: 19,99 → 232 u (42,8 %) · 17,99 → 151 u (27,9 %) · 21,99 → 109 u (20,1 %) · 18,99 → 50 u (9,2 %). **37 % de las unidades por debajo de 19,99.** Precio medio realizado **20,29**.

**Advertencias:** 109 de las 599 transacciones están **"Diferidas"**. El archivo sí se puede abrir por ASIN usando la puntuación del título (ver `historia-19sep.md`).

### 5.5 W8 · transacciones 2026-08-24 → 2026-09-15 (23 días)

| Línea | Importe |
|---|---:|
| Ventas brutas | 9.532,08 |
| Tarifas Amazon | −3.865,14 |
| Reembolsos (29 devoluciones) | −561,12 |
| Almacenamiento FBA | −295,38 |
| Publicidad + agencia | −3.153,70 |
| **Devolución de inventario (removal)** | **−3.774,96** |
| COGS (492 u × 5,94) | −2.922,48 |
| **RESULTADO** | **−US$ 5.028,32 · −10,22/u · −218,62/día** |
| **Resultado SIN el removal** | **−US$ 1.253,36 · −54,49/día** |

### 5.6 Velocidad de venta — W3 / 15-sep

| | R46 | QW5 |
|---|---:|---:|
| Unidades PPC en W3 (19 d) | **34** | **159** |
| Unidades/día (PPC-attributed) | **1,79** | **8,37** |
| Unidades 30 d totales (Helium 15-sep) | **241** | **402** |
| Revenue 30 d (Helium 15-sep) | US$ 4.986 | US$ 7.661 |

> ### ⚠️ INVERSIÓN COMPLETA DE LOS ASINS
> En agosto: **R46 ~497 u vs QW5 ~182 u**. Al 15-sep: **QW5 402 u vs R46 241 u**. QW5 vende **1,67×** lo de R46.
> **La premisa "R46 = ASIN económico principal" está INVALIDADA.** Toda decisión que la asuma (reparto 65/35 del presupuesto, Paid Core aprobado) es inejecutable tal como está escrita.

## 3 · INVENTARIO

| Dato | Valor | Etiqueta |
|---|---|---|
| Compradas | **5.000 u (2.500 por ASIN)** por US$ 29.700 | `VERIFIED` |
| **Stock declarado por el titular (15-sep)** | **1.700 u por SKU = 3.400 u totales** | `VERIFIED` |
| Composición del 1.700 (FBA disponible / reservado / físico) | **`UNKNOWN`** | — |
| Cifra citada el 28-sep (expediente de seguro) | **3.550 u** | `CONFLICT` con 3.400 |
| Capital inmovilizado a landed 5,94 | **US$ 20.196** sobre 3.400 u | `CALCULATED` |
| Fecha de recepción · age buckets · pies cúbicos | `UNKNOWN` → sin esto no se cuantifica el recargo por inventario añejo | — |

### 3.1 Removal order — anomalía abierta

| Dato | Valor |
|---|---|
| Cargos | **69 líneas "Tarifa por devolución de inventario"** |
| Importe | **−US$ 3.774,96** |
| IDs | `cG9y5eI/le` · `feGnIY4PCW` · `vaOqCY0NXG` |
| Fechas | 07 → 15 sep |
| Contrapartida | **+US$ 2.092,93** (4 cargos, 10–13 sep) |
| Quién la ordenó · cuántas unidades · qué ASIN | `UNKNOWN` |
| **Qué lo resuelve** | **Informes → Logística de Amazon → Retiradas de inventario (Removal Order Detail), 01/09 → hoy** |
