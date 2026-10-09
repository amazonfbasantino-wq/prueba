# Trabajo — contexto general

Carpeta raíz del trabajo (migrado desde Obsidian / Cowork). **Fuente principal: esta carpeta en la compu de Santi. Google Drive (`AMAZON/`) es copia de lectura para Claude en Cowork/app: al cambiar algo acá, subirlo también allá.** Claude Code lee este archivo
y además el `CLAUDE.md` de cada subcarpeta en la que se trabaje: acá va solo lo que aplica
a TODO; lo específico vive en su carpeta (regla: **write once, reference many**).

## Estructura
Todo lo de venta online vive en **`E-commerce/`**. Un ecosistema = una carpeta.

| Carpeta | Qué hay | Estado |
|---|---|---|
| `E-commerce/Amazon/` | Contexto madre de Amazon (quién soy, meta, cuentas, reglas duras) | ✅ |
| `E-commerce/Amazon/AVIE/` | AVIE Lymphatic Contour Face Brush · B0GT75CR86 (Beauty Michele) · vender stock hasta agotar | ✅ |
| `E-commerce/Amazon/MT-BALL/` | MT Ball con Maxi · **no lanzar en Beauty Michele** | ✅ |
| `E-commerce/Amazon/REFLEX/` | Reflex Game R46 / QW5 (KINAVARGAS) · liquidación | ✅ |
| `E-commerce/Amazon/KINA/` | KINA Face Brush · B0GQJLP4TB · liquidación fuera de Amazon | ✅ |
| `E-commerce/Amazon/_CUENTA-KINAVARGAS/` | Cuenta KINAVARGAS: titular, seguro, casos | ✅ |
| `E-commerce/Amazon/_ARCHIVO/` | Vaults de Obsidian en crudo (sólo consulta) | ⏳ copiar desde la compu |
| `E-commerce/TERPTECH/` | TerpTech (batería 510) · **fuera de Amazon** · B2B mayorista, catálogo, leads, outreach | ✅ |
| `E-commerce/TERPTECH/_CUENTA-DECOHOUSE/` | Cuenta Amazon bloqueada (Sección 3): historia, apelación, US$ 3.000 retenidos, correspondencia | ✅ 2026-10-08 |
| `E-commerce/Etsy/` | Ecosistema Etsy | ⏳ falta el email de la tienda |
| `E-commerce/Paginas-Web/` | Sitios (RapiPet y otros) | ⏳ migrar desde `02 Negocios/` del vault |
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
