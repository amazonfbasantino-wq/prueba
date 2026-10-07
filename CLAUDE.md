# Repo de trabajo de Santi

- **El trabajo vive en `Trabajo/`** (vault migrado desde Obsidian). Mapa y estado de carpetas: `Trabajo/CLAUDE.md`.
- Al empezar una tarea: leer **sólo** el `CLAUDE.md` y el `ESTADO.md` de la carpeta del producto que toque (ej. `Trabajo/Amazon/AVIE/`). Abrir el resto sólo si la tarea lo pide.
- Al cerrar la sesión: actualizar el `ESTADO.md` de ese producto y commitear.
- CSV/exports grandes se procesan con scripts (python), nunca se leen fila por fila.

## Gestión de contexto (trabajar siempre liviano)
- **El estado vive en archivos, no en el chat.** Lo que se decide o avanza va al `ESTADO.md` del producto en el momento, no al final.
- **Una sesión = un bloque** (un producto, una tarea). Al terminar el bloque: actualizar `ESTADO.md`, commitear y proponerle a Santi `/clear`. La sesión nueva arranca leyendo sólo `CLAUDE.md` + `ESTADO.md`.
- **Si un bloque queda a medias**, dejar en `ESTADO.md` una sección `## TAREA EN CURSO` con el punto exacto (ej.: "procesados 12 de 25, falta X; siguiente paso: Y"). Al retomar, se empieza por ahí y se borra al cerrar.
- **Umbral: 50 % de la ventana.** Pasado eso: guardar estado → `/clear`. No esperar al 90 % (ahí compacta solo y se pierden detalles). Si hay que seguir sí o sí: `/compact` con instrucciones de qué conservar.
- **No inflar el contexto:** no volcar exports, CSV ni respuestas largas de APIs/Drive al chat; procesarlos con scripts y traer sólo el resumen o el delta.
- **Tareas repetitivas o automáticas** (rutinas): una sesión nueva por corrida, que lee el estado, hace su parte y lo actualiza.

- El resto del repo (`app.py`, `analyzer.py`, `templates/`) es una app aparte (resumen de descargas, ver `README.md`); no tocarla salvo que se pida.
