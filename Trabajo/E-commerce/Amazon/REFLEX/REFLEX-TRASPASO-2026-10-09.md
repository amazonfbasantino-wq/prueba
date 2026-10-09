# REFLEX — Traspaso completo a la sesión local (2026-10-09)
> Un solo archivo con todo el ecosistema de Reflex Game (KINAVARGAS). Es una **copia de lectura** armada desde la carpeta `Trabajo/E-commerce/Amazon/`: si hay diferencias, mandan los archivos originales. Para trabajar, editar los originales, no este.
## Arranque rápido para la sesión local
1. Objetivo: **liquidar las ~3.700 u y recuperar los US$ 30.000**. Corte: **02-nov-2026** (seguro obligatorio para categorías *enhanced safety*; sin póliza se desactivan los listings).
2. Lo primero: hacer la sección **"SIGUIENTE SESIÓN — local, con Claude in Chrome"** del ESTADO (§3 abajo): relevar precios, competencia y página 1 en amazon.com **como comprador**.
3. **Regla dura:** en la compu/Chrome/IP de Santi **nunca** entrar a Seller Central ni Ads de KINAVARGAS (riesgo de cuentas relacionadas con DecoHOUSE). Ventas, campañas y aviso del seguro salen de la compu de Eugenia.
4. Nada se ejecuta en Seller Central ni Ads sin OK puntual de Santi.
5. Pendientes clave: decidir seguro sí/no · precio de salida 22,99 vs 16,99 · pujas (hoy todo a US$ 0,10 desde el 06-oct) · cotizar B2B para el remanente.

## Índice
1. Contexto madre Amazon (quién soy, reglas duras) — `../Amazon/CLAUDE.md`
2. REFLEX — identidad, economía, reglas — `REFLEX/CLAUDE.md`
3. REFLEX — estado actual (09-oct) — `REFLEX/ESTADO.md`
4. Plan de salida con corte 02-nov + guía de Marvin — `REFLEX/plan-salida-2nov.md`
5. Compliance: flag Children's toys, caja, seguro — `REFLEX/compliance.md`
6. Cuenta KINAVARGAS — datos — `_CUENTA-KINAVARGAS/CLAUDE.md`
7. Cuenta KINAVARGAS — estado — `_CUENTA-KINAVARGAS/ESTADO.md`
8. Cuenta KINAVARGAS — seguro — `_CUENTA-KINAVARGAS/seguro.md`
9. Historia y foto al 19-sep — `REFLEX/historia-19sep.md`
10. Economía unitaria y precio — `REFLEX/economia.md`
11. Ventas y conversión por ventana — `REFLEX/ventas.md`
12. Competencia — `REFLEX/competencia.md`
13. Listing y SEO — `REFLEX/listing-seo.md`
14. PPC — estructura y desperdicio — `REFLEX/ppc.md`
15. PPC — keywords — `REFLEX/ppc-keywords.md`
16. Decisiones y acciones — `REFLEX/decisiones.md`
17. Riesgos y datos faltantes — `REFLEX/riesgos.md`
18. Errores ya corregidos (no re-derivar) — `REFLEX/errores-corregidos.md`
19. Protocolo DELTA-FIRST y fuentes — `REFLEX/protocolo.md`

---

## 1. Contexto madre Amazon (quién soy, reglas duras)

_Fuente: `Trabajo/E-commerce/Amazon/CLAUDE.md`_

## AMAZON — contexto madre (Claude Code)

> Claude Code carga este archivo solo. Cada subcarpeta tiene su propio `CLAUDE.md` con el ecosistema de UN producto.
> Abrí Claude Code **dentro de `AMAZON/`** y trabajá en la carpeta del producto que toque. No leer otras carpetas salvo que la tarea lo pida.

### Quién soy y a dónde voy
- **Santi** (Santino Navarria) · Mendoza, Argentina · vendedor Amazon FBA en **Amazon.com (US)** desde fines de 2023.
- **Visión:** empresa en Amazon con catálogos enteros → primer millón facturado.
- **Meta de corto plazo:** USD 100.000 de **beneficio neto** al 31-dic-2026 (después de producto, fees, envío, ads e impuestos).

### Cuentas y entidades
| Cuenta / entidad | Qué es | Productos |
|---|---|---|
| **Beauty Michele** | Vendedor individual, persona natural, titular en Luján de Cuyo (Mendoza) · titular: tío de Santi · operada por Santi | AVIE (50/50 con mi pareja) · MT Ball (en preparación) |
| **KINAVARGAS** (ACC-002) | Titular Maria Eugenia Vargas, esposa del socio (no es parte de la LLC) · operada por Santi | KINA (discontinuado), Reflex Game (liquidación) |
| **DecoHOUSE** (cuenta personal de Santi) | Desactivada permanente por Sección 3 (08-feb-2026, batería 510 / vape) → `../TERPTECH/_CUENTA-DECOHOUSE/` | — (TerpTech, prohibido) |
| **VIRTUALMED SOLUTIONS LLC** | LLC de Florida (domicilio Sarasota) · miembros: Santi + Pablo · banco: Bank of America | — |
| Socio externo | Maxi (vive en Utah) | MT Ball |

### Mapa de carpetas
| Carpeta | Producto | ASIN | Estado de la mudanza |
|---|---|---|---|
| `AVIE/` | AVIE Lymphatic Contour Face Brush | B0GT75CR86 | ✅ migrado 2026-10-06 |
| `MT-BALL/` | MT Ball (meta ball, con Maxi) | — | ✅ migrado 2026-10-06 |
| `REFLEX/` | Reflex Game (KINAVARGAS) · **modo liquidación** | B0GR46X8Y8 · B0GQW5F2LL | ✅ migrado 2026-10-06 |
| `KINA/` | KINA Lymphatic Drainage Face Brush · **liquidación fuera de Amazon** | B0GQJLP4TB | ✅ migrado 2026-10-06 |
| `../TERPTECH/` | TerpTech: **fuera de Amazon** (prohibido) · ecosistema propio en `E-commerce/TERPTECH/` | B0F9SXP5MW | movido 2026-10-08 |
| `_CUENTA-KINAVARGAS/` | Cuenta KINAVARGAS: titular, seguro, casos, reglas | — | ✅ migrado 2026-10-06 |
| `../TERPTECH/_CUENTA-DECOHOUSE/` | Cuenta bloqueada de Santi: motivo, fondos retenidos, apelación | — | ✅ 2026-10-08 desde Gmail |
| `_ARCHIVO/` | Los dos vaults de Obsidian completos, en crudo (sólo consulta) | — | ver `_ARCHIVO/LEEME.md` |

### Estructura de cada producto
Cada carpeta tiene siempre `CLAUDE.md` (lo estable: identidad, economía, objetivo, reglas) y `ESTADO.md` (dónde quedamos, prioridades, decisiones abiertas; se actualiza al cerrar cada sesión). El resto son archivos temáticos chicos (listing, ppc, keywords, competencia, riesgos…) listados en el `CLAUDE.md` de cada producto. Imágenes y datos en `assets/`.
Regla: **WRITE ONCE — REFERENCE MANY.** Un dato vive en un solo archivo; los demás apuntan.

### Dónde está todo
- **Carpeta local `Trabajo/E-commerce/Amazon/` en la compu de Santi** (Finder): **copia de trabajo para Claude Code** (versión condensada; manda ante diferencias). **Google Drive `AMAZON/`** = copia espejo para que Claude la lea desde Cowork/app; mantenerla al día.
- Vault Obsidian `obsidian c` → `AMAZON/`: misma estructura, versión extendida de algunas tablas, más las imágenes.
- `_ARCHIVO/`: los dos vaults completos en crudo (`obsidian c` y `PROYECTOS 100K`: CSV, imágenes, expedientes viejos), leídos directo desde la compu. **Sólo consulta**; ante diferencias manda esta carpeta.

### Cómo quiero que trabajes
- Actuá como **director comercial / dueño del capital**, no como analista. Cada métrica → impacto en dinero: cuánto, dónde se pierde, qué variable cambiar, cuánto vale corregirla.
- Formato para cada problema importante: **HECHO → CAUSA PROBABLE → IMPACTO → PALANCA → DECISIÓN EMPRESARIAL → DATO FALTANTE.** Separar HECHO / INFERENCIA / HIPÓTESIS.
- Priorizar por **impacto económico × probabilidad de éxito × velocidad × reversibilidad**.
- Pensar en capital invertido, retorno sobre capital, contribution margin, cash flow, rotación, riesgo y escalabilidad. Nunca tráfico, clic, conversión, economía y escala como variables aisladas.
- **No ser pasivo:** señalá oportunidades que no pregunté y decime cuándo una hipótesis o decisión mía está mal.
- **No inventar hechos:** lo que no está en los archivos o no lo dije yo, se marca como hipótesis o se pregunta. No escribir suposiciones como si fueran datos.
- Análisis importante = **dos capas**: (1) completo, guardado en el archivo del producto; (2) resumen ejecutivo en el chat (situación, 3-5 hallazgos, impacto, riesgos, recomendación, datos faltantes). No repetir en el chat lo que ya quedó guardado.
- Respuestas en **español**, estructuradas, listas para copiar y pegar.
- **Lo guardado no se pregunta:** se lee del archivo y se sigue.
- **Máximo 2 frentes EN CURSO** a la vez.
- **Tokens mínimos:** leer sólo el archivo y la sección necesaria. Nada de tareas programadas ni actualizaciones en tiempo real.

### Reglas duras (todas las cuentas)
- **Nunca ejecutar cambios en Seller Central ni en Amazon Ads sin mi autorización explícita y puntual.** Investigar, calcular y escribir en los archivos: sí.
- Marcas ajenas: **prohibidas** en título, bullets y backend · **permitido** pujar por ellas en PPC.
- Términos temporales ("christmas"): no en título ni backend; sí en Recommended Uses y bullets.
- Sin claims médicos en campos indexables ("reducer", "lymph node", "detox", "elimina toxinas").
- Lo que se declara a Amazon, al seguro y en la caja tiene que ser **la misma verdad**.
- Cuidado con phishing de falso soporte Amazon (ej. dominio esc-amazon.com): Amazon sólo se contacta desde Seller Central.

### Al cerrar cada sesión
Actualizar `ESTADO.md` del producto: qué se hizo, qué sigue (en orden), qué NO hacer, y la fecha.

---

## 2. REFLEX — identidad, economía, reglas

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/CLAUDE.md`_

## REFLEX — Reflex Challenge Drop Stick Game (Hand Speed Challenge)

> Ecosistema del producto. Lo estable vive acá; lo que cambia, en `ESTADO.md`.
> Antes de trabajar: leer este archivo + `ESTADO.md`. Abrir el resto sólo si la tarea lo pide.

### ⚠️ Objetivo vigente: LIQUIDAR Y SALIR
Desde el 15-sep (confirmado 28-sep): **vender el stock restante y recuperar capital.** Se espera agotarlo hacia **dic-2026**; después Santi **no vuelve a usar ni el producto ni la cuenta KINAVARGAS**.
Toda decisión de precio, PPC, SEO o compliance se juzga contra ese horizonte de salida, **no contra crecimiento**. Muchas decisiones del expediente (septiembre) se escribieron con lógica de construir marca: ver `ESTADO.md` → qué sigue valiendo.

### Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Dónde quedamos, prioridades, decisiones abiertas, lectura de director |
| `plan-salida-2nov.md` | **Vigente 08-oct:** corte 02-nov, plan agresivo, escenarios con/sin seguro |
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

### Identidad
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

### Economía (resumen — detalle en `economia.md`)
- **Fee Amazon = 4,87 fijo (FBA) + 15 % del precio** (validado contra settlement, ambos ASINs).
- Contribución pre-PPC: 17,99 → 4,48 · 19,99 → 6,18 · 21,99 → 7,88 · 22,99 → ~8,7 · 24,99 → ~10,4 · 27,99 → ~13,0.
- **Precio real por ASIN (25-ago→3-sep):** R46 **20,88** (contrib 7,00/u) · QW5 **19,06** (contrib 5,37/u).
- Break-even ACoS a 19,99 con fee de agencia: **28,1 %** — se compara contra **TACoS**.
- A 19,99 **ningún ASIN es pagable a los CPC observados** (BE CPC QW5 ~0,65 vs real 1,52 · R46 ~0,32 vs 1,04).

### Reglas propias de REFLEX (trampas que ya costaron errores)
1. **Identificar siempre por ASIN, nunca por color.** Los portfolios de Ads están nombrados al revés (R46 = "Yellow").
2. Helium `>96` / `>306` es **posición, no ausencia** de campaña.
3. El Search Term Report **no admite serie diaria**. Para tendencia: Business Report.
4. **Las ventanas de datos no se suman entre sí.** Normalizar por día antes de comparar.
5. **Contribución pre-PPC (decisión de precio) ≠ profit after PPC (decisión de tráfico).**
6. Escala de confianza por keyword: ALTA ≥10 órdenes · MEDIA 5–9 · BAJA 2–4 · NULA 0–1.
7. **No pausar automáticas** (38,7 % de las ventas) · **no reestructurar campañas** antes de Q4.
8. No usar el botón "Update my product listings to fix violations" (reescritura con IA).
9. Lo que se declara al seguro y a Amazon tiene que ser **la misma verdad**, y sigue a la **caja física**.

---

## 3. REFLEX — estado actual (09-oct)

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/ESTADO.md`_

## REFLEX — ESTADO

**Actualizado:** 2026-10-08 · **Último dato:** series al 16-sep, listings al 19-sep, Account Health al 28-sep · stock declarado por Santi 08-oct · **Modo:** LIQUIDACIÓN AGRESIVA con corte 02-nov

