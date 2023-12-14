import crepe
import numpy as np
import matplotlib.pyplot as plt
import librosa

filename = 'audio_file.wav'
filename = 'otpuskai-tri-dnya-dozdya-slowed-and-reverb.mp3'
y, sr = librosa.load(filename)
y = y[:220_500]

print(type(y), y.shape, sr)
print('DEBUG')
print(help(crepe))
time, frequency, confidence, activation = crepe.predict(y[:100], sr, viterbi=True)
print('time', time.shape, time)
notes = librosa.hz_to_midi(frequency)

plt.plot(time, notes)
plt.xlabel('Time (s)')
plt.ylabel('Note')
plt.show()

import pretty_midi

# Создаем миди-файл с одним инструментом
midi_data = pretty_midi.PrettyMIDI()
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

# Считываем последовательность нот и добавляем их в миди-файл
notes = [('C', 0.5), ('D', 1.0), ('E', 0.5), ('F', 0.5)]
for i, (note_name, duration) in enumerate(notes):
    start_time = i
    end_time = start_time + duration
    note_number = pretty_midi.note_name_to_number(note_name)
    note = pretty_midi.Note(
        velocity=100,
        pitch=note_number,
        start=start_time,
        end=end_time
    )
    piano.notes.append(note)

# Добавляем инструмент в миди-файл и сохраняем его
midi_data.instruments.append(piano)
midi_data.write('output.mid')

