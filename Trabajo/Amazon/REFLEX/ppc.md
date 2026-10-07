# REFLEX — PPC: estructura, configuración, métricas y desperdicio

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep · W4 8-ago→6-sep · W6 reportes agencia 14-jul→21-ago. **Las ventanas no se suman entre sí.** Etiquetas: VERIFIED · CALCULATED · INFERRED · UNKNOWN · CONFLICT.

## Estructura

| Dato | W1 (con impresiones) | W2 (configuración 07-sep) |
|---|---:|---:|
| Campañas | **110** (55 por ASIN, espejadas) | **121** = 110 ENABLED + 11 PAUSED |
| Ad groups | 110 — **SKAG estricto, relación 1:1** | 121 — 1:1 |
| Targets | — | **2.620, todos ENABLED** |
| Portfolios | **2**, uno por ASIN, aislamiento presupuestario total | idem |
| Tipos de campaña | **sólo Sponsored Products.** SB y SD: `UNKNOWN` | idem |

**Campañas por match type (W1):** AUTO 8 (4+4) · PRODUCT TARGETING 11 (6 R46 / 5 QW5) · BROAD 19 (8/11) · PHRASE 36 (20/16) · EXACT 36 (17/19).
**Targets por match type (W2):** auto **2.001** · PHRASE 275 · BROAD 168 · EXACT 98 · product targeting 78. Por ASIN: R46 1.094 · QW5 1.262 · mixtos 264.

**Nomenclatura:** `SP-(N)-{Broad|Phrase|Exact}-<ASIN>` · `SP-(N)-ProductT-IndividualP-Exact-<ASIN>` · `Blind-SP-(6)-ProductT-...` · 4 auto por ASIN (`CloseMatch`, `LooseMatch`, `Substitutes`, `Complements`).
`INFERRED` El índice `(N)` es un **ID de keyword semilla**: N=1 → *reflex sticks* · N=3 → *reflex game* · N=7 → *reaction time game* · N=14 → *hand speed challenge game*.
**Fuera de convención:** `familia reflex` y `mixto automatica` (legacy, mixtas, pausadas).

**Las 11 campañas PAUSED (W2):** `mixto automatica` · `familia reflex` · `SP-(CloseMatch)-B0GQW5F2LL` · `SP-(Substitutes)-B0GQW5F2LL` · `SP-(2)-ProductT-IndividualP-Exact-B0GQW5F2LL` · `SP-(5)-Exact-B0GQW5F2LL` · `SP-(2)-Broad-B0GQW5F2LL` · `SP-(1)-Broad-B0GR46X8Y8` · `SP-(3)-Broad-B0GR46X8Y8` · `SP-(4)-Phrase-B0GR46X8Y8` · `SP-(4)-ProductT-IndividualP-Exact-B0GR46X8Y8`.

## Configuración de puja — los cinco problemas estructurales (W2)

| # | Hallazgo | Valor |
|---|---|---|
| **1** | **Estrategia de puja** | **`optimizeForSales` (Dynamic Up & Down) en 119 de 121 campañas.** El 100 % de las activas permite que Amazon suba la puja hasta +100 % |
| **2** | **Presupuesto** | **119 × US$20/día + 2 × US$40/día = US$ 2.460/día** contra un gasto real de ≈**US$ 150/día**. **Sobreaprovisionamiento 16×.** Nada está budget-capped → **bajar presupuestos no ahorra un dólar** |
| **3** | **Pujas** | Sólo **10 valores distintos**: 0,72 (1.035 targets) · 0,74 (757) · 0,85 (363) · 0,90 (264) · 0,91 (113). **Pujas por plantilla, no por keyword.** Mediana R46 **0,72** · QW5 **0,85** |
| **4** | **CPC vs puja** | CPC ponderado real **1,602 = 2,1× la puja media (0,754)**. **El 97,2 % de los clics se paga por encima de la puja.** `INFERRED`: dynamic bidding **más** multiplicador de placement Top-of-Search |
| **5** | **ASIN propio** | **QW5 paga por aparecer en la ficha de R46 en 35 campañas** (puja 0,85). R46 targetea a QW5 en 3 |

