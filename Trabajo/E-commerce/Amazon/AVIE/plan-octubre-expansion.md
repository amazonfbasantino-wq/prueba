# AVIE — Octubre: expansión con publicidad que se paga con las ventas (2026-10-08)

> **Decisión de Santi (2026-10-08):** octubre es mes de **expansión y posicionamiento**. Se acepta quemar unidades y margen para ganar velocidad y llegar a fin de año mejor rankeado. La publicidad se financia con lo que Amazon paga por los pedidos. Trabajo de PPC **diario**.
> Campañas listas para cargar: `campanas-octubre.csv` (133 objetivos + 146 negativas) · **archivo masivo para subir: `AVIE_OCT_bulk_carga.xlsx`** (lo genera `scripts/generar_bulk.py`). Fuente de keywords: `datos/2026-10_cerebro_*.csv` + `datos/2026-10_ads_search_terms.csv`.

## 1 · Cuánto te paga Amazon según el precio (HECHO: tarifas reales de las transacciones)
| Precio | Tarifas Amazon | **Te pagan** | Margen (− 2,86 de producto) | ACOS máx. |
|---|---|---|---|---|
| 9,99 | 4,04 | **5,95** | 3,09 | 30,9 % |
| 10,99 | 5,74 | 5,25 | 2,39 | 21,8 % |
| 11,99 | 5,89 | 6,10 | 3,24 | 27,0 % |
| 12,99 | 6,04 | **6,95** | 4,09 | 31,5 % |
| 13,99 | 6,19 | 7,80 | 4,94 | 35,3 % |
| 14,99 | 6,34 | **8,65** | 5,79 | 38,6 % |
- Por debajo de 10 USD, Amazon cobra 8 % de comisión y una tarifa FBA más baja (3,24). Desde 10 USD pasa a 15 % y 4,09.
- **Zona muerta: entre 10,00 y 11,80 te pagan MENOS que a 9,99.** No usar esos precios nunca.
- Los ~5,80 que ve Santi a 9,99 son los 5,95 menos devoluciones y descuentos.
- **HECHO:** a 9,99 (jul-sep) se vendían ~2,5/día. El mejor ritmo (jun, ~8/día) fue a 12,99-13,99 con cupón y publicidad fuerte. **9,99 no trae volumen sola.**

### Estrategia de precio (decisión de Santi 2026-10-08)
1. **Ahora: 14,99** mientras se posiciona.
2. **Plan B: 13,99** si no hay resultados. Criterio del 16-oct (7 días de campañas nuevas): **< 4 pedidos/día y CVR de ads < 8 %** → bajar a 13,99.
3. **Cuando esté posicionado (BFCM o diciembre): 9,99 mostrando −33 %** (9,99 contra 14,99 = −33,4 %). A 9,99 Amazon paga 5,95 por unidad (tarifas bajas por estar debajo de 10 USD).

**Condición para que Amazon muestre el −33 % tachado (INFERENCIA de las reglas de precio de referencia de Amazon, verificar en Seller Central):** el precio de referencia ("Was Price" o "Typical price") sale de la **mediana de lo que pagaron los clientes en los últimos 90 días**. Hoy esa ventana (jul-oct) está llena de ventas a **9,99** → **si se baja a 9,99 ahora, NO aparece ningún descuento.**
- Hace falta que **más de la mitad de las ventas de los últimos 90 días sean a 14,99**. A ~5-6 pedidos/día eso se daría alrededor de **mediados de noviembre** (fecha estimada; se recalcula con las ventas reales).
- **Cada día que se vende por debajo de 14,99 baja la referencia.** Si se pasa a 13,99, el tachado futuro mostraría −28,6 %, no −33 %. Evitar bajas cortas de prueba.
- Las ofertas de Black Friday (Lightning Deal o Best Deal) tienen su propia validación de precio. Revisar en Seller Central → Promociones las fechas de postulación.

## 2 · Presupuesto: escalera agresiva que se paga con las ventas (decisión de Santi 08-oct)
**Lógica de Santi (correcta):** con saldo positivo, Amazon cobra la publicidad del saldo y la tarjeta no se toca. Se acepta **quemar unidades**: que lo que pagan esas unidades se vaya en publicidad, para subir orgánico.
**Tope de quema:** 400 unidades × 8,65 = **3.460 USD de publicidad acumulada desde el 9-oct**. Al llegar a ese número, se pasa a modo rentable (regla §3a pura), haya o no ranking.

