# Mis Descargas con Claude

Una app que corre en tu computadora y vigila tu carpeta de **Descargas**. Cuando se termina de descargar un archivo:

1. Lo detecta en el momento (también si lo bajaste con la extensión de Claude en Chrome).
2. Claude lo **lee y lo resume**: de qué se trata, puntos clave y qué harías con él.
3. Lo muestra en una **página local** que se actualiza sola, y te avisa con una notificación.

Soporta **PDF** (incluidos los escaneados), **Excel** (.xlsx), **CSV**, **imágenes** (PNG, JPG, GIF, WebP) y **texto** (TXT, MD, JSON, HTML, etc.).

## Instalación (una sola vez)

Necesitás **Python 3.10 o superior** ([descargar](https://www.python.org/downloads/); en Windows marcá *"Add Python to PATH"* al instalar).

```bash
# 1. Bajá este repositorio y entrá a la carpeta
git clone https://github.com/amazonfbasantino-wq/prueba.git
cd prueba

# 2. Instalá las dependencias
pip install -r requirements.txt

# 3. Creá tu archivo de configuración
#    Windows:      copy .env.example .env
#    macOS/Linux:  cp .env.example .env
```

Abrí el archivo `.env` y poné tu **API key de Anthropic** (la sacás en <https://console.anthropic.com/>):

```
ANTHROPIC_API_KEY=sk-ant-tu-clave
```

Por defecto vigila tu carpeta de Descargas. Si usás otra, completá `WATCH_FOLDER`.

## Uso

```bash
python app.py
```

Abrí **<http://localhost:5000>** en tu navegador y dejá esa pestaña abierta. Cada vez que descargues algo, aparece arriba de todo con el resumen de Claude.

En cada archivo podés:

- **Abrir archivo**: lo abre en el navegador.
- **Volver a analizar**: le pide a Claude un resumen nuevo.
- **Quitar**: lo saca de la lista (no borra el archivo).

El historial se guarda en `historial.json`, así que sigue ahí aunque cierres la app.

## Cómo funciona

| Archivo | Qué hace |
|---|---|
| `app.py` | Vigila la carpeta, espera a que la descarga termine (ignora los `.crdownload` de Chrome), manda el archivo a analizar y sirve la página. |
| `analyzer.py` | Lee el archivo según su tipo y le pide el resumen a Claude. |
| `templates/index.html` | La página que muestra las descargas, en vivo. |

Para cambiar qué te responde Claude, editá el texto `PROMPT` en `analyzer.py`.

## Notas

- Cada archivo analizado usa tu API de Anthropic, que tiene costo por uso. Los archivos de texto muy largos se recortan (unos 60.000 caracteres) para no gastar de más.
- La página solo se ve desde tu computadora (`127.0.0.1`), no desde otros dispositivos de la red.
- Los formatos que Claude no puede leer, como `.zip` o `.exe`, aparecen en la lista con un aviso.
