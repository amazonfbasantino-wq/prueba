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
