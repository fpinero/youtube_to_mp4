import yt_dlp
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


def solicitar_carpeta_destino():
    return input("Por favor, ingresa la carpeta destino para el vídeo: ")


def solicitar_url_video():
    return input("Por favor, ingresa la URL del vídeo de YouTube: ")


def mostrar_resoluciones_disponibles(ydl, url):
    info = ydl.extract_info(url, download=False)
    formats = info['formats']
    video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') == 'none']
    video_formats.sort(key=lambda x: int(x.get('height', 0)), reverse=True)

    print("Resoluciones disponibles:")
    for i, format in enumerate(video_formats[:3], start=1):
        print(f"{i}) {format.get('height', 'Unknown')}p")

    seleccion = int(input("Elige la resolución para descargar (1, 2, 3): "))
    return video_formats[seleccion - 1]['format_id']


def descargar_video(ydl, url, format_id, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    ydl_opts = {
        'format': f'{format_id}+bestaudio/best',
        'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Vídeo descargado exitosamente.")


def main():
    carpeta_destino = solicitar_carpeta_destino()
    url = solicitar_url_video()

    ydl = yt_dlp.YoutubeDL()
    format_id = mostrar_resoluciones_disponibles(ydl, url)
    descargar_video(ydl, url, format_id, carpeta_destino)


if __name__ == "__main__":
    main()