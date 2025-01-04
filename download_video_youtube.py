import os
import argparse
from yt_dlp import YoutubeDL

def download_video(video_url, resolution=None, audio_only=False, audio_format="mp3", output_dir="./"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'outtmpl': f"{output_dir}/%(title)s.%(ext)s",
    }

    if audio_only:
        ydl_opts.update({
            'format': f'bestaudio[ext={audio_format}]/bestaudio',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': audio_format,
                'preferredquality': '192',
            }],
        })
    elif resolution:
        ydl_opts.update({
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        })

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        print(f"Descarga completada. Revisa la carpeta: {output_dir}")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Descarga videos de YouTube en máxima calidad, con opciones de resolución o solo audio."
    )

    parser.add_argument(
        '--url',
        type=str,
        required=True,
        help="URL del video de YouTube que deseas descargar."
    )
    parser.add_argument(
        '--resolution',
        type=int,
        required=False,
        help="Resolución máxima deseada para el video (ejemplo: 1080, 720). Por defecto, descarga la máxima calidad."
    )
    parser.add_argument(
        '--audio-only',
        action='store_true',
        help="Descarga solo el audio del video."
    )
    parser.add_argument(
        '--audio-format',
        type=str,
        required=False,
        default='mp3',
        help="Formato del audio si descargas solo audio (opciones: mp3, m4a, opus). Por defecto: mp3."
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        required=False,
        default='./',
        help="Carpeta de salida para el archivo descargado. Por defecto: el directorio actual."
    )

    return parser.parse_args()

def main():
    args = parse_arguments()

    download_video(
        video_url=args.url,
        resolution=args.resolution,
        audio_only=args.audio_only,
        audio_format=args.audio_format,
        output_dir=args.output_dir
    )

if __name__ == "__main__":
    main()
