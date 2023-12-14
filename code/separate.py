import torch
import demucs
import soundfile as sf
import numpy as np

# Загружаем модель Demucs
model = demucs.pretrained.DEMUCS_SEPARATE_STEMS_4()

# Загружаем аудиофайл
audio, sr = sf.read('input_track.mp3')

# Разделяем трек на 4 аудиодорожки
sources = model.separate(torch.from_numpy(audio).unsqueeze(0)).squeeze(0).detach().cpu().numpy()

# Сохраняем аудиофайлы каждой дорожки
sf.write('output_piano.wav', sources[0], sr)
sf.write('output_vocal.wav', sources[1], sr)
sf.write('output_bass.wav', sources[2], sr)
sf.write('output_drums.wav', sources[3], sr)
