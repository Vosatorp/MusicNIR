import os
import subprocess

# Путь к папке с треками
tracks_folder = 'tracks'

# Получаем список всех файлов в папке tracks
track_files = os.listdir(tracks_folder)

# Итерируемся по файлам и вызываем команду Demucs для каждого файла
for track_file in track_files:
    # Фильтруем файлы, оставляя только mp3 файлы
    if track_file.endswith('.mp3'):
        # track_file = track_file.replace(" ", "_")
        print('track_file', track_file)
        # Составляем команду для вызова Demucs
        command = f""" python3 -m demucs -d cpu "{tracks_folder}/{track_file}" """

        # Вызываем команду в терминале
        subprocess.run(command, shell=True)
