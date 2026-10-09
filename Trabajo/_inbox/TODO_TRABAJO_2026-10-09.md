# TODO TRABAJO — foto del 2026-10-09

> Archivo generado con `scripts/exportar_todo.py`: junta en uno solo todos los archivos de `Trabajo/`.
> **No editar acá.** La versión que manda es cada archivo en su carpeta; esto es sólo para leer o pasar a otra sesión.
> Cada sección empieza con `## 📄 <ruta>` = el archivo original.

## Índice
- `CLAUDE.md`
- `_inbox/LEEME.md`
- `_inbox/PROMPT_TRASPASO.md`
- `_inbox/TRASPASO_migracion-a-code_2026-10-09.md`
- `Amazon/CLAUDE.md`
- `Amazon/_ARCHIVO/LEEME.md`
- `Amazon/_CUENTA-KINAVARGAS/CLAUDE.md`
- `Amazon/_CUENTA-KINAVARGAS/ESTADO.md`
- `Amazon/_CUENTA-KINAVARGAS/seguro.md`
- `Amazon/AVIE/CLAUDE.md`
- `Amazon/AVIE/ESTADO.md`
- `Amazon/AVIE/aplus.md`
- `Amazon/AVIE/competencia.md`
- `Amazon/AVIE/keywords.md`
- `Amazon/AVIE/listing.md`
- `Amazon/AVIE/ppc.md`
- `Amazon/AVIE/riesgos.md`
- `Amazon/KINA/CLAUDE.md`
- `Amazon/KINA/ESTADO.md`
- `Amazon/KINA/canales.md`
- `Amazon/KINA/economia.md`
- `Amazon/KINA/patente.md`
- `Amazon/KINA/proveedor.md`
- `Amazon/MT-BALL/CLAUDE.md`
- `Amazon/MT-BALL/ESTADO.md`
- `Amazon/MT-BALL/imagenes.md`
- `Amazon/MT-BALL/keywords.md`
- `Amazon/MT-BALL/listing.md`
- `Amazon/MT-BALL/operacion.md`
- `Amazon/MT-BALL/ppc.md`
- `Amazon/MT-BALL/riesgos.md`
- `Amazon/MT-BALL/assets/keywords_Q4_tracker.csv`
- `Amazon/REFLEX/CLAUDE.md`
- `Amazon/REFLEX/ESTADO.md`
- `Amazon/REFLEX/competencia.md`
- `Amazon/REFLEX/compliance.md`
- `Amazon/REFLEX/decisiones.md`
- `Amazon/REFLEX/economia.md`
- `Amazon/REFLEX/errores-corregidos.md`
- `Amazon/REFLEX/historia-19sep.md`
- `Amazon/REFLEX/listing-seo.md`
- `Amazon/REFLEX/ppc-keywords.md`
- `Amazon/REFLEX/ppc.md`
- `Amazon/REFLEX/protocolo.md`
- `Amazon/REFLEX/riesgos.md`
- `Amazon/REFLEX/ventas.md`
- `Amazon/TERPTECH/CLAUDE.md`
- `Amazon/TERPTECH/FICHA_DE_PRODUCTO.md`
- `Etsy/CLAUDE.md`
- `Paginas-Web/CLAUDE.md`

---

## 📄 `CLAUDE.md`

# Trabajo — contexto general

Carpeta raíz del trabajo (migrado desde Obsidian / Cowork). **Fuente principal: esta carpeta en la compu de Santi. Google Drive (`AMAZON/`) es copia de lectura para Claude en Cowork/app: al cambiar algo acá, subirlo también allá.** Claude Code lee este archivo
y además el `CLAUDE.md` de cada subcarpeta en la que se trabaje: acá va solo lo que aplica
a TODO; lo específico vive en su carpeta (regla: **write once, reference many**).

## Estructura
| Carpeta | Qué hay | Estado |
|---|---|---|
| `Amazon/` | Contexto madre de Amazon (quién soy, meta, cuentas, reglas duras) | ✅ migrado |
| `Amazon/AVIE/` | AVIE Lymphatic Contour Face Brush · B0GT75CR86 (Beauty Michele) | ✅ migrado |
| `Amazon/MT-BALL/` | MT Ball, magic meta ball con Maxi (Beauty Michele) | ✅ migrado |
| `Amazon/REFLEX/` | Reflex Game R46 / QW5 (KINAVARGAS) · modo liquidación | ✅ migrado |
| `Amazon/KINA/` | KINA Lymphatic Drainage Face Brush · B0GQJLP4TB · liquidación fuera de Amazon | ✅ migrado |
| `Amazon/TERPTECH/` | TerpTech Premium 650mAh · B0F9SXP5MW · batería 510 | ✅ ficha + 6 imágenes + line sheet · falta `ESTADO.md` |
| `Amazon/_CUENTA-KINAVARGAS/` | Cuenta KINAVARGAS: titular, seguro, casos | ✅ migrado |
| `Amazon/_ARCHIVO/` | Vaults de Obsidian en crudo (sólo consulta) | ⏳ pendiente: copiar desde los vaults en la compu |
| `Etsy/` | Ecosistema Etsy | ⏳ pendiente |
| `Paginas-Web/` | TerpTech / DTC, RapiPet y otros sitios | ⏳ pendiente: migrar desde `02 Negocios/` del vault |
| `_compartido/` | Lo transversal a todos los ecosistemas | vacío |
| `_inbox/` | Traspasos de chats viejos a repartir (ver `_inbox/LEEME.md`) | 1 traspaso |

Cada producto sigue la misma estructura: `CLAUDE.md` (lo estable) + `ESTADO.md` (dónde quedamos)
+ archivos temáticos (`listing.md`, `ppc.md`, `keywords.md`, `riesgos.md`, …) + `assets/`.

## Cómo trabajar
- Abrir Claude Code en la carpeta del producto/ecosistema que toque: así se carga sólo ese contexto.
- Antes de investigar afuera, buscar primero acá (grep por producto, ASIN, competidor, proveedor).
- Al cerrar cada sesión, actualizar el `ESTADO.md` del producto.

## Migrar más notas
`python scripts/migrar_obsidian.py RUTA_AL_VAULT` (desde la raíz del repo) muestra el plan;
con `--aplicar` copia. Ajustar `REGLAS` en el script al sumar productos nuevos.

---

## 📄 `_inbox/LEEME.md`

# _inbox — traspaso de chats viejos a la estructura `Trabajo/`

Acá caen los resúmenes (`TRASPASO_<tema>_<fecha>.md`) que genera cada chat viejo (Cowork / claude.ai / Code en la nube).
Una sesión local de Claude Code los reparte en la carpeta que corresponde y después los borra de acá.

`TODO_TRABAJO_<fecha>.md` **no es un traspaso**: es una foto de todo `Trabajo/` en un solo archivo (`python scripts/exportar_todo.py`), para leerlo donde no está el repo. No se reparte: su contenido ya está en las carpetas.

## Cómo se genera un traspaso
En cada chat viejo, pegar el prompt de `PROMPT_TRASPASO.md`. Guardar la respuesta como archivo en esta carpeta.

## Cómo lo procesa la sesión local (instrucciones para Claude)
Cuando Santi diga "procesá el inbox":
1. Leer cada `TRASPASO_*.md` de esta carpeta (uno por vez).
2. Ver su campo **Destino**. Si no tiene destino o no encaja, usar esta tabla:

| Tema del chat | Carpeta destino |
|---|---|
| AVIE / MT Ball / Reflex / KINA / TerpTech (Amazon) | `Amazon/<PRODUCTO>/` |
| Cuenta KINAVARGAS (seguro, casos, salud de cuenta) | `Amazon/_CUENTA-KINAVARGAS/` |
| Cuenta personal de Santi bloqueada (Sección 3), apelación | `Amazon/_CUENTA-PERSONAL-SANTI/` (crear: `CLAUDE.md` + `ESTADO.md`) |
| Shopify / web propia de TerpTech (DTC) | `Paginas-Web/TERPTECH-DTC/` (crear) y una línea en `Amazon/TERPTECH/CLAUDE.md` que apunte ahí |
| RapiPet u otro sitio | `Paginas-Web/<SITIO>/` (crear) |
| Etsy | `Etsy/` (una subcarpeta por tienda/producto si crece) |
| Transversal (LLC VirtualMed, impuestos, banco, meta 100k) | `_compartido/` |
| Ni idea | dejarlo acá y preguntar a Santi |

3. Repartir el contenido sin duplicar (**write once, reference many**):
   - Hechos estables (identidad, cuentas, proveedor, economía, reglas) → `CLAUDE.md` de esa carpeta.
   - Dónde quedamos, pendientes, decisiones abiertas, próximos pasos → `ESTADO.md`.
   - Detalle largo de un tema (listing, ppc, apelación, integración…) → archivo temático (`apelacion.md`, `integracion-shopify.md`, …) listado en el `CLAUDE.md`.
   - Si un dato ya existe en otro archivo: no copiarlo; poner referencia. Si contradice lo que hay: **no pisar**, anotarlo en `ESTADO.md` → "⚠️ Contradicciones a confirmar" con las dos versiones y fechas.
4. Mantener las marcas HECHO / INFERENCIA / HIPÓTESIS del traspaso. No inventar nada que no esté.
5. Nada de DNI, números de cuenta bancaria, contraseñas ni tokens completos en los archivos (sólo "últimos 4").
6. Actualizar la tabla de estado de `Trabajo/CLAUDE.md` (y de `Amazon/CLAUDE.md` si aplica).
7. Borrar el `TRASPASO_*.md` procesado, commitear (`git commit -m "Traspaso <tema>"`) y pushear.
8. Si existe la copia espejo en Google Drive, recordarle a Santi qué archivos cambiaron para subirlos.

---

## 📄 `_inbox/PROMPT_TRASPASO.md`

# Prompt para pegar en cada chat viejo

Copiá todo lo que está entre las líneas y pegalo en el chat (Shopify TerpTech, cuenta bloqueada, Etsy, etc.).
Guardá la respuesta como `Trabajo/_inbox/TRASPASO_<tema>_<AAAA-MM-DD>.md`.

---

Voy a cerrar este chat y pasar todo a una sesión de Claude Code que trabaja con carpetas locales. Armame UN solo archivo Markdown de traspaso con TODO lo valioso de esta conversación, para que otra sesión lo pueda repartir sin haber leído este chat.

Reglas:
- No inventes nada. Marcá cada dato como **HECHO** (confirmado, con fecha si la hay), **INFERENCIA** o **HIPÓTESIS**.
- Datos concretos > prosa: números, fechas, ASIN, montos, nombres, links, IDs de caso, nombres de archivos.
- Sin DNI, números de cuenta bancaria, contraseñas ni tokens completos (sólo últimos 4).
- Si algo se decidió y después se cambió, poné sólo la decisión vigente y una línea con la descartada y por qué.
- Si hay archivos/imágenes que se usaron en el chat, listalos con su nombre para que yo los copie a mano.

Formato exacto:

# TRASPASO — <tema> · <fecha de hoy>
**Origen:** <nombre del chat / herramienta> · **Destino sugerido:** <carpeta, ej. `Paginas-Web/TERPTECH-DTC/`>

## 1. Contexto estable (va a CLAUDE.md)
Qué es, cuentas/entidades involucradas, plataforma, proveedores, economía (costos, precios, márgenes), reglas y restricciones.

## 2. Estado actual (va a ESTADO.md)
- Dónde quedamos (última fecha con dato).
- Prioridades ordenadas.
- Decisiones tomadas (fecha · decisión · por qué).
- Decisiones abiertas (qué tengo que decidir yo).
- Próximos pasos concretos.

## 3. Detalle por tema (archivos temáticos)
Un subtítulo `### <tema>` por cada asunto largo (ej. apelación, integración, listing, pagos), con todo el detalle técnico: pasos hechos, configuraciones, textos redactados, respuestas recibidas.

## 4. Errores y aprendizajes
Qué salió mal, qué no hay que repetir, qué funcionó.

## 5. Datos faltantes
Lo que no se sabe y hay que confirmar, y dónde se confirma.

## 6. Archivos adjuntos
Nombre · qué es · dónde está hoy.

---

---

## 📄 `_inbox/TRASPASO_migracion-a-code_2026-10-09.md`

# TRASPASO — Mudanza Obsidian/Cowork → Claude Code · 2026-10-09
**Origen:** sesión de Claude Code en la nube "obsidian-data-migration" (2026-10-06 → 10-09) · **Destino sugerido:** `Trabajo/CLAUDE.md` y `ESTADO` de cada carpeta (casi todo ya está aplicado; esto es el registro y los pendientes)

> El contenido de los productos **ya está en el repo** (ver tabla de `Trabajo/CLAUDE.md`). Este traspaso no repite datos de productos: sólo lo que se decidió sobre cómo trabajar y lo que quedó pendiente.

## 1. Contexto estable
- HECHO · Repo GitHub `amazonfbasantino-wq/prueba`. Rama principal: **`claude/hopeful-allen-FxQrV`** (no existe `main`). Rama de trabajo de la mudanza: `claude/obsidian-data-migration-i9q4nd`.
- HECHO · Estructura: `Trabajo/` → ecosistema (`Amazon/`, `Etsy/`, `Paginas-Web/`) → una carpeta por producto. Cada producto: `CLAUDE.md` (estable) + `ESTADO.md` (dónde quedamos) + archivos temáticos + `assets/`. Regla **write once, reference many**.
- HECHO · `CLAUDE.md` en la raíz del repo: al empezar, leer sólo `CLAUDE.md` + `ESTADO.md` del producto; al cerrar, actualizar `ESTADO.md` y commitear; CSV grandes con scripts.
- HECHO · Fuente principal = carpeta local en la compu de Santi (clon del repo). **Google Drive `AMAZON/` = copia espejo de lectura** para Claude en Cowork/app (decisión 2026-10-08; antes se había dicho "Drive no se usa" y se revirtió).
- HECHO · `scripts/migrar_obsidian.py RUTA_VAULT [--aplicar]`: clasifica notas de un vault (carpeta o .zip) en `Trabajo/` por palabras clave (`REGLAS`); sin `--aplicar` sólo muestra el plan; nunca pisa archivos.
- HECHO · Una sesión de Claude Code en la nube **no ve la compu de Santi**. Para trabajar sobre Finder: Claude Code local (app de escritorio, pestaña Code, o `claude` en Terminal) dentro del clon:
  `git clone https://github.com/amazonfbasantino-wq/prueba.git ~/Trabajo-Santi`

## 2. Estado actual
**Migrado y verificado (tamaño + codificación):** Amazon madre, AVIE, MT-BALL (+ `keywords_Q4_tracker.csv`), REFLEX, KINA, `_CUENTA-KINAVARGAS`, TerpTech (ficha + 6 imágenes + line sheet PDF; las imágenes y el PDF los subió Santi por git, commit `1432368`).

**En Drive `AMAZON/TERPTECH/`:** `CLAUDE.md` y `07_line_sheet_mayorista.pdf` (subidos 2026-10-08). La ficha está suelta en `AMAZON/` como `TERPTECH_FICHA_DE_PRODUCTO.md`.

**Pendientes (por orden):**
1. Santi: arrastrar `TERPTECH/imagenes/` a Drive `AMAZON/TERPTECH/` (muy pesadas para subirlas desde la nube).
2. Santi: abrir el PDF en Drive y confirmar que se ve bien (sólo se verificó el tamaño, 4907 bytes).
3. Reemplazar el `CLAUDE.md` de Drive `AMAZON/` por la versión del repo (la de Drive es vieja: sin TerpTech). Pendiente de OK de Santi.
4. `Amazon/TERPTECH/ESTADO.md`: no hay datos de stock, estado de cuenta ni objetivo → preguntar a Santi, no inventar.
5. Traspasar los chats viejos con `PROMPT_TRASPASO.md`: Shopify/TerpTech DTC, cuenta personal bloqueada, Etsy, RapiPet y cualquier otro.
6. `Amazon/_ARCHIVO/`: copiar los vaults crudos (`obsidian c`, `PROYECTOS 100K`) desde la compu (sólo consulta).
7. `Paginas-Web/`: migrar `02 Negocios/` del vault.
8. Commit "Drive vuelve como copia espejo…" y los archivos de `_inbox/` están en la rama de trabajo; fusionar a la rama principal si todavía no se hizo.

**Decisiones abiertas (de Santi):** punto 3; cómo mantener el espejo de Drive al día (a mano al cerrar cada sesión, o sólo cuando haga falta para Cowork).

## 3. Detalle
### Cómo trabajar con poco contexto
- Un chat/sesión por frente (un producto o una cuenta). No mezclar.
- Abrir Claude Code en la carpeta del producto; arranca leyendo `CLAUDE.md` + `ESTADO.md`.
- Al cerrar: "actualizá ESTADO.md y commiteá". Si el chat se llena: cerrar y abrir otro; el `ESTADO.md` es la memoria.
- Archivos pesados (imágenes, PDF, CSV) se suben por git o se copian en la carpeta local, no por el chat.

## 4. Errores y aprendizajes
- Verificar sólo el tamaño no alcanza: `REFLEX/decisiones.md` tenía el mismo tamaño y estaba corrupto (se reconstruyó). Siempre revisar también codificación UTF-8 / caracteres raros, o comparar checksums.
- Drive pidió "Insufficient scope" hasta reconectarlo con acceso completo de lectura.
- La carpeta `TERPTECH_TRANSFER_2026-10-07` de Drive quedó vacía (la subida desde la compu no llegó); se resolvió subiendo por git.

## 5. Datos faltantes
- TerpTech: stock, estado de cuenta/listing, objetivo, economía (→ Santi).
- Nombres reales de las carpetas/sitios de Páginas Web y tiendas de Etsy (→ chats viejos / vault).

## 6. Archivos adjuntos
Ninguno nuevo: todo está en el repo.

---

## 📄 `Amazon/CLAUDE.md`

# AMAZON — contexto madre (Claude Code)

> Claude Code carga este archivo solo. Cada subcarpeta tiene su propio `CLAUDE.md` con el ecosistema de UN producto.
> Abrí Claude Code **dentro de `AMAZON/`** y trabajá en la carpeta del producto que toque. No leer otras carpetas salvo que la tarea lo pida.

## Quién soy y a dónde voy
- **Santi** (Santino Navarria) · Mendoza, Argentina · vendedor Amazon FBA en **Amazon.com (US)** desde fines de 2023.
- **Visión:** empresa en Amazon con catálogos enteros → primer millón facturado.
- **Meta de corto plazo:** USD 100.000 de **beneficio neto** al 31-dic-2026 (después de producto, fees, envío, ads e impuestos).

