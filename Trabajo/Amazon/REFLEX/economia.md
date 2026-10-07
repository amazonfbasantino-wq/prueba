# REFLEX — Economía unitaria y precio

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep · W4 8-ago→6-sep · W5 8–19 vs 20–30 ago · W6 reportes agencia 14-jul→21-ago · W7 settlement 16-ago→8-sep · W8 24-ago→15-sep · W9 Helium 30-ago/10-sep/15-sep · Wx sin declarar. **Las ventanas no se suman entre sí.** Etiquetas: VERIFIED · CALCULATED · INFERRED · UNKNOWN · CONFLICT.

> ⚠️ Con objetivo de **liquidar y salir en diciembre**, la columna "u p/ igualar 19,99" de 4.4 supone que las unidades no vendidas conservan valor. No es así: lo que quede el 1-ene vale poco. Comparar escalones por **contribución total dentro de Q4**, no por contribución por unidad.

## 4 · ECONOMÍA UNITARIA

### 4.1 La fórmula de fees — pieza más sólida del expediente

```
Fee Amazon = unidades × US$ 4,87 (FBA fulfillment) + 15,0 % del precio (referral)
```
`VERIFIED` — validada contra el settlement W7: **524 de 539 filas de pedido encajan exacto**. Vale para **ambos ASINs**.

| Precio | Fee | n filas W7 | Contribución/u (landed 5,94) |
|---:|---:|---:|---:|
| 21,99 | 8,17 | 100 | **+7,88** |
| 20,63 *(operativo R46, Wx)* | 7,96 | — | **+6,73** |
| 19,99 *(referencia)* | 7,87 | 221 | **+6,18** |
| 18,99 | 7,72 | 50 | **+5,33** |
| 18,78 *(operativo QW5, Wx)* | 7,69 | — | **+5,15** |
| 17,99 | 7,57 | 142 | **+4,48** |

**Anomalías de la fórmula (W7):** 15 filas no encajan. 13 con fee superior (10,86 · 11,95 · 12,21 · 12,66 · 14,33 · 14,86 · 16,36 sobre precios de 17,99–21,99) y 2 con fee de sólo US$ 3,00 (referral sin fulfillment). Causa `UNKNOWN`.

### 4.2 Parámetros

| Parámetro | Valor | Etiqueta |
|---|---|---|
| Landed cost (producto + envío) | **US$ 5,94 / u** (29.700 / 5.000) | `VERIFIED` |
| Precio de lista de referencia | US$ 19,99 | `VERIFIED` |
| Fee de agencia PPC | **10 % del ad spend, adicional al gasto** | `VERIFIED` |
| Fee de agencia en importe | ≈ US$ 450/mes | `CALCULATED` |
| Break-even ACoS (raw) | **28,1 %** — se compara contra **TACoS**, no contra ACoS | `CALCULATED` |
| Max ad spend sostenible | ≈ US$ 5,62 / u | `CALCULATED` |
| Costo medio por devolución | ≈ US$ 19,62 (W7) · ≈ US$ 19,35 (W8) | `CALCULATED` |
| Tasa de devolución | ≈ 4,8 % (W7) | `CALCULATED` |
| Almacenamiento FBA | US$ 295,38 en un solo cargo (07-sep) | `VERIFIED` |
| Suscripción Seller Central | US$ 39,99 / mes | `VERIFIED` |

### 4.3 Break-even CPC

```
CPC de equilibrio = (contribución por unidad ÷ 1,10) × CVR
```
El **1,10** es el fee de agencia. Variante con crédito orgánico: × **1,397** (`ESTIMATE`, derivado del share PPC 71,56 % de los reportes de agencia ago 1–21, extrapolado — **no es un dato de la ventana**).

**Break-even por ASIN — ventana W3**, precio medio realizado 19,37 → contribución 5,65/u:

| ASIN | CVR | **BE CPC directo** | CPC real | Gap |
|---|---:|---:|---:|---:|
| **QW5** | 13,5 % | **0,69** | 1,52 | **+119 %** |
| **R46** | 6,9 % | **0,36** | 1,04 | **+193 %** |

