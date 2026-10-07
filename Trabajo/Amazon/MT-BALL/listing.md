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
