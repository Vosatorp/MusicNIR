import sys
import librosa
import sounddevice as sd

# from audio_to_midi.monophonic import wave_to_midi
from sound_to_midi import wave_to_midi

sr = 22050  # Частота дискретизации

filename = input('Введите имя аудио-файла или нажмите Enter чтобы записать аудиопоток\n')
duration = int(input('Введите длительность аудио-файла в секундах\n'))
if not filename:
    # Получаем аудио-поток и дискретизацию
    samples = sd.rec(int(duration * sr), samplerate=sr, channels=1)[:, 0]
    sd.wait()  # Ждем, пока запись закончится
    file_path = 'online'
else:
    samples, sr = librosa.load(filename)
    samples = samples[:int(duration * sr)]
    file_path = filename

print("Starting...")
# file_in = sys.argv[1]
# file_in = "tracks/Adelya - сентябрь.m4a"
file_out = "output.mid"
# y, sr = librosa.load(file_in, sr=None)
print("Audio file loaded!")
midi = wave_to_midi(samples)  # , sr=sr)
print("Conversion finished!")
with open(file_out, 'wb') as f:
    midi.writeFile(f)
print("Done. Exiting!")
# Запись в файл
with open(file_out, "wb") as outf:
    midi.writeFile(outf)
