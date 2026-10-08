# REFLEX — Reflex Challenge Drop Stick Game (Hand Speed Challenge)

> Ecosistema del producto. Lo estable vive acá; lo que cambia, en `ESTADO.md`.
> Antes de trabajar: leer este archivo + `ESTADO.md`. Abrir el resto sólo si la tarea lo pide.

## ⚠️ Objetivo vigente: LIQUIDAR Y SALIR
Desde el 15-sep (confirmado 28-sep): **vender el stock restante y recuperar capital.** Se espera agotarlo hacia **dic-2026**; después Santi **no vuelve a usar ni el producto ni la cuenta KINAVARGAS**.
Toda decisión de precio, PPC, SEO o compliance se juzga contra ese horizonte de salida, **no contra crecimiento**. Muchas decisiones del expediente (septiembre) se escribieron con lógica de construir marca: ver `ESTADO.md` → qué sigue valiendo.

## Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Dónde quedamos, prioridades, decisiones abiertas, lectura de director |
| `compliance.md` | Flag "Children's toys" (plazo 06-dic) + caja física + seguro |
| `historia-19sep.md` | **Lo más nuevo**: foto 19-sep, economía real por ASIN, stock/rotación, resumen |
| `economia.md` | Fórmula de fees, break-even ACoS/CPC, escalera de precio |
| `ventas.md` | Ventas, conversión e inventario por ventana (W1…W8) |
| `ppc.md` | Estructura (110 campañas), 5 problemas de puja, métricas, desperdicio |
| `ppc-keywords.md` | Keywords núcleo, duelo R46 vs QW5, product targeting, harvesting |
| `listing-seo.md` | Listing literal, imágenes, ranks orgánicos, canibalización |
| `competencia.md` | Tendry (líder) y mapa de precios |
| `decisiones.md` | Decisiones DL/D-1…26, acciones aprobadas A-1…20, historial |
| `riesgos.md` | Conflictos abiertos y datos faltantes priorizados |
| `errores-corregidos.md` | Afirmaciones ya anuladas — **no re-derivarlas** |
| `protocolo.md` | DELTA-FIRST y lista de fuentes primarias |
| `assets/caja_retail.jpeg` | Foto de la caja (AGES 3+, internal battery) — en el vault Obsidian |

## Identidad
| Dato | Valor |
|---|---|
| Cuenta | **KINAVARGAS** (ACC-002) · titular Maria Eugenia Vargas · individual · sin Brand Registry |
| ASIN R46 | `B0GR46X8Y8` · marco **AZUL** + palos **AMARILLOS** · alta 4-mar-2026 |
| ASIN QW5 | `B0GQW5F2LL` · marco **AMARILLO** + palos **AZULES** · alta 2-mar-2026 |
| Estructura | 2 ASINs **separados, no fusionados** como variación |
| Marca | "Generic" en Amazon · la caja dice **HM** |
| Caja física | **"AGES 3+" · "FAMILY GAMES" · "INTERNAL BATTERY" · "TYPE-C CHARGE"** · remoto, voz, 3 velocidades |
| Categoría | Amazon la movió (fin ago/mediados sep) a **Toys & Games › Kids' Handheld Games** |
| Título actual (19-sep) | **Ambos:** `Reflex Challenge Drop Stick Game` (32 car., sin sufijo de color) |
| Compra | **5.000 u (2.500/ASIN) por US$ 29.700 → landed 5,94/u** (declarado, provisional) |
| PPC | Agencia externa (nombre UNKNOWN), fee **10 % del ad spend** adicional |

## Economía (resumen — detalle en `economia.md`)
- **Fee Amazon = 4,87 fijo (FBA) + 15 % del precio** (validado contra settlement, ambos ASINs).
- Contribución pre-PPC: 17,99 → 4,48 · 19,99 → 6,18 · 21,99 → 7,88 · 22,99 → ~8,7 · 24,99 → ~10,4 · 27,99 → ~13,0.
- **Precio real por ASIN (25-ago→3-sep):** R46 **20,88** (contrib 7,00/u) · QW5 **19,06** (contrib 5,37/u).
- Break-even ACoS a 19,99 con fee de agencia: **28,1 %** — se compara contra **TACoS**.
- A 19,99 **ningún ASIN es pagable a los CPC observados** (BE CPC QW5 ~0,65 vs real 1,52 · R46 ~0,32 vs 1,04).

## Reglas propias de REFLEX (trampas que ya costaron errores)
1. **Identificar siempre por ASIN, nunca por color.** Los portfolios de Ads están nombrados al revés (R46 = "Yellow").
2. Helium `>96` / `>306` es **posición, no ausencia** de campaña.
3. El Search Term Report **no admite serie diaria**. Para tendencia: Business Report.
4. **Las ventanas de datos no se suman entre sí.** Normalizar por día antes de comparar.
5. **Contribución pre-PPC (decisión de precio) ≠ profit after PPC (decisión de tráfico).**
6. Escala de confianza por keyword: ALTA ≥10 órdenes · MEDIA 5–9 · BAJA 2–4 · NULA 0–1.
7. **No pausar automáticas** (38,7 % de las ventas) · **no reestructurar campañas** antes de Q4.
8. No usar el botón "Update my product listings to fix violations" (reescritura con IA).
9. Lo que se declara al seguro y a Amazon tiene que ser **la misma verdad**, y sigue a la **caja física**.
