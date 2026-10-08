# AVIE — Lymphatic Contour Face Brush · B0GT75CR86

> Ecosistema completo del producto. Lo estable vive acá; lo que cambia, en `ESTADO.md`.
> Antes de trabajar: leer este archivo + `ESTADO.md`. Abrir el resto sólo si la tarea lo pide.

## Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Dónde quedamos, pendientes, fechas, decisiones abiertas |
| `listing.md` | Título, destacado, backend, bullets, atributos, imágenes — copy vigente |
| `aplus.md` | A+ Premium: alt text final, headline/body, pendientes |
| `analisis-2026-10-08.md` | Economía real, caja por mes, PPC 7 días, regla de escala, meta realista de octubre |
| `estrategia-ticket-2pack.md` | Promo "compra 2" vs 2-pack ASIN, números, logística, proyección de stock Q4 |
| `resumen-tarjeta.md` | Cargos de Amazon a la tarjeta del tío (995,63 USD, 25-may→7-oct) y en qué se fue la plata |
| `plan-octubre-expansion.md` | **Plan vigente de octubre:** expansión, presupuesto diario que se paga con las ventas, 5 campañas, rutina diaria, precio 14,99 → 13,99 → 9,99 (−33 %) |
| `campanas-octubre.csv` | 117 objetivos + 123 negativas (fuente) → `AVIE_OCT_bulk_carga.xlsx` para subir en Amazon Ads (exactas long-tail, rivales, ASIN, frase, automática de cosecha) |
| `AVIE_OCT_bulk_carga.xlsx` · `scripts/generar_bulk.py` | Archivo masivo de Amazon Ads (259 filas) y el script que lo arma desde el CSV |
| `plan-q4-pulsos.md` | Plan de pulsos de 8 días (nov-dic o vuelta atrás si octubre falla) |
| `ppc.md` | Plan anterior de 900 USD/mes (versiones A/B) y reglas de PPC heredadas |
| `competencia.md` | Los 9 ASINs rivales, los dos mercados, a quién atacar |
| `keywords.md` | GAP de indexación, ángulo regalo, capas de puja |
| `riesgos.md` | 14 contradicciones/bloqueantes + compliance |
| `datos/` | CSV de Marvin (search terms, Cerebro) · transacciones 25-may→7-oct · portfolios 7 días · plan HTML del 21-sep |
| `assets/aplus/` | 10 imágenes finales del A+ Premium (5 desktop + 5 mobile) |

## Identidad
| Dato | Valor |
|---|---|
| ASIN · SKU | B0GT75CR86 · `avie 011` · https://www.amazon.com/dp/B0GT75CR86 |
| Mercado | Amazon.com (US) · USD · sales tax lo recauda Amazon |
| Cuenta | **Beauty Michele** — vendedor individual, persona natural (Luján de Cuyo) |
| Propiedad | Santi **50/50 con su pareja** |
| Marca | AVIE · campo Brand = **"Generic"** · **sin Registro de Marca** (IP Accelerator en trámite) |
| Categoría · nodo | Beauty #159.716 · Contour Brushes #122 · nodo `face-contour-brushes` (**correcto, NO TOCAR**) |
| Diferenciadores | Color **pink** (todos los rivales son marrón/negro) · **estuche rígido** (regalo) |
| Variaciones · límite compra | ninguna · 5 uds/pedido (rivales: 30) |
| A+ | subido 2026-09-16, aparece como **A+ Premium** (verificar cómo, sin Brand Registry) |
| Proveedor | Dongguan Songli Plastic Industry Co., Ltd. |

## Economía por unidad (corregida 2026-10-08 con transacciones reales → `analisis-2026-10-08.md`)
- **Costo puesto en FBA: 2,86 USD** (producto 2,50 + 3PL 0,36) · lote: 5.000 uds = 14.300 USD
- **FBA 3,24 si el precio < 10 USD · 4,09 si ≥ 10 USD** (HECHO: tarifas por pedido en transacciones) · comisión Beauty **8 % hasta 10,00, 15 % por encima** · con cupón, la comisión se cobra sobre el precio lleno · cupón: 5 USD + % de ventas

| Precio | Tarifas Amazon | Margen/ud | **Break-even ACOS** | ROAS mín. |
|---|---|---|---|---|
| 9,99 | 4,04 | 3,09 | 30,9 % | 3,23 |
| 12,99 | 6,04 | 4,09 | 31,5 % | 3,17 |
| 13,99 | 6,19 | 4,94 | 35,3 % | 2,83 |
| **14,99** | 6,34 | **5,79** | **38,6 %** | **2,59** |
| 16,99 | 6,64 | 7,49 | 44,1 % | 2,27 |
| 17,99 | 6,79 | 8,34 | 46,4 % | 2,16 |

**Zona muerta 10,00-11,80:** te pagan menos que a 9,99 (5,25 a 10,99 contra 5,95 a 9,99). No usar.

**El precio es la palanca, no el PPC.** Vendía más caro y más rápido: mayo 134 + junio 346 uds a 12,99-13,99; ago-sep a 9,99 → 104/mes.

## Foto base (al 15-sep-2026)
| Dato | Valor |
|---|---|
| Stock FBA | 3.778 uds → **≈10.805 USD de capital inmovilizado** |
| Velocidad | ≈5 uds/día (104 últimos 30 días) → **~755 días de rotación** |
| PPC 4-ago→15-sep | gasto 1.204,87 · ventas 1.321,39 · **ACOS 91,2 %** · 347,62 USD en 209 términos sin venta |
| CPC · CTR · CVR | 1,05 · **1,38 %** · 10,3 % |
| Reseñas · devoluciones | 38 · 4,4★ · devoluciones 3,7 % (el producto no es el problema) |
| Orgánico | top 50 en sólo **0,34 %** del volumen del nicho |

**El número que manda es el capital parado (10.805 USD), no el ACOS.**

## Objetivo declarado (2026-09-16)
Vender el máximo **por vía orgánica**, a precio **> 14,99 USD**, subiendo de a poco. Límite **31-dic-2026**.
- **Octubre = expansión** (decisión de Santi 2026-10-08): se aceptan quemar unidades y margen para posicionarse; los ads se pagan con lo que entra de los pedidos → `plan-octubre-expansion.md`.
- Presupuesto ads: **piso 500 USD/mes con la tarjeta; sin tope si el ROAS lo paga desde el saldo** (regla de escala en `analisis-2026-10-08.md` §5). (Antes: 900 USD en octubre.)
- Señal de victoria del dueño: 50 uds/día nov · 80-100/día Navidad · 2.000 uds dic · TACOS 5 % dic.
- **Acta de discrepancia (vigente):** con 900 USD en oct, el análisis proyecta **≈1.380 uds en Q4**, TACOS 25-30 %, ≈2.400 uds en stock al 31-dic, cierre real ~31-mar-2027.
- **Ángulo:** REGALO FEMENINO (62 kw · 74.747 búsq./mes · nadie en el nicho lo trabaja).
- **Revisión fija: LUNES, 45-60 min.**

## Reglas propias de AVIE
- Título ≤ 74 caracteres (si no, Amazon oculta el "Destacado del artículo").
- No usar "Natural Material" mientras el atributo Material diga "Plastic".
- "Gift for Her" fuera de la cabecera → Recommended Uses, bullet 5, alt text, A+.
- No perseguir `contour brush` ni `face mask brush` (otra intención de compra).
- Excels previos entregados (fuera de esta carpeta): Plan_AVIE_Ejecutar_para_Sole.xlsx, AVIE_Cuaderno_Semanal.xlsx, AVIE_Operacion_Despertar.xlsx.
