# MusicNIR historical research archive

Retired on 2026-10-29. Current internal research continues in
[Audio2MIDI Research](https://github.com/Vosatorp/audio2midi-difficulty-control-paper);
selected tools, cleaned notebooks and author paper/slides are preserved in
[migration PR 7](https://github.com/Vosatorp/audio2midi-difficulty-control-paper/pull/7).

This public historical repository retains its original branches, source code,
references and datasets. Complete all-ref/file backups were verified before
retirement. The original README below describes the earlier research environment,
not the current product setup. No production or model evaluation was changed.

## Original research description

# Automatic Music Transcription

**Автор:** Дмитрий Протасов

**Научный руководитель:** Иван Матвеев

## Постановка задачи

Генеративные музыкальные модели довольно удобно строить в пространстве
MIDI-файлов. Проблема – нет большого количества таких MIDI-датасетов,
для большинства песен в интернете есть только их аудиоформат. Эту
проблему предлагается решать алгоритмом преобразования
аудио-представления песен в её MIDI-представление.

Целью работы является исследование и улучшение существующих алгоритмов извлечения MIDI из
песен



## Usage

Install dependencies

```bash
# clone project
git clone https://github.com/Vosatorp/MusicNIR.git

# install requirements
pip install -r requirements.txt
