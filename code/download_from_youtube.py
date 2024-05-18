import os

import moviepy.editor as mp
from pytube import YouTube

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
    # 'https://youtu.be/k7UuSWRSEHA?si=lNPFKvTru1XUd2pD',  # Ed Sheeran - Bad Habits | Piano Cover by Pianella Piano
    'https://youtu.be/5jGhAD7UWT4?si=JU3T9cuxlhXUYxKT',  # Отпускай
    'https://youtu.be/6cHVdvRoJ2w?si=IhLl7Hx0DazNLwSo',  # Буду твоим песиком
    'https://youtu.be/Sm4riYkjBz4?si=Jb8sTdjcxCzrOjZ2',  # Три дня дождя — Если я умру
    'https://youtu.be/8DmQOoSAV98?si=HEBTOIxXgseNTDa8',  # Три дня дождя - Беги от меня
    'https://youtu.be/0haP_owHzvw?si=QJeagv-54JFG1Vg9',  # Три дня дождя & Zivert - Выдыхай
    'https://youtu.be/sXTVRVMAkdY?si=2B3uv-ijAmnXd5Iq',  # Три дня дождя, lowlife - Траблы
    'https://youtu.be/ZpKiC5kbOis?si=b_Li_a1tOD1KmrWG',  # Самый лучший день
    'https://youtu.be/w1TT8D3RuOk?si=HI2axdcKY2Q7Bv4M',  # Три дня дождя, polnalyubvi — Температура
    'https://youtu.be/a7t4sLDYsHM?si=dvE3RvR8vYfOM2B0',  # Три дня дождя, МУККА — Вода
    'https://youtu.be/6J0G56lpB8k?si=TCzve2s28KoVfa6t',  # тринадцать карат - останови меня
    'https://youtu.be/HFA-GrJMU9c?si=ijU_3dJ2-JIQQTmo',  # ПОШЛАЯ МОЛЛИ - КЛЕОПАТРИ
    'https://youtu.be/h2TwTAwBTLs?si=dHRL_yW4-qpsKFnD',  # Три дня дождя — Кристаллические лярвы
    'https://youtu.be/mEOT3TuUW3Y?si=0xoRMPaZUu5fULDZ',  # Три дня дождя — За край
    'https://youtu.be/g0K3TUAfRjU?si=hWkKohlc8wcuABKq',  # Все хотят меня поцеловать
    'https://youtu.be/ogeP8z5lwYo?si=h9f6FwsE9pZRUCPF',  # ПОШЛАЯ МОЛЛИ - ДАЖЕ МОЯ БЭЙБИ НЕ ЗНАЕТ
    'https://youtu.be/2-cdoPBMH4w?si=Y2uiumWRsLWejStV',  # баночка с окурками
    'https://youtu.be/zY7yvZcZIoE?si=A-APOk925iucSL3Z',  # PYROKINESIS,МУККА- Днями-ночами
    'https://youtu.be/dMCkMh25AYI?si=n0RZovchxOBOsVnW',  # DROWNING
    'https://youtu.be/ryotss9iX4U?si=x_eNsgyUIVGnFKKL',  # ATL - Танцуйте
    'https://youtu.be/oGpIJTYGzLk?si=OVmX-Xt1u4BC2uVN',  # NEFFEX - Till I'm On Top
    'https://youtu.be/wOBnq0Ewz5k?si=-12t_dqDu_tMWvNS',  # Feduk & Allj - Розовое вино
    'https://youtu.be/hgyVG_rHl5g?si=-EyQvVWhmoeR7l6F',  # ЛСП - Белый танец
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
