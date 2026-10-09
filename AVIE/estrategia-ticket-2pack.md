# AVIE — Subir el ticket: "compra 2" y 2-pack (2026-10-08)

> Pregunta de Santi: con un producto barato el margen no alcanza para la publicidad → ¿incentivar que compren 2 o hacer un pack de 2 para bajar costos y ganar margen?
> Datos: `datos/2026-10_transacciones.csv`. Economía base: `CLAUDE.md` (a 14,99: tarifas 6,34 · margen 5,79 · ACOS máx. 38,6 %).

## 1 · El punto clave: qué abarata y qué no
- **HECHO:** en los pedidos de 2 unidades del MISMO ASIN, Amazon cobra las tarifas **por unidad**. Ejemplo: pedido de 19,98 (2 × 9,99) → tarifas 8,08 = 2 × 4,04. Diez pedidos así en el período, todos con la misma lógica.
→ **"Compra 2 y ahorrá" NO baja las tarifas de Amazon.** Lo que mejora es la plata que deja cada pedido: un solo clic pagado trae 2 unidades.
- **Un 2-pack de verdad (ASIN nuevo, 2 cepillos en una sola unidad de venta) SÍ baja las tarifas por unidad.** Se paga una sola comisión FBA por un paquete un poco más grande: ~4,10-4,70 por cepillo contra 6,34 de hoy (HIPÓTESIS: la tarifa FBA del 2-pack, 5,20, es una estimación; falta medir y pesar).

## 2 · Opción A — Promoción "Compra 2, ahorrá X %" sobre el ASIN actual
Sin logística, sin perder reseñas ni el Amazon's Choice, se activa en el día (Seller Central → Publicidad → Promociones → Porcentaje de descuento, condición "compra mínima 2 unidades"; verificar que la cuenta lo habilite).
| Descuento por llevar 2 | Paga el cliente | Margen del pedido | Margen por unidad | ACOS máx. |
|---|---|---|---|---|
| — (pedido de 1) | 14,99 | **5,79** | 5,79 | 38,6 % |
| 5 % | 28,48 | 9,37 | 4,68 | 32,9 % |
| **10 %** | **26,98** | **7,91-8,58** | 3,95-4,29 | 29,3-31,8 % |
| 15 % | 25,48 | 6,45 | 3,22 | 25,3 % |
| 20 % | 23,98 | 4,98 | 2,49 | 20,8 % (peor que vender 1) |
(Supuesto conservador: comisión sobre precio lleno + ~2,5 % de tarifa de promoción. Sin esa tarifa, el 10 % deja 8,58.)

**Lectura:** el 10 % es el punto justo: el pedido de 2 deja **+37-48 % más que un pedido de 1** y mueve el doble de stock. Con 15 % o más ya no conviene.
**Límite real:** sólo una parte de los compradores va a llevar 2 (HIPÓTESIS: 10-25 % en temporada de regalos). Si el 20 % lo toma, el margen promedio por pedido sube ~10 %. **Ayuda, pero sola no vuelve rentable un ACOS de 151 %.**
**Requisito:** subir el **límite de compra de 5 a 30** (pendiente desde septiembre).
**Mensaje:** "Una para vos, otra para regalar" (bullet 5 + A+). El ángulo regalo encaja justo con el "compra 2".

## 3 · Opción B — 2-pack como ASIN propio
| Precio 2-pack | Margen sin reempaque | Margen con reempaque (~2 USD/pack) | ACOS máx. (con reempaque) |
|---|---|---|---|
| 19,99 | 6,07 | 4,07 | 20,4 % |
| 22,99 | 8,62 | 6,62 | 28,8 % |
| **24,99** | 10,32 | **8,32** | **33,3 %** |
| 27,99 | 12,87 | 10,87 | 38,8 % |
Referencia de mercado: Aeki 2 uds a **17,98** (667 reseñas, 1.469/mes) · Cxguu 2 uds a 9,99. A 24,99 el 2-pack queda en 12,50 por cepillo: más barato que AVIE suelto (14,99), pero más caro que el 2-pack de Aeki.

