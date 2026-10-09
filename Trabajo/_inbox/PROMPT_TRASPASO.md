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
