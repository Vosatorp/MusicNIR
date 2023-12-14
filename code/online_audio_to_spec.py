import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import sounddevice as sd

# Задаем параметры для записи аудио
sr = 44100  # Частота дискретизации

filename = input('Введите имя аудио-файла или нажмите Enter чтобы записать аудиопоток\n')
duration = int(input('Введите длительность аудио-файла в секундах\n'))
if not filename:
    # Получаем аудио-поток и дискретизацию
    samples = sd.rec(int(duration * sr), samplerate=sr, channels=1)
    sd.wait()  # Ждем, пока запись закончится
else:
    samples, sr = librosa.load(filename)

# Преобразуем поток в формат numpy array и извлекаем признаки
y = np.squeeze(samples)
D = librosa.stft(y)
D_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# Отображаем спектрограмму
plt.figure(figsize=(12, 4))
librosa.display.specshow(D_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()
plt.tight_layout()
plt.show()