## Cuentas y entidades
| Cuenta / entidad | Qué es | Productos |
|---|---|---|
| **Beauty Michele** | Vendedor individual, persona natural, titular en Luján de Cuyo (Mendoza) | AVIE (50/50 con mi pareja) · MT Ball (en preparación) |
| **KINAVARGAS** (ACC-002) | Titular Maria Eugenia Vargas (no es parte de la LLC) | KINA (discontinuado), Reflex Game (liquidación) |
| Cuenta personal de Santi | Bloqueada por Sección 3 | — |
| **VIRTUALMED SOLUTIONS LLC** | LLC de Florida (domicilio Sarasota) · miembros: Santi + Pablo · banco: Bank of America | — |
| Socio externo | Maxi (vive en Utah) | MT Ball |

## Mapa de carpetas
| Carpeta | Producto | ASIN | Estado de la mudanza |
|---|---|---|---|
| `AVIE/` | AVIE Lymphatic Contour Face Brush | B0GT75CR86 | ✅ migrado 2026-10-06 |
| `MT-BALL/` | MT Ball (meta ball, con Maxi) | — | ✅ migrado 2026-10-06 |
| `REFLEX/` | Reflex Game (KINAVARGAS) · **modo liquidación** | B0GR46X8Y8 · B0GQW5F2LL | ✅ migrado 2026-10-06 |
| `KINA/` | KINA Lymphatic Drainage Face Brush · **liquidación fuera de Amazon** | B0GQJLP4TB | ✅ migrado 2026-10-06 |
| `TERPTECH/` | TerpTech Premium 650mAh (batería 510) | B0F9SXP5MW | ✅ ficha + 6 imágenes + line sheet · falta `ESTADO.md` |
| `_CUENTA-KINAVARGAS/` | Cuenta KINAVARGAS: titular, seguro, casos, reglas | — | ✅ migrado 2026-10-06 |
| `_ARCHIVO/` | Los dos vaults de Obsidian completos, en crudo (sólo consulta) | — | ver `_ARCHIVO/LEEME.md` |

## Estructura de cada producto
Cada carpeta tiene siempre `CLAUDE.md` (lo estable: identidad, economía, objetivo, reglas) y `ESTADO.md` (dónde quedamos, prioridades, decisiones abiertas; se actualiza al cerrar cada sesión). El resto son archivos temáticos chicos (listing, ppc, keywords, competencia, riesgos…) listados en el `CLAUDE.md` de cada producto. Imágenes y datos en `assets/`.
Regla: **WRITE ONCE — REFERENCE MANY.** Un dato vive en un solo archivo; los demás apuntan.

## Dónde está todo
- **Carpeta local `Trabajo/Amazon/` en la compu de Santi** (Finder): **copia de trabajo para Claude Code** (versión condensada; manda ante diferencias). **Google Drive `AMAZON/`** = copia espejo para que Claude la lea desde Cowork/app; mantenerla al día.
- Vault Obsidian `obsidian c` → `AMAZON/`: misma estructura, versión extendida de algunas tablas, más las imágenes.
- `_ARCHIVO/`: los dos vaults completos en crudo (`obsidian c` y `PROYECTOS 100K`: CSV, imágenes, expedientes viejos), leídos directo desde la compu. **Sólo consulta**; ante diferencias manda esta carpeta.

## Cómo quiero que trabajes
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

## Reglas duras (todas las cuentas)
- **Nunca ejecutar cambios en Seller Central ni en Amazon Ads sin mi autorización explícita y puntual.** Investigar, calcular y escribir en los archivos: sí.
- Marcas ajenas: **prohibidas** en título, bullets y backend · **permitido** pujar por ellas en PPC.
- Términos temporales ("christmas"): no en título ni backend; sí en Recommended Uses y bullets.
- Sin claims médicos en campos indexables ("reducer", "lymph node", "detox", "elimina toxinas").
- Lo que se declara a Amazon, al seguro y en la caja tiene que ser **la misma verdad**.
- Cuidado con phishing de falso soporte Amazon (ej. dominio esc-amazon.com): Amazon sólo se contacta desde Seller Central.

## Al cerrar cada sesión
Actualizar `ESTADO.md` del producto: qué se hizo, qué sigue (en orden), qué NO hacer, y la fecha.

---

## 📄 `Amazon/_ARCHIVO/LEEME.md`

# _ARCHIVO — los dos vaults de Obsidian completos, en crudo

Acá están, sin tocar, los dos vaults de Obsidian de Santi:

