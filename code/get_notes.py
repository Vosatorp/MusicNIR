import time

import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

# настройки звуковой карты и микрофона
sample_rate = 44100
block_size = 1024
mic_device_id = sd.default.device[0]

# настройки спектрограммы
fft_size = 2048
hop_size = block_size // 2

# вычисляем частоты, соответствующие каждой строке в спектрограмме
freqs = np.fft.rfftfreq(fft_size, d=1/sample_rate)[:fft_size//2+1]

# функция, которая будет вызываться при получении нового блока аудио-сигнала
def callback(indata, frames, time, status):
    # вычисляем спектр сигнала
    magnitude = np.abs(np.fft.rfft(indata[:, 0], n=fft_size))
    magnitude = 20 * np.log10(magnitude / np.max(magnitude))

    # обновляем спектрограмму
    specgram.set_data(np.hstack((specgram.get_array(), magnitude.reshape((-1, 1)))))

    # находим индекс строки с максимальной энергией по оси частот для каждого столбца (момента времени)
    max_row_indexes = np.argmax(specgram.get_array(), axis=0)

    # вычисляем частоты, соответствующие максимальной энергии в каждый момент времени
    max_freqs = freqs[max_row_indexes]

    # выводим информацию о частоте, соответствующей максимальной энергии в текущий момент времени
    print(f"Max frequency: {max_freqs[-1]:.2f} Hz")

    # обновляем график
    plt.draw()

# создаем график и спектрограмму
fig, ax = plt.subplots()
specgram = ax.imshow(np.zeros((fft_size // 2 + 1, 1)), aspect='auto', origin='lower',
                     extent=[0, block_size/sample_rate, 0, sample_rate/2], cmap='jet')
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')

# запускаем запись с микрофона
with sd.InputStream(device=mic_device_id, channels=1, samplerate=sample_rate,
                     blocksize=block_size, callback=callback):
    plt.show()
