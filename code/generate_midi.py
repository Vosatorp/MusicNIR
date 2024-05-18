import random

import pretty_midi
from pydub import AudioSegment

# from pydub.generators import FluidSynth

def create_piano_sound():
    piano = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Acoustic Grand Piano'))
    for note_number in range(21, 109):  # Диапазон нот пианино (от A0 до C8)
        note = pretty_midi.Note(
            velocity=100,  # Сила звука ноты (от 0 до 127)
            pitch=note_number,
            start=0,
            end=0.5  # Длительность ноты (в секундах)
        )
        piano.notes.append(note)
    return piano

# Генерация случайной мелодии на пианино
midi_data = pretty_midi.PrettyMIDI()
piano = create_piano_sound()

for _ in range(16):
    note_number = random.randint(60, 71)  # Генерация случайной ноты (от C4 до B4)
    note = pretty_midi.Note(
        velocity=100,
        pitch=note_number,
        start=0.5,
        end=1.0
    )
    piano.notes.append(note)

midi_data.instruments.append(piano)

# Сохранение MIDI-файла
midi_data.write("random_piano_melody.mid")

# Преобразование MIDI в аудио WAV с помощью FluidSynth
soundfont = "path/to/soundfont.sf2"  # Путь к SoundFont файлу (набор звуковых данных)
# midi_audio = FluidSynth(soundfont).midi_to_audio("random_piano_melody.mid")

# Сохранение аудиофайла WAV
# output_file = "output_audio.wav"
# midi_audio.export(output_file, format="wav")
