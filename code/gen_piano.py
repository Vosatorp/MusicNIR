from pyo import *

# Создание сервера Pyo
s = Server().boot()

# Установка частоты дискретизации
s.setSamplingRate(44100)

# Создание объекта MidiTable для чтения MIDI-нот
midi = MidiTable()

# Создание объекта Piano для синтеза звука пианино
piano = Piano(midi, mul=0.3).out()

# Генерация рандомной мелодии из MIDI-нот
notes = [60, 62, 64, 65, 67, 69, 71]
durations = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

for i in range(8):
    note = random.choice(notes)
    duration = random.choice(durations)
    midi.note = note
    midi.velocity = 100
    midi.time = 0
    midi.play()

    # Задержка перед проигрыванием следующей ноты
    s.sleep(duration)

# Остановка сервера Pyo
s.stop()
