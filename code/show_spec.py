import os
import pdb

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice as sd


def get_max_energy_freqs(y, sr, window=15):
    S = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
    max_energy_index = np.argmax(S_db, axis=0)
    # /Users/vosatorp/miniconda3/envs/xch/lib/python3.9/site-packages/librosa/core/spectrum.py:256: UserWarning: n_fft=2048 is too large for input signal of length=1
    #   warnings.warn(
    # How to fix this warning?
    n_fft = 2048  # librosa.util.next_power_of_two(S.shape[0])
    max_energy_freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    max_energy_freqs = max_energy_freqs[max_energy_index]
    max_energy_freqs = scipy.signal.medfilt(max_energy_freqs, kernel_size=window)
    return max_energy_freqs


# make function get_fund_freqs
def get_fund_freqs(y, sr, window=15):
    # определение массива фундаментальных частот и массива времени
    frequencies, times = librosa.piptrack(y=y, sr=sr)
    # получение индекса максимальной фундаментальной частоты по времени
    fund_freq_idx = frequencies.argmax(axis=0)
    fund_freqs = frequencies[fund_freq_idx, np.arange(fund_freq_idx.size)]
    # получение фундаментальной частоты по индексу и времени
    fund_freqs = scipy.signal.medfilt(fund_freqs, kernel_size=window)
    return fund_freqs


def show_spec(y, sr, file_path, subdir, filename, window=15):
    S = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    max_energy_freqs = get_max_energy_freqs(y, sr, window=window)
    fund_freqs = get_fund_freqs(y, sr, window=window)

    # Plot spectrogram and maximum energy frequency
    fig, ax = plt.subplots(nrows=2, sharex=True, figsize=(12, 6))
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log', ax=ax[0])
    ax[0].set(title=file_path)
    ax[0].label_outer()
    ax[1].plot(librosa.times_like(max_energy_freqs), max_energy_freqs, label='max energy frequency')
    ax[1].set_yscale('log')  # установка логарифмической шкалы для оси игрек
    ax[1].plot(librosa.times_like(fund_freqs), fund_freqs, label='fund freqs from librosa')
    ax[1].legend()

    new_subdir = os.path.join('figures', subdir)
    if not os.path.exists(new_subdir):
        os.makedirs(new_subdir)
    plt.savefig(os.path.join(new_subdir, f'{os.path.splitext(filename)[0]}.png'), bbox_inches='tight', format='png')
    plt.close()


def show_demucs_separated():
    # Папка с аудиофайлами
    # audio_folder = "separated/htdemucs"
    audio_folder = "demucs_separated/mdx_extra"
    # Проходимся по всем файлам в папке
    # pdb.set_trace()
    for subdir in os.listdir(audio_folder):
        print(subdir)
        res = input("Получать картинки из этого файла?\n>>> ")
        if res:
            for filename in os.listdir(os.path.join(audio_folder, subdir)):
                # Получаем путь к файлу
                file_path = os.path.join(audio_folder, subdir, filename)

                # Загружаем аудиофайл и вычисляем его спектрограмму
                samepls, sr = librosa.load(file_path)
                show_spec(samepls, sr, file_path, subdir, filename)
                # show_fundamental_frequency(subdir, filename)

show_demucs_separated()

# sr = 22050  # Частота дискретизации
#
# filename = input('Введите имя аудио-файла или нажмите Enter чтобы записать аудиопоток\n')
# duration = int(input('Введите длительность аудио-файла в секундах\n'))
# if not filename:
#     # Получаем аудио-поток и дискретизацию
#     samples = sd.rec(int(duration * sr), samplerate=sr, channels=1)[:, 0]
#     sd.wait()  # Ждем, пока запись закончится
#     file_path = 'online'
# else:
#     samples, sr = librosa.load(filename)
#     samples = samples[:int(duration * sr)]
#     file_path = filename
#
# show_spec(samples, sr, file_path)