**Placements: `UNKNOWN`.** La columna viene vacía en las 2.620 filas. Con puja 0,85 y Up&Down el techo es 1,70, pero `reflex sticks` en QW5 pagó **2,60** → sólo un modificador de placement lo explica. **Leerlos en la UI de Amazon Ads.**
**Negativos existentes: `UNKNOWN`** — no vienen en el export.
**Creación de targets:** 14-jul (77) · 15-jul (22) · 26-jul (11) · 25-jul (8) · 3 legacy.

## Métricas — W1 · 1-ago → 3-sep

**Cuenta:** spend **5.097,93** · sales **8.948,47** · orders **443** · units **455** · impresiones **105.948** · clics **3.273** · CTR **3,09 %** · CPC **1,56** · CVR **13,53 %** · ACoS **56,97 %** · ROAS 1,76 · fee agencia 509,79 · marketing real **5.607,72 = 62,67 % de las ventas atribuidas**.

| Métrica | **R46** | **QW5** |
|---|---:|---:|
| Spend | **2.238,58** (43,9 %) | **2.859,35** (56,1 %) |
| Attributed sales | **4.876,62** (54,5 %) | 4.071,85 (45,5 %) |
| Orders / Units | 233 / 239 | 210 / 216 |
| Impresiones | 38.153 | **67.795 (+77 %)** |
| **CTR** | **4,10 %** | **2,52 %** |
| CPC | 1,43 | 1,68 |
| **CVR** | **14,9 %** | 12,3 % |
| **ACoS** | **45,9 %** | **70,2 %** |
| Contribución | **−985,42** | **−1.810,40** |

**Por delivery type (W1):** AUTO 2.283,45 (44,79 %, CVR 9,25 %, ACoS 65,93 %) · MANUAL KEYWORD 2.199,63 (43,15 %, CVR **21,09 %**, ACoS 49,75 %) · PRODUCT TARGETING 614,85 (12,06 %, CVR 14,21 %, ACoS 57,82 %).
**Subtipos AUTO:** LOOSE 1.547,55 (ACoS 65,4 %) · CLOSE 506,58 (79,7 %) · SUBSTITUTES 168,48 (**43,4 %**) · COMPLEMENTS 60,84 (84,6 %).
**Por match type:** AUTO 44,8 % gasto / ACoS 65,9 % · PHRASE 20,1 % / 48,6 % · EXACT 14,6 % / 49,6 % · PT 12,1 % / 57,8 % · BROAD 8,4 % / **52,9 % con CTR 7,76 %**.

## Métricas — W3 · 27-ago → 14-sep (19 días)

**Cuenta:** spend **2.245,85** (118/día, era 150) · sales **3.646,09** · orders/units **187/193** · impresiones **24.374** (**−59 %**/día) · CTR **6,69 %** *(sube por caída de impresiones)* · CPC **1,38** · CVR **11,47 %** · ACoS **61,60 %**.

| | R46 W1 | **R46 W3** | QW5 W1 | **QW5 W3** |
|---|---:|---:|---:|---:|
| ACoS | 45,9 % | **80,9 %** (+35 pts) | 70,2 % | **57,5 %** (−12,7 pts) |
| CVR | 14,9 % | **6,9 %** (−54 % rel.) | 12,3 % | **13,5 %** (+10 % rel.) |
| Spend / unidades | 2.238 / 239 | **516 / 34** | 2.859 / 216 | **1.730 / 159** |

## Métricas — W4 · 8-ago → 6-sep