**La métrica de cada día es el TACOS** = gasto en ads ÷ ventas TOTALES (ads + orgánico). Las ventas totales están en Seller Central sin demora; el ACOS de 24 h no sirve (Amazon atribuye ventas hasta 7 días después del clic).
| TACOS (últimos 3 días) | Qué significa | Acción |
|---|---|---|
| ≤ 38 % | Rentable: cubre hasta el producto | Subir un nivel |
| 38-55 % | **Zona de expansión:** se queman unidades, pero lo que paga Amazon cubre la publicidad. La tarjeta no se toca | Subir un nivel si las campañas gastan ≥ 80 % del presupuesto (es decir, están frenadas por presupuesto) |
| 55-80 % | La publicidad cuesta más de lo que entra: se usa el colchón de la tarjeta | Mantener el nivel y cortar lo que no vende |
| > 80 % dos días seguidos, o saldo negativo | Quema sin retorno | Bajar un nivel |
| La tarjeta ya pagó 400 USD en el mes | Colchón agotado | Volver al piso |

| Nivel | USD/día | Reparto (EMPUJE · PROBADAS · QUICKWIN · RIVALES · ASIN · DESCUBRIR · AUTO · SUBST · CLOSE) |
|---|---|---|
| 0 · piso | 20 | 8 · 4 · 3 · 0 · 1 · 0 · 1 · 2 · 1 |
| **1 · arranque (9-oct)** | **60** | 20 · 12 · 10 · 3 · 4 · 3 · 3 · 3 · 2 |
| 2 | 90 | 30 · 18 · 15 · 4 · 6 · 4 · 5 · 5 · 3 |
| 3 · techo (lo que propuso Marvin) | 126 | 40 · 25 · 22 · 6 · 8 · 6 · 7 · 8 · 4 |
- **Nunca se sube más de un nivel cada 48 h**: los datos de 24 h llegan incompletos.
- Más presupuesto no compra ventas si las pujas no ganan subastas: **la agresividad va a EMPUJE** (puja alta + 60 % extra en primera posición), donde una venta mueve el ranking.
- **Cuenta corriente de la quema:** el seguimiento diario (`seguimiento-diario.csv`) acumula el gasto y lo compara con los 3.460 USD.

