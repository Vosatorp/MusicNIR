from pytube import YouTube
import moviepy.editor as mp
import os

# список ссылок на видео
links = [
    # 'https://youtu.be/W9RCD7gML8o',  # Демоны
    # 'https://youtu.be/oNr5-rQnhiM',  # Habibati
    # 'https://youtu.be/QkNnWHIjHOM',  # Нон-стоп
    # 'https://youtu.be/MoM6FFPw-4c',  # Типичная вечеринка с бассейном
    # 'https://youtu.be/kPkft7RLX9s',  # Контракт
    # 'https://youtu.be/i7o5erke_iU',  # Супермаркет
    # 'https://youtu.be/RB-RcX5DS5A',  # Scientist
    # 'https://youtu.be/bIssr5UumZU',  # Ne Angel Lizer
    # 'https://youtu.be/yKNxeF4KMsY',  # Colplay - Yellow
    # 'https://youtu.be/83RUhxsfLWs?si=AJMyAxSm61-lMeYp',  # NEFFEX - Grateful
    # 'https://youtu.be/kXYiU_JCYtU?si=Fs8FZA6Odxv0YP8k',  # Linkin Park - Numb
    'https://youtu.be/k7UuSWRSEHA?si=lNPFKvTru1XUd2pD',  # Ed Sheeran - Bad Habits | Piano Cover by Pianella Piano
]

if not os.path.exists('tracks'):
    os.makedirs('tracks')

def create_audio(link):
    try:
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first()
        filepath = audio.download()  # скачивание в формате mp4
        mp.AudioFileClip(filepath).write_audiofile(f"tracks/{yt.title}.mp3")  # конвертация в mp3
        os.remove(filepath)  # удаляем оригинальный файл
        print(f"{yt.title} успешно скачан")
    except Exception as e:
        print(f"Не удалось скачать {link}: {e}")

# проходим по каждой ссылке
for link in links:
    create_audio(link)
