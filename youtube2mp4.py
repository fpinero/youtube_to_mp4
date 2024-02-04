from pytube import YouTube
import os


def solicitar_carpeta_destino():
    return input("Por favor, ingresa la carpeta destino para el vídeo: ")


def solicitar_url_video():
    return input("Por favor, ingresa la URL del vídeo de YouTube: ")


def mostrar_resoluciones_disponibles(streams):
    # Filtrar streams que contienen solo vídeo (sin audio)
    video_streams = streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc()

    # Mostrar las tres mejores resoluciones
    print("Resoluciones disponibles:")
    for i, stream in enumerate(video_streams[:3], start=1):
        print(f"{i}) {stream.resolution}")

    # Solicitar al usuario que elija una resolución
    seleccion = int(input("Elige la resolución para descargar (1, 2, 3): "))
    return video_streams[seleccion - 1]


def descargar_video(stream, carpeta_destino):
    # Asegurarse de que la carpeta de destino existe
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Descargar el vídeo
    stream.download(output_path=carpeta_destino)
    print("Vídeo descargado exitosamente.")


def main():
    carpeta_destino = solicitar_carpeta_destino()
    url = solicitar_url_video()

    yt = YouTube(url)
    stream_seleccionado = mostrar_resoluciones_disponibles(yt.streams)
    descargar_video(stream_seleccionado, carpeta_destino)


if __name__ == "__main__":
    main()