`VERIFIED` cita literal del baseline: **"Ninguno de los dos ASINs es pagable hoy a ningún CPC observado."**

> ⚠️ **DOS CÁLCULOS DE BE CPC CONVIVEN — no son un conflicto de fuente, son dos supuestos de precio.**
> **(a)** Baseline W3: usa el **precio medio realizado agregado 19,37** → contribución **5,65/u** para ambos ASINs → BE **QW5 0,69 · R46 0,36**.
> **(b)** Análisis del 15-sep: usa el **ASP realizado POR ASIN** (QW5 **18,92** → contrib **5,27**; R46 **18,76** → contrib **5,13**) → BE **QW5 0,65 · R46 0,32**.
> **(b) es el más correcto** porque los dos ASINs se venden a precios distintos. Usar (b) para decisiones por ASIN y (a) sólo para lecturas agregadas. **La conclusión no cambia con ninguno de los dos.**

**Break-even por keyword a distintos precios — W1** (`CALCULATED`):

| Término | CVR | CPC real | Máx @19,99 | Máx @19,99 +org | Máx @24,99 +org | Máx @27,99 +org |
|---|---:|---:|---:|---:|---:|---:|
| reflex drop sticks game | 24,1 % | 2,25 | 1,35 | 1,89 | **3,19** | 3,97 |
| reflex sticks | 22,1 % | 2,24 | 1,24 | 1,73 | **2,93** | 3,64 |
| reflex game | 21,6 % | 1,77 | 1,21 | 1,70 | **2,86** | 3,56 |
| reaction game | 21,1 % | 2,08 | 1,18 | 1,65 | **2,79** | 3,47 |
| reflex challenge game | 18,4 % | 2,10 | 1,03 | 1,45 | **2,44** | 3,04 |
| reflex drop sticks | 17,5 % | 2,19 | 0,98 | 1,37 | **2,32** | 2,88 |
| reaction time game | 16,7 % | 2,19 | 0,94 | 1,31 | **2,21** | 2,75 |
| hand speed challenge game | 15,7 % | 2,13 | 0,88 | 1,23 | 2,08 | 2,59 |
| **reaction time drop sticks** | **34,8 %** | 1,84 | **1,95** | **2,73** | 4,61 | 5,73 |

`VERIFIED` A US$ 19,99 el CPC real supera al de equilibrio en **8 de las 9** keywords núcleo, incluso dando crédito completo al orgánico. A **US$ 24,99 con crédito orgánico las 9 pasan a ser pagables.**

### 4.4 Análisis de precio 2026-09-17 — economía por escalón (QW5, sin PPC)

`CALCULATED` · descuento realizado −5,4 % (ASP 18,92 sobre lista 19,99, `VERIFIED` W3) mantenido constante.

| Lista | Net rev/u | Fee/u | Landed | **Contrib/u** | Margen | Contrib 1.700 u | u p/ igualar 19,99 | Caída máx. tolerada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 19,99 | 18,91 | 7,71 | 5,94 | **5,26** | 27,8 % | 8.949 | 1.700 | — |
| 22,99 | 21,75 | 8,13 | 5,94 | **7,68** | 35,3 % | 13.050 | **1.166** | **−31,43 %** |
| 24,99 | 23,64 | 8,42 | 5,94 | **9,28** | 39,3 % | 15.784 | **964** | **−43,30 %** |
| 27,99 | 26,48 | 8,84 | 5,94 | **11,70** | 44,2 % | 19.884 | **765** | **−55,00 %** |
| 29,99 | 28,37 | 9,13 | 5,94 | **13,30** | 46,9 % | 22.618 | **673** | **−60,44 %** |

**Separación obligatoria:** *contribution pre-PPC* (decisión de PRECIO, positiva en los 5 escalones) ≠ *profit after PPC* (decisión de ADQUISICIÓN DE TRÁFICO, negativa hoy). No mezclarlas.
