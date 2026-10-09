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
| AVIE / MT Ball / Reflex / KINA (Amazon) | `E-commerce/Amazon/<PRODUCTO>/` |
| Cuenta KINAVARGAS (seguro, casos, salud de cuenta) | `E-commerce/Amazon/_CUENTA-KINAVARGAS/` |
| TerpTech (mayoristas, catálogo, leads, 3PL, Shopify/DTC) | `E-commerce/TERPTECH/` (TerpTech ya no va en Amazon) |
| Cuenta Amazon bloqueada (DecoHOUSE, Sección 3), apelación, fondos retenidos | `E-commerce/TERPTECH/_CUENTA-DECOHOUSE/` |
| RapiPet u otro sitio | `E-commerce/Paginas-Web/<SITIO>/` (crear) |
| Etsy | `E-commerce/Etsy/` (una subcarpeta por tienda/producto si crece) |
| Transversal (LLC VirtualMed, impuestos, banco, meta 100k) | `_compartido/` |
| Ni idea | dejarlo acá y preguntar a Santi |

3. Repartir el contenido sin duplicar (**write once, reference many**):
   - Hechos estables (identidad, cuentas, proveedor, economía, reglas) → `CLAUDE.md` de esa carpeta.
   - Dónde quedamos, pendientes, decisiones abiertas, próximos pasos → `ESTADO.md`.
   - Detalle largo de un tema (listing, ppc, apelación, integración…) → archivo temático (`apelacion.md`, `integracion-shopify.md`, …) listado en el `CLAUDE.md`.
   - Si un dato ya existe en otro archivo: no copiarlo; poner referencia. Si contradice lo que hay: **no pisar**, anotarlo en `ESTADO.md` → "⚠️ Contradicciones a confirmar" con las dos versiones y fechas.
4. Mantener las marcas HECHO / INFERENCIA / HIPÓTESIS del traspaso. No inventar nada que no esté.
5. Nada de DNI, números de cuenta bancaria, contraseñas ni tokens completos en los archivos (sólo "últimos 4").
6. Actualizar la tabla de estado de `Trabajo/CLAUDE.md` (y de `E-commerce/Amazon/CLAUDE.md` si aplica).
7. Borrar el `TRASPASO_*.md` procesado, commitear (`git commit -m "Traspaso <tema>"`) y pushear.
8. Si existe la copia espejo en Google Drive, recordarle a Santi qué archivos cambiaron para subirlos.