- `obsidian c/` — vault operativo (incluye su propia carpeta `AMAZON/` con las imágenes de AVIE y Reflex en `assets/`).
- `PROYECTOS 100K/` — vault histórico: expedientes completos, CSV y exports de Amazon Ads, Business Reports, settlements, Helium 10, fotos de producto, decisiones (DEC-###), investigaciones (RES-###), SOPs y el registro de conflictos.

## Cómo usarlo
- **La fuente de trabajo es `AMAZON/`** (la carpeta de arriba): está ordenada por producto y actualizada al 07-oct-2026.
- `_ARCHIVO/` es **sólo para consulta**: buscar un dato crudo, un CSV, una imagen o el detalle de un análisis viejo.
- **Ante cualquier diferencia entre `_ARCHIVO/` y `AMAZON/`, manda `AMAZON/`.**
- Muchos documentos del archivo están superados por versiones posteriores (están marcados SUPERSEDED, LEGACY o "no enviar"). No reabrir decisiones viejas a partir de ellos.
- Los CSV crudos se procesan con código (python/pandas), no leyendo filas.

---

## 📄 `Amazon/_CUENTA-KINAVARGAS/CLAUDE.md`

# CUENTA KINAVARGAS (ACC-002) — lo que es de la cuenta, no de un producto

> Seguro, titular, documentos, seguridad. Los productos de esta cuenta tienen su carpeta: `../REFLEX/` (liquidación activa) y `../KINA/` (fuera de Amazon, liquidación multicanal).

## Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Dónde quedamos, prioridades, decisiones abiertas |
| `seguro.md` | Requisito de seguro de Amazon (deadline 01-oct, vencido), brokers, decisiones, trampas |

## Datos de la cuenta
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

## Productos de la cuenta
| Producto | ASIN | Estado |
|---|---|---|
| Reflex Game R46 / QW5 | B0GR46X8Y8 · B0GQW5F2LL | Activos · **modo liquidación**, salir en dic-2026 |
| KINA Lymphatic Drainage Face Brush | B0GQJLP4TB | **Desactivado** por patente · discontinuado en Amazon · stock retirado a Miami |

## Casos
| Caso | Estado |
|---|---|
| CASE-001 · patente de diseño D1063405 (complaint 20503982181) | ABIERTO · appeal despriorizado → `../KINA/patente.md` |
| CASE-003 · INFORM Act (bug de verificación de CUIT) | ✅ Resuelto |
| Children's toys (QW5, aviso 22-sep, plazo 06-dic) | ABIERTO → `../REFLEX/compliance.md` |
| Seguro de responsabilidad civil (deadline 01-oct) | ABIERTO / vencido → `seguro.md` |

## Objetivo de la cuenta
Liquidar el stock de Reflex hasta diciembre y **no volver a usar la cuenta** después (decisión de Santi, 28-sep). Todo se evalúa contra ese horizonte: proteger la cuenta hasta vaciarla, no construir nada a largo plazo.

## Reglas duras de la cuenta
1. **No cambiar la legal entity a la LLC.** Dispara reverificación en pleno Q4 y, con la cuenta personal de Santi bloqueada por Sección 3, puede vincular KINAVARGAS con esa cuenta.
2. **No crear ASINs nuevos de KINA** (ni FBM ni con otro listing) para esquivar el reclamo de patente: arriesga la cuenta entera.
3. **Phishing:** "Joseph" @esc-amazon.com (y cualquier dominio no oficial) = estafa. No compartir Case ID, Merchant ID, documentos ni códigos. Canales válidos: Seller Central, Account Health, foros oficiales.
4. Lo que se declara a Amazon, al seguro y en la caja del producto tiene que ser **la misma verdad**.
5. No mezclar con Beauty Michele (AVIE / MT Ball): otra cuenta, otro titular, cero datos cruzados.
6. No guardar en estos archivos DNI completos, números bancarios ni contraseñas.

---

## 📄 `Amazon/_CUENTA-KINAVARGAS/ESTADO.md`

# CUENTA KINAVARGAS — ESTADO

**Actualizado:** 2026-10-06 (migración) · **Último dato:** 28-sep

## ⚠️ Primero: confirmar
1. **¿Qué pasó con el seguro después del 01-oct?** Mirar Configuración → Información de la cuenta → Seguros para empresas, y Account Health.
2. ¿Respondieron Sadler (Paul Owens), Veracity, Coyle, Allianz/Chubb AR por la póliza a nombre de Eugenia?
3. ¿Se mandó la corrección a Sadler (toy/children's product, importador, proyección USD 60,000)?
4. ¿Quién figura como **importador de registro** de Reflex? (define a nombre de quién va el CPC y qué se declara al seguro)

## Prioridades
1. **Seguro aceptado por Amazon** → protege ~US$ 17.800 de stock de Reflex en el único trimestre que importa. Prima esperada US$ 1.000–3.500/año: comprar es decisión obvia frente al capital en juego.
2. **Compliance de Reflex** (`../REFLEX/compliance.md`) — mismo underwriter va a pedir CPC/tests: hacer las dos cosas juntas.
3. Mantener la cuenta sana hasta vaciarla (no tocar legal entity, no listings nuevos de KINA).

## Decisiones abiertas (de Santi)
- Camino del seguro: (a) póliza a nombre de **Eugenia** vía productor argentino o surplus lines — preferido; (b) póliza a nombre de **VirtualMed** con Eugenia como *additional named insured* — Well preguntó si Amazon lo acepta, pero expone la LLC (riesgo de vínculo con la cuenta bloqueada de Santi); (c) cambiar legal entity — **descartado**.
- Póliza corta / provisoria (sólo hasta diciembre) vs anual: Santi prefiere corta.

## Historial
- 2026-10-06 · Migrado a `AMAZON/_CUENTA-KINAVARGAS/`.
- 2026-09-28 · Well dice NO a persona física extranjera (pide LLC + FEIN). Se descubre que la cuenta personal de Santi está bloqueada por Sección 3 → se descarta usar VirtualMed. Vuelve el camino a nombre de Eugenia. Account Health: Healthy, AHR 232; el seguro todavía no aparecía como Priority Action.
- 2026-09-24 · Contacto con brokers: Santi como encargado de seguros de su LLC, Eugenia como Named Insured, estructura expuesta desde el primer mensaje.
- 2026-09-15 · Agosto ≈ US$ 15.000 brutos → el umbral de US$ 10.000/mes se disparó: obligación real. 3 defectos en la aplicación a Sadler.
- 2026-09-14 · KINA confirmado discontinuado en Amazon; Reflex único producto a asegurar.
- 2026-09-03 · INFORM Act resuelto.
- 2026-08-31 · Amazon pide prueba de seguro antes del 01-oct.

---

## 📄 `Amazon/_CUENTA-KINAVARGAS/seguro.md`

# CUENTA KINAVARGAS — Seguro de responsabilidad civil (Amazon BSA §9)

## Requisito de Amazon (verificado)
- CGL / Product Liability, base **occurrence** · **US$ 1M por ocurrencia / US$ 1M agregado** · deducible ≤ **US$ 10.000** · carrier **AM Best A−** o mejor.
- Additional insured: **"Amazon.com Services LLC and its affiliates and assignees"** · P.O. Box 81226, Seattle, WA 98108-1226, Attn Risk Management.
- **Named Insured = legal entity de Seller Central = Maria Eugenia Vargas** (persona física). El COI se compara carácter por carácter.
- Gatillo: la cuenta superó **US$ 10.000 brutos en un mes** (agosto ≈ US$ 15.000). Aviso del 31-ago, **plazo 01-oct-2026** (vencido; estado actual UNKNOWN).
- Cambio de Amazon del **02-nov-2026** sobre categorías *enhanced-safety*: Reflex cae en dos (producto infantil + batería).

## El bloqueo estructural
Casi ningún carrier de EE.UU. asegura a una **persona física extranjera sin entidad US**. Los que lo hacen van por **surplus lines / Lloyd's vía broker**.
- **Well Insurance (28-sep):** exige LLC/Corp US + dirección US + FEIN. "Ninguna aseguradora US cubre a un extranjero sin entidad US".
- **VirtualMed SOLUTIONS LLC** cumple los 3 (FL Doc L23000540019, Sarasota, FEIN), **pero** Santi es miembro y su cuenta personal de Amazon está **bloqueada por Sección 3** → mostrar la LLC a Amazon puede vincular KINAVARGAS con la cuenta bloqueada. **No recomendado** sin análisis aparte.

## Proveedores — dónde está cada uno
| Prioridad | Proveedor | Estado |
|---|---|---|
| 1 | **Sadler & Company** (Paul Owens) | Aplicación enviada 14-sep. Underwriter asignado. **Corregir la declaración antes del quote** (ver abajo) |
| 1 | **Productor argentino → Allianz / Chubb AR** (póliza corta a nombre de Eugenia) | A contactar. Allianz AR 0810-222-2243 · Liderar Seguros (0261) 425-3109 · Seguros Mendoza +54 261 508-9118 · Mendoza Broker 261 541-3000. Duda: jurisdicción US + COI |
| 2 | Veracity · Coyle Group (surplus lines) | Esperando respuesta |
| 2 | Assureful (modelo pay-as-you-sell, desde ~US$ 26/mes, no confirmado) | Borrador en Gmail sin enviar |
| — | Well Insurance | Dice NO a persona física; sólo vía LLC |
| ✖ | Marsh / Amazon Insurance Accelerator · Spott · Azure Risk · Aligned · Konsileo · carriers online con domicilio US | Descartados |

Regla: **broker = puede decir que sí; carrier con formulario online = exige domicilio US y bloquea.**

## Aplicación a Sadler (14-sep) — 3 defectos a corregir por escrito ANTES de la cotización
1. Se declaró "consumer recreational game" → la caja dice **AGES 3+**: declarar **toy / children's product**. Si no, el carrier puede **rescindir por misrepresentation** y la póliza no sirve.
2. Se declaró sólo "Retailer" → marcar también **Importer / Distributor** (el importador responde como fabricante en EE.UU.).
3. "18.000" se lee dieciocho en EE.UU. → escribir **USD 60,000** de proyección (la cifra real, no 18,000).

## Economía de la decisión
Prima de mercado para toy: US$ 1.000–10.000/año, típica ~3.500. Frente a ~US$ 17.800 de stock de Reflex por liquidar en Q4, **comprar es obvio**; lo que importa es que la póliza **no se caiga** (declaración exacta).

## Documentos que pide un broker
DNI de Eugenia + domicilio tal cual Seller Central · captura de legal entity y Merchant Token · ASINs + fotos + ficha técnica (material, batería, edad) · ventas brutas 12 meses + proyección · invoices de proveedores · certificados (CPC/CPSIA) · historial de reclamos (cero) · captura del aviso de Amazon.

## Prohibido sin autorización puntual
Comprar seguro · pagar quote/bind · subir COI · cambiar legal entity · sacar EIN · contratar domicilio US · esconder categorías para abaratar.

---

## 📄 `Amazon/AVIE/CLAUDE.md`

# AVIE — Lymphatic Contour Face Brush · B0GT75CR86

> Ecosistema completo del producto. Lo estable vive acá; lo que cambia, en `ESTADO.md`.
> Antes de trabajar: leer este archivo + `ESTADO.md`. Abrir el resto sólo si la tarea lo pide.

## Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Dónde quedamos, pendientes, fechas, decisiones abiertas |
| `listing.md` | Título, destacado, backend, bullets, atributos, imágenes — copy vigente |
| `aplus.md` | A+ Premium: alt text final, headline/body, pendientes |
| `ppc.md` | Plan 900 USD/mes, versiones A/B, reglas de PPC |
| `competencia.md` | Los 9 ASINs rivales, los dos mercados, a quién atacar |
| `keywords.md` | GAP de indexación, ángulo regalo, capas de puja |
| `riesgos.md` | 14 contradicciones/bloqueantes + compliance |
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

## Economía por unidad (cerrada 2026-09-16)
- **Costo puesto en FBA: 2,86 USD** (producto 2,50 + 3PL 0,36) · lote: 5.000 uds = 14.300 USD
- **FBA 3,24** · comisión Beauty **8 % hasta 10,00 USD, 15 % por encima** (estimación del calculador FBA)

| Precio | Neto Amazon | Margen/ud | **Break-even ACOS** | Términos rentables (de 18 con venta) |
|---|---|---|---|---|
| 9,99 | 5,95 | 3,09 | **30,9 %** | 2 |
| 14,99 | 9,50 | 6,64 | 44,3 % | 11 |
| 16,99 | 11,20 | 8,34 | **49,1 %** | 12 |
| 19,95 | 13,72 | 10,86 | 54,4 % | 14 |

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
- Presupuesto ads: **900 USD en octubre** (camino A); nov-dic según resultados.
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

---

## 📄 `Amazon/AVIE/ESTADO.md`

# AVIE — ESTADO

**Actualizado:** 2026-10-06 (migración) · **Último trabajo real:** 2026-09-22 · **Frente:** ⏸️ EN PAUSA por límite de 2 frentes

## ⚠️ Primero: datos que faltan (las fechas duras ya pasaron)
Al 06-oct no hay registro de que se haya ejecutado nada. Antes de cualquier análisis, confirmar:
1. **Precio real hoy** (¿se subió a 16,99 el 1-oct? ¿sigue en 9,99 o 12,99?) → define break-even 30,9 % vs 49,1 %.
2. ¿Se publicó **imagen principal nueva + título v3** (límite era 30-sep)?
3. ¿Se lanzaron campañas de octubre? ¿Versión A o B? ¿Cuánto se gastó del 1 al 6-oct?
4. Stock FBA actual y ventas de los últimos 30 días.
5. ¿A+ Premium aprobado y alt text cargado? ¿Estado del IP Accelerator?

## Orden de ejecución pendiente (no ejecutar sin OK puntual de Santi)
1. **Precio a 16,99** — sin esto, cada dólar de PPC financia pérdida.
2. **Imagen principal limpia** (hoy collage de 4 → CTR 1,38 %).
3. **Título v3 + destacado + backend v3** (`listing.md`) — antes, decidir si se quita "lymph node".
4. **Corregir atributos:** Público "Girls" → Women · Material vs copy · Fabricante → AVIE · rellenar Palabra clave genérica, Beneficios, Características, Recommended Uses (11 de regalo).
5. **Subir límite de compra** 5 → 30 (regalo/multipack).
6. **A+:** cargar alt text final + headline/body del módulo 1 · escribir headline/body módulos 2-5 · **falta módulo REGALO**, escala y comparativa vs piedra.
7. **PPC:** elegir versión A o B (`ppc.md`) y lanzar 29 USD/día **después** del precio.

## Decisiones abiertas (de Santi)
- Versión A (6 campañas) o B (8 campañas) del plan PPC.
- Aceptar o rebatir el acta: criterio de victoria 2.000 uds / TACOS 5 % vs proyección ≈1.380 uds / TACOS 25-30 %.
- Qué hacer con el capital inmovilizado (≈2.400 uds proyectadas al 31-dic): ¿segundo canal, liquidación parcial, 2-pack?

## No hacer
Tocar el nodo · meter marcas ajenas en backend · reestructurar campañas antes de 21 días de datos · cambiar pujas con menos de 14 días entre cambios.

## Lectura de director
El problema de AVIE no es el PPC: es **precio + existencia**. A 9,99 sólo 2 de 18 términos son rentables y el producto es invisible (0,34 % del volumen en top 50). Q4 regalo es la única ventana del año para rotar 10.805 USD de stock parado a precio alto. Cada semana de octubre sin precio 16,99 + imagen + título es Q4 perdido, no postergado.

## Historial
- 2026-10-06 · Migrado a `AMAZON/AVIE/` desde `02 Negocios/Amazon-FBA/Productos/AVIE-B0GT75CR86/`.
- 2026-09-22 · Alt text A+ Premium final + headline/body módulo 1. Imágenes mobile generadas.
- 2026-09-21 · Título v3 (63 car.), backend v3, Cerebro 9 ASINs, auditoría de atributos. Manual entregado (`plan-ejecucion-B0GT75CR86.html`).
- 2026-09-16 · Economía cerrada, objetivo nuevo, camino A, acta de discrepancia, decisión versión B de PPC.

---

## 📄 `Amazon/AVIE/aplus.md`

# AVIE — A+ Premium (alt text, headline y body)

## 7 · A+ Premium
Imágenes finales en `assets/aplus/` (desktop-1…5 y mobile-1…5).
Reglas alt text: máx 100 car., sin puntuación, sin repetir palabra, describir lo que se ve + 1-2 keywords, sin claims. Territorio libre: facial · tools · set · soft · bristles · gift · women · her · self care · wellness · skin · sensitive · neck · cheekbone · ergonomic.


| # | Módulo | Slot | Alt text | Car. |
|---|---|---|---|---|
| 1 | header | **desktop** | `AVIE pink brush in a marble bowl beside its case on the bathroom counter with towels and leaves` | 95 |
| 1 | header | **mobile** | `Soft bristle head beside its pink gift case` | 43 |
| 2 | features | **desktop** | `Labelled graphic on a beige backdrop naming soft bristles contoured design and comfortable grip` | 96 |
| 2 | features | **mobile** | `Curved head with dense fibres and smooth body` | 45 |
| 3 | rutina | **desktop** | `Four numbered steps beside the woman using a brush at her vanity with round mirror and plants` | 94 |
| 3 | rutina | **mobile** | `Model easing the pad across her cheek and jaw` | 45 |
| 4 | viaje | **desktop** | `Brush with its case packed in a cream pouch beside luggage dried flowers and one lipstick on linen` | 98 |
| 4 | viaje | **mobile** | `Pouch holding the rose box and a lipstick` | 41 |
| 5 | skincare | **desktop** | `Woman in bath towel using the brush along her jaw beside its case on a bright marble counter` | 92 |
| 5 | skincare | **mobile** | `Person sweeping the pad below one ear` | 37 |

**Tags (iguales en los dos slots del mismo módulo):** `avie` · `b0gt75cr86` · `aplus-premium` · `header|features|rutina|viaje|skincare` · `v1`
**AI-generated people:** tildar SÓLO en el módulo 3 (rutina) y el 5 (skincare). Destildar en 1, 2 y 4.


### Pendientes del A+
- Ningún titular nombra el drenaje linfático; "ritual" repetido en 4 de 5 → corregir.
- **Falta módulo REGALO** (el más barato de ganar), escala/tamaño y comparativa vs piedra gua sha.
- Headline + body de los módulos 2-5 sin escribir. Verificar contador de caracteres en Seller Central.

### Headline y Body text · MÓDULO 1 (header) — escrito 2026-09-22

**Headline (69 car.)**
```
Lymphatic Drainage Massager and Gua Sha Tool in One Soft Facial Brush
```

**Body text (≈520 car.)**
```
Most lymphatic drainage tools are hard stone or cold steel. AVIE is a soft-bristle massager: it glides over the face without dragging the skin, so a full pass takes about two minutes and feels good enough to repeat every day.

The curved head follows the jawline, cheekbones and neck. Use it dry in the morning to de-puff, or over your oil or serum at night.

Every AVIE ships in a hard travel case that keeps the bristles clean in a bag or a drawer - and makes it ready to give.
```

**Por qué así:**
- Es el **primer lugar del listing entero donde aparece `lymphatic drainage massager`** (68.965 búsq./mes, rankean 8 de 8 competidores y AVIE no) junto a `gua sha` (187.132). El título de 63 car. ya está cerrado y el backend está al tope: este campo era la única puerta que quedaba.
- El body abre nombrando la **categoría rival por material** (piedra, acero) sin nombrar marcas — ahí es donde el cepillo blando gana.
- Cierra con el **estuche rígido** y el gancho de regalo, que es el ángulo aprobado y el diferenciador frente a Aeki y Ghnadyvc.

**Compliance verificado:** sin claims médicos (no dice toxinas, no dice reduce, no dice drena linfa) · **no dice "Natural Material"** (contradiría el atributo Material = Plastic) · sin marcas ajenas · sin "makeup" (evita la intención maquillaje de `contour brush` y `face mask brush`).

---

## 📄 `Amazon/AVIE/competencia.md`

# AVIE — Competencia

## Competencia (fichas 2026-09-16, 9 ASINs del Cerebro 2026-09-21)

El nicho tiene **dos mercados dentro del mismo nodo**, y AVIE está compitiendo en el equivocado.

### Los dos mercados
- **Abajo (8,99-9,99):** se gana con volumen brutal y 1.000+ reseñas. AVIE tiene 38 reseñas y juega acá.
- **Arriba (14,99-19,95):** venden 750-2.115 uds/mes con sólo **64-207 reseñas**. **El objetivo vive arriba.**

### Fichas abiertas 2026-09-16
| ASIN | Marca | Precio | Nota·Reseñas | Uds/mes | A+ | Choice |
|---|---|---|---|---|---|---|
| B0FD354L27 | FLAHOLD | 8,99 | 4,3 · 1.564 | 10K+ | ✅ | ✅ |
| B0H5MBL5PY | Kitsch | 9,99 | 4,6 · 114 | 10K+ | ✅ | ✅ |
| B0GLYRSGM2 | Cxguu (2 uds) | 9,99 | 4,4 · 468 | 4K+ | ✅ | ✅ |
| **B0GFSMWTPK** | **Aeki** (estuche rígido) | **16,99** | **4,1 · 91** | **750** | — | ✅ |
| B0FWK4FTCD | Aeki (2 uds) | 17,98 | 4,2 · 667 | 1.469 | — | Overall Pick |
| B0FWK4QMQJ | Aeki | 14,99 | 4,2 · 667 | 1K+ | — | — |
| B0GSQW56YT | Ghnadyvc (3 en 1) | 17,99 | 4,8 · 207 | 2.115 | ✅ | — |
| **B0GVBQ7P79** | **Cheersendex** (caja regalo) | **19,95** | **4,7 · 64** | **782** | — | ✅ |
| **B0GT75CR86** | **AVIE** | **9,99** | 4,4 · 38 | **104** | ✅ (nuevo) | — |

### ASINs a atacar con PPC
- ✅ **B0GFSMWTPK** — Aeki 16,99, nota **4,1**, 91 reseñas. Es el gemelo de AVIE (estuche rígido) y el más débil de arriba.
- ✅ **B0GVBQ7P79** — Cheersendex 19,95, 64 reseñas. Ángulo regalo.
- ❌ **NO B0FD354L27** (FLAHOLD 8,99, 1.564 reseñas): ahí se va hoy el 15 % del presupuesto — **185,79 USD con ACOS 76,6 %, 8,44 USD de ads por unidad**. Campaña PAUSADA.

### Los 9 ASINs del Cerebro (definidos 2026-09-21)
| # | ASIN | Marca | Precio | Nota·Rev | Uds/mes | Nodo · puesto | Para qué sirve |
|---|---|---|---|---|---|---|---|
| 1 | B0FD354L27 | FLAHOLD | 8,99 | 4,3·1.564 | 10K+ | Contour Brushes #1 | Universo completo de keywords |
| 2 | B0H5MBL5PY | Kitsch | 9,99 | 4,6·114 | 10K+ | Contour Brushes #2 | Keywords de marca US y clean beauty |
| 3 | B0GLYRSGM2 | Cxguu 2 uds | 9,99 | 4,4·468 | 4K+ | Manual Facial Cleansing #6 | Multipack y otro nodo |
| 4 | B0GSQW56YT | Ghnadyvc | 17,99 | 4,8·207 | 2.115 | Contour Brushes #10 | **El modelo del rango alto** |
| 5 | B0GFSMWTPK | Aeki | 16,99 | 4,1·91 | 750 | Contour Brushes #13 | **Su gemelo: estuche rígido** |
| 6 | B0GVBQ7P79 | Cheersendex | 19,95 | 4,7·64 | 782 | Contour Brushes #19 | **Ángulo regalo a 19,95** |
| 7 | B0G8KQ5XFG | Kotomotoy | 9,99 | 4,5·152 | 700 | Contour Brushes #16 | **Maestro de campos estructurados** |
| 8 | B0FWK4FTCD | Aeki 2 uds | 17,98 | 4,2·667 | 1.469 | Manual Massage Tools | Overall Pick, nodo Health & Household |
| 9 | B0F5S6N75Z | Kitsch acero | 12,99 | 4,6·1.312 | 1K+ | Manual Massage Tools #5 | Gua sha acero, otro nodo |

### CORRECCIÓN al market tracker (importante)
- **B0F5S6N75Z (11,1 %) y B09RQ9GLDJ (9,6 %) son la misma ficha de Kitsch** en variaciones distintas (Iridescent y Silver).
- **B0GSKVSPV2 (7,7 %) es la variación Grey-2pcs de FLAHOLD.**
- **≈28 % del donut son DOS productos, no cinco.** → **La cuota real de AVIE frente a cepillos comparables es mayor que el 1,9 % que marca el tracker.** No usar el 1,9 % como número de decisión.

### Lo que hace Kotomotoy (B0G8KQ5XFG) y AVIE no
`Recommended Uses` con 11 valores de regalo · `Set Name` con keyword completa · campo Fabricante = "Lymphatic Contour Face Brush Factory" · **8 bullets**. Está en #16 con 700 uds/mes con el mismo precio de 9,99 que AVIE, que hace 104.

---

## 📄 `Amazon/AVIE/keywords.md`

# AVIE — Keywords (GAP de indexación y capas de puja)

## PARTE 2 · Cerebro 9 ASINs + AVIE (2026-09-21) — GAP de indexación

3.529 keywords en bruto procesadas; universo relevante tras filtrar ruido: **1.704 keywords · 2.603.847 búsquedas/mes**. La conclusión es que AVIE nunca compitió en igualdad.

### Dónde está AVIE en su propio nicho
| Dónde | Keywords | Búsquedas/mes | % del universo |
|---|---|---|---|
| Aparece (top 306) | 359 | 516.040 | 19,8 % |
| Top 200 | 215 | 208.185 | 8,0 % |
| Top 100 | 81 | 59.479 | 2,3 % |
| **Top 50** | **14** | **8.819** | **0,34 %** |
| **Top 10** | **4** | **1.406** | **0,05 %** |

**HECHO: es visible (top 50) en el 0,34 % del volumen del nicho.** No es un problema de puja: es un problema de existencia.

### El GAP
**218 keywords relevantes donde rankean 4+ de los 9 competidores y AVIE no = 674.329 búsquedas/mes.**
Alcanzables (volumen 500-15.000): **116 kw · 172.223 búsquedas/mes**.

Las peores:
| Keyword | Búsquedas/mes | Competidores que rankean |
|---|---|---|
| `lymphatic drainage massager` | 68.965 | **8 de 8** |
| `lymphatic` | 7.087 | **8 de 8** |
| `lymphatic drainage tools` | 2.512 | **8 de 8** |
| `gua sha` | 187.132 | 6 |
| `lymphatic drainage` | 128.729 | 4 |

> **Cuando 8 de 8 rankean y vos no, no es competencia: es que no estás indexado.** De ahí "massager" en el título v3 y "drainage" en el destacado.

### HALLAZGO: sus mejores posiciones son keywords de MARCAS AJENAS (ganadas por el PPC)
| Keyword | Posición | Volumen |
|---|---|---|
| `kitsch face brush for lymphatic drainage` | **#23** | 1.764 |
| `kitsch lymphatic brush` | #40 | 637 |
| `kitch lymphatic contour face brush` | #49 | 1.246 |
| `kitsch face brush` | #58 | 2.516 |
| `kitsch lymphatic face brush` | #61 | — |
| `nuvetra lymphatic face brush` | #65 | — |
| `aeki lymphatic contour face brush` | #70 | 5.652 |
| `cotsoco lymphatic contour face brush` | #82 | — |
| **`gelly brush`** | **#42** | 1.596 · **0 de 8 competidores rankean** |
| Mejor genérica: `face brush for lymphatic drainage` | **#52** | 6.735 |

**Lectura empresarial:** el activo orgánico que tiene hoy está construido sobre demanda de marca ajena — es real, convierte (`kitsch/kitch` = 4 clics, 2 ventas) y es **prestado**. `gelly brush` en #42 sin competencia es territorio propio y está sin explotar. Y `lymphatic contour face brush avie` ya tiene 1 clic y 1 venta: **la marca empieza a buscarse sola**.
Pujar por marcas ajenas: permitido. Meterlas en backend: prohibido.

### ÁNGULO REGALO CONFIRMADO POR DATOS
**62 keywords alcanzables · 74.747 búsquedas/mes · media de 1,0 competidor de 8 rankeando.** Nadie en el nicho trabaja el regalo. Ver `CLAUDE.md` (Objetivo).

### Volumen por raíz en su cluster (2026-09-16)
brush 129.561 · lymphatic 93.199 · face 90.025 · contour 49.977 · **drainage 23.916 (NO estaba en el título)** · facial 3.559 · glow 3.296 · sculpting 3.223 · guasha 3.055 · soft 2.112 · bristle 854.

### Lo que el PPC SÍ construyó pese al ACOS del 91 %
face brush for lymphatic drainage 212→**48** (+164) · lymphatic face brush 209→**114** (+95) · lymphatic facial brush 196→102 (+94) · lymphatic drainage face brush 143→77 (+66) · face sculpting brush lymphatic 204→139 (+65).
**INFERENCIA, no causa probada:** coincide con el PPC (1.204 USD) *y* con la bajada de precio a 9,99 en agosto. No se puede atribuir sólo al PPC.

### Keywords vírgenes (volumen, sin PPC)
`face sculpting brush` 2.200/mes (org #130, 0 clics) · `face sculpting brush lymphatic` 1.023/mes (org #139).

### NO perseguir
`contour brush` (14.719/mes) ni `face mask brush` (4.280): son brochas de maquillaje y de mascarilla, otra intención de compra. Org #296 y >306.

### PINK — su único diferenciador de color
Aeki marrón/negro · Ghnadyvc marrón · Cheersendex nogal · Kitsch negro. Términos con "pink": 7-9 clics, 6 ventas (CVR ~67-86 %). **ADVERTENCIA: muestra de 9 clics, no concluyente.**


## PARTE 3 · Capas de puja por keyword (16-sep, siguen vigentes)
- Cabeza: lymphatic contour face brush 0,45 · lymphatic face brush 0,45 · lymphatic drainage brush 1,10 · face brush for lymphatic drainage 0,30 · lymphatic brush 0,35. No perseguir contour brush / face mask brush.
- Cuerpo: lymphatic brush for face 0,50 (0/12, vigilar) · face lymphatic drainage brush 0,80 · **face sculpting brush 0,60 (virgen)** · facial brush for lymphatic drainage 1,30 · guasha brush for face 1,30 · lymphatic drainage face brush 0,50 (0/6) · guasha brush 1,50 · face sculpting brush lymphatic 0,60.
- Cola: pink / dry / soft / natural bristles / ergonomic / rose quartz.

---

## 📄 `Amazon/AVIE/listing.md`

# AVIE — Listing (copy vigente, listo para pegar)

> Versión v3 del 2026-09-21. Anula el título de 196 car. del 16-sep. Estado: **pendiente de ejecución** (confirmar en `ESTADO.md`).

## Regla de los 75 caracteres
Seller Central: *"La información aparecerá solo cuando el nombre del producto tenga menos de 75 caracteres."* Con título ≥75 se pierde el subtítulo.
Rivales de marca van cortos y con subtítulo (Aeki 59 · Cheersendex 68 · Kitsch 68/55); los de volumen, largos y sin él (Ghnadyvc 188 · FLAHOLD 179). AVIE juega arriba → corto.

## 1 · Título (63 car.)
```
AVIE Lymphatic Contour Face Brush - Gua Sha Glow Massager, Pink
```

## 2 · Destacado del artículo / Item Highlight (113 car., cero palabras repetidas del título)
```
Dry brushing for drainage and de-puffing. Guasha tool for jawline sculpting and double chin. Travel case included
```
Cubren juntos: lymphatic + drainage + massager (gap 68.965 búsq.) · gua sha · guasha · dry brush · jawline · sculpting · double chin · glow (blinda #42-50) · pink · travel case.

## 3 · Backend Search Terms (247 de 250 bytes)
```
gelly depuffer puffiness lymph node detox firming toning korean spa kit scraper quartz jade roller cooling morning routine facece guasa lympathic limphatic escova drenagem rosto cepillo masajeador brosse visage drenaje linfatico esthetician vanity
```
⚠️ Contiene **"lymph node"** (y "detox", "firming") = lenguaje de claim. Decidir si se quitan antes de publicar (ver `riesgos.md` #8).

## 4 · Bullets (1 cluster cada uno)
1 drainage (sin "stimulates") · 2 sculpting/jawline/double chin · 3 guasha + dry brush + soft bristle · 4 pink/ergonomic/sensible · 5 **regalo + estuche rígido** (acá va "gift for her" y lo estacional).
Modelo Kotomotoy (B0G8KQ5XFG): **8 bullets**.

## 5 · Atributos a corregir / rellenar
| Campo | Hoy | Acción |
|---|---|---|
| Público de destino | "Girls" + "Unisex Adult" | → **Women / Female** ("Girls" = niñas) |
| Material | "Plastic" | Alinear con el copy (no decir "Natural Material" si queda Plastic) |
| Fabricante | "Dongguan Songli Plastic Indrustry Co., Ltd." | → **AVIE** (expone proveedor + errata) |
| Palabra clave genérica | 2 valores | **Agujero nº1** — rellenar multivalor |
| Beneficios (115 car. c/u) | sólo "Massager" | **Agujero nº2** — Cxguu rellena 12 y vende 4K/mes |
| Características especiales / del material | 1 valor c/u | Rellenar |
| Recommended Uses | — | **11 valores de regalo** (Christmas gifts for her, Stocking Stuffers, Mother's Day…) |
| Set Name | — | Keyword completa |
| Límite de compra | 5 | → 30 |
| Nodo | `face-contour-brushes` | **NO TOCAR** |

## 6 · Imágenes del listing (orden objetivo)
1 principal limpia (producto 85 %) · 2 pink + estuche · 3 drainage · 4 jawline · 5 cerdas · 6 regalo · 7 medidas · 8 vs piedra · 9 vídeo.
Hoy: principal en **collage de 4 elementos** = problema nº1 (CTR 1,38 %).

---

## 📄 `Amazon/AVIE/ppc.md`

# AVIE — PPC

Presupuesto aprobado para octubre. **Hay dos repartos vivos y no coinciden: resolver antes de tocar Ads.**

## Hallazgo que manda en las pujas
**Pagaba 1,05 USD de CPC igual en términos con CVR del 4 % que en los de CVR del 28 %.** Ese es el error estructural, no el gasto total. La cabeza (`lymphatic contour face brush`, CVR 7,4 %) baja a 0,45.
Contexto: ACOS 91,2 % · **347,62 USD gastados en 209 términos sin una sola venta**.

## VERSIÓN A — plan aprobado (master PPC, 2026-09-21) · 6 campañas
| Campaña | Términos | Puja | USD/día |
|---|---|---|---|
| `AVIE_BRUSH_EW_EX_US` | guasha brush · aeki lymphatic contour face brush · dry brush for lymphatic drainage | 1,50 | 8 |
| `AVIE_BRUSH_EW2_EX_US` | facial brush for lymphatic drainage · lymphatic drainage brush for face · guasha brush for face · dry brush face | 1,30 | 6 |
| `AVIE_BRUSH_EW3_EX_US` | lymphatic drainage brush · pink lymphatic drainage brush | 1,10 | 4 |
| `AVIE_BRUSH_GEN_EX_US` | lymphatic contour face brush · lymphatic face brush | **0,45** | 3 |
| `AVIE_BRUSH_COMP_ASIN_US` | B0GFSMWTPK (Aeki 16,99) · B0GVBQ7P79 (Cheersendex 19,95) | 1,20 | 4 |
| `AVIE_BRUSH_GIFT_PH_US` | gua sha gift set · facial massager gift · skin care tools gift set | 0,80 | 4 |
| ~~SP-(1)-ProductT-IndividualP-Exact~~ (B0FD354L27) | **PAUSADA** — 8,44 USD/ud | — | 0 |
| **Total** | | | **29** |

## VERSIÓN B — decisión de Santi del 2026-09-16 · 8 campañas
Aprobó recortar para financiar dos campañas nuevas y quedar igual en 29/día:
| Campaña | Versión A | Versión B |
|---|---|---|
| AVIE_BRUSH_EW_EX_US | 8 | 6 |
| AVIE_BRUSH_EW2_EX_US | 6 | 5 |
| AVIE_BRUSH_EW3_EX_US | 4 | 4 |
| AVIE_BRUSH_GEN_EX_US | 3 | 3 |
| AVIE_BRUSH_COMP_ASIN_US | 4 | 4 |
| AVIE_BRUSH_GIFT_PH_US | 4 | **2** |
| **AVIE_BRUSH_SCULPT_EX_US** (face sculpting brush · face sculpting brush lymphatic, puja 0,60) | — | **2** |
| **AVIE_BRUSH_PINK_EX_US** (pink lymphatic drainage brush · pink guasha brush · pink facial brush · pink lymphatic face brush, puja 1,40) | — | **3** |
| **Total** | **29** | **29** |

## ⚠️ CONTRADICCIÓN ABIERTA — DECISIÓN QUE HACE FALTA
El master PPC del **21-sep** no incorpora la decisión del **16-sep**. O el master no la absorbió, o la decisión se revirtió sin dejar acta. **Ninguna de las dos versiones está ejecutada en Ads.**
- **Versión A** concentra en términos maduros. Más seguro, cero exploración.
- **Versión B** compra dos apuestas baratas: `face sculpting brush` (2.200/mes, **0 clics históricos**, territorio virgen) y el cluster `pink` (único diferenciador de color). Cuesta 5 USD/día quitados a EW y GIFT.
- **Sesgo a declarar:** el cluster `pink` se apoya en una muestra de 7-9 clics. No es evidencia, es una hipótesis barata.

## El número que decide: break-even ACOS
| Precio | Break-even ACOS |
|---|---|
| 9,99 | **30,9 %** |
| 14,99 | 44,3 % |
| 16,99 | **49,1 %** |
| 19,95 | 54,4 % |

**Con ACOS histórico del 91 % y precio 9,99, cada campaña pierde dinero por definición.** A 16,99 el mismo PPC entra en zona viable. **La palanca es el precio del 1-oct, no la puja.** Poner los 900 USD antes de subir el precio es financiar pérdidas.

## Reglas heredadas de la fase anterior (siguen vigentes)
- Una keyword no gradúa a exact hasta **10+ clics y 2+ pedidos**.
- Una campaña no se evalúa antes de **21 días**; entre cambios de puja, **14 días**.
- Única acción semanal permitida: negativizar términos con **15+ clics y 0 pedidos**.
- Familias más fuertes confirmadas: **"drainage"** y **"contour face"**.
- Riesgo histórico diagnosticado: **bucle de sobreoptimización** (demasiadas reestructuraciones sobre datos insuficientes).

## Revisión
**Todos los lunes, 45-60 min.** Seguir posición orgánica de: lymphatic contour face brush · lymphatic face brush · lymphatic drainage brush · face brush for lymphatic drainage · guasha brush for face · face sculpting brush.

---

## 📄 `Amazon/AVIE/riesgos.md`

# AVIE — Riesgos y contradicciones abiertas

> Se revisa cada lunes. Lo cerrado se tacha con fecha.

| # | HECHO | RIESGO / IMPACTO | DATO FALTANTE o DECISIÓN |
|---|---|---|---|
| 1 | El master dice "precio actual 9,99" (ficha 16-sep) y a la vez "calendario: 12,99 hoy → 16,99 el 1-oct" | Todo el break-even ACOS y el reparto de pujas dependen del precio real. Si hoy es 9,99, el break-even es 30,9 % y **cada campaña pierde** | **Confirmar el precio real de hoy.** Bloquea el plan de PPC |
| 2 | Hay dos repartos de presupuesto vivos (6 campañas vs 8 campañas), ambos a 29/día | Se ejecuta el equivocado o no se ejecuta ninguno | Elegir versión A o B → `ppc.md` |
| 3 | **A+ subido el 16-sep sin Registro de Marca** | A+ requiere Brand Registry o autorización de marca. Si se subió por una vía no estándar, puede caerse | Confirmar cómo se subió y si está aprobado |
| 4 | Campo **Brand = "Generic"**, y el título v3 empieza con **"AVIE"** | Riesgo de rechazo del título o de supresión | Confirmar si se puede cambiar Brand sin Registro. IP Accelerator en trámite |
| 5 | Campo **Material = "Plastic"**, el copy dice **"Natural Material"** | Reseña negativa por expectativa incumplida + incoherencia de ficha | Decidir cuál es la verdad y alinear ambos |
| 6 | **Público de destino = "Girls"** (= niñas) | Segmentación errónea y riesgo de política en categoría Beauty | Cambiar a Women / Female |
| 7 | Campo **Fabricante** = "Dongguan Songli Plastic **Indrustry** Co., Ltd." | Expone al proveedor a la competencia + errata visible | Poner AVIE |
| 8 | Backend v3 incluye **"lymph node"** | Lenguaje de claim médico/cosmético en categoría Beauty | Decidir si se quita antes de publicar |
| 9 | Cliente espera **TACOS 5 % en diciembre**; el análisis dice **25-30 %** | El frente se declara fracasado estando en plan | Acordar el criterio de victoria real (ver acta de discrepancia) |
| 10 | Objetivo declarado: **2.000 uds en diciembre**; el análisis dice **≈1.380** y cierre al 31-mar-2027 | Mismo riesgo que #9 + decisiones de recompra sobre una proyección falsa | Aceptar o rebatir el acta del 16-sep |
| 11 | **Límite de compra: 5 uds/pedido** (competidores: 30) | Techo artificial en regalo y multipack, justo el ángulo elegido | Subirlo antes de Q4 |
| 12 | **Sin variaciones** (todos los competidores tienen 2-4) | Menos superficie de ficha y menos reseñas acumuladas | Evaluar variación (2-pack o segundo color) |
| 13 | **Imagen principal en collage de 4 elementos** | CTR 1,38 % — es el problema nº1 declarado | Fecha límite **30-sep** |
| 14 | 3.778 uds en stock, ≈**10.805 USD de capital inmovilizado**, rotación ~755 días al ritmo actual | Es el mayor riesgo económico del producto, por encima del ACOS | Ninguna decisión tomada sobre liquidación parcial o segundo canal |

## Compliance — reglas duras
- **Marcas ajenas (kitsch, kojeva, nuvetra, aeki, cotsoco): PROHIBIDO en backend y en copy. PERMITIDO pujar por ellas en PPC.**
- **Términos temporales ("christmas"): NO en título ni backend.** Sí en Recommended Uses y bullet 5.
- **Claims médicos/cosméticos:** evitar "reducer", "lymph node", "lifting firming" en campos indexables.
- **Sin autorización explícita y puntual de Santi no se ejecuta nada en Seller Central ni en Amazon Ads.**

---

## 📄 `Amazon/KINA/CLAUDE.md`

# KINA — Lymphatic Drainage Face Brush (B0GQJLP4TB)

> Ecosistema del producto. Lo estable vive acá; lo que cambia, en `ESTADO.md`. Cuenta: `../_CUENTA-KINAVARGAS/`.

## ⚠️ Objetivo vigente: LIQUIDAR EL INVENTARIO FUERA DE AMAZON
Desde el 03-sep (DEC-018 / DEC-019): KINA **no se construye como marca**. Se liquida el stock y se recupera capital.
Orden de optimización: **1 velocidad de venta · 2 recuperación de capital · 3 simplicidad operativa · 4 margen.** Sin descuentos irracionales: el piso lo fija la recuperación de capital.
La reactivación en Amazon está **despriorizada** (no resuelta): el caso de patente sigue abierto.

## Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Hechos vigentes, datos pendientes, decisiones abiertas |
| `patente.md` | Historia del reclamo D1063405 sobre el listing viejo en Amazon |
| `canales.md` | Red de liquidación: veredicto por canal, TikTok/Maxi |
| `economia.md` | Costo, fulfillment desde Miami, margen por canal, precios B2B |
| `proveedor.md` | Henan: invoice, conflictos de documentos, certificado de fabricante |

## Identidad
| Dato | Valor |
|---|---|
| Producto | Cepillo facial de drenaje linfático, **negro**, función gua sha |
| **Diseño para la venta (Santi, 07-oct)** | **Mango plano, sin la curvatura** del diseño reclamado · color negro. Con este diseño no aplica el reclamo de patente |
| ASIN | **B0GQJLP4TB** — listing **desactivado** por reclamo de patente · discontinuado en Amazon (14-sep) |
| Cuenta | KINAVARGAS (titular Maria Eugenia Vargas) |
| Marca | Listing bajo **"Generic"**. "KINA" es el nombre impreso, **NO es marca registrada** |
| Material | **NO VERIFICADO** (conflicto C-27): listing dice Plastic, una decisión vieja dice Walnut Wood, ni invoice ni caja lo declaran → **no afirmar ningún material** |
| Medidas | 3.2 × 1.3 × 2.5 in, < 8 oz |
| Proveedor | Henan Small Brush Dizzy Dyeing Trading Co., Ltd. (`proveedor.md`) |
| Compra | **8.500 u** a US$ 1,67 + DDP → **landed ≈ US$ 1,97/u** (2,07 si el total real es 17.626) · **capital ≈ US$ 16.700–17.600** |
| Stock | Removal de FBA procesada el 04-sep, en tránsito a Miami · ~500 u ya en Miami · Santi esperaba "miles" fuera de Amazon a mediados de sep · **cantidad real UNKNOWN** |
| Warehouse | Miami (2970 NW 75 AVE, FL 33122) · hace pick & pack unitario y mayorista a costo ≤ FBA (confirmado 06-sep) |
| Mercado | El mismo que AVIE: usar los datos de mercado de `../AVIE/` para estimar demanda |

## Reglas propias de KINA
1. **Nunca decir "purchased 8,000"**: se compraron **8.500**; ~8.000 fueron a Amazon.
2. **Nunca decir que KINA es marca registrada** ni que el listing está bajo Brand KINA.
3. **No afirmar material** en ningún listing hasta tenerlo verificado (caja, cartón o declaración firmada de Henan).
4. **No crear ASINs nuevos en Amazon** para esquivar el reclamo: arriesga la cuenta entera.
5. **No abrir cuentas a nombre de la LLC si sus dueños tienen cuentas de Amazon suspendidas** (Santi: Sección 3) — en Amazon nunca; en otros canales, evaluar caso por caso.
6. **No presentar a la LLC como dueña del inventario** sin una transferencia real y documentada (la compradora en la invoice es Eugenia).
7. KINA se vende con **mango plano** (sin curvatura), fuera del diseño reclamado. No volver a plantear la patente como freno para vender.
8. Nada se crea ni se ejecuta (cuentas, tiendas, listings, contactos, gasto) sin aprobación explícita de Santi.

---

## 📄 `Amazon/KINA/ESTADO.md`

# KINA — ESTADO

**Actualizado:** 2026-10-07 · **Último trabajo real:** 06-sep · **Fase:** PRE-EJECUCIÓN (nada creado, nada contactado)

## Hechos vigentes
- Objetivo: **liquidar el inventario fuera de Amazon** (DEC-018 / DEC-019).
- **Diseño para la venta: mango plano, sin curvatura, color negro** (Santi, 07-oct).
- Removal de FBA procesada el 04-sep; ~500 u ya estaban en Miami; Santi esperaba miles fuera de Amazon a mediados de septiembre.
- El warehouse de Miami hace pick & pack unitario y mayorista a costo ≤ FBA (06-sep).
- Plan TikTok Shop de 15 días y mensaje a Maxi redactados el 06-sep, sin enviar.

## Datos pendientes
1. Unidades que llegaron a Miami (Removal Order ID, despachadas, vendibles vs no vendibles, costo de la removal).
2. Ventas desde septiembre por cualquier canal.
3. Costo exacto por orden del warehouse de Miami.
4. Respuesta de Maxi (si se le mandó).
5. Material real del producto.

## Decisiones abiertas (de Santi)
- Canales donde se vende (ver `canales.md`).
- Piso de precio por unidad.
- Propuesta a Maxi (% o fee) si se va por TikTok Shop.

## No hacer
Afirmar material sin verificarlo · llamar "marca registrada" a KINA · decir "purchased 8,000" · registrar tiendas a nombre de alguien sin rol real · crear, publicar o contactar sin aprobación de Santi.

## Historial
- 2026-10-07 · Santi define el diseño de venta: mango plano, negro.
- 2026-10-06 · Migrado a `AMAZON/KINA/`.
- 2026-09-14 · KINA discontinuado en Amazon; fuera del seguro.
- 2026-09-06 · Warehouse de Miami confirma pick & pack ≤ FBA. Plan TikTok Shop + mensaje a Maxi.
- 2026-09-04 · Removal de FBA procesada, unidades en tránsito.
- 2026-09-03 · DEC-018 (salida de Amazon) y DEC-019 (objetivo = liquidación).

---

## 📄 `Amazon/KINA/canales.md`

# KINA — Canales de liquidación

> Investigación de septiembre (fuentes oficiales 03/04/06-sep). **Nada abierto, nadie contactado.**

## Diseño
KINA se vende con **mango plano, sin la curvatura** del diseño reclamado, color negro (Santi, 07-oct). El reclamo de patente queda como historia del listing viejo en Amazon (`patente.md`), no como freno de canales.

## Veredicto por canal (EE.UU.)
| Canal | Potencial | Acceso hoy | Nota |
|---|---|---|---|
| **eBay** | Medio | 🟢 **Abierto** como vendedor Argentina | Payout Payoneer USD · fees ≈ 18,7 % · el sobre barato no aplica (2,5 in de alto) · vender en **packs** (la competencia: 2×8,99 · 3×8,49 · 4+×7,49) |
| **B2B / liquidación por lote** | Alto | 🟢 Abierto | Compradores de excedentes de belleza: oferta en 24–48 h, compra en firme, producto nuevo y sellado. Liquidation.com: lotes ≥ US$ 5.000, paga tras la entrega |
| **Faire** (B2B a retailers) | Medio | 🟡 Sólo con LLC (W-9 + EIN + banco US) | 0 % Faire Direct · 15 % + US$ 10 primer pedido marketplace. Mejor precio que un liquidador, ritmo lento |
| **Shopify Payments / DTC mínimo** | Medio | 🟡 Con LLC (acepta pasaporte extranjero) | Destino del tráfico de TikTok / Google / Meta |
| **Walmart** | Medio-alto | 🟡 Casi abierto | Filtro real: historial de ventas + GS1 |
| **TikTok Shop US** | **Muy alto** (vía LIVE) | 🔴 Bloqueo estructural | El representante necesita ID de EE.UU. (+ SSN/ITIN según fuente). Ni Santi ni Pablo lo tienen |
| TikTok creators / orgánico → eBay o checkout | Alto | 🟢 Abierto | No requiere TikTok Shop |
| Google Shopping | Medio | 🟢 | Capa de tráfico |
| Meta | Alto | ⚪ Sin verificar | |
| Etsy | — | ❌ Excluido | Política de reventa |

**Dato 28-sep:** VirtualMed LLC tiene FEIN, dirección en Sarasota y banco (Bank of America). La compradora en la invoice de KINA es Eugenia.

## Fuera de EE.UU.
Argentina / LatAm (MercadoLibre, distribuidores y mayoristas de belleza), Amazon MX y otros. Costo a resolver: flete Miami → destino + importación.

## Volumen esperable (con datos de AVIE + Helium Influencer Finder, 06-sep)
- La demanda de búsqueda de AVIE **sí** proyecta eBay / Walmart; **no** proyecta TikTok (ahí la demanda se crea con contenido).
- Video shoppable de ~5.000 vistas → ~3–15 u. **Un LIVE de ~47.000 vistas → decenas a +100 u en una sesión.** Si se va a TikTok, el volumen está en LIVE.
- Con ~500 u ningún canal nuevo se justifica (eBay + B2B). Con **miles**, sí: Walmart primero, TikTok LIVE después.

## TikTok Shop — plan de 15 días (06-sep, no ejecutado)
- Única puerta: **representante con ID de EE.UU. con rol real**. Opción: **Maxi** (Utah) entrando como socio de la entidad que registra la tienda. Nunca un prestanombre (descartado el registered agent de Tampa).
- Mensaje a Maxi redactado (sin enviar): propuesta concreta (% o fee — **falta completar**).
- Producto principal: **bundle x2 a 19,99** (mueve el doble de unidades por orden). Margen estimado ≈ 35–40 % con fulfillment ~US$ 4.
- Secuencia: representante + costo por orden (días 1–2) → registro con datos idénticos en EIN, registro y banco (3–5) → producto (5–7) → afiliados (7–10) → muestras + primer LIVE (10–15). No contactar creadores antes de tener el producto publicado con comisión.

## Secuencia recomendada en septiembre (sólo con aprobación)
0 datos de la LLC · 1 eBay Argentina · 2 B2B en paralelo · 3 Shopify con LLC · 4 TikTok orgánico → eBay/checkout · 5 Walmart · 6 Google + Meta · 7 removal grande (ya hecho el 04-sep).

---

## 📄 `Amazon/KINA/economia.md`

# KINA — Economía: costo, fulfillment y precio por canal

## Costo
- **Landed ≈ US$ 1,97/u** (16.726 / 8.500) · **2,07** si el total real es 17.626 (conflicto C-24, ver `proveedor.md`).
- Capital total ≈ **US$ 16.700–17.600**.
- **Costo de reposición desde China del mismo arquetipo: US$ 0,50–1,50 FOB** (MOQ 10–1.000). Un liquidador cotiza contra eso, no contra el retail.
- Último dato en Amazon: precio 14,99 (efectivo ≈ 12,77) · 33 u/30 d.

## Fulfillment desde Miami (paquete 3.2 × 1.3 × 2.5 in, < 8 oz)
- **El franqueo es el costo dominante**, no el pick & pack.
- USPS Ground Advantage retail (desde 12-jul-2026, < 1 lb tarifa plana por zona): **US$ 7,90 (zona 1) → 9,45 (zona 8–9)**. Con etiqueta de plataforma: ~US$ 3–6 (orden de magnitud).
- 3PL benchmark: pick & pack 0,99–3,20 · storage 1–5/bin/mes · devoluciones 1–7 · **mínimos mensuales** (ej. US$ 1.000/mes) que a bajo volumen pesan más que el pick.
- **El warehouse actual de Miami** hace pick & pack a costo ≤ FBA y no tiene mínimo conocido → probablemente gana a cualquier 3PL nuevo.
- **Costo por orden de 1 unidad ≈ US$ 4,50–9,50.**

## Margen por canal (estimaciones)
| Canal | Precio | Neto/u aprox. | Nota |
|---|---|---|---|
| eBay, 1 unidad | 14,99 | **2,29–7,29** | Frágil: el franqueo se come casi todo |
| eBay, pack x2 / x3 | 2×8,99 / 3×8,49 | mejor por orden | El franqueo casi no sube con 2–3 u |
| TikTok Shop, 1 unidad | 12,99 | ≈ 4,59 (35 %) | Supuestos: 6 % referral (3 % los primeros 30 días), 15 % afiliado, US$ 4 fulfillment |
| TikTok Shop, bundle x2 | 19,99 | ≈ 3,98/u · 7,95/orden | Mueve el doble por orden |
| Faire (retailers) | WSP comparable 5–28 | — | Mín. de pedido del comprador 100–150 u |
| Liquidador / comprador de excedentes | anclado a 0,50–1,50 | ≈ costo o menos | Velocidad máxima, recuperación mínima |

## Envío B2B por lote
500 u ≈ 6 pies cúbicos → 2–3 cartones (parcel) o pallet LTL. LTL 1 pallet nacional ≈ US$ 456 mediana; Miami es el más barato del país (US$ 0,42/milla).

## Qué pedir en cualquier cotización
Tarifa comercial USPS < 1 lb por zona · mínimo mensual · materiales · integración con eBay · fee de devolución · peso/medidas del cartón máster.

---

## 📄 `Amazon/KINA/patente.md`

# KINA — Caso de patente D1063405 (CASE-001)

## Datos del reclamo
| Dato | Valor |
|---|---|
| Complaint ID | **20503982181** |
| Patente | U.S. Design Patent **D1063405S / USD1063405S1** |
| Prioridad / presentación | 23-sep-2022 · concedida 25-feb-2025 |
| Inventora / titular | Cecily J. Braden · CJB Global Imports Inc. |
| Reporter | Hasmeet Singh · vía **Corsearch / Zeal** |
| Efecto | Listings **deactivated** |
| Estado | **ABIERTO** · appeal **despriorizado** (DEC-018), no resuelto ni abandonado |

## ASINs afectados — 12 confirmados
`B0GG739XY6` · `B0GRJRXF2N` · `B0GVQS3VD4` · `B0GTQQ656Z` · `B0G2PNF63V` · `B0GVRQV3S9` · `B0GVXSX3KY` · **`B0GQJLP4TB` (KINA)** · `B0GKCFQJHR` · `B0FRRFSTS7` · `B0G4NGJ4ZT` · `B0G82RJN3S`
Una nota vieja decía 13 → **no inventar el #13**.

## Acceso al appeal (por qué se frenó)
- No aparece opción de written appeal en Seller Central. Seller Support dijo: hay que pasar por **Account Health por llamada**.
- "Call me now" de Account Health falla: *"Internal failure — Sorry, we are unable to process your request."* (desktop y app, con datos de contacto verificados).
- Objetivo si se retoma: Account Health → verificación (la hace Eugenia) → habilitar **written appeal** → presentar dossier **por escrito**. No defender la patente oralmente en inglés.
- Frase de cierre para la llamada: *"Could you please enable the written appeal option? We already have the complete appeal and supporting evidence ready to submit."*

## Estrategia de defensa (decidida)
1. D1063405 protege un **diseño ornamental específico**, no cualquier cepillo curvo.
2. Hay **prior art anterior a sep-2022** con configuraciones curvas/crescent.
3. Pedir **revisión manual producto vs diseño reclamado en contexto de prior art**.
4. **Reconocer la similitud visual general.** NO decir "completely different".
5. La cadena de suministro prueba **buena fe**, NO autorización de patente.
6. NO pedirle a Amazon que declare la patente inválida.
7. Las **cerdas no sirven**: en la patente están en líneas punteadas (no reclamadas).
8. Marco jurídico si hace falta: *Egyptian Goddess / ordinary observer + prior art*, idealmente validado por abogado de patentes de EE.UU. (pendiente).

### Prior art (usar 2–4, no volcar todo)
- **USD936977S1 — "Crescent brush"** · prioridad 8-may-2020 · concedida 30-nov-2021 · Anisa International · citado en el historial de D1063405.
- **US20200015579A1 — "Crescent shaped cosmetic brush"** · prioridad 13-jul-2018 · publicada 16-ene-2020.
- Opcionales: USD790226S1 (2016) · USD859000S1 (2018).

## Lista negra — NO DECIR
"the patent is fake / invalid" · "Cecily copied the design" · "Hasmeet / Corsearch lack authority" · "other sellers sell it so we can too" · "our product is totally different" · "Henan owns / licenses the patent" · "the manufacturer certificate gives patent rights" · "KINA is a registered trademark" · "Maria lives in Miami" · "purchased 8,000" · inventar fechas de fabricación o uso previo a 2022.
**No presentar** una carta de autorización del proveedor chino (evaluada como dañina para la defensa).

## Material preparado (versiones viejas, no finales)
`KINA_Amazon_Patent_Appeal_Partner_Review` (formulación legal vieja, superada) · `KINA_Amazon_Video_Call_Preparation` (sólo ayuda) · script de llamada a Account Health (SOP-003, en pausa).

---

## 📄 `Amazon/KINA/proveedor.md`

# KINA — Proveedor Henan Small Brush

- **Nombre legal:** Henan Small Brush Dizzy Dyeing Trading Co., Ltd. · contacto histórico: Lucy Lu.
- Santi afirma que es la **fábrica** real, aunque el nombre diga "Trading Co.".

## Invoice canónica
| Campo | Valor |
|---|---|
| Invoice No. · fecha | **20260131** · 31-ene-2026 |
| Buyer / Consignee | **Maria Eugenia Vargas** |
| Producto | "Lymphatic brush" |
| Cantidad | **8.500 u** a **US$ 1,67** |
| Mercadería + DDP | 14.195 + 2.531 = **US$ 16.726** (aritmético) |
| Entrega | 2970 NW 75 AVE, Miami, FL 33122 |

Explicación de Miami: *"I live in Argentina. The Miami address is our warehouse and delivery location in the United States. It is not my personal residence."*

## ⚠️ Conflictos abiertos — no resolver inventando
- **C-24 (crítico):** el cálculo da **16.726** pero el "FINAL PAYMENT" figura como **17.626**. No presentar un documento manipulado; Henan corrige sólo si es un error real.
- **C-25:** invoice vieja del **08-ene-2026** a nombre de **Santi Navarria**, "pink brush", **8.000 PCS** a 1,66, total también 16.726. Se conserva hasta poder explicarla.
- **C-27:** material del producto sin declarar en invoice ni caja.

## Certificado de fabricante (pedido, pendiente)
Firmado y sellado por Henan: fabricó y suministró el Lymphatic Brush · compradora Maria Eugenia Vargas · 8.500 u · invoice 20260131 · 31-ene-2026.
Usarlo **sólo** si lo firman y es verdad. Prueba la cadena de suministro; **no da derechos sobre la patente**.

---

## 📄 `Amazon/MT-BALL/CLAUDE.md`

# MT BALL — Magic Meta Ball for Kids (marca MTBALL)

> Ecosistema del producto. Lo estable vive acá; lo que cambia, en `ESTADO.md`.
> Antes de trabajar: leer este archivo + `ESTADO.md`. Abrir el resto sólo si la tarea lo pide.

## Archivos
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Fase actual, checklist de prerrequisitos, cronograma, datos faltantes |
| `listing.md` | Carga paso a paso en Seller Central + título, bullets, descripción, backend |
| `imagenes.md` | Correcciones obligatorias, orden de galería, guion del video |
| `keywords.md` | Núcleo del nicho, señales de temporada, trampas, mercado |
| `ppc.md` | Campañas fase FBM y fase FBA, negativas, reglas de los lunes |
| `operacion.md` | Reglas FBM, pase a FBA, calendario de precios, caja necesaria |
| `riesgos.md` | Riesgos, criterios de corte por fecha, datos faltantes |
| `assets/keywords_Q4_tracker.csv` | 79 keywords en 3 grupos para el Keyword Tracker de Helium 10 |

## Identidad
| Dato | Valor |
|---|---|
| Producto | Bola transformable disco → bola con luces LED, familia "magic meta ball" |
| Marca | **MTBALL** (impresa en la caja; **no** usar "Generic") · marca sin registrar (USPTO pendiente) |
| Socio | **Maxi** (vive en Utah) — falta acuerdo escrito de capital, margen y quién paga Ads |
| Cuenta | **Beauty Michele** (la misma de AVIE) · hoy plan **individual** → hay que pasar a Professional |
| SKUs | `MTB-PARENT` · `MTB-1PK` (1 u) · `MTB-2PK` (pack x2) · prefijo MTB- para separar de AVIE |
| Medidas | bola 16 cm (6,3") · disco 24 cm (9,44") × 4 cm |
| Posicionamiento | **juguete para chicos**; perros = uso secundario (1 bullet + 1 imagen) |
| Competidor principal | B0G5KN8PTN a 14,99 USD |
| Stock | **3.000 u en un 3PL de Miami** (~6 meses ahí) · el 3PL no se paga hasta empezar a vender |

## Economía (estimada — FBA y etiquetas a confirmar)
- **Capital: 10.500 USD** (9.700 fábrica + 800 almacén) → **3,50 USD/u**.

| Canal / precio | Neto/u antes de Ads | ACoS de equilibrio |
|---|---|---|
| FBM 19,99 envío gratis, despacha el 3PL | ~5,5 | ~27 % |
| FBM 19,99 envío gratis, despacha Maxi | ~7,5 | ~37 % |
| FBA 17,99 | 7,79 | 43 % |
| FBA 19,99 | 9,49 | 47 % |
| FBA 21,99 | 11,19 | 51 % |
| FBA 24,99 | 13,74 | 55 % |
| FBA pack x2 29,99 | 6,50 por u | 43 % |

**Lectura:** la restricción es la **velocidad**, no el margen. Recuperar los 10.500 USD ≈ 1.900–2.100 u con Ads incluidos. Más unidades a 19,99–21,99 > menos unidades a 24,99–29,99.

## Objetivo y decisiones
| # | Decisión | Estado |
|---|---|---|
| 1 | Vender en Beauty Michele | ✅ Santi |
| 2 | Arrancar **FBM a 19,99 con envío gratis** para validar y juntar reviews | ✅ Santi (Claude recomendaba FBA directo) |
| 3 | Pasar a **FBA desde el 1-nov** | Propuesto |
| 4 | Kids-first; perros secundario | Propuesto |
| 5 | Variación 1 u + pack x2 | Propuesto |
| 6 | **Objetivo Q4: 3.000 u** (Santi) · escenario base estimado: **1.800–2.100 u** (Claude) | Discrepancia abierta |

## Reglas propias de MT BALL
- Marcas ajenas (phlat ball, sky sphere, transformo, morphofly, curiovas, magicmeta): **nunca** en título ni backend; sí como target de PPC.
- Nunca decir "Safe for Pets to Chew" ni "levitate": es falso (plástico duro + LED + pila).
- "Anti gravity flying ball" es **otro producto** (orbe con hélice): no va en título ni exact.
- Es un **juguete infantil con pilas en la misma cuenta que AVIE**: compliance primero. Sin CPC + tests no se publica stock.
- FBM: siempre etiqueta con **Buy Shipping**, nunca mostrar más de 300 u.

---

## 📄 `Amazon/MT-BALL/ESTADO.md`

# MT BALL — ESTADO

**Actualizado:** 2026-10-06 (migración) · **Último trabajo real:** 2026-09-29 · **Fase:** 0 — prerrequisitos

## ⚠️ Primero: confirmar (el cronograma ya está corriendo)
Según el plan, al 06-oct ya debería estar: listing cargado (1–3 oct), imágenes corregidas + video (1–7 oct) y FBM activo con Ads (~6–8 oct). No hay registro de nada de eso. Confirmar:
1. ¿Beauty Michele ya está en plan **Professional**?
2. ¿Hay **2 UPC GS1**?
3. ¿La fábrica mandó **tests ASTM F963 + CPSIA**? ¿Qué **tipo de pila** lleva?
4. ¿El 3PL acepta despachar FBM con acuerdo escrito, o salen **300 u a Maxi**? ¿Cuánto se le debe al 3PL?
5. ¿Hay acuerdo con Maxi (capital, margen, Ads)?
6. ¿Se pidió la marca en USPTO?

## Checklist de prerrequisitos (antes de publicar)
- [ ] Plan Professional (39,99 USD/mes)
- [ ] 2 UPC GS1 (unidad y pack)
- [ ] Tests ASTM F963 + CPSIA + CPC emitido por el importador
- [ ] Tipo de pila (si es botón LR41/AG3 → Reese's Law: tornillo + advertencias)
- [ ] Fotos de las advertencias de la caja
- [ ] Medidas y peso reales de la caja
- [ ] Marca MTBALL en USPTO (~350 USD) → Brand Registry
- [ ] Acuerdo escrito con el 3PL, o 300 u a Maxi
- [ ] Acuerdo con Maxi

## Cronograma
| Fecha | Hito | Dueño |
|---|---|---|
| 29-sep → 3-oct | Prerrequisitos | Santi + Maxi |
| 1–3 oct | Listing cargado con stock 0 + CPC y tests subidos | Santi |
| 1–7 oct | Imágenes corregidas + video | Diseñador |
| ~6–8 oct | FBM activo (300 u) + Ads fase FBM | Santi (con OK) |
| 13 y 20 oct | Revisión semanal | Santi + Claude |
| 20–25 oct | Envío FBA ola 1 (1.000 u) | Santi |
| 1-nov | FBA activo · FBM a 0 · campaña regalos · Vine si hay Brand Registry | Santi |
| **10-nov** | **Tope: stock recibido en FBA** | — |
| 27-nov → 1-dic | Black Friday / Cyber Monday | — |
| 2–18 dic | Pico: precio y budget máximos | — |
| ~20-dic | Último envío para Navidad → bajar precio | — |

## Lectura de director
- **El cuello de botella no es el listing: es la caja y el 3PL.** El 3PL no se paga hasta vender, y para vender hay que sacar mercadería del 3PL. Si el 3PL retiene stock, el plan entero se cae. Resolver esto antes que cualquier copy.
- **FBM en octubre sirve para indexar y validar, no para facturar:** se esperan ~3–8 reviews al 1-nov. El año se juega en que el stock esté en **FBA antes del 10-nov**. Cada día de atraso en la ola 1 resta días del pico de diciembre.
- **Riesgo cruzado:** un problema de compliance con un juguete infantil puede afectar a toda Beauty Michele, incluida AVIE. Una cuenta propia o la LLC para MT Ball merece evaluarse.
- 3.000 u en Q4 es el objetivo de Santi; la estimación base es 1.800–2.100. Con eso se recupera el capital; la ganancia está en el remanente de primavera.

## Próximo paso
- **Santi:** checklist de prerrequisitos.
- **Claude, al recibir los datos:** calendario de caja semana a semana y ajuste de precios con el costo real de envío.

## Historial
- 2026-10-06 · Migrado a `AMAZON/MT-BALL/` desde `02 Negocios/Amazon-FBA/Productos/MT-BALL/`.
- 2026-09-29 · MASTER v1: listing, plan Q4, keywords (Cerebro B0G5KN8PTN), PPC, cronograma.

---

## 📄 `Amazon/MT-BALL/imagenes.md`

# MT BALL — Imágenes y video

### 5. Imágenes y video
#### Correcciones obligatorias antes de subir
| Imagen | Problema | Arreglo |
|---|---|---|
| Main | Flechas azules y remolino = gráfico en la imagen principal (puede ser rechazada) | Bola + disco (+ caja opcional) sobre blanco puro, sin flechas |
| Dimensiones | Ícono "Safe for Pets to Chew": falso (plástico duro + LED + pila) → riesgo de reclamo y responsabilidad | Reemplazar por "Built-in LED Lights" |
| Glow. Levitate. Play. | No levita → devoluciones "no es como se describe" | "Glow. Pop. Play." |
| Pets & Families | "Starts bouncing automatically": confirmar con una muestra | Si no rebota sola: "pops up when you press it" |
| Render de 7 pétalos con logo MT | El producto real tiene 6 pétalos y otra textura | No usar |
| Set 1–7 | Versiones comprimidas | Subir sólo el set en alta resolución |

#### Orden de la galería (MTB-1PK)
1. Main limpia (bola + disco)
2. Transformación disco → bola (Interactive Fun, corregida)
3. Glowing Catch (luces día/noche)
4. Multiple Ways to Play
5. Product Dimensions (corregida)
6. Great Gift for Kids (Navidad — cambiarla en enero)
7. Glow. Pop. Play.
8. **Video**

MTB-2PK: main con 2 bolas + 2 cajas; imagen nueva "One for each sibling"; el resto igual.

#### Video (20–30 s, producto REAL, sin gráficos exagerados)
Tirar el disco → se abre en el aire → toca el piso como bola → presionar botón → luces de noche → nene/familia jugando → perro persiguiendo (supervisado) → caja de regalo. Es el mayor multiplicador de conversión en este nicho.

---

## 📄 `Amazon/MT-BALL/keywords.md`

# MT BALL — Keywords

### 6. Keywords (fuente: Cerebro B0G5KN8PTN, 29-sep)
- Núcleo real del nicho: **304 keywords, ~50.800 búsquedas/mes**, bid mediano USD 0,64, CPR 8 (barato de rankear).
- Tracker completo: `assets/keywords_Q4_tracker.csv` (79 keywords en 3 grupos) → cargar en H10 Keyword Tracker, revisar los lunes.

**Top núcleo para rankear (exact):** magic meta ball for kids · metaball · meta ball · pop up ball · pop up ball toy · magic ball toy · light up magic ball · ufo magic ball · bouncing magic metaball · flying saucer ball with lights.

**Señales de temporada (PPC desde nov):** christmas toys 2026 (+269%) · stocking staffers for kids (+102%) · light up outdoor toys (+43%) · best gifts for active kids (+40%) · gifts for kids · kids gifts 6-8.

**Trampas (no usar en título/exact):** anti gravity flying ball (otro producto, la bola con hélice) · magic 8 ball · pokemon/bakugan · toddler · "under 15 dollars".

#### Mercado (HECHO — Cerebro B0G5KN8PTN, 29-sep-2026)
- 2.603 keywords, 1,1M búsquedas/mes totales → **engañoso**: la mayoría es tráfico ajeno (toddler toys 121k, frisbee, bouncy balls, magic 8 ball, pokemon ball).
- **Núcleo real meta ball** (304 kws, filtrando marcas y productos distintos): **~50.800 búsquedas/mes**. Bid mediano **$0,64**. CPR mediano **8** (≈8 ventas en 8 días para rankear cada kw → nicho barato de posicionar).
- El competidor está top-10 orgánico en 130 de esas 304 kws (~19.500 búsq/mes).
- Keywords madre del nicho: pop up ball 1.763 · sky sphere ball 1.658 · magic ball 1.171 · flying ball toy 919 · magic ball toy 691 · pop up balls 624 · pop ball 613 · magic flying ball 549 · magic meta ball for kids 531 (+45%) · flat ball 526 · pop up balls for kids 524 · pop up ball toy 480 · bouncing magic metaball 393 (+60%) · light up magic ball 384 (+40%) · metaball 372 · ufo magic ball 364 (+64%).
- Raíces con más volumen dentro del núcleo: ball, flying, magic, pop/pop up, metaball, saucer, bouncing, kids, light/led, transforming, ufo.

#### Trampas de lectura (INFERENCIA)
- **"anti gravity flying ball"** (13.230, +923%), anti-gravity ball (2.373, +1.164%), curiovas, "that returns", induction, hover → es **otro producto** (orbe/boomerang con hélice). El competidor rankea 19–61 ahí: tráfico que no convierte. **No va en título ni en PPC exacto.** Como mucho, un test auto/broad chico para medir.
- **Perros:** 51 kws, 13.838 búsq/mes, pero el competidor rankea mediana **#192** → no gana ahí. Hundirse en "dog" diluye relevancia de toys. Perros = uso secundario (1 bullet + 1 imagen), no posicionamiento.
- Marcas ajenas (phlat ball, sky sphere, transformo, morphofly, curiovas, magicmeta) → **no** en título ni backend (riesgo de supresión). Sí como targeting PPC.

---

## 📄 `Amazon/MT-BALL/listing.md`

# MT BALL — Listing (carga en Seller Central + copy)

> Copy en inglés US, listo para pegar. Versión MASTER v1 del 29-sep. Santi carga; Claude acompaña.

### 3. Creación del listing en Seller Central — paso a paso
> Santi carga. Claude acompaña campo por campo si hace falta.

**Paso 1 — Crear**
Catálogo → Agregar productos → "Estoy agregando un producto que no se vende en Amazon".

**Paso 2 — Tipo de producto / categoría**
Usar la misma ruta de categorías que el competidor B0G5KN8PTN (copiarla de su página, en la línea de categorías arriba del título). Esperado: Toys & Games › Sports & Outdoor Play.

**Paso 3 — Variaciones**
- "¿Tiene variaciones?" → **Sí** · Tema: **Number of Items** (si no aparece para ese tipo de producto, usar "Size" con valores "1 Pack" / "2 Pack").
- Padre: SKU `MTB-PARENT` (sin precio ni stock).

| SKU | Number of Items | UPC | Precio | Stock inicial |
|---|---|---|---|---|
| MTB-1PK | 1 | UPC #1 | 19,99 | 0 hasta tener OK del 3PL → luego 300 |
| MTB-2PK | 2 | UPC #2 | 29,99 | 0 hasta armar los packs |

**Paso 4 — Identidad**
- Marca: **MTBALL** (NO "Generic": la caja tiene marca).
- Fabricante: MTBALL.
- Número de pieza del fabricante: MTB-1PK / MTB-2PK.

**Paso 5 — Oferta (fase FBM)**
- Condición: Nuevo.
- Canal de envío: **"Enviaré este artículo yo mismo"**.
- Tiempo de preparación: **1 día**.
- Plantilla de envío: crear "MTB Free Shipping" → Estándar, **envío gratis** a EE.UU. contiguo. Sin envío urgente/ultrarrápido al principio.
- Stock máximo visible: **300**.

**Paso 6 — Atributos de seguridad y cumplimiento** (completar con el test de laboratorio)
- Edad mínima recomendada del fabricante: _según test_ (probablemente 6 años).
- Advertencia de seguridad (CPSIA): _según test_ (p. ej. choking hazard / small parts si aplica).
- ¿Necesita pilas? Sí · ¿Incluye pilas? Sí · Tipo/cantidad: _según ficha del proveedor_.
- Material: _según ficha del proveedor_ (DATO FALTANTE).
- Color: Black / Yellow.
- Dimensiones y peso del artículo y del paquete: medidos (Paso 2 del checklist).

**Paso 7 — Cumplimiento después de guardar**
Rendimiento → **Administrar tu cumplimiento** → subir **CPC + reportes de test**. Hasta que esté aprobado, el ASIN puede quedar inactivo; por eso se carga ya.

**Paso 8 — Copy, imágenes y video** → más abajo y `imagenes.md`.

### 4. Copy (copiar y pegar — inglés US)

#### Título MTB-1PK (≈150 car., ninguna palabra repetida más de 2 veces)
```
MTBALL Magic Meta Ball for Kids - Pop Up Flying Saucer Ball with LED Lights, Transforming Light Up Toy for Indoor & Outdoor Play, Christmas Gift for Boys & Girls
```
Los primeros ~75 caracteres ("MTBALL Magic Meta Ball for Kids - Pop Up Flying Saucer Ball with LED Lights") llevan las keywords principales (se ven en mobile).

#### Título MTB-2PK
```
MTBALL Magic Meta Ball for Kids 2 Pack - Pop Up Flying Saucer Balls with LED Lights, Transforming Light Up Toys for Indoor & Outdoor Play, Christmas Gift for Siblings
```

#### Bullets MTB-1PK
```
MAGIC FLAT-TO-BALL TRANSFORMATION – Throw it like a flying saucer, then watch it pop back into a ball on impact. Press the center button to flatten it again and repeat the surprise over and over.
BUILT-IN LED LIGHTS FOR DAY & NIGHT PLAY – Colorful lights make every toss, catch and kick easy to see in the backyard, at the park or in the living room after dark.
MANY WAYS TO PLAY – Toss & catch, kick & chase, mini-hoop shots or backyard games. Keeps kids active and off screens, and gets the whole family playing together.
SIZED FOR SMALL HANDS – 6.3 in (16 cm) as a ball, 9.4 in (24 cm) as a flat disc. Lightweight and durable for everyday indoor and outdoor play. Also fun for supervised fetch with dogs (not a chew toy).
READY-TO-GIFT BOX – Arrives in a bold gift box, perfect for Christmas, birthdays, Easter baskets and stocking stuffers for boys and girls.
```

#### Bullets MTB-2PK (los 4 primeros iguales; el 5.º cambia)
```
2-PACK FOR SIBLINGS & FRIENDS – One for each kid means no fighting over who plays first. Two gift boxes, ready for Christmas, birthdays and stocking stuffers.
```

#### Descripción del producto (hasta tener A+)
```
Meet MTBALL, the magic meta ball that turns every throw into a surprise. Toss it flat like a flying saucer and it pops back into a ball when it lands. Press the center button to flatten it again and keep the fun going.

Built-in LED lights make it easy to follow at night, so playtime does not have to end when the sun goes down. Kids can toss and catch it, kick it, shoot mini hoops or invent their own backyard games, and the whole family can join in.

At 6.3 inches as a ball and 9.4 inches as a disc, it is sized for small hands and made for everyday indoor and outdoor play. It comes in a bold gift box, ready for Christmas, birthdays and stocking stuffers.

Adult supervision recommended. Not a chew toy.
```

#### Backend / términos de búsqueda (220 bytes — no repite palabras del título ni usa marcas ajenas)
```
metaball magicmeta ufo deformation throwing flat popping bouncing bouncy disc frisbee stocking stuffer birthday party family game backyard beach park camping glow night fetch dog cool gadget teens adults 5 6 7 8 9 10 year old
```
⚠️ **CONTRADICCIÓN (detectada 2026-10-06):** el backend incluye `magicmeta`, que el análisis del 29-sep lista como **marca ajena**. Decidir antes de publicar: si es marca, quitarla del backend (riesgo de supresión) y usarla sólo como target de PPC.

**Prohibido en título y backend:** phlat ball, sky sphere, transformo, morphofly, curiovas (marcas ajenas → riesgo de supresión). Sí se pueden usar como targets en PPC.

---

## 📄 `Amazon/MT-BALL/operacion.md`

# MT BALL — Operación: FBM → FBA, precios y caja

### 7. Operación FBM (octubre) — reglas que protegen la cuenta de AVIE
1. Quién despacha: **3PL con acuerdo escrito** o **Maxi con 300 u** (más barato: ~USD 2/u menos).
2. Preparación de 1 día · **siempre comprar la etiqueta con Buy Shipping** (protege ante A-to-z y asegura tracking válido).
3. Métricas: envío tardío <4% · tracking válido >95% · cancelación <2,5%. Si alguna se acerca al límite → **pausar la oferta FBM**.
4. No mostrar más stock del que se puede despachar a tiempo (tope 300).
5. Inserto neutro en la caja: sin incentivos ni pedido de review positiva.
6. "Request a Review" en cada pedido entre 5 y 30 días después de la entrega.

**Expectativa realista (corrige la hipótesis "FBM me llena de reviews"):** ~3–8 pedidos/día en oct → ~100–200 pedidos → **~3–8 reviews al 1-nov**. El motor real de reviews es Vine (requiere Brand Registry + oferta FBA, verificar).

### 8. Transición a FBA (sin perder ventas)
1. ~20–25 oct: crear envío FBA **ola 1 = 1.000 u** desde el 3PL (carrier asociado de Amazon; el costo se descuenta del saldo).
2. Para no quedarse sin oferta mientras la mercadería viaja: crear un **segundo SKU FBA** en el mismo ASIN (`MTB-1PK-FBA`) y mantener el SKU FBM activo hasta que FBA reciba el stock. Después, FBM a cantidad 0.
3. Stock recibido en FBA: **antes del 10-nov**.
4. Ola 2 (1.000 u) a inicios de nov, pagada con ventas · ola 3 a fin de nov según velocidad.
5. Con FBA + Brand Registry: inscribir **Vine** (30 u) el mismo día.

### 9. Calendario de precios
| Ventana | Canal | Unidad | Pack x2 |
|---|---|---|---|
| Oct (lanzamiento) | FBM | 19,99 envío gratis | 29,99 (cuando haya packs) |
| 1–26 nov | FBA | 19,99 + cupón 10% las 2 primeras semanas | 29,99 |
| 27-nov → 1-dic (BF/CM) | FBA | 17,99 (oferta) | 26,99 |
| 2–18 dic | FBA | 21,99–24,99 (sólo si vende ≥30 u/día) | 29,99 |
| 19–31 dic | FBA | 17,99 para liquidar | — |
Nota: Amazon calcula el precio tachado con lo que se pagó en los últimos 90 días; no se puede inventar un "antes".

### 13. Caja mínima para arrancar (estimación a confirmar)
| Concepto | USD | Se paga con |
|---|---|---|
| Plan Professional | 40/mes | Tarjeta |
| 2 UPC GS1 | ~60 | Tarjeta |
| CPC + test | 0 si la fábrica tiene test válido · 500–1.500 si no | Tarjeta |
| Marca USPTO (1 clase) | ~350 | Tarjeta |
| 3PL: despacho FBM / salida ola 1 (+ deuda si hay) | ~300–600 + deuda | Efectivo ← cuello de botella |
| Envío a FBA + placement | ~500–700 | Saldo de la cuenta Amazon |
| Vine | ~200 (verificar promos) | Saldo / tarjeta |
| Ads octubre | ~1.000 | Saldo de ventas / tarjeta |
| **Efectivo real necesario** | **~800–2.500** | |
- Amazon libera la plata ~7 días después de la entrega + ciclo de 14 días → la primera plata de ventas llega ~2–3 semanas después de la primera venta.
- Usar el saldo de AVIE sólo con acuerdo explícito (AVIE es 50/50) y devolverlo con las primeras ventas de MT Ball.

---

## 📄 `Amazon/MT-BALL/ppc.md`

# MT BALL — PPC

> Propuesta. NO ejecutar sin OK puntual de Santi.

### 10. Ads
#### Fase FBM (oct) — budget total USD 30–40/día
| Campaña | Tipo | Targets | Bid | Budget/día |
|---|---|---|---|---|
| MTB-SP-EXACT-RANK | Exact | Top núcleo (`keywords.md`) | tope ~0,70 | 20–25 |
| MTB-SP-AUTO-DISC | Auto | Close/loose match | 0,45 | 10–15 |

#### Fase FBA (desde nov)
| Campaña | Tipo | Targets | Bid inicial | Budget/día nov → dic |
|---|---|---|---|---|
| MTB-SP-EXACT-RANK | Exact | Top núcleo | sugerido + Top of Search +50% | 30 → 80 |
| MTB-SP-AUTO-DISC | Auto | — | 0,60 | 20 → 40 |
| MTB-SP-PHRASE-CORE | Phrase | magic ball · pop up ball · metaball · flying saucer ball · transforming ball | 0,55 | 15 → 40 |
| MTB-SP-ASIN-COMP | Product | B0G5KN8PTN + ASINs de pág. 1 con peor rating o precio mayor | 0,50 | 15 → 30 |
| MTB-SP-GIFT-Q4 | Phrase/exact | Señales de temporada + tracker grupo B/C | 1,00 | 20 → 50 |
| MTB-SBV (requiere Brand Registry) | Video | Núcleo + regalo | — | 20 → 40 |

**Negativas desde el día 0:** magic 8 ball · eight ball · 8 ball · pokemon · bakugan · magic mike · bouncy balls bulk · toddler · birth ball · under 15.
**Anti-gravity:** sólo test aislado USD 5/día; sin ventas en 14 días → negativa.

**Reglas semanales (lunes, cuando Santi pide la revisión)**
1. 20+ clics y 0 ventas → negativa exacta.
2. Keyword núcleo con ACoS < equilibrio → +15% bid.
3. Keyword núcleo en top-10 orgánico → −15% bid.
4. Search term que convierte en Auto → pasarlo a Exact y negativo en Auto.
5. Keyword de temporada con volumen +50% en la semana → abrir campaña o +20% budget.

**Rampa de inversión (estimación):** oct ~USD 1.000 · nov ~USD 3.700 · 1–18 dic ~USD 4.500 → **~USD 9.000–9.500**, TACoS objetivo 20–25%.

---

## 📄 `Amazon/MT-BALL/riesgos.md`

# MT BALL — Riesgos y criterios de corte

### 14. Riesgos principales
1. **Compliance:** sin CPC + tests, el ASIN se bloquea; un problema con un juguete infantil puede afectar a toda la cuenta (incluida AVIE).
2. **3PL con deuda:** puede retener la mercadería → envíos tardíos en FBM.
3. **FBM en Q4:** posible supresión de la oferta nov–ene en Toys (verificar requisitos de la cuenta).
4. **Foco:** con Reflex y el seguro activos, MT Ball es el 3.er frente → que Maxi lleve la operación diaria.
5. **Stock remanente en enero:** no es stock muerto (segundo pico en primavera/verano) pero inmoviliza caja.
6. **`magicmeta` en el backend** pese a figurar como marca ajena (ver `listing.md`). Decidir antes de publicar.

### 12. Indicadores y criterios de corte
| Fecha | Señal | Decisión |
|---|---|---|
| 20-oct | CVR < 6% con 100+ clics en exact núcleo (FBM) | El problema es precio/imagen, no la puja → corregir antes de gastar más |
| 31-oct | Alguna métrica FBM cerca del límite | Pausar FBM y acelerar FBA |
| 15-nov | < 5 keywords núcleo en top-20 | Objetivo baja a ~2.000; guardar stock para primavera |
| 5-dic | < 30 u/día | No subir a 24,99; quedarse en 19,99–21,99 |
| 20-dic | Remanente > 1.200 u | Plan primavera (Easter + outdoor) y revisar costo de almacenaje en FBA |

### 15. DATO FALTANTE
Deuda y tarifas del 3PL · tests de fábrica · tipo de pila · material · medidas/peso reales · aporte de Maxi · estado de la marca · si la cuenta cumple las holiday guidelines de Toys para FBM.

---

## 📄 `Amazon/MT-BALL/assets/keywords_Q4_tracker.csv`

```csv
keyword,tier,vol_sep26,tendencia_pct,bid_sug,rank_org_competidor,uso
magic meta ball for kids,A-core,531,45,0.54,27,Rankear oct-nov; convierte en dic
metaball,A-core,372,8,0.54,8,Rankear oct-nov; convierte en dic
meta ball,A-core,338,63,0.57,8,Rankear oct-nov; convierte en dic
magicmeta ball,A-core,318,57,,3,Rankear oct-nov; convierte en dic
pop up ball,A-core,1763,-5,0.81,12,Rankear oct-nov; convierte en dic
pop up ball toy,A-core,480,-31,0.42,7,Rankear oct-nov; convierte en dic
pop up balls,A-core,624,-7,0.94,13,Rankear oct-nov; convierte en dic
pop up balls for kids,A-core,524,-27,0.55,11,Rankear oct-nov; convierte en dic
pop ball,A-core,613,-3,0.84,14,Rankear oct-nov; convierte en dic
pop balls,A-core,563,15,0.57,28,Rankear oct-nov; convierte en dic
magic ball,A-core,1171,-21,0.58,34,Rankear oct-nov; convierte en dic
magic ball toy,A-core,691,-46,0.64,34,Rankear oct-nov; convierte en dic
light up magic ball,A-core,384,40,,18,Rankear oct-nov; convierte en dic
led magic ball,A-core,389,1,0.64,37,Rankear oct-nov; convierte en dic
ufo magic ball,A-core,364,64,0.48,13,Rankear oct-nov; convierte en dic
magic ufo ball,A-core,361,-12,0.49,7,Rankear oct-nov; convierte en dic
bouncing magic metaball,A-core,393,60,0.53,16,Rankear oct-nov; convierte en dic
magic metaball bounce,A-core,362,3,0.61,6,Rankear oct-nov; convierte en dic
metaball pop up,A-core,381,18,,2,Rankear oct-nov; convierte en dic
magic ball popup,A-core,394,35,0.45,12,Rankear oct-nov; convierte en dic
magic ball flattens and pops up,A-core,389,-1,0.67,24,Rankear oct-nov; convierte en dic
transforming ball,A-core,347,16,,8,Rankear oct-nov; convierte en dic
transforming ball toy,A-core,356,6,,19,Rankear oct-nov; convierte en dic
magic transforming ball,A-core,317,24,,18,Rankear oct-nov; convierte en dic
flat ball,A-core,526,-14,0.7,1,Rankear oct-nov; convierte en dic
flying saucer ball with lights,A-core,405,14,,9,Rankear oct-nov; convierte en dic
flying saucer ball for kids,A-core,333,34,,26,Rankear oct-nov; convierte en dic
magic saucer ball,A-core,348,-10,,18,Rankear oct-nov; convierte en dic
magic flying ball,A-core,549,1,1.04,19,Rankear oct-nov; convierte en dic
flying ball toy,A-core,919,7,0.62,35,Rankear oct-nov; convierte en dic
pop up light up balls,A-core,317,6,,20,Rankear oct-nov; convierte en dic
ball popping toy,A-core,469,-14,0.85,25,Rankear oct-nov; convierte en dic
christmas toys 2026,B-regalo (ya en datos),997,269,0.55,42,Estacional con dato actual
stocking staffers for kids,B-regalo (ya en datos),356,102,1.04,209,Estacional con dato actual
stocking stuffers for kidd,B-regalo (ya en datos),181,23,,206,Estacional con dato actual
gifts for kids,B-regalo (ya en datos),2362,12,1.13,223,Estacional con dato actual
kids gifts 6-8,B-regalo (ya en datos),2048,24,1.17,179,Estacional con dato actual
gifts for kids 6-10,B-regalo (ya en datos),287,-12,,77,Estacional con dato actual
unique gifts for 5 year old boy,B-regalo (ya en datos),329,2,,117,Estacional con dato actual
popular toys for 7 year old boys,B-regalo (ya en datos),366,-14,,263,Estacional con dato actual
boytoys for ages 8-13,B-regalo (ya en datos),224,-17,,26,Estacional con dato actual
best gifts for active kids,B-regalo (ya en datos),132,40,1.05,98,Estacional con dato actual
gifts for active kids,B-regalo (ya en datos),114,9,1.17,86,Estacional con dato actual
outdoor toys for teenagers,B-regalo (ya en datos),388,27,1.2,101,Estacional con dato actual
magical gifts,B-regalo (ya en datos),181,2,,37,Estacional con dato actual
magic gifts for kids,B-regalo (ya en datos),93,10,,124,Estacional con dato actual
surprise balls for boys,B-regalo (ya en datos),65,-17,0.68,34,Estacional con dato actual
gifts for toys for tots,B-regalo (ya en datos),229,26,,-,Estacional con dato actual
light up toys for kids ages 4-8,B-regalo (ya en datos),141,-6,0.99,189,Estacional con dato actual
balls for kids ages 4-8,B-regalo (ya en datos),608,-36,0.9,26,Estacional con dato actual
balls for kids ages 8-12,B-regalo (ya en datos),198,3,0.89,74,Estacional con dato actual
unique outdoor toys,B-regalo (ya en datos),373,25,,6,Estacional con dato actual
light up outdoor toys,B-regalo (ya en datos),483,43,0.76,144,Estacional con dato actual
glow in the dark toys,B-regalo (ya en datos),3136,-4,0.81,205,Estacional con dato actual
light up balls for kids,B-regalo (ya en datos),997,16,0.81,63,Estacional con dato actual
stocking stuffers for kids,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
stocking stuffers for boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
stocking stuffers for girls,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
christmas gifts for kids,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
christmas gifts for boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
christmas gifts for girls,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
gifts for 6 year old boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
gifts for 7 year old boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
gifts for 8 year old boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
gifts for 9 year old boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
gifts for 10 year old boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
gifts for 8 year old girls,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
toys for 8 year old boys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
outdoor toys for kids ages 8-12,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
cool toys for kids,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
trending toys 2026,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
viral toys 2026,B-regalo (ya en datos),624,-,0.59,193,Estacional con dato actual
tiktok toys,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
stocking stuffers for teens,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
white elephant gifts for kids,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
christmas gifts for kids under 25,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
sibling gifts,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
gifts for grandkids,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
kids gifts under 25,C-navidad (sin dato),,,,,Medir en Magnet/SQP: Cerebro de septiembre no la muestra
```

---

## 📄 `Amazon/REFLEX/CLAUDE.md`

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

---

## 📄 `Amazon/REFLEX/ESTADO.md`

# REFLEX — ESTADO

**Actualizado:** 2026-10-06 (migración) · **Último dato:** series al 16-sep, listings al 19-sep, Account Health al 28-sep · **Modo:** LIQUIDACIÓN

## ⚠️ Primero: confirmar (todo lo posterior al 28-sep es UNKNOWN)
1. **Stock FBA por ASIN hoy** (disponible / reservado / en tránsito). Conflicto: 3.400 u el 15-sep vs **3.550 u** citadas el 28-sep.
2. **Precio vigente de cada ASIN** y ventas de los últimos 30 días por ASIN.
3. ¿Qué pasó con el **seguro** (venció el 01-oct)? ¿Amazon mandó algún aviso nuevo?
4. ¿Se avanzó con el **flag "Children's toys"** de QW5 (plazo 06-dic)? ¿Se pidieron tests?
5. ¿La agencia sigue? ¿Se ejecutó algo del takeover del 14-sep?

## La cuenta de la liquidación (estimación — validar con el dato 1)
| | |
|---|---|
| Stock 15-sep | 3.400 u (1.700/ASIN) |
| Velocidad medida | ~17–21 u/día total (992 pedidos FBA en 60 d al 28-sep · 643 u en 30 d al 15-sep) |
| Stock estimado hoy | **~3.000 u ≈ US$ 17.800 de capital** a 5,94 |
| Días al 31-dic | 86 |
| **Ritmo necesario para salir en diciembre** | **~35 u/día ≈ 2× el actual** |
| Rotación por ASIN (27-ago→14-sep) | QW5 8,4 u/día → 203 días · **R46 1,8 u/día → ~950 días** |

**Q4 puede dar ese salto** (Tendry vendió 7.303 u en un mes de temporada a 29,99 vs 723 en agosto), pero sólo si QW5 sigue publicado y R46 deja de ser stock muerto.

## Prioridades (impacto × probabilidad × velocidad × reversibilidad)
1. **Salvar QW5 del flag "Children's toys" antes del 06-dic** → `compliance.md`. QW5 es el ASIN que vende (≈2/3 de las unidades, US$ 10.834 de GMS en riesgo) y el plazo cae en pleno pico. La caja dice **AGES 3+**: la vía honesta es **laboratorio (ASTM F963-23 + CPSIA + CPC)**, no reclasificar a 14+.
2. **Resolver el seguro** (venció el 01-oct). Detalle en el paquete de la cuenta KINAVARGAS. Una suspensión en noviembre congela las ~3.000 u.
3. **Plan de salida para R46** (1.700 u, ~950 días al ritmo actual = el verdadero stock muerto, ≈ US$ 10.000).
4. **Escalera de precio sólo si no frena la salida:** 22,99 (20-oct) → 24,99 (10-nov) → 27,99 condicional, con regla de corte: si las u/día caen >25 % o quedan por debajo del ritmo necesario, se vuelve al escalón anterior.
5. **Cortar desperdicio de PPC** (≈ US$ 2.100/mes): recorte −70 % de las dos `SP-(LooseMatch)` + lista DO NOT BID de product targeting. Sin tocar estructura ni automáticas sanas.

## Qué sigue valiendo y qué cambia con el objetivo de salir
| Decisión de septiembre | Con objetivo LIQUIDAR |
|---|---|
| Escalera de precio 22,99 → 27,99 | **Vale, condicionada a velocidad** (la salida manda sobre el margen) |
| No romper con la agencia ahora | Vale — cambiar de manos a semanas del pico es riesgo |
| No pausar automáticas / no reestructurar | Vale |
| 3 core ranking keywords + ficha de ranking investment + blindaje (−375/mes) | **Pierde sentido** salvo que se pague dentro de Q4: no se invierte en ranking que se abandona en enero |
| Fusionar R46 + QW5 como variación (antes "baja reversibilidad") | **Reabrir:** la irreversibilidad pesa poco si la cuenta se abandona en diciembre, y R46 heredaría la página de QW5 (rating 4,1, #1 en `reflex challenge game`). Verificar riesgo antes |
| Main image CONCEPTO A, A+ Basic, backend nuevo | Sólo si se ejecuta antes de noviembre; después no se amortiza |
| Título de QW5 (A-18) | **Obsoleto:** Amazon dejó ambos títulos en 32 car. el 4–14 sep |

## Decisiones abiertas (de Santi)
- Vía de compliance de QW5 (y R46, que tiene la misma caja): laboratorio sí/no y quién es el importador de registro (a su nombre va el CPC).
- Qué hacer con el remanente que quede el 1-ene: liquidación de Amazon, removal + venta fuera de Amazon, o seguir en 2027 (contradice la salida).
- Fusión R46 + QW5.
- Autorizar la escalera de precio (D-25) y el recorte de LooseMatch (D-13).

## No hacer
Ejecutar en Seller Central o Ads sin OK puntual · pausar automáticas · reestructurar campañas · usar el botón de IA de Amazon para "arreglar" el listing · declarar al seguro algo distinto de lo que dice la caja.

## Historial
- 2026-10-06 · Migrado a `AMAZON/REFLEX/` desde el vault PROYECTOS 100K (índice 17-sep + historia 19-sep) y el expediente de seguro (28-sep). Caja revisada: AGES 3+, batería interna.
- 2026-09-28 · Flag "Children's toys" en QW5 (aviso del 22-sep, plazo 06-dic). Objetivo confirmado: liquidar y salir.
- 2026-09-19 · Títulos de ambos ASINs reducidos a 32 car. sin color. QW5 lidera (BSR #153, 4,1★) · R46 cae (#288, 3,8★).
- 2026-09-15 · Stock confirmado 1.700/SKU. Cambio a modo liquidación. Inversión de ASINs (QW5 > R46).
- 2026-09-14 · Takeover de Ads por Santi (sin registro de ejecución).
- 2026-09-07/08 · Auditoría de agencia, decisiones DL-1…D-24.

---

## 📄 `Amazon/REFLEX/competencia.md`

# REFLEX — Competencia

## Líder — Tendry `B0DLN5C44D`

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

## Otros competidores

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

## Nuestras referencias propias

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

## 📄 `Amazon/REFLEX/compliance.md`

# REFLEX — Compliance: flag "Children's toys", caja y seguro

## El flag (captura Account Health 28-sep)
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

## La caja física (foto en `assets/caja_retail.jpeg`, revisada 06-oct)
**"AGES 3+"** · **"FAMILY GAMES"** · **"INTERNAL BATTERY"** · **"TYPE-C CHARGE"** · marca HM · Made in China.

**Consecuencia (HECHO + regla del expediente):** la clasificación sigue a la caja. Si la caja dice 3+, es **producto infantil para la CPSC**.
- La "Vía A" (sostener ante Amazon que es *training equipment 14+*) **no es viable con esta caja**: contradice el empaque y lo que se declara al seguro.
- Vía que queda: **laboratorio ASTM F963-23 + CPSIA → CPC emitido por el importador de registro**.
- La batería es interna y recargable por USB-C → refuerza la exposición (tipo de celda sigue UNKNOWN; probablemente litio).
- R46 tiene la misma caja → es probable que reciba el mismo flag.

## Palanca económica
- Costo de tests: estimado US$ 500–1.500 (a cotizar) · plazo típico 2–4 semanas.
- Contra: US$ 10.834 de GMS de QW5 + el pico de diciembre + el ASIN que vende 2/3 de las unidades.
- **Fecha límite práctica para pedir el test: mediados de octubre**, para tener el CPC subido con margen antes del 06-dic.

## Seguro (resumen — expediente completo en la carpeta de la cuenta KINAVARGAS)
- Amazon exige CGL + Product Liability US$ 1M/1M. **Deadline 01-oct-2026 (vencido; estado actual UNKNOWN).**
- Named Insured = **Maria Eugenia Vargas** (legal entity de la cuenta).
- Well Insurance: no asegura persona física extranjera; pide LLC US + FEIN.
- VirtualMed (LLC de Santi y Pablo) cumple eso, pero **la cuenta personal de Santi está bloqueada por Sección 3** → mostrar la LLC a Amazon arriesga vincular KINAVARGAS. Camino preferido: póliza corta a nombre de Eugenia vía productor argentino (Allianz/Chubb AR) o surplus lines (Sadler, Veracity, Coyle).
- **Regla:** al seguro se declara lo mismo que dice la caja → **toy / children's product, con batería**.

## Datos faltantes
Importador de registro (a su nombre va el CPC) · tipo de celda de la batería · cotización de laboratorio · estado del seguro después del 01-oct · traspaso `REFLEX_TRASPASO_COMPLIANCE_Q4_2026-09-28` (no está en ninguno de los dos vaults).

---

## 📄 `Amazon/REFLEX/decisiones.md`

# REFLEX — Decisiones, acciones aprobadas e historial

> ⚠️ Escritas ANTES del cambio de objetivo a liquidación (15/28-sep) y antes del flag de compliance (22-sep). Ver `ESTADO.md` → qué sigue valiendo. **Nada de esto está ejecutado en Amazon.**

## Decisiones tomadas

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

## Acciones aprobadas y no ejecutadas

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

## Bloqueo permanente (sin autorización puntual)
No ejecutar en Seller Central ni Ads · no comprar seguro ni pagar quote/bind · no subir COI · no cambiar la Legal Entity · no sacar EIN · no contratar domicilio US · no esconder categorías para cotizar · no quitar `toy` por conveniencia del seguro · **no reestructurar campañas antes de Q4** · **no pausar automáticas**.

## Historial (E = ejecutado en Amazon · A = aprobado, sin evidencia de ejecución)

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

## 📄 `Amazon/REFLEX/economia.md`

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

---

## 📄 `Amazon/REFLEX/errores-corregidos.md`

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

---

## 📄 `Amazon/REFLEX/historia-19sep.md`

# REFLEX — Foto al 19-sep, economía por ASIN, stock y resumen

> Fuente: `REFLEX_HISTORIA_COMPLETA_RESUMEN_v1.1` (PROYECTOS 100K, 19-sep). Series hasta el 16-sep; observación directa de listings del 19-sep. **Es lo más nuevo del expediente y corrige partes del índice del 17-sep** (títulos, precio por ASIN).

### DELTA 19-SEP-2026 — ESTADO OBSERVADO

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

### LA ECONOMÍA REAL, POR FIN ABIERTA POR ASIN

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

### EL CAMBIO DE TÍTULO DEL 4 DE SEPTIEMBRE

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

### EL STOCK AL 15 DE SEPTIEMBRE

Se compraron **5.000 unidades**. Entre el 10 de abril y el 4 de septiembre se vendieron **1.501**. Eso deja 3.499, que es el número que el vault venía usando como techo.

El **15 de septiembre** Santi confirmó **1.700 unidades por SKU, o sea 3.400 en total**. Es compatible con el cálculo anterior: entre el 4 y el 15 de septiembre hubo más ventas y el retiro de inventario.

Lo que **no está confirmado** es qué son exactamente esas 1.700: si es stock disponible en FBA, si incluye reservado, si incluye unidades no vendibles, o si es inventario físico total. Sin un informe de inventario por ASIN no se puede cerrar.

A la velocidad medida entre el 27 de agosto y el 14 de septiembre: **QW5 vendía 8,37 unidades por día, stock para 203 días. R46 vendía 1,79 por día, stock para 950 días.** Combinado son **335 días** — el inventario cruza a 2027 con cualquier estrategia de precio. Para liquidar las 1.700 de QW5 antes de fin de año harían falta **15,89 unidades diarias**, casi el doble de lo que vende.

**No hay riesgo de quedarse sin stock. Hay riesgo de sobrestock.** Y con el inventario cruzando a 2027 aparece el recargo por inventario añejo, que **todavía no se puede cuantificar** porque faltan los tramos de antigüedad y el volumen en pies cúbicos por unidad.

Capital inmovilizado al 15 de septiembre: **3.400 × 5,94 = US$20.196**, con la salvedad de que los 5,94 son un coste declarado y provisional.

### LO QUE SIGUE SIN SABERSE

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

### RESUMEN CORTO

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

## 📄 `Amazon/REFLEX/listing-seo.md`

# REFLEX — Listing, imágenes y SEO orgánico

> ⚠️ **Actualización 19-sep:** los títulos de abajo (capturas del 29-ago) **ya no están vigentes**. Al 19-sep ambos ASINs muestran `Reflex Challenge Drop Stick Game` (32 car., sin sufijo de color). QW5 tiene 9 imágenes, R46 7; ninguno tiene A+ ni video. Ver `historia-19sep.md`.
> Ventanas: W1 1-ago→3-sep · W9 Helium 30-ago/10-sep/15-sep. **No se suman entre sí.**

## Listing al 29-ago (histórico)

### R46 · B0GR46X8Y8

| Campo | Contenido | Chars |
|---|---|---:|
| TITLE | `Reflex Challenge Drop Stick Game - Remote Control - Reflex Sticks.` | **66 / 75** ✅ |
| ITEM HIGHLIGHTS (probable "Subtítulo") | `Reflex Challenge game - Reflex drop sticks game - Remote control 3 Adjustable Speed - (Sky Blue)` | **96 / 125** ✅ |
| BULLETS 1–4 | `Fast-Paced Reaction Game` · `Durable & Safe Construction` · `Multiple Game Modes` · `Adjustable Speed Settings` | — |
| BULLET 5 | no existe | — |
| BACKEND | `UNKNOWN` | — |

### QW5 · B0GQW5F2LL

| Campo | Contenido | Chars |
|---|---|---:|
| TITLE | `Reflex Challenge Drop Stick Game, Remote Control 3 Adjustable Speed, Reflex Drop Sticks Challenge Game, Reaction Training Toy,(Yellow)` | **134 / 75** ❌ incumplía |
| ITEM HIGHLIGHTS | `UNKNOWN` | — |
| BULLET 1 | idéntico al de R46 | — |
| BULLETS 2–4 | `2026 Enhanced Remote Control & Voice System` · `3 Adjustable Speed Levels` (incluye **`children 3+`**) · `6 Interactive Game Modes` | — |
| BULLET 5 | no existe | — |
| BACKEND | `UNKNOWN` | — |

Los bullets de QW5 son mejores. El bullet 1 está duplicado entre ASINs. **"children 3+" y "coordination toy" son el motivo del flag de compliance** (ver `compliance.md`) — y coinciden con la caja (AGES 3+).

### Política de Amazon vigente desde 27-jul-2026
- **TITLE ≤ 75 caracteres** · **ITEM HIGHLIGHTS ≤ 125**. Ambos son input de búsqueda.
- Una palabra puede aparecer **hasta DOS veces**.
- **Auto-truncado y auto-edición por Amazon, sin opt-out.** Truncado en móvil ≈ 60 car.

### Main images (29-ago) — ambas incumplían
| ASIN | Composición | Problema |
|---|---|---|
| R46 | producto + **caja de retail** en el tercio inferior | caja en main |
| QW5 | producto + **mano humana con motion blur** + remoto + soga + cable + caja | **mano humana prohibida** + saturación |

Decisión D-12: **CONCEPTO A** (producto limpio sobre blanco) como main en ambos. No ejecutada.

## SEO / orgánico — ranks W9 (tres fechas sin fusionar)

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

## Canibalización R46 vs QW5
| Fecha | Ambos rankeando | Gana QW5 | Gana R46 |
|---|---:|---:|---:|
| 30-ago | 63 | 50 | 10 |
| 10-sep | 59 | 58 | 1 |
| **15-sep** | **59** | **55** | **4** |

Halo cruzado de atribución: **1,6 % / 0,8 %** → no se canibalizan por atribución. Lo que existe es **solapamiento de gasto PPC**: 121 términos servidos por ambos = **61,4 % del gasto (W1)**. Es un problema de PPC, no de SEO.

## Keywords contaminantes
14 identificadas (13 sólo en el tracker de QW5): `speed stick` (desodorante) · `game stick` (consola) · `match sticks` · `speed training equipment` · `lacrosse stick` · `boost controller` · `hockey training equipment` · `speed controller` · `stick control` · `training equipment` · `grip stick` · `speed training` · `speed limit 3` · `birth control device`. Son **47,6 % del volumen rastreado** en Helium, pero su gasto PPC es **0,26–1,90 %**: **no explican la caída de CVR**. Además: `danny go sticks` (fuera del tracker).

## CTR / CVR de referencia (agosto — al 15-sep se invirtió)
| | R46 | QW5 |
|---|---:|---:|
| CTR | **4,10 %** | 2,52 % |
| CVR | **14,9 %** | 12,3 % |
| Unit Session % | **21,35 %** | 17,17 % |

Inferencia fuerte de agosto: la brecha de CTR de QW5 era de main image. Confounds no descartados: prueba social, badge de precio, placements.

---

## 📄 `Amazon/REFLEX/ppc-keywords.md`

# REFLEX — PPC: keywords, duelo de ASINs, product targeting y harvesting

> Ventanas: W1 1-ago→3-sep · W2 snapshot 7-sep · W3 27-ago→14-sep. **No se suman entre sí.**

## Keywords núcleo — W1 (21 términos, span ≥21 d y ≥4 compras)

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

## Duelo R46 vs QW5 sobre el mismo término — W1

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

## Core keywords con confianza de muestra — W3

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

## Product targeting — W1

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

## Harvesting observado — W1

El ciclo existe pero se hace **a mano, con 2–9 días de retraso, y sólo sobre la familia *reflex / reaction / drop sticks***. **Nunca cosechados** (exclusivos de AUTO con ≥2 compras): `outdoor games` (11 compras) · `backyard games` · `yard games` · `hand eye coordination toys` · `speed reaction exercise` · `energy stick toy` · `b0grwq7n45` · `b0dmnc5b2h` · `b0fzl2qpkk`.

## Términos huérfanos rentables (≥2 compras, ACoS <28,1 %, sin Exact propia) — W1

20 términos · **+US$ 130 de contribución con US$ 128 de gasto**. Muestra de 2 órdenes = confianza **BAJA**; falta su search volume.

`reaction time drop sticks` R46 · `drop sticks challenge game` QW5 · `b0dmnc5b2h` R46 · `reaction game falling sticks` QW5 · `energy stick toy` R46 · `speed reaction exercise` QW5 · `lawn games for adults` R46 · `camp games` R46 · `tapout falling sticks` QW5 · `falling sticks catching game` R46 · `drop sticks` R46 · `hand eye coordination toys` R46 · `falling sticks` QW5 · `beach games for adults` R46 · `reflex sticks challenge game reaction training` QW5 · `reaction speed training toy` QW5 · `reaction test game` QW5 · `the reflex sticks` QW5 · `reflex challenge` QW5 · `reflex test` QW5.

---

## 📄 `Amazon/REFLEX/ppc.md`

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

---

## 📄 `Amazon/REFLEX/protocolo.md`

# REFLEX — Protocolo DELTA-FIRST y fuentes

> Los archivos fuente (CSV de Amazon, Helium) viven en el vault **PROYECTOS 100K** (`90_INBOX/MASTER_IMPORTS/AMAZON/SOURCES/`) y en Descargas, no en esta carpeta.

## DELTA-FIRST (regla permanente desde 15-sep)

```
LAST VERIFIED BASELINE → NEW DATA ONLY → CALCULATE DELTA → FLAG MATERIAL CHANGES → DECIDE
```
**Nunca:** día nuevo → re-analizar todo el histórico.

El histórico completo se reabre **sólo** por: (1) contradicción entre fuentes · (2) anomalía material · (3) cambio de estrategia · (4) Santi pide auditoría completa.

### Umbrales de materialidad

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

### Reglas de procesamiento
- Los CSV crudos **se procesan con código (python/pandas), nunca leyendo filas**. Al modelo le llegan agregados.
- Un export nuevo se compara contra el último dato y **sólo el delta entra al contexto**.
- Si un dominio no cambió: **`NO ANALYSIS`**.
- Al cerrar una revisión se actualiza `ESTADO.md` con fecha y valores nuevos; no se crea un archivo por día.

### Formato de una revisión
```
WHAT CHANGED
ANOMALIES
ACTION REQUIRED
NO ACTION
```
Sin recapitular el histórico.

## Fuentes primarias (en PROYECTOS 100K)

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

## Lo que todavía no existe y hay que bajar de Amazon
1. **Informe de inventario FBA por ASIN** (bloqueante #1)
2. Removal Order Detail 01/09 → hoy
3. Bulk Operations export (placements y negativos)
4. Export del listing con backend e Item Highlights
5. Returns report / Voice of the Customer (causa del 19→20 ago)

---

## 📄 `Amazon/REFLEX/riesgos.md`

# REFLEX — Conflictos abiertos y datos faltantes

> Los riesgos de mayor impacto hoy (06-oct) son de **compliance y seguro**: ver `compliance.md`. Esta lista es el registro técnico del expediente.

## Conflictos de Reflex / cuenta KINAVARGAS

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

## Datos faltantes — ordenados por lo que desbloquean

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

## 📄 `Amazon/REFLEX/ventas.md`

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

---

## 📄 `Amazon/TERPTECH/CLAUDE.md`

# TERPTECH — TerpTech Premium 650mAh · B0F9SXP5MW (AMZ-P003)

> Batería 510 recargable con diseño de personaje y display digital. Listada en Amazon US bajo "Generic", categoría Soldering Irons.

## Archivos
| Archivo | Para qué |
|---|---|
| `FICHA_DE_PRODUCTO.md` | Identidad, specs, variantes, bullets, cómo estuvo expuesto, reviews, datos faltantes |
| `imagenes/` | 6 imágenes: 3 colores, infografía, listing (Seller Central y público), review 5★ con foto, fábrica |
| `07_line_sheet_mayorista.pdf` | Line sheet B2B original |

Sin `ESTADO.md` todavía: no hay registro de estado de cuenta, stock ni objetivo. No inventarlo; preguntar a Santi.

---

## 📄 `Amazon/TERPTECH/FICHA_DE_PRODUCTO.md`

---
tipo: ficha-producto
producto: TerpTech Premium 650mAh
claves: TerpTech, B0F9SXP5MW, AMZ-P003, batería 510, 650mAh
fecha: 2026-10-07
fuentes: vault "proyectos 100k" (AMZ-P003 PRODUCT_INFO, VISUAL_EVIDENCE, MASTER_STATE) + vault "obsidian c" (Producto, Line Sheet) + capturas del listing
---

# TERPTECH — FICHA DE PRODUCTO Y EVIDENCIA

> Solo información del producto y cómo estuvo expuesto. Sin historia de cuenta ni métricas.
> `UNKNOWN` = no existe en ningún vault. `CONFLICT` = dos fuentes dicen cosas distintas.

## 1. Identidad

| Campo | Valor | Fuente |
|---|---|---|
| Nombre | **TerpTech Premium 650mAh** (nunca "StarTech") | Santi |
| ASIN (Amazon US) | B0F9SXP5MW | captura del listing |
| SKU / FNSKU | Río LA5 / X004P581AN | captura de Seller Central |
| Marca mostrada en Amazon | Generic | captura del listing |
| Categoría de Amazon | Industrial & Scientific › Soldering Irons | captura del listing |
| Tipo real (venta B2B) | Batería 510 recargable, diseño de personaje, con display digital | vault obsidian c |

## 2. Títulos usados

- **Amazon (EN):** "TerpTech Premium Mini Solder with Rechargable Battery 650mAh Replacement Pen Battery"
- **Seller Central (ES, traducción automática):** "Mini soldador TerpTech Premium con batería recargable de 650 mAh. Batería de repuesto para bo…" (cortado en la captura)
- **Line sheet B2B (EN):** "TerpTech Premium 650mAh 510-Thread Battery — collectible character design with digital voltage display"

## 3. Especificaciones

| Spec | Valor | Fuente |
|---|---|---|
| Capacidad | 650 mAh | listing + line sheet |
| Potencia | 15 W | listing |
| Fuente de energía | Battery Powered, recargable por USB | listing |
| Voltaje | **CONFLICT C-16:** bullets → 3 niveles 2.8V / 3.2V / 3.5V · infografía → 24 ajustes, rango 1.8V–4.2V | listing vs infografía |
| Display | Digital, lectura de voltaje en tiempo real | listing |
| Rosca | 510 universal | line sheet / listing ("Universal Thread") |
| Activación | 5 clics en el "ojo izquierdo" encender/apagar · 3 clics cambia modo · 2 clics ajusta voltaje | listing |
| Calentamiento | Llega a temperatura en segundos | listing |
| Special features (Amazon) | Lightweight, Portable, Rechargeable, Wireless | listing |
| Usos declarados (Amazon) | Electronics Repair, Jewelry Soldering, Residential Use | listing |
| **Dimensiones** | `UNKNOWN` — no hay ficha dimensional en ningún vault | — |
| **Peso** | `UNKNOWN` | — |
| **Packaging / caja / case pack** | `UNKNOWN` (line sheet dice "Case pack: 50 / 100 — definir") | line sheet |
| **Certificados** (FCC, CE, RoHS, UN38.3, MSDS/SDS) | `UNKNOWN` — **no hay ningún certificado en los vaults**. Pedírselos a la fábrica | — |
| Fábrica / proveedor | `UNKNOWN` — solo foto de la planta (cartelería en chino) | imagen 06 |

## 4. Variantes y diseño

- Muñeco tipo personaje: cuerpo de color, gorra, ojos grandes, boca con el display, patitas.
- **3 colores físicos:** naranja con gorra negra (la que se vendió y aparece en el listing) · negro con detalles naranjas · rosa con detalles blancos. Hay 1.100 unidades de cada color.
- La infografía muestra combinaciones algo distintas: amarillo/negro, rosa/blanco, gris/naranja.
- Line sheet B2B: Yellow · Pink · Black.

## 5. Bullets del listing de Amazon (transcriptos de la captura, el texto está cortado a la derecha)

1. **Digital Display: Quick Activation & Adjustments** — Turn on with 5 clicks on the "left eye" and switch modes with 3 clicks. Adjust temperature with 2 cl[icks] between 2.8V, 3.2V, and 3.5V. The digital display provides real-time vo[ltage] readings, and fast heating reaches working temperature in seconds.
2. **Portable, Rechargeable** thread burner Compact Small and compact des[ign] with USB rechargeable functionality for maximum mobility. Perfect fo[r] repairs, hobbies, and workstations.
3. **Battery-powered 15-watt portable soldering iron** eliminates cord restri[ctions], ideal for mobile repairs and tight spaces.
4. **Universal Thread:** Compatible with Multiple Soldering batteryTypes & Universal Thread Works with rosin-core, leaded, lead-free, and low-mel[t]…
5. (5.º bullet fuera de la captura — `UNKNOWN`)

Descripción larga, A+ Content y backend keywords: `UNKNOWN` (no capturados).

## 6. Cómo estuvo expuesto en Amazon

- Galería: 7 imágenes + video (badge "3+"). Las miniaturas visibles son: foto principal en mano (display en 2.8V) · "Key Features" · "Precise Voltage Output" (3 unidades en 2.8V/3.2V/3.6V) · foto de uso portátil en un auto · "Fun & Unique Design" (variantes de color) · foto colgando como llavero.
- Rating: **4.4★ con 80–81 reviews**.
- BSR que se vio: Industrial & Scientific #21.485–#22.316 · Soldering Irons #56–#60.
- Listing Health Score (herramienta de terceros): 9.2.
- Top keywords del listing (herramienta de terceros): "510 threaded battery", "vape pen".
- Precio medio de venta: $23.74.

## 7. Reviews positivas

- **Reo Clark — 5★ Verified Purchase — "Built well good battery"**
  > "Great little battery built well works great had it for awhile it's in and out of pockets vehicles and works everytime good battery great for cartridges."
  Incluye foto del cliente: la unidad naranja con un cartucho puesto (imagen 05).
- Del resto de las 80 reviews no hay texto guardado (`UNKNOWN`). En las notas figura este resumen: "funciona siempre, buena para cartuchos".

## 8. Argumentos de venta (line sheet B2B)

- 650 mAh: dura más que las baterías novelty típicas de 400–500 mAh.
- Display digital: algo premium que la mayoría de las baterías con personaje no tiene.
- Diseño coleccionable, con atractivo novelty probado.
- Prueba social: 4.4★ con más de 80 reviews verificadas en Amazon.

## 9. Índice de imágenes (carpeta `imagenes/`)

| Archivo | Contenido |
|---|---|
| 01_producto_3_colores.jpeg | Las 3 variantes físicas juntas |
| 02_infografia_custom_brightness.png | Render de marketing: 24 ajustes 1.8–4.2V, 3 unidades con display |
| 03_listing_amazon_titulo_bullets.jpeg | Seller Central: título en ES, ASIN, SKU, FNSKU |
| 04_listing_amazon_resumen.jpeg | Listing público: foto principal, título, item specifics, bullets, galería |
| 05_review_5_estrellas_verificada.jpeg | Review 5★ verificada con foto del cliente |
| 06_fabrica_produccion.jpeg | Planta con cientos de unidades en bandejas (3 colores) |
| 07_line_sheet_mayorista.pdf | Line sheet B2B |

## 10. Qué falta conseguir (para cualquier canal)

1. Dimensiones y peso del producto, y de la caja individual y la caja master → pedir a la fábrica.
2. Certificados: FCC, CE, RoHS, UN38.3, MSDS/SDS de la batería de litio → pedir a la fábrica.
3. Fotos originales en alta resolución de la galería (las 7 + el video): hoy solo hay capturas de pantalla.
4. Texto completo del 5.º bullet y de la descripción, y más reviews positivas (se pueden capturar desde la página de reviews del ASIN si sigue pública).

---

## 📄 `Etsy/CLAUDE.md`

# Ecosistema Etsy

## Resumen
<!-- tienda(s), nicho, estado -->

## Productos / listings
<!-- si crecen, una subcarpeta por producto como en Amazon/ -->

Notas de detalle compartidas: `_comun/`

---

## 📄 `Paginas-Web/CLAUDE.md`

# Páginas web

## Sitios
<!-- dominio, plataforma (Shopify/WordPress/...), objetivo, estado -->

Notas de detalle compartidas: `_comun/`