CPC **1,59** vs puja media 0,754 = **2,1×**. **ACoS 47,2 % → 72,5 % en once días con el CPC casi plano (+4 %) y el CVR cayendo 15,94 % → 11,70 % (−27 %).** "El CPC explica el ACoS" es **falso**: son dos problemas distintos.
QW5 **64 % del gasto**, ACoS 71,3 % · R46 ACoS 43,0 %. AUTO CloseMatch 84,3 % · Complements 80,0 % · **Substitutes 32,2 % — la única auto sana, recibe 2,6 % del gasto**.

## Serie de la agencia — W6

| Período | Gasto | US$/día | CTR | CVR | ACoS | TACoS | Rank R46 | Rank QW5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 14–31 jul (18 d) | 1.335,82 | 74,2 | 1,20 % | 21,73 % | 41,56 % | 37,97 % | #45 | #96 |
| 1–7 ago | 1.070,76 | 153,0 | 1,11 % | 14,97 % | 50,53 % | 40,58 % | #23 | #86 |
| 8–14 ago | 1.079,01 | 154,1 | 1,14 % | 16,29 % | 46,11 % | 32,62 % | #31 | #73 |
| 15–21 ago | 1.015,64 | 145,1 | 1,05 % | 14,94 % | 52,43 % | 33,95 % | **#90** | **#34** |

La agencia **duplicó el ritmo diario de julio a agosto (+106 %) y lo dejó plano tres semanas.** No hay reportes posteriores al 21-ago (la semana 22–28 ago existe como pestaña: pedirla). **Nombre y fecha de inicio de la agencia: `UNKNOWN`.**

## Desperdicio — W1

| Bucket | n términos | Spend | % gasto | Uds | Contribución |
|---|---:|---:|---:|---:|---:|
| Rentable (<28,1 % ACoS) | 176 | 503,50 | 9,9 % | 221 | **+811,93** |
| Zona 28–45 % | 29 | 635,08 | 12,5 % | 88 | −154,75 |
| Pérdida 45–70 % | 19 | 925,42 | 18,2 % | 87 | −480,30 |
| Sangría >70 % | 22 | 1.042,30 | 20,4 % | 59 | −781,91 |
| Muerto ≥5 clics | 17 | 159,79 | 3,1 % | 0 | −175,77 |
| Muerto 2–4 clics | 122 | 440,09 | 8,6 % | 0 | −484,10 |
| **Ruido ≤1 clic** | **1.093** | **1.391,75** | **27,3 %** | 0 | **−1.530,92** |

**176 términos (9,9 % del gasto) producen toda la contribución positiva: +US$ 812. Los otros 1.302 restan US$ 3.608.**

**La cola larga está en dos campañas:** US$ 1.128 de los 1.391,75 salen de `SP-(LooseMatch)-B0GQW5F2LL` (637,83 · 492 términos) y `SP-(LooseMatch)-B0GR46X8Y8` (490,17 · 462 términos). **No es un problema de negativos**: son términos irrepetibles. La palanca es puja/bidding de esas dos campañas.

**Deterioro en W3:** términos sin compras **35,9 % → 48,6 %** del gasto · cola ≤1 clic **27,3 % → 34,9 %** (652 términos, US$ 783).

**Sangría concentrada (W1):** 17 términos con compras, ACoS >70 % y gasto ≥US$20 = **−US$ 662. 14 de los 17 son de QW5.** Venden → la palanca es puja, no exclusión. Mayores: `b0dln5c44d` QW5 (125,00 · 6 u · 108,8 %) · `outdoor games` QW5 (152,14 · 11 u · 71,8 %) · `hand speed challenge game` QW5 (132,80 · 8 u · 88,0 %).

**Negativos duros (0 compras, ≥5 clics):** 17 términos, US$ 159,79 = **3,1 % del problema**: `toys & games` · `popdarts` · `physical education equipment` · `gaming equipment` · `blazepod` · `beach games` · `ripstick`.

**Waste agregado (W1) ≈ US$ 2.100 / 34 d = US$ 62/día.**
**Solapamiento (W1):** 121 términos servidos por **los dos ASINs** = **61,4 % del gasto**.
