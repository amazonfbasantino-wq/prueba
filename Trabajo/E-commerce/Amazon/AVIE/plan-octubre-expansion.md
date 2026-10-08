# AVIE — Octubre: expansión con publicidad que se paga con las ventas (2026-10-08)

> **Decisión de Santi (2026-10-08):** octubre es mes de **expansión y posicionamiento**. Se acepta quemar unidades y margen para ganar velocidad y llegar a fin de año mejor rankeado. La publicidad se financia con lo que Amazon paga por los pedidos. Trabajo de PPC **diario**.
> Campañas listas para cargar: `campanas-octubre.csv` (117 objetivos + 123 negativas) · **archivo masivo para subir: `AVIE_OCT_bulk_carga.xlsx`** (lo genera `scripts/generar_bulk.py`). Fuente de keywords: `datos/2026-10_cerebro_*.csv` + `datos/2026-10_ads_search_terms.csv`.

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

## 2 · Presupuesto diario que se paga solo
**Presupuesto de ads de hoy = pedidos de ayer × lo que paga Amazon por pedido − 5 USD** (almacenamiento + plan).
- A 14,99 (te pagan 8,65): 3 pedidos → ≈ **21 USD** · 4 → ≈ 30 USD · 5 → ≈ 38 USD. (A 13,99: × 7,80.)
- **Piso 20 USD/día · techo 45 USD/día** en octubre, salvo que el ROAS de los últimos 7 días sea ≥ 2,5.
- **Freno de mano:** si el saldo de la cuenta de vendedor queda en negativo, se baja al piso hasta que vuelva a positivo (así no se toca la tarjeta).
- Esto financia la publicidad con las ventas, **no** recupera el costo del producto (2,86 por unidad): es la "quema de unidades" que Santi aceptó para posicionarse.