**Lo que hace difícil la opción B en este Q4:**
1. **No se puede convertir la ficha actual en "pack de 2".** Cambiar la cantidad de un ASIN con ventas es un cambio de producto que Amazon no permite. Hay que crear un **ASIN nuevo**, con su UPC o la exención de GTIN.
2. **Reseñas:** si se arma como **variación** del ASIN actual ("1 unidad / 2 unidades"), comparte las 38 reseñas. Si no, arranca en cero. Con marca "Generic" y sin Brand Registry, la variación **puede no estar disponible** → verificar en Seller Central (herramienta de variaciones) antes de decidir.
3. **Logística:** las unidades están sueltas dentro de FBA. Para empaquetarlas hay que pedir una **orden de retiro** a un 3PL en EE. UU., armar los packs con etiqueta "vendido como set" y reenviarlos a FBA. En Q4 los retiros y las recepciones se demoran: es realista tenerlos de vuelta **a mediados o fines de noviembre**, con riesgo de no llegar a Black Friday. Costo estimado de retiro + armado + reingreso: ~2 USD por pack (HIPÓTESIS; pedir cotización al 3PL).
4. **Excepción:** si hay unidades **fuera de FBA** (en el 3PL o en camino), con esas se puede armar el 2-pack sin pagar el retiro. **Dato que falta.**

## 4 · Recomendación
1. **Ya (cuesta 0, se puede deshacer):** promoción "Compra 2, ahorrá 10 %" + límite de compra 5 → 30 + bullet o A+ de "una para vos, otra para regalar".
2. **Decidir antes del 15-oct:** 2-pack como variación, **sólo si** (a) la herramienta de variaciones lo deja hacer con la marca "Generic" y (b) hay unidades en el 3PL o el 3PL cotiza retiro + armado + reingreso por debajo de ~2 USD por pack con fecha antes del 15-nov. Si no se cumple, el 2-pack queda para Q1 2027.
3. **No subir el precio del suelto por ahora:** el CTR cayó a 0,38 % con 14,99. El ticket se sube con el pedido de 2, no con el precio unitario.

## 5 · Stock y Q4 (respuesta a "1.500-2.000 en oct-nov y el resto en diciembre")
- **HECHO:** el mejor mes, junio (249 pedidos, ~8/día), salió a pérdida: neto 1.731,73 − ads 1.001,92 − producto ~712 − almacenamiento 132 − plan 40 − reembolsos 88 ≈ **−240 USD**.
- **HECHO:** bajar el precio no trajo volumen. Entre julio y septiembre, a 9,99, se vendieron 41, 82 y 77 pedidos por mes (~2,5/día). **El freno es que no lo ven, no el precio.**
- **Argumento de Santi (válido):** junio fue temporada baja y Q4 trae más tráfico de regalo. **HIPÓTESIS:** las búsquedas del nicho en nov-dic suben entre 1,5 y 2,5 veces. Se puede verificar con el historial de volumen de Helium 10.
- **Proyección con la eficiencia corregida y Q4 a favor:** oct (8-31) 150-250 · nov 400-550 · dic 400-600 → **≈1.000-1.400 uds al 31-dic**. Con "compra 2" se suman ~10-20 % de unidades.
- **Venderlo todo (3.900 uds en 84 días = 46/día) no es realista solo con Amazon.** Hay que definir el plan para lo que sobre (~2.500 uds): seguir vendiendo en Q1 2027 (el almacenamiento baja en enero, pero aparece el recargo por inventario envejecido), sacar unidades para venderlas por otro canal (mayorista o TikTok Shop), o liquidación de Amazon como último recurso. **Decisión de Santi, a tomar antes del 30-nov.**