### 🔻 Cambio 2026-10-08 — corte 02-nov y modo agresivo (análisis completo: `plan-salida-2nov.md`)
- Santi: **activo hasta el 02-nov** · **3.700 u** · meta **recuperar US$ 30.000** · ser agresivos.
- El 02-nov es la regla nueva de Amazon: seguro US$ 1M obligatorio para *enhanced safety* (infantil + batería) sin umbral de ventas → sin póliza se desactivan los listings (reversible, el stock queda en FBA). Plazo exacto (¿fecha dura o 45 días desde el email?) **sin confirmar**.
- **Hallazgo central:** el pico (BF 27-nov, diciembre) cae **después** del corte. Sin seguro las 3.700 u rinden ~US$ 10–14k; con seguro ~US$ 27–30k. **El seguro vale ~US$ 14–18k** → reabrir la decisión esta semana.
- Costo hundido: cada unidad se compara contra su valor fuera de Amazon (~2–4 B2B), no contra 5,94. **Sin seguro, la escalera de subida queda anulada**: bajar precio (QW5 16,99 · R46 14,99) + cupón + PPC sólo en exact de CVR ≥ 20 % (tope ~6,5/pedido).
- **3.700 no cierra** con 5.000 − 1.501 vendidas al 04-sep (máx. 3.499) → C-28 se agrava.
- **09-oct · guía de Marvin (06-oct):** todas las pujas están a **US$ 0,10** desde el 06-oct (≈ PPC apagado, y PPC era ~70 % de las unidades) · plan: 2 automáticas nuevas a 2×S +40 % TOS, pausar LooseMatch, ataque a Hot Dog Drop `B0FZK1DD6D` · pujas pensadas para ROAS 3 a 22,99 (lógica de margen, no de liquidación) · revisión a 15 días no entra antes del 02-nov. `reflex challenge game` de QW5 cayó de #1 a **#12** orgánico. Detalle y topes de puja: `plan-salida-2nov.md` §9.

### SIGUIENTE SESIÓN — local, con Claude in Chrome (en el Chrome de Santi)
**Regla dura:** en el Chrome / compu / IP de Santi **sólo navegar amazon.com como comprador** (páginas públicas). **Nunca entrar a Seller Central ni Ads de KINAVARGAS desde ahí**: es la vía de vínculo con DecoHOUSE (cuentas relacionadas, ver `../../TERPTECH/_CUENTA-DECOHOUSE/ESTADO.md`). Lo de Seller Central (ventas, campañas, aviso del seguro) sale de la compu de Eugenia como export/captura.

Relevar y guardar en `competencia.md` (foto con fecha):
1. QW5 `B0GQW5F2LL` y R46 `B0GR46X8Y8`: precio, cupón, deal, rating/reviews, "bought in past month", BSR, título, imágenes, variantes, Buy Box.
2. Competencia: Tendry `B0DLN5C44D` · Hot Dog Drop `B0FZK1DD6D` · ATG `B0DYNYMZHR` (US$ 26,99 en la web, sin fecha) · los que aparezcan arriba.
3. Página 1 de `reflex drop sticks game`, `reflex challenge game`, `reaction time game`: quién ocupa patrocinados y orgánicos, rango de precios, cupones, deals de Q4.
4. Con eso: decidir precio de salida (22,99 vs 16,99) y topes de puja (`plan-salida-2nov.md` §9).

### ⚠️ Primero: confirmar (todo lo posterior al 28-sep es UNKNOWN)
1. **Stock FBA por ASIN hoy** (disponible / reservado / en tránsito). Conflicto: 3.400 u el 15-sep vs **3.550 u** citadas el 28-sep.
2. **Precio vigente de cada ASIN** y ventas de los últimos 30 días por ASIN.
3. ¿Qué pasó con el **seguro** (venció el 01-oct)? ¿Amazon mandó algún aviso nuevo?
4. ¿Se avanzó con el **flag "Children's toys"** de QW5 (plazo 06-dic)? ¿Se pidieron tests?
5. ¿La agencia sigue? ¿Se ejecutó algo del takeover del 14-sep?

### La cuenta de la liquidación (estimación — validar con el dato 1)
| | |
|---|---|
| Stock 15-sep | 3.400 u (1.700/ASIN) |
| Velocidad medida | ~17–21 u/día total (992 pedidos FBA en 60 d al 28-sep · 643 u en 30 d al 15-sep) |
| Stock estimado hoy | **~3.000 u ≈ US$ 17.800 de capital** a 5,94 |
| Días al 31-dic | 86 |
| **Ritmo necesario para salir en diciembre** | **~35 u/día ≈ 2× el actual** |
| Rotación por ASIN (27-ago→14-sep) | QW5 8,4 u/día → 203 días · **R46 1,8 u/día → ~950 días** |

**Q4 puede dar ese salto** (Tendry vendió 7.303 u en un mes de temporada a 29,99 vs 723 en agosto), pero sólo si QW5 sigue publicado y R46 deja de ser stock muerto.

### Prioridades (impacto × probabilidad × velocidad × reversibilidad)
1. **Salvar QW5 del flag "Children's toys" antes del 06-dic** → `compliance.md`. QW5 es el ASIN que vende (≈2/3 de las unidades, US$ 10.834 de GMS en riesgo) y el plazo cae en pleno pico. La caja dice **AGES 3+**: la vía honesta es **laboratorio (ASTM F963-23 + CPSIA + CPC)**, no reclasificar a 14+.
2. **Resolver el seguro** (venció el 01-oct). Detalle en el paquete de la cuenta KINAVARGAS. Una suspensión en noviembre congela las ~3.000 u.
3. **Plan de salida para R46** (1.700 u, ~950 días al ritmo actual = el verdadero stock muerto, ≈ US$ 10.000).
4. **Escalera de precio sólo si no frena la salida:** 22,99 (20-oct) → 24,99 (10-nov) → 27,99 condicional, con regla de corte: si las u/día caen >25 % o quedan por debajo del ritmo necesario, se vuelve al escalón anterior.
5. **Cortar desperdicio de PPC** (≈ US$ 2.100/mes): recorte −70 % de las dos `SP-(LooseMatch)` + lista DO NOT BID de product targeting. Sin tocar estructura ni automáticas sanas.

