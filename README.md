# YouTube Downloader Script

Este script te permite descargar videos de YouTube en la máxima calidad disponible, con opciones para especificar resoluciones, descargar solo el audio en formatos personalizados y elegir rutas de salida. Es ideal para usuarios que desean un enfoque flexible y completo para la descarga de contenido multimedia desde YouTube.

---

## Características

- **Descarga por defecto en máxima calidad**: El script selecciona automáticamente el mejor video y audio disponibles.
- **Especificación de resolución**: Permite descargar el video en una resolución específica, como 1080p o 720p.
- **Descarga solo audio**: Puedes descargar solo el audio del video en formatos como MP3, M4A u Opus.
- **Ruta de salida personalizable**: Por defecto, guarda el archivo en el directorio actual, pero puedes especificar una ruta de salida diferente.
- **Combinación automática de video y audio**: Usa FFmpeg para combinar video y audio cuando se descargan por separado.

---

## Instalación y Dependencias

### 1. Instalar Python
Asegúrate de tener Python 3.7 o superior instalado. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### 2. Instalar `yt-dlp`
Ejecuta el siguiente comando para instalar **yt-dlp**, una herramienta para descargar videos de YouTube:
```bash
pip install yt-dlp
```

### 3. Instalar FFmpeg (Requerido para combinación de video y audio)
- **Windows**:
  1. Descarga FFmpeg desde [ffmpeg.org](https://ffmpeg.org/download.html). Si vas a ```BtbN``` te enviará a GitHub. Donde debes descargar por ejemplo: ```ffmpeg-n7.1-latest-win64-gpl-7.1.zip```
  2. Una vez descargado, descomprimir en C:\ y renombrar el directorio como ```ffmpeg```.
  3. Cofigurar ruta en variables de entorno ```Path``` con el valor ```C:\ffmpeg\bin```. Esta ruta cambia dependiendo de donde esta ubicado el directorio y como se llame el directorio.
- **Linux**:
  ```bash
  sudo apt update && sudo apt install ffmpeg
  ```
- **macOS**:
  ```bash
  brew install ffmpeg
  ```

### 4. Clonar
Clona el repositorio con
```
git clone https://github.com/sorodriguezz/youtube-python.git
```

---

## Cómo Usarlo

Ejecuta el script desde la terminal con las opciones necesarias:

### Descarga en máxima calidad (por defecto):
```bash
python download_video_youtube.py --url https://www.youtube.com/watch?v=VIDEO_ID
```

### Descargar con una resolución específica (ejemplo: 720p):
```bash
python download_video_youtube.py --url https://www.youtube.com/watch?v=VIDEO_ID --resolution 720
```

### Descargar solo el audio (formato por defecto: MP3):
```bash
python download_video_youtube.py --url https://www.youtube.com/watch?v=VIDEO_ID --audio-only
```

### Descargar solo el audio en otro formato (ejemplo: M4A):
```bash
python download_video_youtube.py --url https://www.youtube.com/watch?v=VIDEO_ID --audio-only --audio-format m4a
```

### Especificar una carpeta de salida:
```bash
python download_video_youtube.py --url https://www.youtube.com/watch?v=VIDEO_ID --output-dir ./mi_directorio
```

### Mostrar ayuda:
```bash
python download_video_youtube.py --help
```

---

## Salida del Comando `--help`

```text
usage: youtube_downloader.py [-h] --url URL [--resolution RESOLUTION] [--audio-only] [--audio-format AUDIO_FORMAT] [--output-dir OUTPUT_DIR]

Descarga videos de YouTube en máxima calidad, con opciones de resolución o solo audio.

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL del video de YouTube que deseas descargar.
  --resolution RESOLUTION
                        Resolución máxima deseada para el video (ejemplo: 1080, 720). Por defecto, descarga la máxima calidad.
  --audio-only          Descarga solo el audio del video.
  --audio-format AUDIO_FORMAT
                        Formato del audio si descargas solo audio (opciones: mp3, m4a, opus). Por defecto: mp3.
  --output-dir OUTPUT_DIR
                        Carpeta de salida para el archivo descargado. Por defecto: el directorio actual.
```

---

## Ejemplos

### 1. Descargar un video en máxima calidad:
```bash
python youtube_downloader.py --url https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

### 2. Descargar un video en 720p:
```bash
python youtube_downloader.py --url https://www.youtube.com/watch?v=dQw4w9WgXcQ --resolution 720
```

### 3. Descargar solo el audio en formato MP3:
```bash
python youtube_downloader.py --url https://www.youtube.com/watch?v=dQw4w9WgXcQ --audio-only
```

### 4. Descargar solo el audio en formato M4A y guardarlo en una carpeta llamada `audios`:
```bash
python youtube_downloader.py --url https://www.youtube.com/watch?v=dQw4w9WgXcQ --audio-only --audio-format m4a --output-dir ./audios
```

---

## Notas

1. **FFmpeg es obligatorio** para combinar video y audio en el caso de que se descarguen por separado.
2. Si no se especifica una opción, el script descarga el video completo con la máxima calidad disponible.
3. El formato predeterminado para el audio es MP3, pero puedes elegir M4A u Opus.
4. Para descargas en resoluciones muy altas (como 4K), asegúrate de que tienes suficiente espacio en disco.

---

## Licencia
Este script es de uso libre. Puedes modificarlo y distribuirlo según tus necesidades.

