# AVIE — Semáforo de las campañas que ya existen (2026-10-08)

> Fuentes: captura de Marvin del 08-oct (ACOS por campaña y campañas nuevas propuestas) · `datos/2026-10-08_portfolios_7d.csv` · `datos/2026-10_ads_search_terms.csv`.
> 🔴 = pausar / no reactivar · 🟡 = mantener con cambios · 🟢 = mantener. **Todo se pausa, no se archiva** (se puede volver atrás).
> INFERENCIA a confirmar al subir: las 4 campañas nuevas de Marvin están en los portfolios MARVIN1 y "Avie Lymph Drain Pink", que son los únicos que gastaron en los últimos 7 días.

## 🔴 Pausar YA (están activas y pierden plata)
| Campaña | Cómo está | Por qué | Reemplazo en el bulk nuevo |
|---|---|---|---|
| 🔴 `AVIE_PINK_EX_US` | Puja 1,40 · 10 USD/día | Portfolio Pink, 7 días: 101,99 USD → 3 pedidos · **ACOS 227 %** · CPC real 1,82 · CVR 5,4 % → CPC máx. por la regla de Marvin: **0,27** | Las 3 pink que sí vendieron van a `AVIE_OCT_PROBADAS_EX` |
| 🔴 `AVIE_COMP_ASIN_US` | Puja 1,30 · **20 USD/día** | Historial de ASIN targeting: CVR 9,4 %, ACOS 92,6 % → CPC máx. **0,47** | `AVIE_OCT_ASIN`: mismos ASINs + B0G3685P2S, a 0,65 y 3 USD/día |
| 🔴 `AVIE_GEN_EX_US` | 0,50 · 8 USD/día | Puja bien, pero duplica keywords que ya están en el bulk nuevo | `lymphatic contour face brush` (0,50) y `lymphatic face brush` en PROBADAS |
| 🔴 `AVIE_SCULPT_EX_US` | 0,65 · 4 USD/día | Duplica | `face sculpting brush` y `face sculpting brush lymphatic` en QUICKWIN a 0,65 |
| 🔴 Cualquier otra campaña activa dentro de MARVIN1 o "Avie Lymph Drain Pink" | — | MARVIN1, 7 días: ACOS 92 %, CPC 1,32 | La cubre la estructura nueva |

## 🔴 No reactivar (de acuerdo con Marvin)
`SP-(2)-Phrase` 345 % · `SP-(3)-ProductT` 223 % · `SP-(6)-Broad` 217 % · `SP-(7)-Broad` 152 % · `SP-(25)-Broad` 146 % · `SP-(1)-Exact` 143 % · `SP-(2)-Broad` 126 % · `SP-(20)-Broad` 125 % · `SP-(2)-ProductT` 116 % · `SP-(28)-Broad` 109 % · `SP-(4)-Phrase` 104 % · `SP-(1)-ProductT` (FLAHOLD, 8,44 USD por unidad) · `SP-(Complements)` · todas las que gastaron sin vender.
**Por qué no se reactivan aunque el mal resultado haya sido de ejecución:** lo bueno que tenían adentro ya se rescató. Los términos que vendieron están en exacta en `AVIE_OCT_PROBADAS_EX` con puja correcta. Prenderlas de nuevo repite el problema: amplias con puja pareja de 1,05 y sin negativas.

## 🟡 Mantener con cambios (las "redes" que funcionaron)
| Campaña | Dato | Cambio |
|---|---|---|
| 🟡 `SP-(Substitutes)` | 18 pedidos, CTR 4,34 % (la mejor fuente de términos nuevos) | Activar a **3 USD/día**, puja **≤ 0,60** · cargar ASIN negativo **B0FD354L27** (FLAHOLD) · los ASIN que vendan → `AVIE_OCT_ASIN` |
| 🟡 `SP-(CloseMatch)` | CTR 2,97 % | Activar a **2 USD/día**, puja **≤ 0,60** · negativas exactas: `gua sha facial tools`, `kojeva lymphatic face brush`, `contour brush`, `face mask brush`, `facial brush` |
| 🟡 `SP-(LooseMatch)` | Perdía plata | **Dejar pausada.** La reemplaza `AVIE_OCT_AUTO_COSECHA`: amplia a 0,40 con 146 negativas y freno de 25 USD sin venta |

## 🟢 Aplicar (archivo `AVIE_OCT_bulk_carga.xlsx`, 301 filas)
`AVIE_OCT_EMPUJE_EX` 20 · `AVIE_OCT_PROBADAS_EX` 12 · `AVIE_OCT_QUICKWIN_EX` 10 · `AVIE_OCT_RIVALES_EX` 3 · `AVIE_OCT_ASIN` 4 · `AVIE_OCT_DESCUBRIR_PH` 3 · `AVIE_OCT_AUTO_COSECHA` 3 → **55 USD/día + 5 de las dos autos viejas = 60 USD/día (nivel 1)**. Si ya se subió la versión anterior del bulk: subir sólo `AVIE_OCT_bulk_empuje_ex.xlsx`, pausar en PROBADAS `gua sha brush`, `guasha brush for face`, `guasha brush`, `gua sha brush for face`, y en RIVALES `contour glow brush`, `contour glow face brush`, `contour glow brush for face`, y llevar los presupuestos a los del nivel 1.

## 🟡 Presupuesto de Marvin (126 USD/día): no de entrada, sí como techo
Corrección del 08-oct tras la objeción de Santi: los 126 USD/día quedan como **nivel 3 (techo)** de una escalera que arranca en **60** y sube sólo si el TACOS de 3 días queda ≤ 55 %, es decir, si lo que paga Amazon por las ventas cubre la publicidad (`plan-octubre-expansion.md` §2). Tope de quema: 3.460 USD (400 unidades).

## Orden para hacerlo (15 minutos)
1. Pausar las 4 🔴 de Marvin (y cualquier otra activa en MARVIN1 o Pink).
2. Subir `AVIE_OCT_bulk_carga.xlsx` (Amazon Ads → Masivo → subir). Si alguna fila da error, mandar captura.
3. Crear el portfolio "AVIE OCT" y mover ahí las 6 nuevas más SP-(Substitutes) y SP-(CloseMatch).
4. Activar las 2 🟡 con su presupuesto, puja y negativas.
5. Al día siguiente: informe de términos de búsqueda → primera rutina.