### Qué sigue valiendo y qué cambia con el objetivo de salir
| Decisión de septiembre | Con objetivo LIQUIDAR |
|---|---|
| Escalera de precio 22,99 → 27,99 | **Vale, condicionada a velocidad** (la salida manda sobre el margen) |
| No romper con la agencia ahora | Vale — cambiar de manos a semanas del pico es riesgo |
| No pausar automáticas / no reestructurar | Vale |
| 3 core ranking keywords + ficha de ranking investment + blindaje (−375/mes) | **Pierde sentido** salvo que se pague dentro de Q4: no se invierte en ranking que se abandona en enero |
| Fusionar R46 + QW5 como variación (antes "baja reversibilidad") | **Reabrir:** la irreversibilidad pesa poco si la cuenta se abandona en diciembre, y R46 heredaría la página de QW5 (rating 4,1, #1 en `reflex challenge game`). Verificar riesgo antes |
| Main image CONCEPTO A, A+ Basic, backend nuevo | Sólo si se ejecuta antes de noviembre; después no se amortiza |
| Título de QW5 (A-18) | **Obsoleto:** Amazon dejó ambos títulos en 32 car. el 4–14 sep |

### Decisiones abiertas (de Santi)
- **Precio vigente (¿22,99?) y precio de salida:** 22,99 con PPC fuerte vs 16,99 con PPC fino (§9.5).
- Reactivar las manuales ganadoras con tope de CPC por CVR, en vez de dejarlas a 0,10.
- **¿Seguro sí o no antes del 02-nov?** Define plan A (vaciar en octubre + B2B) o B (vender Q4 completo). Ver `plan-salida-2nov.md` §5.
- Autorizar plan A: precio QW5 16,99 / R46 14,99, cupón 10–15 %, PPC agresivo con tope, y cotizar 3 compradores B2B ya.
- Vía de compliance de QW5 (y R46, que tiene la misma caja): laboratorio sí/no y quién es el importador de registro (a su nombre va el CPC).
- Qué hacer con el remanente que quede el 1-ene: liquidación de Amazon, removal + venta fuera de Amazon, o seguir en 2027 (contradice la salida).
- Fusión R46 + QW5.
- Autorizar la escalera de precio (D-25) y el recorte de LooseMatch (D-13).

### No hacer
Ejecutar en Seller Central o Ads sin OK puntual · pausar automáticas · reestructurar campañas · usar el botón de IA de Amazon para "arreglar" el listing · declarar al seguro algo distinto de lo que dice la caja.

### Historial
- 2026-10-09 · La sesión en la nube no puede usar el Chrome de Santi ni abrir amazon.com (red bloqueada). Próxima sesión: local con Claude in Chrome, sólo páginas públicas.
- 2026-10-09 · Revisado Gmail cemar4025 (últimos 60 d): es el mail de **DecoHOUSE**, no de KINAVARGAS. No hay avisos de Amazon de KINAVARGAS (seguro 02-nov, flag, ventas) ni reenvíos desde vargaseugenia82 (último mail de ella: 15-sep). El aviso del seguro hay que sacarlo de Seller Central o del Gmail de Eugenia.
- 2026-10-09 · Leída la guía de Marvin (06-oct): pujas a 0,10, automáticas nuevas, Hot Dog Drop. Cruce con el corte del 02-nov en `plan-salida-2nov.md` §9. El CSV de Cerebro recibido es de Kitsch (AVIE), no de Reflex.
- 2026-10-08 · Corte 02-nov + 3.700 u + meta 30k. Investigación del cambio de seguro de Amazon y del mercado (Walmart US$ 10,6–21,4). Plan A/B y escenarios en `plan-salida-2nov.md`. Nada ejecutado.
- 2026-10-06 · Migrado a `AMAZON/REFLEX/` desde el vault PROYECTOS 100K (índice 17-sep + historia 19-sep) y el expediente de seguro (28-sep). Caja revisada: AGES 3+, batería interna.
- 2026-09-28 · Flag "Children's toys" en QW5 (aviso del 22-sep, plazo 06-dic). Objetivo confirmado: liquidar y salir.
- 2026-09-19 · Títulos de ambos ASINs reducidos a 32 car. sin color. QW5 lidera (BSR #153, 4,1★) · R46 cae (#288, 3,8★).
- 2026-09-15 · Stock confirmado 1.700/SKU. Cambio a modo liquidación. Inversión de ASINs (QW5 > R46).
- 2026-09-14 · Takeover de Ads por Santi (sin registro de ejecución).
- 2026-09-07/08 · Auditoría de agencia, decisiones DL-1…D-24.

---

## 4. Plan de salida con corte 02-nov + guía de Marvin

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/plan-salida-2nov.md`_

## REFLEX — Plan de salida agresivo con corte 02-nov-2026

> Sesión 2026-10-08. Datos nuevos de Santi: **stock 3.700 u** · **activo hasta el 02-nov** · objetivo **recuperar el capital (US$ 30.000 por las 5.000 u)** · modo **agresivo**.
> Etiquetas: HECHO · ESTIMACIÓN · HIPÓTESIS. Nada de esto está ejecutado en Seller Central ni en Ads.

### 1 · Por qué el 02-nov (HECHO externo)
Desde el **02-nov-2026** Amazon exige seguro CGL US$ 1M/1M a **toda** publicación en categorías *enhanced safety* (productos infantiles, baterías de litio), **sin importar el volumen de ventas**. Reflex cae en las dos (caja AGES 3+ e INTERNAL BATTERY). Sin prueba de seguro, **se desactivan los listings de esas categorías** (acción a nivel listing, no suspensión de cuenta; reversible al subir la póliza).
- Ventana para subir la prueba: fuentes secundarias hablan de **45 días desde el email de Amazon**, otras toman el 02-nov como fecha dura. **No confirmado contra el aviso de Amazon** → ver el email/Account Health de KINAVARGAS. Si el reloj corre desde el email, el corte real puede caer a mitad de diciembre.
- El inventario **no se pierde**: queda varado en FBA (cobra almacenaje) hasta remover, liquidar o reactivar.

### 2 · El hecho que cambia todo el plan: el pico está DESPUÉS del corte
- Tendry (líder) vendió **7.303 u en el mes de temporada a 29,99** vs **723 u en agosto a 18,99** (≈10×). Black Friday cae el **27-nov**, Cyber Monday el **30-nov**, diciembre es regalo.
- Cortar el 02-nov = vender **octubre (pre-temporada, ritmo de agosto/septiembre)** y perder **todo** el trimestre que justificaba tener 3.700 u.
- **Lectura de director:** el seguro no es un trámite de la cuenta; es la decisión que vale más plata de todo REFLEX (ver §5). Si Santi ya decidió no asegurar, el plan es §4; si no está cerrado, hay que reabrirlo **esta semana**.

### 3 · Reencuadre económico: el costo es hundido
Los 5,94/u ya se pagaron. Desde hoy cada unidad se compara contra **lo que vale fuera de Amazon**, no contra el costo:

| Destino de una unidad | Caja neta/u (ESTIMACIÓN) |
|---|---:|
| Amazon a 19,99 (sin PPC) | **12,12** |
| Amazon a 16,99 | **9,57** |
| Amazon a 14,99 | **7,87** |
| Venta propia fuera de Amazon (eBay / TikTok / MCF) | 6–9, lenta, con su propio riesgo de compliance |
| Lote B2B a revendedores (Walmart 3P vende genéricos a US$ 11–19) | **2–4** después de removal (~1,0–1,5/u) y flete |
| FBA Liquidations de Amazon (5–10 % del valor) | **0,5–1,5** |

Fórmula: caja Amazon = precio − (4,87 + 15 % precio). **Regla de corte:** una unidad vendida en Amazon antes del 02-nov vale la pena mientras `precio − fee − PPC por unidad > ~3` (valor de salida B2B). A 16,99 eso deja **~6,5 de PPC por pedido** de margen; a 19,99, ~9.
→ Bajar precio ya **no destruye valor**: cada unidad que no se vende en octubre vale ~3 en noviembre. La escalera de subida (22,99 → 27,99) **queda anulada si no hay seguro**.

### 4 · Plan A — sin seguro: vaciar lo máximo antes del 02-nov (25 días)
**Meta:** 1.100–1.500 u en Amazon (45–60 u/día, ~2,5× el ritmo actual) + preparar la salida del resto **en paralelo, no después**.

| # | Palanca | Qué | Por qué |
|---|---|---|---|
| 1 | **Precio por ASIN** | QW5 19,x → **16,99**; R46 → **14,99** (o 15,99). Revisión cada 72 h: si no sube la velocidad ≥ +50 %, otro escalón de −1 | Los dos tienen título idéntico: el más barato capta la búsqueda. R46 es stock muerto (~950 días): que compita por precio |
| 2 | **Cupón visible** 10–15 % en ambos | Badge verde en resultados | Sube CTR en búsqueda; costo fijo bajo (verificar tarifa vigente) |
| 3 | **PPC: más gasto, sólo donde convierte** | Subir presupuesto en exact de CVR ≥ 20 % (`reflex drop sticks game`, `reflex sticks`, `reflex game`, `reaction game`, `reaction time drop sticks`) y en auto sanas. Recorte −70 % a las dos `SP-(LooseMatch)` | Tope de PPC por pedido ~6,5 (a 16,99). A precio más bajo sube la CVR → más keywords pasan a ser pagables |
| 4 | **Deals** | Si la cuenta califica (Professional, rating ≥ 3,5): Prime Exclusive Discount / Best Deal en QW5 durante la última quincena de octubre | Visibilidad de deal sin depender del CPC |
| 5 | **Agencia** | Mandato único por escrito: "vaciar antes del 02-nov, tope de PPC por pedido US$ 6,5" | Su fee (10 %) sólo se justifica si ejecuta esto ya |
| 6 | **Salida del remanente, desde HOY** | Cotizar 3 compradores B2B / liquidadores (lote 1.000–2.500 u) + costo de removal + destino (Miami 2970 NW 75 Ave) | El removal en Q4 tarda semanas: si se pide el 02-nov, el dinero llega en enero |
| 7 | **MCF (HIPÓTESIS a verificar)** | Vender en eBay/TikTok/Shopify despachando desde FBA con Multi-Channel Fulfillment | Si MCF despacha inventario de listings desactivados, evita el removal. Ojo: Walmart y TikTok también piden CPC para juguetes |

**No se toca:** estructura de campañas, automáticas sanas, el botón de IA de Amazon, ni crear listings nuevos (2-pack, variación): un listing nuevo de juguete con batería dispara compliance y seguro igual.

### 5 · Escenarios para las 3.700 u (ESTIMACIÓN — hasta tener stock, precio y ventas reales)

| Escenario | Amazon | Remanente | Caja de las 3.700 u |
|---|---|---|---:|
| **A0 · sin seguro, sin cambios** | 500 u a ~19 · PPC 90/día → ~3.200 | 3.200 u × 1,5–3 | **~8.000–12.800** |
| **A · sin seguro, agresivo (§4)** | 1.125 u a ~16,5 · PPC 150/día → ~6.200 | 2.575 u × 1,5–3 | **~10.000–14.000** |
| **A+ · agresivo + MCF/venta propia** | ~6.200 | ~800 u × 7 + 1.775 × 3 | **~17.000** (si MCF funciona) |
| **B · con seguro antes del corte** | oct: 750 u a 18,99 → ~5.200 · nov–dic: ~2.360 u a 22,99, 40 u/día → ~24.900 | ~590 u × 3 | **~31.900 − seguro (1.000–3.500) − test lab QW5 (500–1.500) ≈ 27.000–30.000** |

**Diferencia B − A ≈ US$ 14.000–18.000.** Un seguro de 1.000–3.500 que destraba eso es la mejor inversión disponible en REFLEX. El test de laboratorio de QW5 (plazo 06-dic) **sólo importa en el escenario B**: sin seguro, el listing muere antes del 06-dic de todos modos.

### 6 · "Recuperar el capital": cuánto falta realmente
- Invertido en mercadería: **US$ 29.700** (5.000 × 5,94). PPC acumulado no consolidado: ~US$ 10.000–12.000 más.
- Ya cobrado: **desconocido**. Hasta el 04-sep se vendieron 1.501 u por US$ 28.009 brutos (≈ 16.500 después de fees, antes de PPC). Del 04-sep al 08-oct no hay serie.
- **HIPÓTESIS:** caja neta acumulada después de PPC ≈ US$ 10.000–13.000 → faltarían **~17.000–20.000**.
- Con eso: **el escenario A no recupera el capital; el B sí (o queda muy cerca).** Confirmar con la suma de depósitos (Pagos → Todos los extractos, mar→hoy).

### 7 · Conflicto de stock (C-28, se agrava)
5.000 compradas − 1.501 vendidas al 04-sep = **3.499 como máximo** ese día. Después hubo más ventas (≈17–21 u/día) y un removal (US$ 3.774,96). **3.700 hoy no cierra** contra eso. Lecturas posibles: (a) cifra de memoria; (b) incluye unidades fuera de FBA (¿las del removal, en Miami?); (c) incluye devoluciones/no vendibles; (d) error en una serie anterior. **El plan no cambia de signo, pero cuánto se liquida fuera de Amazon depende de esto.**

### 8 · Datos que faltan (en orden)
1. **Seguro:** ¿se decidió no asegurar? ¿Llegó el email de Amazon por el 02-nov y qué plazo da? ¿Respondió Sadler / algún broker con cotización?
2. **Informe de inventario FBA por ASIN** (disponible / reservado / no vendible / en tránsito) + dónde están las unidades del removal.
3. **Precio vigente y ventas de los últimos 30 días por ASIN** (Business Report).
4. **Total depositado desde marzo** (para medir cuánto capital falta).
5. Si la cuenta es Professional y califica para Deals / Prime Exclusive Discount.

### Fuentes externas (consultadas 08-oct)
- Seller Forums: "New Commercial Liability Insurance Requirements effective November 2, 2026" · EcommerceBytes 10-sep-2026 · SellerEssentials / NVINC (45 días, nivel listing) · PPC Land (plazo no explícito en el aviso).
- Precios Walmart (genéricos con control remoto US$ 10,59–21,38, varios en liquidación).
- FBA Liquidations: recupero bruto típico 5–10 % del valor (Seller Forums).

### 9 · Cruce con la guía de campañas de Marvin (v1.1, 06-oct) — leída 09-oct
**HECHOS (de la guía):**
- El 06-oct Santi dejó **todas las campañas y targets a US$ 0,10**. Con PPC ≈ 70 % de las unidades (W1), eso equivale a **apagar casi toda la publicidad**: la velocidad de octubre probablemente cayó, justo cuando hay que vaciar antes del 02-nov.
- Plan de Marvin: 1 automática nueva por ASIN (`AUTO_<ASIN>_REFLEX-…`), puja **2 × S** (S = sugerida de Amazon, **todavía sin cargar**), pujas fijas, **+40 % top of search**, presupuestos propuestos 20 (QW5) / 15 (R46). Pausar las dos `SP-(LooseMatch)` (coincide con D-13). Resto a 0,10. Revisión a 15 días (→ ~21-oct si arrancó el 06-oct; fecha real de arranque UNKNOWN).
- Ataque a **Hot Dog Drop `B0FZK1DD6D`** (product targeting exacto): QW5 0,75 · R46 0,40 · 10 + 5 US$/día. Lo pidió Santi, no Marvin. Pujas calculadas para **ROAS 3 a US$ 22,99**.
- Helium 06-oct (sólo QW5), orgánico: `reaction time game` #3 · `drop stick challenge` #10 · **`reflex challenge game` #12 (era #1 en septiembre)** · `reflex drop sticks game` #60 · `reflex game` #83. Patrocinado >96 en casi todo (consistente con pujas a 0,10).

**Dónde choca con el corte del 02-nov:**
1. **ROAS 3 es lógica de margen, no de liquidación.** Con costo hundido, el tope de PPC por pedido es `precio − fee − valor de salida (~3)`, ÷1,10 por la agencia: a 22,99 → **~10,6/pedido (ROAS ≈ 2,2)**; a 16,99 → **~5,4/pedido (ROAS ≈ 3,1)**. A precio alto se puede pujar más agresivo de lo que propone la guía.
2. **Tope de puja por CVR, no por sugerida.** CPC máx = tope/pedido × CVR. QW5 (CVR 13,5 %): ~1,43 a 22,99 · ~0,73 a 16,99. R46 (6,9 %): ~0,73 · ~0,37. **2 × S con +40 % arriba puede superarlo** si S > ~0,50 (QW5 a 16,99) o > ~1,00 (QW5 a 22,99). Usar `min(2 × S, CPC máx)`.
3. **15 días de aprendizaje + 7 de atribución no entran en 24 días.** Revisar a los 5–7 días con reglas de corte, no a los 15.
4. **Dejar las 6 automáticas viejas y las manuales ganadoras a 0,10 desperdicia lo que ya convertía** (`reflex challenge game`, `reaction game`, `reaction time game`, `reflex drop sticks game`, PT Tendry): reactivar sólo las exact/phrase con historial ≥ 5 pedidos, a `min(CPC histórico, CPC máx)`.
5. **El precio define todo lo anterior:** la guía asume 22,99. ¿Es el precio vigente? Si sí, choca con la baja a 16,99 del §4 → decidir: **22,99 con PPC más fuerte** vs **16,99 con PPC más fino**. Sin datos de velocidad post-06-oct no se puede elegir con números.

### 10 · Archivos recibidos el 09-oct
- `REFLEX-guia-campanas-Marvin-2026-10-06.html` → resumido en §9.
- `US_AMAZON_cerebro_B0H5MBL5PY_2026-10-04.csv` → **no es de Reflex**: B0H5MBL5PY es **Kitsch** (cepillo linfático), competidor de **AVIE**. 4.567 keywords. Se procesa en una sesión de AVIE.

---

## 5. Compliance: flag Children's toys, caja, seguro

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/compliance.md`_

## REFLEX — Compliance: flag "Children's toys", caja y seguro

### El flag (captura Account Health 28-sep)
| Dato | Valor |
|---|---|
| Aviso | "Children's toys: Food and Product Safety Issues" del **22-sep-2026** |
| ASIN | **B0GQW5F2LL (QW5)** · SKU "Reflex Dad blue" · R46 todavía no marcado |
| GMS en riesgo | **US$ 10.833,57** |
| Estado | *Listing at risk of removal* · **plazo 06-dic-2026** |
| Exige | **ASTM F963-23 + CPSIA** · vía indicada por Amazon: laboratorio TIC partner |
| Motivo | título/bullets dicen "suitable for children 3+" y "coordination toy" |
| Documentos subidos | ninguno ("No compliance documents have been submitted yet") |
| Account Health | Healthy · AHR 232 · 992 pedidos FBA en 60 días |

### La caja física (foto en `assets/caja_retail.jpeg`, revisada 06-oct)
**"AGES 3+"** · **"FAMILY GAMES"** · **"INTERNAL BATTERY"** · **"TYPE-C CHARGE"** · marca HM · Made in China.

**Consecuencia (HECHO + regla del expediente):** la clasificación sigue a la caja. Si la caja dice 3+, es **producto infantil para la CPSC**.
- La "Vía A" (sostener ante Amazon que es *training equipment 14+*) **no es viable con esta caja**: contradice el empaque y lo que se declara al seguro.
- Vía que queda: **laboratorio ASTM F963-23 + CPSIA → CPC emitido por el importador de registro**.
- La batería es interna y recargable por USB-C → refuerza la exposición (tipo de celda sigue UNKNOWN; probablemente litio).
- R46 tiene la misma caja → es probable que reciba el mismo flag.

### Palanca económica
- Costo de tests: estimado US$ 500–1.500 (a cotizar) · plazo típico 2–4 semanas.
- Contra: US$ 10.834 de GMS de QW5 + el pico de diciembre + el ASIN que vende 2/3 de las unidades.
- **Fecha límite práctica para pedir el test: mediados de octubre**, para tener el CPC subido con margen antes del 06-dic.

### Seguro (resumen — expediente completo en la carpeta de la cuenta KINAVARGAS)
- Amazon exige CGL + Product Liability US$ 1M/1M. **Deadline 01-oct-2026 (vencido; estado actual UNKNOWN).**
- Named Insured = **Maria Eugenia Vargas** (legal entity de la cuenta).
- Well Insurance: no asegura persona física extranjera; pide LLC US + FEIN.
- VirtualMed (LLC de Santi y Pablo) cumple eso, pero **la cuenta personal de Santi está bloqueada por Sección 3** → mostrar la LLC a Amazon arriesga vincular KINAVARGAS. Camino preferido: póliza corta a nombre de Eugenia vía productor argentino (Allianz/Chubb AR) o surplus lines (Sadler, Veracity, Coyle).
- **Regla:** al seguro se declara lo mismo que dice la caja → **toy / children's product, con batería**.

### Datos faltantes
Importador de registro (a su nombre va el CPC) · tipo de celda de la batería · cotización de laboratorio · estado del seguro después del 01-oct · traspaso `REFLEX_TRASPASO_COMPLIANCE_Q4_2026-09-28` (no está en ninguno de los dos vaults).

---

## 6. Cuenta KINAVARGAS — datos

_Fuente: `Trabajo/E-commerce/Amazon/_CUENTA-KINAVARGAS/CLAUDE.md`_

## CUENTA KINAVARGAS (ACC-002) — lo que es de la cuenta, no de un producto

> Seguro, titular, documentos, seguridad. Los productos de esta cuenta tienen su carpeta: `../REFLEX/` (liquidación activa) y `../KINA/` (fuera de Amazon, liquidación multicanal).

### Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Dónde quedamos, prioridades, decisiones abiertas |
| `seguro.md` | Requisito de seguro de Amazon (deadline 01-oct, vencido), brokers, decisiones, trampas |

### Datos de la cuenta
| Dato | Valor |
|---|---|
| Alias | **KINAVARGAS** · ID interno ACC-002 |
| Titular / legal entity | **Maria Eugenia Vargas**, persona física · tipo **individual** |
| Residencia del titular | Godoy Cruz, Mendoza, Argentina (dirección histórica: Siena 2723) |
| Miami | **No es residencia**: es el warehouse / delivery (2970 NW 75 AVE, Miami FL 33122) |
| Marketplace | Amazon.com (US) |
| Brand Registry | **NO** — todos los listings bajo "Generic" |
| Relación con la LLC | Eugenia **no es parte** de VIRTUALMED SOLUTIONS LLC (Santi + Pablo) |
| Roles | Eugenia hace las verificaciones de identidad; Santi prepara documentación y opera |

### Productos de la cuenta
| Producto | ASIN | Estado |
|---|---|---|
| Reflex Game R46 / QW5 | B0GR46X8Y8 · B0GQW5F2LL | Activos · **modo liquidación**, salir en dic-2026 |
| KINA Lymphatic Drainage Face Brush | B0GQJLP4TB | **Desactivado** por patente · discontinuado en Amazon · stock retirado a Miami |

### Casos
| Caso | Estado |
|---|---|
| CASE-001 · patente de diseño D1063405 (complaint 20503982181) | ABIERTO · appeal despriorizado → `../KINA/patente.md` |
| CASE-003 · INFORM Act (bug de verificación de CUIT) | ✅ Resuelto |
| Children's toys (QW5, aviso 22-sep, plazo 06-dic) | ABIERTO → `../REFLEX/compliance.md` |
| Seguro de responsabilidad civil (deadline 01-oct) | ABIERTO / vencido → `seguro.md` |

### Objetivo de la cuenta
Liquidar el stock de Reflex hasta diciembre y **no volver a usar la cuenta** después (decisión de Santi, 28-sep). Todo se evalúa contra ese horizonte: proteger la cuenta hasta vaciarla, no construir nada a largo plazo.

### Reglas duras de la cuenta
1. **No cambiar la legal entity a la LLC.** Dispara reverificación en pleno Q4 y, con la cuenta personal de Santi bloqueada por Sección 3, puede vincular KINAVARGAS con esa cuenta.
2. **No crear ASINs nuevos de KINA** (ni FBM ni con otro listing) para esquivar el reclamo de patente: arriesga la cuenta entera.
3. **Phishing:** "Joseph" @esc-amazon.com (y cualquier dominio no oficial) = estafa. No compartir Case ID, Merchant ID, documentos ni códigos. Canales válidos: Seller Central, Account Health, foros oficiales.
4. Lo que se declara a Amazon, al seguro y en la caja del producto tiene que ser **la misma verdad**.
5. No mezclar con Beauty Michele (AVIE / MT Ball): otra cuenta, otro titular, cero datos cruzados.
6. No guardar en estos archivos DNI completos, números bancarios ni contraseñas.

---

## 7. Cuenta KINAVARGAS — estado

_Fuente: `Trabajo/E-commerce/Amazon/_CUENTA-KINAVARGAS/ESTADO.md`_

## CUENTA KINAVARGAS — ESTADO

**Actualizado:** 2026-10-06 (migración) · **Último dato:** 28-sep

### ⚠️ Primero: confirmar
1. **¿Qué pasó con el seguro después del 01-oct?** Mirar Configuración → Información de la cuenta → Seguros para empresas, y Account Health.
2. ¿Respondieron Sadler (Paul Owens), Veracity, Coyle, Allianz/Chubb AR por la póliza a nombre de Eugenia?
3. ¿Se mandó la corrección a Sadler (toy/children's product, importador, proyección USD 60,000)?
4. ¿Quién figura como **importador de registro** de Reflex? (define a nombre de quién va el CPC y qué se declara al seguro)

### Prioridades
1. **Seguro aceptado por Amazon** → protege ~US$ 17.800 de stock de Reflex en el único trimestre que importa. Prima esperada US$ 1.000–3.500/año: comprar es decisión obvia frente al capital en juego.
2. **Compliance de Reflex** (`../REFLEX/compliance.md`) — mismo underwriter va a pedir CPC/tests: hacer las dos cosas juntas.
3. Mantener la cuenta sana hasta vaciarla (no tocar legal entity, no listings nuevos de KINA).

### Decisiones abiertas (de Santi)
- Camino del seguro: (a) póliza a nombre de **Eugenia** vía productor argentino o surplus lines — preferido; (b) póliza a nombre de **VirtualMed** con Eugenia como *additional named insured* — Well preguntó si Amazon lo acepta, pero expone la LLC (riesgo de vínculo con la cuenta bloqueada de Santi); (c) cambiar legal entity — **descartado**.
- Póliza corta / provisoria (sólo hasta diciembre) vs anual: Santi prefiere corta.

### Historial
- 2026-10-06 · Migrado a `AMAZON/_CUENTA-KINAVARGAS/`.
- 2026-09-28 · Well dice NO a persona física extranjera (pide LLC + FEIN). Se descubre que la cuenta personal de Santi está bloqueada por Sección 3 → se descarta usar VirtualMed. Vuelve el camino a nombre de Eugenia. Account Health: Healthy, AHR 232; el seguro todavía no aparecía como Priority Action.
- 2026-09-24 · Contacto con brokers: Santi como encargado de seguros de su LLC, Eugenia como Named Insured, estructura expuesta desde el primer mensaje.
- 2026-09-15 · Agosto ≈ US$ 15.000 brutos → el umbral de US$ 10.000/mes se disparó: obligación real. 3 defectos en la aplicación a Sadler.
- 2026-09-14 · KINA confirmado discontinuado en Amazon; Reflex único producto a asegurar.
- 2026-09-03 · INFORM Act resuelto.
- 2026-08-31 · Amazon pide prueba de seguro antes del 01-oct.

---

## 8. Cuenta KINAVARGAS — seguro

_Fuente: `Trabajo/E-commerce/Amazon/_CUENTA-KINAVARGAS/seguro.md`_

## CUENTA KINAVARGAS — Seguro de responsabilidad civil (Amazon BSA §9)

### Requisito de Amazon (verificado)
- CGL / Product Liability, base **occurrence** · **US$ 1M por ocurrencia / US$ 1M agregado** · deducible ≤ **US$ 10.000** · carrier **AM Best A−** o mejor.
- Additional insured: **"Amazon.com Services LLC and its affiliates and assignees"** · P.O. Box 81226, Seattle, WA 98108-1226, Attn Risk Management.
- **Named Insured = legal entity de Seller Central = Maria Eugenia Vargas** (persona física). El COI se compara carácter por carácter.
- Gatillo: la cuenta superó **US$ 10.000 brutos en un mes** (agosto ≈ US$ 15.000). Aviso del 31-ago, **plazo 01-oct-2026** (vencido; estado actual UNKNOWN).
- Cambio de Amazon del **02-nov-2026** sobre categorías *enhanced-safety*: Reflex cae en dos (producto infantil + batería).

### El bloqueo estructural
Casi ningún carrier de EE.UU. asegura a una **persona física extranjera sin entidad US**. Los que lo hacen van por **surplus lines / Lloyd's vía broker**.
- **Well Insurance (28-sep):** exige LLC/Corp US + dirección US + FEIN. "Ninguna aseguradora US cubre a un extranjero sin entidad US".
- **VirtualMed SOLUTIONS LLC** cumple los 3 (FL Doc L23000540019, Sarasota, FEIN), **pero** Santi es miembro y su cuenta personal de Amazon está **bloqueada por Sección 3** → mostrar la LLC a Amazon puede vincular KINAVARGAS con la cuenta bloqueada. **No recomendado** sin análisis aparte.

### Proveedores — dónde está cada uno
| Prioridad | Proveedor | Estado |
|---|---|---|
| 1 | **Sadler & Company** (Paul Owens) | Aplicación enviada 14-sep. Underwriter asignado. **Corregir la declaración antes del quote** (ver abajo) |
| 1 | **Productor argentino → Allianz / Chubb AR** (póliza corta a nombre de Eugenia) | A contactar. Allianz AR 0810-222-2243 · Liderar Seguros (0261) 425-3109 · Seguros Mendoza +54 261 508-9118 · Mendoza Broker 261 541-3000. Duda: jurisdicción US + COI |
| 2 | Veracity · Coyle Group (surplus lines) | Esperando respuesta |
| 2 | Assureful (modelo pay-as-you-sell, desde ~US$ 26/mes, no confirmado) | Borrador en Gmail sin enviar |
| — | Well Insurance | Dice NO a persona física; sólo vía LLC |
| ✖ | Marsh / Amazon Insurance Accelerator · Spott · Azure Risk · Aligned · Konsileo · carriers online con domicilio US | Descartados |

Regla: **broker = puede decir que sí; carrier con formulario online = exige domicilio US y bloquea.**

### Aplicación a Sadler (14-sep) — 3 defectos a corregir por escrito ANTES de la cotización
1. Se declaró "consumer recreational game" → la caja dice **AGES 3+**: declarar **toy / children's product**. Si no, el carrier puede **rescindir por misrepresentation** y la póliza no sirve.
2. Se declaró sólo "Retailer" → marcar también **Importer / Distributor** (el importador responde como fabricante en EE.UU.).
3. "18.000" se lee dieciocho en EE.UU. → escribir **USD 60,000** de proyección (la cifra real, no 18,000).

### Economía de la decisión
Prima de mercado para toy: US$ 1.000–10.000/año, típica ~3.500. Frente a ~US$ 17.800 de stock de Reflex por liquidar en Q4, **comprar es obvio**; lo que importa es que la póliza **no se caiga** (declaración exacta).

### Documentos que pide un broker
DNI de Eugenia + domicilio tal cual Seller Central · captura de legal entity y Merchant Token · ASINs + fotos + ficha técnica (material, batería, edad) · ventas brutas 12 meses + proyección · invoices de proveedores · certificados (CPC/CPSIA) · historial de reclamos (cero) · captura del aviso de Amazon.

### Prohibido sin autorización puntual
Comprar seguro · pagar quote/bind · subir COI · cambiar legal entity · sacar EIN · contratar domicilio US · esconder categorías para abaratar.

---

## 9. Historia y foto al 19-sep

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/historia-19sep.md`_

## REFLEX — Foto al 19-sep, economía por ASIN, stock y resumen

> Fuente: `REFLEX_HISTORIA_COMPLETA_RESUMEN_v1.1` (PROYECTOS 100K, 19-sep). Series hasta el 16-sep; observación directa de listings del 19-sep. **Es lo más nuevo del expediente y corrige partes del índice del 17-sep** (títulos, precio por ASIN).

#### DELTA 19-SEP-2026 — ESTADO OBSERVADO

*Esto es una foto del 19 de septiembre, no un reemplazo de nada de lo que sigue. El histórico queda intacto más abajo.*

**Fechas de alta de los ASINs** — dato nuevo, antes figuraba como no registrado:

- **QW5 `B0GQW5F2LL`: alta el 2 de marzo de 2026**
- **R46 `B0GR46X8Y8`: alta el 4 de marzo de 2026**

QW5 se dio de alta **dos días antes** que R46.

**Los títulos.** Al 19 de septiembre, **los dos listings muestran exactamente el mismo título**: `Reflex Challenge Drop Stick Game`, 32 caracteres sobre un tope de 75. Y **desaparecieron los sufijos de color**: ya no está `(Yellow)` en QW5 ni `(Sky Blue)` en R46.

Esto confirma, desde la página pública, lo que se había detectado en los datos de transacciones a partir del 4 de septiembre. **Los dos ASINs quedaron con un título idéntico y sin ningún identificador de variante.** Cómo llegaron ahí —auto-edición de Amazon, un cambio manual, u otra causa— **sigue sin estar establecido**.

**Estado de los dos listings al 19-sep:**

| | **QW5** `B0GQW5F2LL` | **R46** `B0GR46X8Y8` |
|---|---|---|
| Rating | **4,1** | 3,8 |
| Reviews | 29 | 31 |
| BSR Kids' Handheld | **#153** | #288 |
| Prueba social | **300+ comprados** | **50+ comprados** |
| Imágenes | **9** | 7 |
| A+ | **sin publicar** | **sin publicar** |
| Vídeo | **ninguno** | **ninguno** |

Comparado con la foto del 15 de septiembre: QW5 sumó una review (28 → 29) y dos imágenes (7 → 9), y su BSR **empeoró** de #103 a #153. R46 mantuvo 31 reviews, su BSR empeoró de #246 a #288, y su prueba social **bajó otro escalón, de "100+ comprados" a "50+ comprados"**.

Ninguno de los dos tiene A+ publicado ni un solo vídeo, cuatro días después de la última medición y con el trimestre encima.

#### LA ECONOMÍA REAL, POR FIN ABIERTA POR ASIN

Todo el expediente dice, en varios documentos, que **el settlement no se puede abrir por ASIN porque los dos listings comparten el título**. Eso es falso. Los títulos se diferencian en la puntuación: el de QW5 sigue con **coma** después de "Game" y el de R46 con **guion**. El reporte de transacciones trunca a 40 caracteres, pero la coma y el guion sobreviven al truncado.

Usando eso, se sacó la economía real de cada variante en la ventana del **25 de agosto al 3 de septiembre**, que es el tramo donde los dos ASINs son identificables:

| | **R46** | **QW5** |
|---|---:|---:|
| Pedidos | 69 | 157 |
| Unidades | **75** | **165** |
| Facturación | US$1.565,65 | US$3.145,34 |
| **Precio medio real** | **US$20,88** | **US$19,06** |
| Fee de Amazon por unidad | 7,94 | 7,76 |
| **Contribución por unidad** | **US$7,00** | **US$5,37** |
| Contribución total del período | US$524,94 | US$885,24 |

**R46 vende cada unidad con US$1,63 más de contribución que QW5**, porque se vende US$1,82 más caro. Pero QW5 vende **2,2 veces más unidades**, así que aporta más plata en total.

Esto cierra, con datos propios y no estimados, el conflicto C-12 que estaba abierto: **el precio operativo no es 19,99, y no es el mismo en los dos ASINs**.

#### EL CAMBIO DE TÍTULO DEL 4 DE SEPTIEMBRE

A partir del **4 de septiembre** empieza a aparecer en las transacciones una tercera forma del título: **"Reflex Challenge Drop Stick Game" a secas**, sin coma, sin guion, sin nada más.

- hasta el 3 de septiembre: **0 pedidos** con el título corto
- 4 de septiembre: aparecen 9
- 8 de septiembre: 20
- 12 de septiembre: 24
- **14 de septiembre: 24 pedidos con el título corto y CERO con las formas largas de ambos ASINs**

En diez días el título corto pasó de no existir a ser el **100 %** de los pedidos, y las dos formas originales desaparecieron.

**Qué significa exactamente, no se sabe.** Lecturas posibles:

1. **Amazon auto-editó los títulos.** La política del 27 de julio fija el tope en 75 caracteres y permite truncado y auto-edición sin aviso ni opción de rechazarlo. El título de QW5 tenía **134 caracteres**: es candidato obvio. Pero el de R46 tenía 66 y cumplía, así que esto no explicaría por qué también cambió.
2. **Alguien cambió los dos títulos** a principios de septiembre.
3. **Amazon cambió cómo muestra el nombre del producto** en el reporte de transacciones.

Lo seguro: **el cambio empieza el 4 de septiembre y se completa alrededor del 14**, y ese es el mismo tramo en que **R46 se derrumbó** en el ranking orgánico. **Es una coincidencia temporal, no una causa demostrada.** Aun así es la pista más concreta que existe sobre el colapso de R46, y no está investigada.

**Confirmado el 19 de septiembre**, mirando los listings directamente: los dos títulos son exactamente `Reflex Challenge Drop Stick Game`, 32 caracteres, **sin `(Yellow)` ni `(Sky Blue)`**.

#### EL STOCK AL 15 DE SEPTIEMBRE

Se compraron **5.000 unidades**. Entre el 10 de abril y el 4 de septiembre se vendieron **1.501**. Eso deja 3.499, que es el número que el vault venía usando como techo.

El **15 de septiembre** Santi confirmó **1.700 unidades por SKU, o sea 3.400 en total**. Es compatible con el cálculo anterior: entre el 4 y el 15 de septiembre hubo más ventas y el retiro de inventario.

Lo que **no está confirmado** es qué son exactamente esas 1.700: si es stock disponible en FBA, si incluye reservado, si incluye unidades no vendibles, o si es inventario físico total. Sin un informe de inventario por ASIN no se puede cerrar.

A la velocidad medida entre el 27 de agosto y el 14 de septiembre: **QW5 vendía 8,37 unidades por día, stock para 203 días. R46 vendía 1,79 por día, stock para 950 días.** Combinado son **335 días** — el inventario cruza a 2027 con cualquier estrategia de precio. Para liquidar las 1.700 de QW5 antes de fin de año harían falta **15,89 unidades diarias**, casi el doble de lo que vende.

**No hay riesgo de quedarse sin stock. Hay riesgo de sobrestock.** Y con el inventario cruzando a 2027 aparece el recargo por inventario añejo, que **todavía no se puede cuantificar** porque faltan los tramos de antigüedad y el volumen en pies cúbicos por unidad.

Capital inmovilizado al 15 de septiembre: **3.400 × 5,94 = US$20.196**, con la salvedad de que los 5,94 son un coste declarado y provisional.

#### LO QUE SIGUE SIN SABERSE

- **Qué pasó el 19 de agosto.** La caída de conversión más cara del proyecto, sin causa identificada.
- **Qué pasó del 16 de junio al 2 de julio.** Diecisiete días con cero sesiones, sin ninguna nota en el vault.
- **Qué pasó el 4 de septiembre con los títulos.** El cambio coincide con el colapso de R46.
- **Por qué se cayó R46.** Descartado el precio; medido el colapso de conversión; sin causa.
- **Los placements.** La columna viene vacía en las 2.620 filas del export. Es lo que explica el 97 % del exceso de CPC.
- **Los negativos que ya existen.** No vienen en ningún export.
- **El backend de los dos listings.** Nunca se recuperó.
- **Quién ordenó el retiro de inventario** de US$3.774,96 y cuántas unidades salieron.
- **Qué son exactamente las 1.700 unidades por SKU.**

Versiones contradictorias: el **stock** tuvo tres cifras sucesivas — ~4.100 estimadas, ≤3.499 calculadas, **3.400 confirmadas (la más actual)**. El **precio medio realizado** aparece como 19,83, 20,29, 19,73 y 19,75, todos correctos para su ventana: **la cifra buena para decidir es la de cada ASIN — R46 20,88 y QW5 19,06**.

#### RESUMEN CORTO

**1 · Inversión:** **US$29.700** en mercadería + PPC acumulado no consolidado (estimación US$10.000–12.000 con fee de agencia). Sin registro de flete, aduana, 3PL ni prep por separado. Total aproximado: **US$40.000–42.000**.

**2 · Comprado:** **5.000 u**, 2.500 por variante.

**3 · Queda:** **3.400 u** (1.700/SKU, 15-sep). Composición no confirmada. Capital: **US$20.196**.

**4 · Vendido:** **1.501 u por US$28.009** entre el 10-abr y el 4-sep, precio medio **US$18,66**. Hay ventas anteriores al 10-abr sin serie.

**5 · PPC:** ventanas que se superponen y **no se suman**: 1.335,82 (14–31 jul) · 5.097,93 (1 ago–3 sep) · 3.367,05 facturados (16 ago–8 sep) · 2.245,85 (27 ago–14 sep). Más 10 % de fee de agencia. **Total acumulado no consolidado.**

**6 · Mejor ASIN (19-sep): QW5 (`B0GQW5F2LL`).** Vende 1,67× más, convierte el doble (13,5 % vs 6,9 %), mejor ACoS (57,5 % vs 80,9 %), #1 en `reflex challenge game` + cinco top-5. Rating 4,1 vs 3,8, BSR #153 vs #288, 300+ vs 50+ comprados. **R46 deja US$1,63 más por unidad pero su stock tendría ~950 días de vida.**

**7 · Los cinco problemas abiertos más importantes**
1. **Títulos idénticos y sin identificador de variante** desde el 4–14 sep; no se sabe quién/qué los cambió; coincide con el derrumbe de R46.
2. **Caída de conversión del 19-ago sin causa.** ≈ US$4.470/mes, casi el doble que todo el problema de publicidad.
3. **Colapso de R46 sin diagnóstico.** Sin ninguna keyword en top-10, 1.700 u a ~950 días.
4. **A 19,99 con el PPC observado no cierra** — pero la contribución pre-PPC es +5,26/u. Lo negativo es el resultado después de anuncios. Escalera de precio decidida, no ejecutada. El 5,94 de costo es provisional.
5. **Placements y negativos desconocidos** — sin eso no se puede tocar el PPC con criterio.

*Nada de esto se ejecutó en Seller Central ni en Amazon Ads.*

---

## 10. Economía unitaria y precio

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/economia.md`_

## REFLEX — Economía unitaria y precio

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep · W4 8-ago→6-sep · W5 8–19 vs 20–30 ago · W6 reportes agencia 14-jul→21-ago · W7 settlement 16-ago→8-sep · W8 24-ago→15-sep · W9 Helium 30-ago/10-sep/15-sep · Wx sin declarar. **Las ventanas no se suman entre sí.** Etiquetas: VERIFIED · CALCULATED · INFERRED · UNKNOWN · CONFLICT.

> ⚠️ Con objetivo de **liquidar y salir en diciembre**, la columna "u p/ igualar 19,99" de 4.4 supone que las unidades no vendidas conservan valor. No es así: lo que quede el 1-ene vale poco. Comparar escalones por **contribución total dentro de Q4**, no por contribución por unidad.

### 4 · ECONOMÍA UNITARIA

#### 4.1 La fórmula de fees — pieza más sólida del expediente

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

#### 4.2 Parámetros

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

#### 4.3 Break-even CPC

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

#### 4.4 Análisis de precio 2026-09-17 — economía por escalón (QW5, sin PPC)

`CALCULATED` · descuento realizado −5,4 % (ASP 18,92 sobre lista 19,99, `VERIFIED` W3) mantenido constante.

| Lista | Net rev/u | Fee/u | Landed | **Contrib/u** | Margen | Contrib 1.700 u | u p/ igualar 19,99 | Caída máx. tolerada |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 19,99 | 18,91 | 7,71 | 5,94 | **5,26** | 27,8 % | 8.949 | 1.700 | — |
| 22,99 | 21,75 | 8,13 | 5,94 | **7,68** | 35,3 % | 13.050 | **1.166** | **−31,43 %** |
| 24,99 | 23,64 | 8,42 | 5,94 | **9,28** | 39,3 % | 15.784 | **964** | **−43,30 %** |
| 27,99 | 26,48 | 8,84 | 5,94 | **11,70** | 44,2 % | 19.884 | **765** | **−55,00 %** |
| 29,99 | 28,37 | 9,13 | 5,94 | **13,30** | 46,9 % | 22.618 | **673** | **−60,44 %** |

**Separación obligatoria:** *contribution pre-PPC* (decisión de PRECIO, positiva en los 5 escalones) ≠ *profit after PPC* (decisión de ADQUISICIÓN DE TRÁFICO, negativa hoy). No mezclarlas.

---

## 11. Ventas y conversión por ventana

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/ventas.md`_

## REFLEX — Ventas y conversión por ventana

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep · W4 8-ago→6-sep · W5 8–19 vs 20–30 ago · W6 reportes agencia 14-jul→21-ago · W7 settlement 16-ago→8-sep · W8 24-ago→15-sep · W9 Helium 30-ago/10-sep/15-sep · Wx sin declarar. **Las ventanas no se suman entre sí.** Etiquetas: VERIFIED · CALCULATED · INFERRED · UNKNOWN · CONFLICT.

### 5 · VENTAS Y CONVERSIÓN — POR VENTANA

#### 5.1 W1 · 2026-08-01 → 2026-09-03 (34 días) — SRC-014 + SRC-018

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

#### 5.2 Wx · ventana NO DECLARADA (~30 d entre 02/08 y 02/09) — Business Report por ASIN

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

#### 5.3 W5 · ruptura de conversión del 19→20 de agosto — SRC-018

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

#### 5.4 W7 · settlement 2026-08-16 → 2026-09-08 (24 días, 599 transacciones)

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

#### 5.5 W8 · transacciones 2026-08-24 → 2026-09-15 (23 días)

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

#### 5.6 Velocidad de venta — W3 / 15-sep

| | R46 | QW5 |
|---|---:|---:|
| Unidades PPC en W3 (19 d) | **34** | **159** |
| Unidades/día (PPC-attributed) | **1,79** | **8,37** |
| Unidades 30 d totales (Helium 15-sep) | **241** | **402** |
| Revenue 30 d (Helium 15-sep) | US$ 4.986 | US$ 7.661 |

> ### ⚠️ INVERSIÓN COMPLETA DE LOS ASINS
> En agosto: **R46 ~497 u vs QW5 ~182 u**. Al 15-sep: **QW5 402 u vs R46 241 u**. QW5 vende **1,67×** lo de R46.
> **La premisa "R46 = ASIN económico principal" está INVALIDADA.** Toda decisión que la asuma (reparto 65/35 del presupuesto, Paid Core aprobado) es inejecutable tal como está escrita.

### 3 · INVENTARIO

| Dato | Valor | Etiqueta |
|---|---|---|
| Compradas | **5.000 u (2.500 por ASIN)** por US$ 29.700 | `VERIFIED` |
| **Stock declarado por el titular (15-sep)** | **1.700 u por SKU = 3.400 u totales** | `VERIFIED` |
| Composición del 1.700 (FBA disponible / reservado / físico) | **`UNKNOWN`** | — |
| Cifra citada el 28-sep (expediente de seguro) | **3.550 u** | `CONFLICT` con 3.400 |
| Capital inmovilizado a landed 5,94 | **US$ 20.196** sobre 3.400 u | `CALCULATED` |
| Fecha de recepción · age buckets · pies cúbicos | `UNKNOWN` → sin esto no se cuantifica el recargo por inventario añejo | — |

#### 3.1 Removal order — anomalía abierta

| Dato | Valor |
|---|---|
| Cargos | **69 líneas "Tarifa por devolución de inventario"** |
| Importe | **−US$ 3.774,96** |
| IDs | `cG9y5eI/le` · `feGnIY4PCW` · `vaOqCY0NXG` |
| Fechas | 07 → 15 sep |
| Contrapartida | **+US$ 2.092,93** (4 cargos, 10–13 sep) |
| Quién la ordenó · cuántas unidades · qué ASIN | `UNKNOWN` |
| **Qué lo resuelve** | **Informes → Logística de Amazon → Retiradas de inventario (Removal Order Detail), 01/09 → hoy** |

---

## 12. Competencia

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/competencia.md`_

## REFLEX — Competencia

### Líder — Tendry `B0DLN5C44D`

> ⚠️ **Las dos columnas son de fechas distintas. No compararlas como si fueran el mismo momento.**

| Campo | **2026-08-29 `VERIFIED`** | **~dic-2025 / ene-2026 — `HISTORICAL EVIDENCE`** |
|---|---|---|
| Precio | **US$ 18,99** (típico 20,99, badge "Lowest price in 30 days") | **US$ 29,99** |
| Rating | 4,0 | 4,0 |
| Reviews | **387** | 245 |
| BSR Sports & Outdoors | #13.823 | **#2.073** |
| BSR Speed & Agility | #20 | **#5** |
| Unidades 30 d `ESTIMATE` | **723** | **7.303** |
| Revenue 30 d `ESTIMATE` | US$ 15.332 | **US$ 216.370,29** |
| Prueba social | 300+ bought | **6K+ bought** |
| Listing Health Score | **9,7** | `UNKNOWN` |
| Variantes | 6-Stick Single $18,99 · **10-Stick Dual $39,99** | 2 variantes |
| Videos | `CONFLICT` **8 ó 14 según fuente** | `UNKNOWN` |
| Bundles | −5 % / −8 % / −12 % por 2/3/5 u | — |
| Bullet distintivo | bullet titulado **"Christmas Games"** | — |

`CONFIRMED` **Estacionalidad Q4**: el mismo ASIN vendió **7.303 u a 29,99 en temporada** vs **723 a 18,99 en agosto**.

### Otros competidores

| id | ASIN | Marca | Precio | Rating | Reviews | Fecha del dato |
|---|---|---|---|---|---:|---|
| C-02 | `UNKNOWN` | — | **$28,77** | 3,6 | 161 · **10K+ bought** | **~ene-2026 HISTÓRICO** |
| C-03 | `UNKNOWN` | — | **$16,69** | 4,0 | 18 · **6K+ bought** | **~ene-2026 HISTÓRICO** |
| C-04 | B0DYNYMZHR | ATG | `UNKNOWN` | — | — | 2026-08-29 |
| C-05 | B0DYSQFSQV | — | `UNKNOWN` | — | — | 2026-08-29 |
| C-06 | B0GZW99DG4 | — (Plus, EVA, voice) | `UNKNOWN` | — | — | 2026-08-29 |
| C-07 | B0G442Y91B | Jurfest | `UNKNOWN` | — | — | 2026-08-29 |
| C-08 | B0DJRFS89G | rafonie | `UNKNOWN` | — | — | 2026-08-29 |
| C-09 | B0DMNC5B2H | RVOGJP | `UNKNOWN` | — | — | 2026-08-29 |
| C-10 | B0DLSF9J14 | — | `UNKNOWN` | — | — | 2026-08-29 |
| C-11 | B0DLWLWZ7D | — | `UNKNOWN` | — | — | 2026-08-29 |
| C-12 | B0DLWB9HC5 / B0DLWCKLG1 | — | `UNKNOWN` | — | — | 2026-08-29 |
| C-13 | B0DLNLGRWG | — | `UNKNOWN` | — | — | 2026-08-29 |
| C-14 | B0G6798DTH | — | `UNKNOWN` | — | — | 2026-08-29 |
| C-15 | B0H7GW8LN2 | — | `UNKNOWN` | — | — | 2026-08-29 |
| C-16 | B0DQ8LF627 | balinging | `UNKNOWN` | — | — | 2026-08-29 |
| C-29 | — | Champs MMA (ADJACENT) | $18,66 | 4,0 | **7.354** | 2026-08-29 |

**Fuera de Amazon (2026-08-29):** Walmart Kehuo $11,30 · YOTQUSKI $9,99 · eBay `billion.storee` $35,81 (seller 99,6 %, 7.700+ vendidos) · TikTok Shop SKYQI $18,99 (193 sold), $12,99 (103), Double Stick Catch $14,99 (315), $21,97 (87) · Shopify TTpen $22,00.

**Mapa de precios verificado 2026-08-29:** piso $7,46–12,36 · low $14,86–17,97 · **mid $18,99–19,99** · mid-high $22,00–25,19 · premium eBay $35,81 · premium Amazon $39,99 · **histórico Q4 $28,77–29,99**.

### Nuestras referencias propias

| | R46 29-ago | **R46 15-sep** | QW5 29-ago | **QW5 15-sep** |
|---|---|---|---|---|
| Precio | 19,99 (badge "90-day low price") | 19,99 | 19,99 (sin badge) | 19,99 |
| Rating (reviews) | 3,7 (27) | **3,8 (31)** | 3,9 (22) | **4,1 (28)** |
| LHS | 7,3 | **7,5** | 6,7 | **8,9** |
| Prueba social | 300+ bought | **100+ bought** | 100+ bought | **300+ bought** |
| Revenue 30 d | ~10.373 | **4.986** | ~3.424 | **7.661** |
| Unidades 30 d | ~497 | **241** | ~182 | **402** |
| BSR | Speed & Agility #68 | Kids' Handheld **#246** | Speed & Agility #32 | Kids' Handheld **#103** |

---

## 13. Listing y SEO

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/listing-seo.md`_

## REFLEX — Listing, imágenes y SEO orgánico

> ⚠️ **Actualización 19-sep:** los títulos de abajo (capturas del 29-ago) **ya no están vigentes**. Al 19-sep ambos ASINs muestran `Reflex Challenge Drop Stick Game` (32 car., sin sufijo de color). QW5 tiene 9 imágenes, R46 7; ninguno tiene A+ ni video. Ver `historia-19sep.md`.
> Ventanas: W1 1-ago→3-sep · W9 Helium 30-ago/10-sep/15-sep. **No se suman entre sí.**

### Listing al 29-ago (histórico)

#### R46 · B0GR46X8Y8

| Campo | Contenido | Chars |
|---|---|---:|
| TITLE | `Reflex Challenge Drop Stick Game - Remote Control - Reflex Sticks.` | **66 / 75** ✅ |
| ITEM HIGHLIGHTS (probable "Subtítulo") | `Reflex Challenge game - Reflex drop sticks game - Remote control 3 Adjustable Speed - (Sky Blue)` | **96 / 125** ✅ |
| BULLETS 1–4 | `Fast-Paced Reaction Game` · `Durable & Safe Construction` · `Multiple Game Modes` · `Adjustable Speed Settings` | — |
| BULLET 5 | no existe | — |
| BACKEND | `UNKNOWN` | — |

#### QW5 · B0GQW5F2LL

| Campo | Contenido | Chars |
|---|---|---:|
| TITLE | `Reflex Challenge Drop Stick Game, Remote Control 3 Adjustable Speed, Reflex Drop Sticks Challenge Game, Reaction Training Toy,(Yellow)` | **134 / 75** ❌ incumplía |
| ITEM HIGHLIGHTS | `UNKNOWN` | — |
| BULLET 1 | idéntico al de R46 | — |
| BULLETS 2–4 | `2026 Enhanced Remote Control & Voice System` · `3 Adjustable Speed Levels` (incluye **`children 3+`**) · `6 Interactive Game Modes` | — |
| BULLET 5 | no existe | — |
| BACKEND | `UNKNOWN` | — |

Los bullets de QW5 son mejores. El bullet 1 está duplicado entre ASINs. **"children 3+" y "coordination toy" son el motivo del flag de compliance** (ver `compliance.md`) — y coinciden con la caja (AGES 3+).

#### Política de Amazon vigente desde 27-jul-2026
- **TITLE ≤ 75 caracteres** · **ITEM HIGHLIGHTS ≤ 125**. Ambos son input de búsqueda.
- Una palabra puede aparecer **hasta DOS veces**.
- **Auto-truncado y auto-edición por Amazon, sin opt-out.** Truncado en móvil ≈ 60 car.

#### Main images (29-ago) — ambas incumplían
| ASIN | Composición | Problema |
|---|---|---|
| R46 | producto + **caja de retail** en el tercio inferior | caja en main |
| QW5 | producto + **mano humana con motion blur** + remoto + soga + cable + caja | **mano humana prohibida** + saturación |

Decisión D-12: **CONCEPTO A** (producto limpio sobre blanco) como main en ambos. No ejecutada.

### SEO / orgánico — ranks W9 (tres fechas sin fusionar)

| Keyword | SV sep | R46 30-ago | R46 10-sep | **R46 15-sep** | QW5 30-ago | QW5 10-sep | **QW5 15-sep** |
|---|---:|---:|---:|---:|---:|---:|---:|
| reflex drop sticks game | 1.936 | 19 | 36 | **48** | 8 | 5 | **18** |
| reflex game | 1.211 | 9 | 25 | **30** | 16 | 10 | **22** |
| hand speed challenge game | 1.023 | **4** | 19 | **29** | 5 | 4 | **7** |
| reflex sticks | 672 | 8 | 14 | **16** | 6 | 4 | **11** |
| drop stick game | 654 | 28 | 23 | **27** | 8 | 11 | **18** |
| reflex drop sticks | 646 | 11 | 17 | **17** | 10 | 8 | **21** |
| reaction time game | 629 | 6 | 17 | **24** | **2** | 3 | **3** |
| **reflex challenge game** | 621 | 6 | 14 | **15** | 4 | **1** | **#1** |
| reflex game falling sticks | 580 | 12 | 15 | **22** | 16 | 8 | **12** |
| reflex drop sticks challenge game | 555 | 14 | 20 | **22** | 4 | 7 | **15** |
| reflex stick game | 501 | — | 15 | **23** | — | 7 | **10** |
| falling stick game | 344 | 7 | 20 | **33** | 5 | 3 | **#2** |
| drop stick challenge | 152 | 80 | 68 | **74** | 1 | 2 | **#3** |
| reaction challenge game | 219 | 2 | 16 | **19** | 7 | 2 | **#3** |
| reflex challenge | 39 | — | 16 | **28** | — | 1 | **#1** |

| Archivo | Top-10 | Top-20 | Sponsored ≤96 |
|---|---:|---:|---:|
| R46 10-sep | **0** | 30 | 43 |
| **R46 15-sep** | **0** | **13** | **0** |
| QW5 10-sep | 58 | 66 | 41 |
| **QW5 15-sep** | **30** | 50 | **8** |

**R46 perdió posición en las 6 keywords core (30 → 13 en top-20). QW5 tomó el #1 en `reflex challenge game`.** Las 0 posiciones sponsored de R46 no significan que no haya campaña (gastó US$ 516 en W3): es posición, no presencia.

### Canibalización R46 vs QW5
| Fecha | Ambos rankeando | Gana QW5 | Gana R46 |
|---|---:|---:|---:|
| 30-ago | 63 | 50 | 10 |
| 10-sep | 59 | 58 | 1 |
| **15-sep** | **59** | **55** | **4** |

Halo cruzado de atribución: **1,6 % / 0,8 %** → no se canibalizan por atribución. Lo que existe es **solapamiento de gasto PPC**: 121 términos servidos por ambos = **61,4 % del gasto (W1)**. Es un problema de PPC, no de SEO.

### Keywords contaminantes
14 identificadas (13 sólo en el tracker de QW5): `speed stick` (desodorante) · `game stick` (consola) · `match sticks` · `speed training equipment` · `lacrosse stick` · `boost controller` · `hockey training equipment` · `speed controller` · `stick control` · `training equipment` · `grip stick` · `speed training` · `speed limit 3` · `birth control device`. Son **47,6 % del volumen rastreado** en Helium, pero su gasto PPC es **0,26–1,90 %**: **no explican la caída de CVR**. Además: `danny go sticks` (fuera del tracker).

### CTR / CVR de referencia (agosto — al 15-sep se invirtió)
| | R46 | QW5 |
|---|---:|---:|
| CTR | **4,10 %** | 2,52 % |
| CVR | **14,9 %** | 12,3 % |
| Unit Session % | **21,35 %** | 17,17 % |

Inferencia fuerte de agosto: la brecha de CTR de QW5 era de main image. Confounds no descartados: prueba social, badge de precio, placements.

---

## 14. PPC — estructura y desperdicio

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/ppc.md`_

## REFLEX — PPC: estructura, configuración, métricas y desperdicio

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep · W4 8-ago→6-sep · W6 reportes agencia 14-jul→21-ago. **Las ventanas no se suman entre sí.** Etiquetas: VERIFIED · CALCULATED · INFERRED · UNKNOWN · CONFLICT.

### Estructura

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

### Configuración de puja — los cinco problemas estructurales (W2)

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

### Métricas — W1 · 1-ago → 3-sep

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

### Métricas — W3 · 27-ago → 14-sep (19 días)

**Cuenta:** spend **2.245,85** (118/día, era 150) · sales **3.646,09** · orders/units **187/193** · impresiones **24.374** (**−59 %**/día) · CTR **6,69 %** *(sube por caída de impresiones)* · CPC **1,38** · CVR **11,47 %** · ACoS **61,60 %**.

| | R46 W1 | **R46 W3** | QW5 W1 | **QW5 W3** |
|---|---:|---:|---:|---:|
| ACoS | 45,9 % | **80,9 %** (+35 pts) | 70,2 % | **57,5 %** (−12,7 pts) |
| CVR | 14,9 % | **6,9 %** (−54 % rel.) | 12,3 % | **13,5 %** (+10 % rel.) |
| Spend / unidades | 2.238 / 239 | **516 / 34** | 2.859 / 216 | **1.730 / 159** |

### Métricas — W4 · 8-ago → 6-sep

CPC **1,59** vs puja media 0,754 = **2,1×**. **ACoS 47,2 % → 72,5 % en once días con el CPC casi plano (+4 %) y el CVR cayendo 15,94 % → 11,70 % (−27 %).** "El CPC explica el ACoS" es **falso**: son dos problemas distintos.
QW5 **64 % del gasto**, ACoS 71,3 % · R46 ACoS 43,0 %. AUTO CloseMatch 84,3 % · Complements 80,0 % · **Substitutes 32,2 % — la única auto sana, recibe 2,6 % del gasto**.

### Serie de la agencia — W6

| Período | Gasto | US$/día | CTR | CVR | ACoS | TACoS | Rank R46 | Rank QW5 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 14–31 jul (18 d) | 1.335,82 | 74,2 | 1,20 % | 21,73 % | 41,56 % | 37,97 % | #45 | #96 |
| 1–7 ago | 1.070,76 | 153,0 | 1,11 % | 14,97 % | 50,53 % | 40,58 % | #23 | #86 |
| 8–14 ago | 1.079,01 | 154,1 | 1,14 % | 16,29 % | 46,11 % | 32,62 % | #31 | #73 |
| 15–21 ago | 1.015,64 | 145,1 | 1,05 % | 14,94 % | 52,43 % | 33,95 % | **#90** | **#34** |

La agencia **duplicó el ritmo diario de julio a agosto (+106 %) y lo dejó plano tres semanas.** No hay reportes posteriores al 21-ago (la semana 22–28 ago existe como pestaña: pedirla). **Nombre y fecha de inicio de la agencia: `UNKNOWN`.**

### Desperdicio — W1

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

---

## 15. PPC — keywords

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/ppc-keywords.md`_

## REFLEX — PPC: keywords, duelo de ASINs, product targeting y harvesting

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep. **No se suman entre sí.**

### Keywords núcleo — W1 (21 términos, span ≥21 d y ≥4 compras)

El núcleo = **44,3 % del gasto, 46,6 % de las unidades, 207 compras. Contribución: −US$ 1.176,03.**

| Término | clics | ord | spend | ACoS | contrib | CPC | CVR | SV |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| reflex challenge game | 114 | 21 | 239,19 | 52,4 % | −120,97 | 2,10 | 18,4 % | 831 |
| reflex sticks | 86 | 19 | 193,02 | 50,7 % | −94,90 | 2,24 | 22,1 % | 1.225 |
| b0dln5c44d *(PT Tendry)* | 148 | 17 | 238,02 | 70,7 % | −156,76 | 1,61 | 11,5 % | — |
| hand speed challenge game | 102 | 16 | 217,46 | 69,1 % | −140,33 | 2,13 | 15,7 % | 628 |
| reflex game | 74 | 16 | 131,35 | 38,4 % | −39,43 | 1,77 | 21,6 % | 1.687 |
| reflex drop sticks game | 54 | 13 | 121,72 | 49,1 % | −53,55 | 2,25 | 24,1 % | 1.999 |
| reaction game | 57 | 12 | 118,57 | 48,6 % | −56,27 | 2,08 | 21,1 % | 831 |
| outdoor games | 115 | 11 | 156,17 | 73,7 % | −103,81 | 1,36 | 9,6 % | — |
| b0g2hj289r *(PT)* | 54 | 10 | 89,39 | 45,6 % | −36,53 | 1,66 | 18,5 % | — |
| reaction time game | 60 | 10 | 131,67 | 66,2 % | −83,04 | 2,19 | 16,7 % | 669 |
| b0fzl2qpkk *(PT)* | 34 | 8 | 48,78 | 29,4 % | −4,22 | 1,43 | 23,5 % | — |
| **reaction time drop sticks** | 23 | 8 | 42,38 | **26,3 %** | **+2,82** | 1,84 | **34,8 %** | — |
| reflex sticks for athletes | 20 | 8 | 45,34 | 29,5 % | −0,43 | 2,27 | 40,0 % | — |
| reflex drop sticks | 40 | 7 | 87,43 | 62,0 % | −52,91 | 2,19 | 17,5 % | 687 |
| **reaction game falling sticks** | 12 | 5 | 23,98 | **24,2 %** | **+4,52** | 2,00 | **41,7 %** | 349 |
| backyard games | 47 | 5 | 63,46 | 67,5 % | −38,91 | 1,35 | 10,6 % | — |
| **b0gr46x8y8** *(ASIN propio)* | 36 | 5 | 64,47 | 58,1 % | −33,84 | 1,79 | 13,9 % | — |
| reflex game falling sticks | 26 | 4 | 54,23 | 66,2 % | −34,93 | 2,09 | 15,4 % | 651 |
| b0fc27kckk *(PT)* | 49 | 4 | 76,79 | 96,0 % | −59,75 | 1,57 | 8,2 % | — |
| drop stick game | 29 | 4 | 57,40 | 59,8 % | −32,24 | 1,98 | 13,8 % | 667 |
| hand speed challenge | 31 | 4 | 59,35 | 76,1 % | −40,56 | 1,91 | 12,9 % | 163 |

**Sólo 2 de los 21 tienen contribución positiva**: `reaction time drop sticks` y `reaction game falling sticks` (CVR 35–42 % vs 13,5 % de la cuenta).

### Duelo R46 vs QW5 sobre el mismo término — W1

| Término | CVR R46 | CVR QW5 | CPC R46 | CPC QW5 | Gana |
|---|---:|---:|---:|---:|---|
| reflex game | **35,3 %** | 10,0 % | 1,95 | 1,62 | **R46** |
| reaction time game | **25,0 %** | 11,1 % | 1,93 | 2,37 | **R46** |
| reflex drop sticks | **23,8 %** | 10,5 % | 1,91 | 2,49 | **R46** |
| reaction game | **25,7 %** | 13,6 % | 1,85 | 2,44 | **R46** |
| reaction time drop sticks | **38,5 %** | 30,0 % | 1,72 | 2,00 | **R46** |
| reflex sticks | **23,6 %** | 19,4 % | 2,04 | 2,60 | **R46** |
| hand speed challenge game | **18,2 %** | 13,8 % | 1,92 | 2,29 | **R46** |
| reflex challenge game | 16,9 % | **22,6 %** | 2,00 | 2,36 | QW5 |
| reflex drop sticks game | 18,8 % | **26,3 %** | 1,83 | 2,43 | QW5 |

⚠️ **Tabla de W1. En W3 los ASINs se invirtieron** (QW5 > R46). No decidir con esto sin re-medir.

### Core keywords con confianza de muestra — W3

Escala: **ALTA ≥10 órdenes · MEDIA 5–9 · BAJA 2–4 · NULA 0–1.** Mínimo 10 clics para veredicto.

| Keyword | ASIN | Clics | Ord | CPC | CVR | ACoS | **Confianza** |
|---|---|---:|---:|---:|---:|---:|---|
| reflex challenge game | QW5 | 56 | 10 | 2,15 | 17,9 % | 64,2 % | **ALTA** |
| reflex drop sticks game | QW5 | 30 | 8 | 2,13 | **26,7 %** | 43,8 % | MEDIA |
| reaction time game | QW5 | 29 | 7 | 2,01 | **24,1 %** | 53,9 % | MEDIA |
| hand speed challenge game | QW5 | 48 | 8 | 2,12 | 16,7 % | 67,0 % | MEDIA |
| reflex sticks | QW5 | 9 | 2 | 2,15 | 22,2 % | 53,8 % | BAJA |
| reflex game | QW5 | 25 | 3 | 1,99 | 12,0 % | 85,6 % | BAJA |
| reflex game | **R46** | **4** | 1 | 1,08 | 25,0 % | 24,0 % | **NULA** |
| reaction time drop sticks | QW5 | 5 | **0** | 1,88 | 0 % | — | **NULA** |

**`PAID CORE KEYWORDS = NONE`.**

### Product targeting — W1

11 campañas · 12,06 % del gasto (US$ 614,85) · 53 orders · ACoS 57,82 % · CVR 14,21 %.

| ASIN objetivo | Desde | Campañas W2 | Puja W2 | Resultado W1 |
|---|---|---:|---:|---|
| **B0DLN5C44D** *(Tendry)* | ambos | **17** | 0,72 / 0,91 | 238,02 · 17 compras · ACoS 70,7 % — **47,7 % desde R46 vs 108,8 % desde QW5** |
| B0G2HJ289R | ambos | 5 | 0,72 / 0,85 | 89,39 · 10 ord · ACoS 45,6 % |
| B0FZL2QPKK | ambos | 11 | 0,72 / 0,85 | 48,78 · 8 ord · **ACoS 29,4 %** |
| B0FC27KCKK | ambos | 6 | 0,80 / 0,85 | 76,79 · 4 ord · **ACoS 96,0 %** |
| B0DMNC5B2H | vía auto | — | — | R46: 3 u · **21,6 %** · +4,32 |
| **`b0gr46x8y8`** *(propio)* | **QW5** | **35** | 0,85 | 64,47 · 5 ord · ACoS 58,1 % · −33,84 |
| **`b0gqw5f2ll`** *(propio)* | **R46** | **3** | 0,72 | `UNKNOWN` |

`b0gr46x8y8` targeteado desde QW5 **es product targeting, no keyword**: no construye ranking. Se clasifica como **PROFIT PPC / CROSS-ASIN CAPTURE**, nunca Paid Core.
Las campañas `Blind-` targetean frases (`reflex test`, `catch the sticks`…), 2.327 impresiones, CVR 17,4 %.

### Harvesting observado — W1

El ciclo existe pero se hace **a mano, con 2–9 días de retraso, y sólo sobre la familia *reflex / reaction / drop sticks***. **Nunca cosechados** (exclusivos de AUTO con ≥2 compras): `outdoor games` (11 compras) · `backyard games` · `yard games` · `hand eye coordination toys` · `speed reaction exercise` · `energy stick toy` · `b0grwq7n45` · `b0dmnc5b2h` · `b0fzl2qpkk`.

### Términos huérfanos rentables (≥2 compras, ACoS <28,1 %, sin Exact propia) — W1

20 términos · **+US$ 130 de contribución con US$ 128 de gasto**. Muestra de 2 órdenes = confianza **BAJA**; falta su search volume.

`reaction time drop sticks` R46 · `drop sticks challenge game` QW5 · `b0dmnc5b2h` R46 · `reaction game falling sticks` QW5 · `energy stick toy` R46 · `speed reaction exercise` QW5 · `lawn games for adults` R46 · `camp games` R46 · `tapout falling sticks` QW5 · `falling sticks catching game` R46 · `drop sticks` R46 · `hand eye coordination toys` R46 · `falling sticks` QW5 · `beach games for adults` R46 · `reflex sticks challenge game reaction training` QW5 · `reaction speed training toy` QW5 · `reaction test game` QW5 · `the reflex sticks` QW5 · `reflex challenge` QW5 · `reflex test` QW5.

---

## 16. Decisiones y acciones

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/decisiones.md`_

## REFLEX — Decisiones, acciones aprobadas e historial

> ⚠️ Escritas ANTES del cambio de objetivo a liquidación (15/28-sep) y antes del flag de compliance (22-sep). Ver `ESTADO.md` → qué sigue valiendo. **Nada de esto está ejecutado en Amazon.**

### Decisiones tomadas

| # | Decisión | Fecha | Estado |
|---|---|---|---|
| DL-1 | **No subir precio en septiembre.** Escalera 19,99 → 22,99 (20-oct) → 24,99 (10-nov) → 27,99 condicional | 09-06/07 | Futura por diseño |
| DL-2 | **La palanca dominante es el precio, no el PPC**: a 19,99 el trimestre cierra en pérdida aun con publicidad optimizada | 09-07 | Vigente |
| DL-3 | **No romper con la agencia ahora** (fee 450/mes vs desperdicio 2.100/mes). Cambiar mandato y reporte (SOP-004), 4 límites duros, auditoría semanal. Revisión **25-oct / 15-nov** | 09-06/07 | Parcial — nuevo mandato `UNKNOWN` |
| DL-4 | R46 principal (65 % del presupuesto) · QW5 cobertura (35 %) | 09-07 | **INVALIDADA** por el delta del 15-sep (QW5 > R46) |
| DL-5 | Identificar siempre por ASIN | 09-07 | Ejecutada |
| DL-6 | **Takeover 14-sep: pujas y negativos, NO estructura.** No pausar automáticas (38,7 % de las ventas) | 09-07/08 | Ejecución `UNKNOWN` |
| DL-7 | **Estacionalidad Q4 confirmada** | 08-30 | Vigente |
| D-8 | Objetivo sep–oct: llegar a Q4 con stock, caja protegida, ranking defendido | 09-08 | Reemplazado por LIQUIDAR (15-sep) |
| D-9 | **3 core ranking keywords**: `reflex game` · `reflex drop sticks game` · `reflex sticks`, con ficha de ranking investment | 09-08 | No ejecutada · **pierde sentido con la salida** |
| D-10 | Arquitectura PPC en 4 buckets (CORE / PROFIT / DISCOVERY / CONQUEST), congelada hasta Q4 | 09-08 | No ejecutada |
| D-11 | No aplicar Negative Exact automático al ASIN perdedor sin medir 4 variables | 09-08 | Restricción activa |
| D-12 | **CONCEPTO A** (producto limpio sobre blanco) como main en ambos | 09-07 | No ejecutada |
| D-13 | Recortar **−70 %** las dos `SP-(LooseMatch)` y pasarlas a `down only` — neto ≈ **+684/30d**, certeza MEDIA. No negativizar 975 términos | 09-07 | No ejecutada |
| D-14 | Regla de negativos: umbral = **2,6 × contribución pre-ad/u** en gasto sin pedidos (16 @19,99 · 23 @22,99 · 27 @24,99 · 34 @27,99) | 09-07 | Adoptada |
| D-15 | Gasto estratégico autorizado: US$ 260/mes en tres partidas con KPI | 09-07 | No ejecutada |
| D-16 | Todas las fechas = `target date + condición GO/NO-GO` | 09-07 | Vigente |
| D-17 | Nueva main de QW5 antes del 20-sep | 09-07 | No ejecutada |
| D-18 | **Verdad del producto y compliance por encima del seguro** — no se elimina `toy` para abaratar la póliza | 09-09 | Vigente |
| D-20 | Doble capa: análisis completo guardado + resumen ejecutivo en el chat | 09-07 | Vigente |
| D-21 | **DELTA-FIRST** como regla permanente (`protocolo.md`) | 09-15 | Vigente |
| D-22 | Blindar las 3 core (≈ −375/mes) y subir precio se deciden juntas | 09-07 | Pendiente · **pierde sentido con la salida** |
| D-24 | `b0gr46x8y8` desde QW5 es product targeting, no Paid Core. **PAID CORE = NONE** | 09-15 | Vigente |
| D-25 | **Precio Q4:** test en **22,99** · techo **27,99** · R46 como control · piso promocional 24,99 | 09-17 | **Pendiente de autorización** |
| D-26 | Título de QW5 por incumplimiento (134/75), título primero y precio después | 09-17 | **Obsoleta:** Amazon ya dejó ambos títulos en 32 car. |

### Acciones aprobadas y no ejecutadas

| # | Cambio exacto | Bloqueante / nota 06-oct |
|---|---|---|
| A-1 | Recortar −70 % las dos `SP-(LooseMatch)` → `down only` | Bulk + autorización · **sigue valiendo** |
| A-2 | Cortar la puja de QW5 sobre `b0gr46x8y8` (US$ 63,99/30d, 5 compras) | Bulk |
| A-3 | Lista **DO NOT BID** de product targeting: **+US$ 355/30d** | Bulk · **sigue valiendo** |
| A-4 | Gasto removible único **609,36/30d (12 %)**, neto **+484,90/30d** | Bulk + autorización |
| A-5 | Bajadas de puja en 3 tiers sobre 22 términos (−22 % a −82 %). `reflex game` en R46 no se toca | No se conoce la puja vigente |
| A-6 | 14 campañas Exact nuevas, tope 1,50 | Bulk + takeover · dudoso con la salida |
| A-7 | Harvesting de 20 términos (+130 con 128 de gasto) | Falta search volume |
| A-8 | Asignar cada keyword núcleo a su ASIN → ≈ US$ 339/mes | D-11 |
| A-9 | Blindaje de las 3 core (≈ −375/mes) | **Pierde sentido con la salida** |
| A-10 | Escalera de precio 22,99 / 24,99 / 27,99 | GO/NO-GO · condicionar a velocidad de salida |
| A-11 | Main image CONCEPTO A en ambos | Producción creativa |
| A-12 | Basic A+ (7 módulos, 6 compatibles sin Brand Registry) | Verificar en Seller Central |
| A-13 | Vine | **ANULADA** — sin Brand Registry |
| A-14 | R46 Item Highlights → `Reaction Time Hand Speed Test - Falling Sticks Catching Game for Athletes, Kids & Adults - 3 Adjustable Speeds (Sky Blue)` | Campo "Subtítulo" sin confirmar · R46 congelado como control |
| A-15 | Backend nuevo. ADD: `reaction time trainer` · `falling sticks` · `catch the stick` · `hand eye coordination toy` · `family game night` · `party game adults` · `screen free game` · `agility trainer` · `reflex trainer`. REMOVE: `speed stick` · `game stick` · `match sticks` · `lacrosse` · `hockey` · `boost controller` · `stick control` · `birth control` | Recuperar el backend actual primero |
| A-16 | Conquesting contra Tendry | Imposible a 19,99; rentable desde 27,99 |
| A-17 | Nuevo mandato y reporte de la agencia (SOP-004) | `UNKNOWN` si se comunicó |
| A-18 | QW5 TITLE → `Reflex Drop Sticks Challenge Game, Falling Stick Reaction Time Toy (Yellow)` | **Obsoleta** (título ya cambiado) — y revisar "Toy" con la vía de compliance |
| A-19 | QW5 Item Highlights → `Hand Speed Challenge Game with Remote Control - 3 Adjustable Speeds, 6 Game Modes, Voice Prompts - Kids & Adults 3+` | ⚠️ **Choca con el flag de compliance**: "Kids 3+" es justamente lo que lo disparó. Sólo después de tener el test de laboratorio |
| A-20 | Escalera de precio QW5 desde 22,99, R46 en 19,99 como control | Autorización |

### Bloqueo permanente (sin autorización puntual)
No ejecutar en Seller Central ni Ads · no comprar seguro ni pagar quote/bind · no subir COI · no cambiar la Legal Entity · no sacar EIN · no contratar domicilio US · no esconder categorías para cotizar · no quitar `toy` por conveniencia del seguro · **no reestructurar campañas antes de Q4** · **no pausar automáticas**.

### Historial (E = ejecutado en Amazon · A = aprobado, sin evidencia de ejecución)

| Fecha | Qué cambió | |
|---|---|---|
| 02/04-mar-2026 | Alta de QW5 y R46 | E |
| abr-2026 | Ya se vendía, a ~14,99 (227 u en abril) | E |
| 16-jun → 2-jul | 17 días con cero sesiones, causa sin registrar | E |
| 27-jul | Amazon: TITLE ≤75 + ITEM HIGHLIGHTS ≤125 | E |
| 14 → 31-jul | Llega la agencia. Baseline PPC: 1.335,82 · ACoS 41,56 % | E |
| ~1-ago | La agencia duplica el gasto diario (+106 %) y lo deja plano | E |
| **19 → 20-ago** | **Ruptura de conversión**: CVR 22,57 % → 15,68 %. Causa `UNKNOWN` | E |
| desde 22-ago | Precios divergen por ASIN: R46 sube, QW5 baja hasta 17,99 | E |
| 25-ago | Rank de categoría se invierte: R46 #90 · QW5 #34 | E |
| 29-ago → 15-sep | Amazon mueve ambos ASINs a Toys & Games › Kids' Handheld Games | E |
| 4 → 14-sep | Títulos reducidos a `Reflex Challenge Drop Stick Game` (32 car.) | E |
| 7 → 15-sep | Removal order −US$ 3.774,96 (quién y cuántas `UNKNOWN`) | E |
| 14-sep | Takeover de Ads por Santi | A — sin registro |
| 22-sep | Flag "Children's toys" en QW5 (plazo 06-dic) | E |
| 20-oct | Precio → 22,99 | A |
| 2-nov | Amazon: cambio en categorías *enhanced-safety* | futuro |
| 10-nov | Precio → 24,99 | A |

---

## 17. Riesgos y datos faltantes

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/riesgos.md`_

## REFLEX — Conflictos abiertos y datos faltantes

> Los riesgos de mayor impacto hoy (06-oct) son de **compliance y seguro**: ver `compliance.md`. Esta lista es el registro técnico del expediente.

### Conflictos de Reflex / cuenta KINAVARGAS

| ID | Descripción | Estado al 06-oct |
|---|---|---|
| **C-28** | Stock: ~4.100 estimado vs ≤3.499 calculado vs **3.400 declarado (15-sep)** vs **3.550 citado (28-sep)** | **ABIERTO** — cierra con el informe de inventario FBA por ASIN |
| **C-29** | Ventana del Business Report por ASIN (590 u) sin declarar vs serie diaria (533 u) | ABIERTO (bajo) |
| **C-30** | Color por ASIN: portfolios de Ads invertidos | ✅ RESUELTO — **R46 = marco AZUL / palos AMARILLOS · QW5 = marco AMARILLO / palos AZULES.** Identificar por ASIN |
| **C-11** | Legal entity de la cuenta | **Probablemente resuelto (28-sep):** Maria Eugenia Vargas, persona física. Confirmar con captura de Account Info → Business Information |
| **C-12** | Precio de referencia 19,99 ≠ precio real | ✅ RESUELTO (19-sep): R46 20,88 · QW5 19,06 (25-ago→3-sep). Falta el precio vigente hoy |
| **C-13** | Batería | **Casi resuelto (06-oct):** la caja dice **INTERNAL BATTERY · TYPE-C CHARGE**. Falta sólo el tipo de celda |
| **C-15** | Política de títulos | ✅ CERRADO: 75 TITLE + 125 ITEM HIGHLIGHTS; se permite repetir una palabra hasta 2 veces |
| **C-16** | Indexación ≠ relevancia ≠ ranking ≠ conversión | Regla metodológica vigente |
| **C-17** | ¿El "Subtítulo" es ITEM HIGHLIGHTS? | ABIERTO — R46 probable · QW5 desconocido |
| **C-18** | "Repetir tokens en backend cuesta cero" | CORREGIDO: es falso |
| **C-19** | `toy` no se elimina por conveniencia del seguro | Vigente — y la caja dice AGES 3+ |
| **C-20** | Rentabilidad PPC ≠ relevancia SEO | `outdoor games` / `backyard games` se excluyen de la puja, no del universo semántico |
| **NUEVO** | Vía A de compliance (14+ training) vs caja AGES 3+ vs seguro declarado como toy | **ABIERTO** — ver `compliance.md` |

### Datos faltantes — ordenados por lo que desbloquean

| # | Dato | Dónde se saca | Qué desbloquea |
|---|---|---|---|
| **1** | **Stock FBA por ASIN + fecha de recepción + antigüedad** | Seller Central → Inventario → Informe de inventario FBA | Plan de salida, C-28, recargo por inventario añejo |
| **2** | **Estado del seguro después del 01-oct** | Configuración → Información de la cuenta → Seguros para empresas | Riesgo de suspensión en Q4 |
| **3** | **Cotización de test ASTM F963-23 + CPSIA** e importador de registro | Laboratorio TIC partner de Amazon / factura de importación | Flag de QW5 (plazo 06-dic) |
| 4 | Precio de lista vigente por ASIN + ventas 30 d por ASIN | Seller Central / Business Report por ASIN | Escalera de precio |
| 5 | Removal Order Detail | Informes → Logística de Amazon → Retiradas de inventario, 01/09 → hoy | Los −US$ 3.774,96 |
| 6 | Placements y sus multiplicadores | UI de Amazon Ads (no viene en exports) | El 97,2 % de clics pagados sobre la puja |
| 7 | Negativos existentes | Bulk Operations export | Ejecutar negativos candidatos |
| 8 | Backend actual de ambos ASINs | Seller Central → Editar listing → Palabras clave | A-15 |
| 9 | Qué cambió el 19→20-ago | Returns report · Voice of the Customer · reseñas · historial del listing | Causa de −US$ 4.470/mes |
| 10 | Volumen (pies cúbicos) por unidad | Informe FBA | Cuantificar recargo por inventario añejo |
| 11 | Semana 22–28 ago de la agencia · nombre y contrato de la agencia | Planilla / factura | Cobertura de W6 |
| 12 | Search volume de los 20 términos de harvesting | Helium / Cerebro | A-7 |
| 13 | Basic A+: si los ASINs son seleccionables | A+ Content Manager | A-12 |
| 14 | Re-export del Search Term Report con atribución madura | Amazon Ads | Tramo 27-ago→3-sep subatribuido |

**No disponible sin Brand Registry:** Search Query Performance por ASIN, Vine, A+ Premium, Sponsored Brands.

---

## 18. Errores ya corregidos (no re-derivar)

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/errores-corregidos.md`_

## REFLEX — Errores de análisis ya corregidos (no re-derivarlos)

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

### Conflictos numéricos conocidos (misma métrica, distinta base)
- Presupuesto diario: **2.460** (119×20 + 2×40) es el correcto.
- Gasto sin compras W1: 1.829,56 (35,9 %) vs 1.991,63 (39,1 %) — definiciones distintas.
- Términos rentables W1: 176 vs 160 — mismo umbral, conteos distintos.
- Resultado W7: −1.194,80 (caja) vs −1.303,22 (reconstrucción).
- ASP realizado: 19,83 (W1) · 20,29 (W7) · 19,73 (Wx) — **usar el de cada ASIN**.
- Videos de Tendry: 8 vs 14 — sin resolver.

---

## 19. Protocolo DELTA-FIRST y fuentes

_Fuente: `Trabajo/E-commerce/Amazon/REFLEX/protocolo.md`_

## REFLEX — Protocolo DELTA-FIRST y fuentes

> Los archivos fuente (CSV de Amazon, Helium) viven en el vault **PROYECTOS 100K** (`90_INBOX/MASTER_IMPORTS/AMAZON/SOURCES/`) y en Descargas, no en esta carpeta.

### DELTA-FIRST (regla permanente desde 15-sep)

```
LAST VERIFIED BASELINE → NEW DATA ONLY → CALCULATE DELTA → FLAG MATERIAL CHANGES → DECIDE
```
**Nunca:** día nuevo → re-analizar todo el histórico.

El histórico completo se reabre **sólo** por: (1) contradicción entre fuentes · (2) anomalía material · (3) cambio de estrategia · (4) Santi pide auditoría completa.

#### Umbrales de materialidad

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

#### Reglas de procesamiento
- Los CSV crudos **se procesan con código (python/pandas), nunca leyendo filas**. Al modelo le llegan agregados.
- Un export nuevo se compara contra el último dato y **sólo el delta entra al contexto**.
- Si un dominio no cambió: **`NO ANALYSIS`**.
- Al cerrar una revisión se actualiza `ESTADO.md` con fecha y valores nuevos; no se crea un archivo por día.

#### Formato de una revisión
```
WHAT CHANGED
ANOMALIES
ACTION REQUIRED
NO ACTION
```
Sin recapitular el histórico.

### Fuentes primarias (en PROYECTOS 100K)

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

### Lo que todavía no existe y hay que bajar de Amazon
1. **Informe de inventario FBA por ASIN** (bloqueante #1)
2. Removal Order Detail 01/09 → hoy
3. Bulk Operations export (placements y negativos)
4. Export del listing con backend e Item Highlights
5. Returns report / Voice of the Customer (causa del 19→20 ago)
