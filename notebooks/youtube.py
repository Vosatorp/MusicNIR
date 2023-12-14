from pytube import YouTube
import moviepy.editor as mp
import os

# список ссылок на видео
links = [
    # 'https://youtu.be/W9RCD7gML8o',  # Демоны
    # 'https://youtu.be/oNr5-rQnhiM',  # Habibati
    # 'https://youtu.be/EaLFJbAlnds',  #
    # 'https://youtu.be/QkNnWHIjHOM',  # Нон-стоп
    # 'https://youtu.be/MoM6FFPw-4c',  # Типичная вечеринка с бассейном
    # 'https://youtu.be/kPkft7RLX9s',  # Контракт
    # 'https://youtu.be/i7o5erke_iU',  # Супермаркет
    # 'https://youtu.be/RB-RcX5DS5A',  # Scientist
    # 'https://youtu.be/bIssr5UumZU',  # Ne Angel Lizer
    'https://youtu.be/yKNxeF4KMsY',  # Colplay - Yellow
]

# создаем папку tracks, если её нет
if not os.path.exists('tracks'):
    os.makedirs('tracks')


def create_audio(link):
    try:
        yt = YouTube(link)

        # находим лучшее качество аудио
        audio = yt.streams.filter(only_audio=True).first()

        # скачиваем аудио в формате mp4
        filepath = audio.download()

        # конвертируем в mp3 и удаляем оригинальный файл
        mp.AudioFileClip(filepath).write_audiofile(f"tracks/{yt.title}.mp3")
        os.remove(filepath)

        print(f"{yt.title} успешно скачан")
    except Exception as e:
        print(f"Не удалось скачать {link}: {e}")


# проходим по каждой ссылке
for link in links:
    create_audio(link)
