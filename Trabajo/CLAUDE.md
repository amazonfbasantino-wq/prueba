# Trabajo — contexto general

Carpeta raíz del trabajo (migrado desde Obsidian / Cowork). **Fuente única: esta carpeta en la compu de Santi; Google Drive no se usa.** Claude Code lee este archivo
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
| `Amazon/TERPTECH/` | TerpTech Premium 650mAh · B0F9SXP5MW · batería 510 | ✅ migrado · canal: B2B mayorista (Shopify descartado 2026-10-08) |
| `Amazon/_CUENTA-KINAVARGAS/` | Cuenta KINAVARGAS: titular, seguro, casos | ✅ migrado |
| `Amazon/_ARCHIVO/` | Vaults de Obsidian en crudo (sólo consulta) | ⏳ pendiente: copiar desde los vaults en la compu |
| `Etsy/` | Ecosistema Etsy | ⏳ pendiente |
| `Paginas-Web/` | TerpTech / DTC, RapiPet y otros sitios | ⏳ pendiente: migrar desde `02 Negocios/` del vault |
| `_compartido/` | Lo transversal a todos los ecosistemas | vacío |
| `_inbox/` | Notas importadas sin clasificar | vacío |

Cada producto sigue la misma estructura: `CLAUDE.md` (lo estable) + `ESTADO.md` (dónde quedamos)
+ archivos temáticos (`listing.md`, `ppc.md`, `keywords.md`, `riesgos.md`, …) + `assets/`.

## Cómo trabajar
- Abrir Claude Code en la carpeta del producto/ecosistema que toque: así se carga sólo ese contexto.
- Antes de investigar afuera, buscar primero acá (grep por producto, ASIN, competidor, proveedor).
- Al cerrar cada sesión, actualizar el `ESTADO.md` del producto.

## Migrar más notas
`python scripts/migrar_obsidian.py RUTA_AL_VAULT` (desde la raíz del repo) muestra el plan;
con `--aplicar` copia. Ajustar `REGLAS` en el script al sumar productos nuevos.
