# REFLEX — Errores de análisis ya corregidos (no re-derivarlos)

> Afirmaciones que circularon y fueron anuladas. **Leer antes de concluir algo nuevo sobre Reflex.**

| Afirmación errónea | Corrección |
|---|---|
| "Ranking orgánico >306 = no traen tráfico" | **`>96` / `>306` es POSICIÓN, no ausencia.** Impresiones, clics y gasto quedan `UNKNOWN`, **no cero** |
| "4 de las 8 keywords P1 no tienen cobertura patrocinada" | **Las 8 tenían gasto real: US$ 1.080,35** |
| "La contaminación (`danny go`, `game stick`, `speed stick`) explica la caída de CVR" | **US$ 13,18 = 0,26 % del gasto.** No la explica |
| "Agosto empeoró vs julio" | Normalizado **por día**: +103 % gasto/día, **+118 % ventas/día**; TACoS 41,77 % → 38,96 %. **Mejoró** |
| Serie diaria construida con el Search Term Report | **No admite serie diaria.** Cualquier curva por día con ese reporte es un artefacto |
| "El CPC explica el ACoS" | ACoS 47,2 % → 72,5 % con **CPC casi plano** y **CVR −27 %**. Son **dos problemas distintos** |
| "Primero campañas, después listing" | **El problema es el listing/conversión.** CVR total −30,5 % > CVR pago −26,6 %. Cuesta **≈US$ 4.470/mes**, casi el doble que todo el PPC |
| "El colapso del 20-ago fue de tráfico" | **No:** sesiones +12,3 %, CVR −26,4 %. El tráfico cae recién en septiembre |
| "2.367 USD/30d recuperables" | Sumaba ventanas y contaba doble. Real: **609,36/30d (12 %)**, neto +484,90 |
| "Auto-targeting propio = 128,46" | **Es 64,47** (64,47 y 63,99 son el mismo hecho) |
| "Los 1.947 USD son contaminantes" | Cero pedidos = 1.991,63 (39,1 %); contaminante sólo **166,99 (8,4 %)** |
| "+245 u y +1.216–2.551 USD/mes" | Es **upside contrafactual máximo**, no forecast |
| "Palos en caída" como main image | Revertido: **CONCEPTO A** (limpio sobre blanco) |
| "Vine antes del 30-sep" | **Vine exige Brand Registry → inejecutable** |
| "A+ bloqueado" | **Basic A+ NO está bloqueado**; sólo Premium exige Brand Registry |
| "Bajar pujas recupera margen sin perder unidades" | Mejora contribución **minimizando** la pérdida de volumen; no la evita |
| Regla de negativos "25 clics" | Reemplazada por **2,6 × contribución pre-ad/u** |
| "Los títulos no están registrados en el vault" | Falso — estaban desde el 29-ago |
| "Amazon prohíbe repetir palabras" | **Falso: permite hasta DOS** |
| Título de QW5 de 140 caracteres | Descartado — tope 75 |
| "Basta con tener todos los tokens" | Separar **indexación / relevancia / ranking / conversión** |
| "En orgánico son gratis" | "La inclusión SEO no tiene ad spend directo" |
| Keyword con 1–2 órdenes "probada" | Escala **ALTA ≥10 · MEDIA 5–9 · BAJA 2–4 · NULA 0–1** |
| "Repetir tokens en backend cuesta cero" | Son bytes que dejan de aportar cobertura |
| Excluir `toy` del título por el seguro | Verdad del producto por encima del underwriting |
| Stock ~4.100 u | ≤3.499 calculado → **3.400 declarado** |
| "El post-mortem apunta a la main de QW5" | Apuntaba al ASIN equivocado: **QW5 mejoró y R46 colapsó** |
| "`b0gr46x8y8` desde QW5 es Paid Core" | Es **product targeting** → PROFIT PPC / CROSS-ASIN CAPTURE |
| "27,99 no tiene downside" | Tolera hasta **−55 %** de caída de unidades; por debajo de 765 u rinde menos que 19,99 |
| "A 19,99 cada unidad genera pérdida" | **Falso:** contribución pre-PPC **+5,26/u**. Lo negativo es el profit after PPC |
| "El settlement no se puede abrir por ASIN" | **Falso (19-sep):** la coma (QW5) y el guion (R46) del título sobreviven al truncado |
| "El recargo por inventario añejo es inevitable" | **Riesgo, no hecho.** Faltan age buckets y pies cúbicos |

## Conflictos numéricos conocidos (misma métrica, distinta base)
- Presupuesto diario: **2.460** (119×20 + 2×40) es el correcto.
- Gasto sin compras W1: 1.829,56 (35,9 %) vs 1.991,63 (39,1 %) — definiciones distintas.
- Términos rentables W1: 176 vs 160 — mismo umbral, conteos distintos.
- Resultado W7: −1.194,80 (caja) vs −1.303,22 (reconstrucción).
- ASP realizado: 19,83 (W1) · 20,29 (W7) · 19,73 (Wx) — **usar el de cada ASIN**.
- Videos de Tendry: 8 vs 14 — sin resolver.