## 3 · Estructura de campañas (todas en un portfolio nuevo "AVIE OCT")
| Campaña | Qué tiene | Objetivos | Puja inicial | USD/día (total 34) |
|---|---|---|---|---|
| `AVIE_OCT_PROBADAS_EX` | Keywords que **ya vendieron** en ads (CVR 15-33 %) | 17 | 0,85 + 30 % en primera posición | 10 |
| `AVIE_OCT_QUICKWIN_EX` | Long-tail con **competencia baja** (CPR 8-10 = alcanzan ~8-10 ventas en 8 días para la página 1) donde **AVIE ya rankea orgánico entre #42 y #110** | 54 | 0,75 | 8 |
| `AVIE_OCT_RIVALES_EX` | Marcas rivales y sus errores de tipeo (kojeva→koneva/kogeva…, aeki→akei/awki…, contour glow, k glow) donde AVIE ya aparece orgánico (#31-#128) | 34 | 0,60 | 3 |
| `AVIE_OCT_ASIN` | Páginas de Aeki B0GFSMWTPK (rival más débil), Cheersendex B0GVBQ7P79, B0G3685P2S | 3 | 0,70 | 4 |
| `AVIE_OCT_DESCUBRIR_PH` | Frase amplia en 5 raíces para encontrar términos nuevos baratos | 5 | 0,55 | 3 |
| `AVIE_OCT_AUTO_COSECHA` | **Automática**: Amazon elige las búsquedas leyendo el listing nuevo → recolecta keywords que hoy no conocemos (ver §3b) | 4 grupos | 0,30-0,70 | 6 |
| Marvin (MARVIN1, "Avie Lymph Drain Pink") | **Pausar** las que pujan por las mismas palabras (si no, las campañas compiten y los datos se mezclan); el resto, a 5 USD/día | — | — | 0-5 |

**Por qué la QUICKWIN es la apuesta de velocidad:** son 54 búsquedas chicas (250-700/mes cada una, unas 21.000/mes en total) con poca competencia, donde Amazon **ya** muestra a AVIE en la página 2-3. Con pocas ventas por keyword AVIE puede pasar a página 1 orgánica, y cada keyword ganada vende sola después. Es ranking "en muchas puertas chicas" en vez de pelear la puerta grande (`lymphatic contour face brush`, CPR 123).
**Ojo:** las top-3 de `RIVALES` (contour glow / k glow, AVIE #31-34) son el mejor atajo: AVIE ya está a un paso de la página 1.
**Ojo:** `dry brush for lymphatic drainage` (29.000/mes en el mapa 10x10, AVIE vendió 3 de 9 clics) puede mezclar búsquedas de cepillo corporal → va en PROBADAS, pero si en 5 días gasta > 15 USD sin venta, se baja la puja.

## 3b · Campaña automática de cosecha (`AVIE_OCT_AUTO_COSECHA`)
**Para qué:** Amazon decide a qué búsquedas mostrar AVIE leyendo el listing (que cambió con Marvin), las reseñas y el comportamiento de compra. Así aparecen keywords que no están en Cerebro ni en nuestras listas. Es la "red de pesca"; las exactas son la "caña".
| Grupo de segmentación | Puja | Por qué |
|---|---|---|
| Coincidencia cercana | 0,70 | Búsquedas casi iguales al listing: la que más keywords nuevas y rentables suele dar |
| Coincidencia amplia | 0,50 | Búsquedas relacionadas más lejanas: barato, explora |
| Sustitutos | 0,60 | Aparece en páginas de rivales: encuentra ASINs que convierten → van a `AVIE_OCT_ASIN` |
| Complementos | 0,30 | Páginas de productos que se compran juntos (aceites, piedras): mínimo, sólo para mirar |
**Negativas cargadas desde el día 1 (123):** las 105 keywords que ya están en campañas exactas (así la auto busca palabras **nuevas** y no compite con las otras) · 5 términos que ya gastaron sin vender · 11 frases de otra intención (electric, makeup, body, drops, supplement, pills, toothbrush, cleansing, exfoliating, powder, ice roller) · 2 ASIN negativos (FLAHOLD B0FD354L27, B0FD6Y9BX5).

**Ciclo de cosecha (se aplica en la rutina diaria):**
| Lo que pasa con un término de la auto | Qué se hace |
|---|---|
| **1+ pedido con ACOS < 60 %** | **Graduar:** agregarlo en exacta a `AVIE_OCT_QUICKWIN_EX` (puja = CPC que pagó en la auto + 0,10) **y** cargarlo como negativa exacta en la auto |
| 1 pedido con ACOS > 60 % | Esperar a 10 clics antes de decidir |
| **ASIN** de un rival con 1+ pedido | Pasarlo a `AVIE_OCT_ASIN` y cargarlo como ASIN negativo en la auto |
| **≥ 8 clics y 0 pedidos** o **≥ 8 USD sin venta** | Negativa exacta en la auto |
| Palabra irrelevante (otra intención) aunque tenga 1-2 clics | Negativa frase en la auto |
**Lunes:** comparar el ROAS de los 4 grupos. El grupo con mejor ROAS sube +0,10, el peor baja −0,10 (o se pausa si no vendió nada en 7 días).

## 4 · Rutina diaria (10 minutos) — qué se puede tocar todos los días y qué no
**Todos los días (mirando los últimos 3 días):**
1. Ajustar el presupuesto con la regla del §2.
2. **Negativizar** (exacta negativa) todo término de búsqueda con **≥ 10 clics y 0 pedidos**, o **≥ 12 USD gastados sin venta**.
3. Keyword con **venta y ACOS < 40 %** → **+10 % de puja**.
4. Keyword con **< 100 impresiones en 3 días** → **+0,10 de puja** (no está entrando a la subasta).
5. Término nuevo que vendió en `DESCUBRIR_PH` → agregarlo a `QUICKWIN_EX` en exacta.

**Una vez por semana (lunes):**
- Keyword con **≥ 15 clics y ACOS > 80 %** → **−20 %** o pausar.
- Mirar el puesto orgánico de 10 keywords de QUICKWIN y de las 3 de contour glow (¿subió?).
- 16-oct: criterio 14,99 → 13,99 (§1). Seguir la cuenta de ventas a 14,99 en la ventana de 90 días para el −33 %.

**No hacer:** reestructurar campañas, cambiar la misma puja dos días seguidos, ni cambiar el precio más de una vez por semana (y menos bajarlo por pocos días: arruina la referencia del −33 %). Historia de AVIE: el error fue el **bucle de sobreoptimización** (`ppc.md`).

## 5 · Qué se espera y cómo se mide
- **HIPÓTESIS:** las long-tail tienen menos competidores pujando → CPC más bajo (0,60-0,90 contra 1,58 actual) y CVR más alto (búsqueda más específica). Si el CPC baja a ~0,80 y el CVR sube al 12 %, cada pedido de ads cuesta ~6,70 USD (hoy 22,60).
- **Señal de que funciona (al 15-oct):** pedidos/día ≥ 6 · CPC promedio ≤ 1,00 · ACOS ≤ 60 % (durante la expansión se acepta por encima del break-even) · 5+ keywords de QUICKWIN que suben ≥ 20 puestos orgánicos.
- **Señal de que no funciona:** ACOS > 100 % con 7 días de datos y ≥ 300 clics → volver al plan de pulsos (`plan-q4-pulsos.md`).