## 3 · Estructura de campañas (portfolio nuevo "AVIE OCT") · actualizada 08-oct con el Keyword Tracker
| Campaña | Qué tiene | Objetivos | Puja inicial | USD/día |
|---|---|---|---|---|
| `AVIE_OCT_EMPUJE_EX` | **Las keywords a subir de ranking:** familia gua sha brush (#33, #84, #92, CVR 29-50 % en muestras chicas) + familia contour glow (#60-73) | 7 | 0,80-0,90 + **60 %** en primera posición | 20 |
| `AVIE_OCT_PROBADAS_EX` | Keywords que **ya vendieron** en ads (CVR 15-33 %) + `lymphatic contour face brush` a 0,50 | 14 | 0,85 (+30 % en primera posición) · la principal a 0,50 | 12 |
| `AVIE_OCT_QUICKWIN_EX` | Long-tail con **competencia baja** donde **AVIE ya rankea orgánico** (Cerebro #42-110 + Keyword Tracker 08-oct: glow brush lymphatic #23, korean lymphatic brush #24, face brush for lymphatic drainage #45…) + las 2 de sculpt | 67 | 0,45-0,75 | 10 |
| `AVIE_OCT_RIVALES_EX` | Marcas rivales y errores de tipeo donde AVIE ya aparece (contour glow #60-73, nuvetra contour glow #30, kojeva/akei/koniva…) | 39 | 0,60 | 2 |
| `AVIE_OCT_ASIN` | Aeki B0GFSMWTPK · Cheersendex B0GVBQ7P79 · B0G3685P2S (reemplaza a `AVIE_COMP_ASIN_US` de Marvin) | 3 | 0,65 | 4 |
| `AVIE_OCT_DESCUBRIR_PH` | Frase en 5 raíces para encontrar términos nuevos | 5 | 0,55 | 3 |
| `AVIE_OCT_AUTO_COSECHA` | Automática **sólo coincidencia amplia** = red de tendencias (§3b) | 1 grupo activo | 0,40 | 3 |
| **SP-(Substitutes)** existente | Automática, sustitutos: 18 pedidos, CTR 4,34 % (dato de Marvin) | — | ≤ 0,60 | 3 |
| **SP-(CloseMatch)** existente | Automática, coincidencia cercana: CTR 2,97 % | — | ≤ 0,60 | 2 |
| **Total (nivel 1)** | | | | **60** |
Qué hacer con cada campaña vieja → `campanas-existentes-semaforo.md`.

**Por qué la QUICKWIN es la apuesta de velocidad:** son búsquedas chicas con poca competencia donde Amazon **ya** muestra a AVIE en la página 2-3. Con pocas ventas por keyword AVIE puede pasar a página 1 orgánica. Es ranking "en muchas puertas chicas" en vez de pelear la grande (`lymphatic contour face brush`, 55.000/mes, AVIE #141).
**Empuje (Keyword Tracker 08-oct):** familia `gua sha brush` (#33, 4.843/mes, CPR 25) y familia `contour glow` (#60-73, ya tiene anuncio en posición 6-12). **Corrección:** `face brush for lymphatic drainage` (#45) NO va a empuje: en ads convirtió 5 % (39 clics, 2 pedidos) → queda en QUICKWIN a 0,45 como prueba con el listing nuevo. El título nuevo de Marvin ("Gua Sha Glow, Massager, Drainage, Pink") es lo que hizo subir estas familias.
**Ojo:** `dry brush for lymphatic drainage` puede mezclar búsquedas de cepillo corporal → si en 5 días gasta > 15 USD sin venta, se baja la puja.

## 3a · Regla de CPC máximo (de Marvin, adoptada)
**CPC máx. = precio × 0,333 × CVR del término** (= ACOS objetivo 33 %; el break-even a 14,99 es 38,6 %).
| CVR del término | CPC máx. a 14,99 | Techo en octubre sólo para las 3 de empuje (ACOS 50 %) |
|---|---|---|
| 7 % | 0,35 | 0,52 |
| 10 % | 0,50 | 0,75 |
| 13 % | 0,65 | 0,97 |
| 18 % | 0,90 | 1,35 |
| 22 % | 1,10 | 1,65 |
| 28 % | 1,40 | 2,10 |
- **Mientras un término tiene < 20 clics** no hay CVR confiable: se usa la puja inicial del bulk (0,40-0,85, equivale a asumir CVR de 8-17 %).
- **Desde 20 clics:** puja = la de la tabla con el CVR real. Se revisa en la rutina diaria.
- ⚠️ Las campañas nuevas que propuso Marvin **no cumplen su propia regla**: `AVIE_PINK_EX_US` a 1,40 con CVR real 5,4 % (máx. 0,27) y `AVIE_COMP_ASIN_US` a 1,30 con CVR histórico 9,4 % (máx. 0,47). Tampoco su total de 126 USD/día (3.780/mes), 7 veces el límite de la tarjeta y 6 veces lo que entra hoy por ventas.

## 3b · Automáticas: cómo quedan las "redes" para encontrar keywords nuevas
| Red | Qué busca | Puja | USD/día |
|---|---|---|---|
| **SP-(Substitutes)** (ya existe) | Páginas de productos rivales → ASINs que convierten | ≤ 0,60 | 3 |
| **SP-(CloseMatch)** (ya existe) | Búsquedas casi iguales al listing nuevo | ≤ 0,60 | 2 |
| **`AVIE_OCT_AUTO_COSECHA`** (nueva, sólo amplia) | **Tendencias y temporada:** búsquedas que hoy no conocemos (gift for her, stocking stuffer, halloween, skincare gift…). Es la que pidió Santi | 0,40 | 3 |
- Se reutilizan las dos automáticas viejas que funcionaron, en vez de duplicarlas: dos automáticas iguales compiten entre sí y mezclan los datos.
- La amplia vieja, SP-(LooseMatch), perdía plata (Marvin: "no activar"). Probablemente por puja alta y sin negativas. La nueva sale a 0,40 y con **146 negativas desde el día 1**: 131 exactas (las keywords que ya están en campañas manuales + 7 sin venta o de otra intención), 13 frases (electric, makeup, body, drops, supplement, pills, toothbrush, cleansing, exfoliating, powder, ice roller, foundation, peel) y 2 ASIN (FLAHOLD, B0FD6Y9BX5).
- **Freno de la nueva:** 25 USD sin venta, o ACOS > 100 % a los 7 días → se pausa.
- En SP-(Substitutes) y SP-(CloseMatch) cargar a mano, como mínimo: ASIN negativo B0FD354L27 (FLAHOLD) y las negativas exactas `gua sha facial tools`, `kojeva lymphatic face brush`, `contour brush`, `face mask brush`, `facial brush`. (Con el archivo masivo descargado se arma la carga completa de un paso.)

**Ciclo de cosecha (rutina diaria, en las 3 redes):**
| Lo que pasa con un término | Qué se hace |
|---|---|
| **1+ pedido con ACOS < 60 %** | **Graduar:** a exacta en `AVIE_OCT_QUICKWIN_EX` (puja = CPC pagado + 0,10, sin pasar la regla §3a) **y** negativa exacta en la red de donde vino |
| 1 pedido con ACOS > 60 % | Esperar a 10 clics |
| **ASIN** rival con 1+ pedido | A `AVIE_OCT_ASIN` + ASIN negativo en la red |
| **≥ 8 clics y 0 pedidos** o **≥ 8 USD sin venta** | Negativa exacta en la red |
| Palabra de otra intención (aunque tenga 1-2 clics) | Negativa frase en la red |
| Término de temporada que vende (ej. "gift") | Graduar igual. Además, avisar: va a Recommended Uses o bullet 5, nunca al título (regla de Amazon de AVIE) |

## 4 · Ciclo de 24 horas (decisión de Santi: análisis diario)
**Lo que manda Santi cada día (5 minutos):**
1. **Informe de términos de búsqueda** de Amazon Ads (Sponsored Products, período "ayer"; si se saltea un día, "últimos 3 días").
2. **Ventas totales de ayer**: unidades y USD (Seller Central → Informes de negocio → Por fecha, o captura del panel).
3. **Export del Keyword Tracker** de Helium 10 (el mismo del 08-oct).
4. Cualquier cambio que haya hecho (precio, cupón, listing, pujas a mano).

**Lo que devuelve Claude:** fila nueva en `seguimiento-diario.csv` (gasto, pedidos de ads, pedidos totales, TACOS, quema acumulada, puestos de las keywords de empuje), el nivel de la escalera de mañana y la lista exacta de cambios (graduar, negativizar, subir o bajar pujas) con el porqué de cada uno. Primera corrida: armar `scripts/rutina_diaria.py` con las columnas reales del informe.

**Reglas por keyword (con datos de 3 días):**
1. **Negativizar** (exacta negativa) todo término con **≥ 10 clics y 0 pedidos**, o **≥ 12 USD sin venta** (en las automáticas: 8 clics u 8 USD).
2. Keyword con **venta y ACOS < 40 %** → **+10 %** de puja, sin pasar el techo de §3a.
3. Keyword con **< 100 impresiones en 3 días** → **+0,10** (no entra a la subasta).
4. Término nuevo que vendió en DESCUBRIR o en las automáticas → graduar (§3b).
5. EMPUJE: si una keyword sube ≥ 10 puestos orgánicos, se mantiene la puja aunque el ACOS sea alto (dentro del techo de 50 %). Si en 7 días no sube nada, se baja al nivel de la regla.

**Una vez por semana (lunes):**
- Keyword con **≥ 15 clics y ACOS > 80 %** → **−20 %** o pausar.
- Mirar el puesto orgánico de 10 keywords de QUICKWIN y de las 3 de contour glow (¿subió?).
- 16-oct: criterio 14,99 → 13,99 (§1). Seguir la cuenta de ventas a 14,99 en la ventana de 90 días para el −33 %.

**No hacer:** reestructurar campañas, cambiar la misma puja dos días seguidos, ni cambiar el precio más de una vez por semana (y menos bajarlo por pocos días: arruina la referencia del −33 %). Historia de AVIE: el error fue el **bucle de sobreoptimización** (`ppc.md`).

## 5 · Qué se espera y cómo se mide
- **HIPÓTESIS:** las long-tail tienen menos competidores pujando → CPC más bajo (0,60-0,90 contra 1,58 actual) y CVR más alto (búsqueda más específica). Si el CPC baja a ~0,80 y el CVR sube al 12 %, cada pedido de ads cuesta ~6,70 USD (hoy 22,60).
- **Señal de que funciona (al 15-oct):** pedidos/día ≥ 6 · CPC promedio ≤ 1,00 · ACOS ≤ 60 % (durante la expansión se acepta por encima del break-even) · 5+ keywords de QUICKWIN que suben ≥ 20 puestos orgánicos.
- **Señal de que no funciona:** ACOS > 100 % con 7 días de datos y ≥ 300 clics → volver al plan de pulsos (`plan-q4-pulsos.md`).
