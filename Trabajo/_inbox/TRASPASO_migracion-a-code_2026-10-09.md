# TRASPASO — Mudanza Obsidian/Cowork → Claude Code · 2026-10-09
**Origen:** sesión de Claude Code en la nube "obsidian-data-migration" (2026-10-06 → 10-09) · **Destino sugerido:** `Trabajo/CLAUDE.md` y `ESTADO` de cada carpeta (casi todo ya está aplicado; esto es el registro y los pendientes)

> El contenido de los productos **ya está en el repo** (ver tabla de `Trabajo/CLAUDE.md`). Este traspaso no repite datos de productos: sólo lo que se decidió sobre cómo trabajar y lo que quedó pendiente.

## 1. Contexto estable
- HECHO · Repo GitHub `amazonfbasantino-wq/prueba`. Rama principal: **`claude/hope-main-negocios`** (antes `claude/hopeful-allen-FxQrV`; no existe `main`). Rama de trabajo de la mudanza: `claude/obsidian-data-migration-i9q4nd`.
- HECHO · Estructura: `Trabajo/E-commerce/` → ecosistema (`Amazon/`, `TERPTECH/`, `Etsy/`, `Paginas-Web/`) → una carpeta por producto. Cada producto: `CLAUDE.md` (estable) + `ESTADO.md` (dónde quedamos) + archivos temáticos + `assets/`. Regla **write once, reference many**.
- HECHO · `CLAUDE.md` en la raíz del repo: al empezar, leer sólo `CLAUDE.md` + `ESTADO.md` del producto; al cerrar, actualizar `ESTADO.md` y commitear; CSV grandes con scripts.
- HECHO · Fuente principal = carpeta local en la compu de Santi (clon del repo). **Google Drive `AMAZON/` = copia espejo de lectura** para Claude en Cowork/app (decisión 2026-10-08; antes se había dicho "Drive no se usa" y se revirtió).
- HECHO · `scripts/migrar_obsidian.py RUTA_VAULT [--aplicar]`: clasifica notas de un vault (carpeta o .zip) en `Trabajo/` por palabras clave (`REGLAS`); sin `--aplicar` sólo muestra el plan; nunca pisa archivos.
- HECHO · Una sesión de Claude Code en la nube **no ve la compu de Santi**. Para trabajar sobre Finder: Claude Code local (app de escritorio, pestaña Code, o `claude` en Terminal) dentro del clon:
  `git clone https://github.com/amazonfbasantino-wq/prueba.git ~/Trabajo-Santi`

## 2. Estado actual
**Migrado y verificado (tamaño + codificación):** Amazon madre, AVIE, MT-BALL (+ `keywords_Q4_tracker.csv`), REFLEX, KINA, `_CUENTA-KINAVARGAS`, TerpTech (ficha + 6 imágenes + line sheet; imágenes y PDF subidos por Santi por git, commit `1432368`).
Después otras sesiones reorganizaron todo bajo `E-commerce/` y sacaron TerpTech de Amazon (hoy `TERPTECH/` en la raíz del repo, con su `ESTADO.md` y `_CUENTA-DECOHOUSE/`). Para el estado de TerpTech, mandan esos archivos, no este traspaso.

**En Drive `AMAZON/TERPTECH/`:** `CLAUDE.md` y `07_line_sheet_mayorista.pdf` (subidos 2026-10-08; ese line sheet ya no se usa, ver `TERPTECH/ESTADO.md`). La ficha está suelta en `AMAZON/` como `TERPTECH_FICHA_DE_PRODUCTO.md`.

**Pendientes de la mudanza:**
1. Espejo de Drive: quedó con la estructura vieja (`AMAZON/…`). Decidir si se mantiene al día y cómo (decisión de Santi).
2. Traspasar los chats viejos con `PROMPT_TRASPASO.md` (los que no se hayan pasado todavía).
3. `E-commerce/Amazon/_ARCHIVO/`: copiar los vaults crudos (`obsidian c`, `PROYECTOS 100K`) desde la compu (sólo consulta).
4. `E-commerce/Paginas-Web/`: migrar `02 Negocios/` del vault.

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
- Nombres reales de las carpetas/sitios de Páginas Web y tiendas de Etsy (→ chats viejos / vault).

## 6. Archivos adjuntos
Ninguno nuevo: todo está en el repo.
