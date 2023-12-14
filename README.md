.. |test| |codecov| |docs|

.. .. |test| image:: https://github.com/gregkseno/master-thesis/workflows/test/badge.svg
..    :target: https://github.com/gregkseno/master-thesis/tree/master
..    :alt: Test status
    
.. .. |codecov| image:: https://img.shields.io/codecov/c/github/intsystems/ProjectTemplate/master
..    :target: https://app.codecov.io/gh/intsystems/ProjectTemplate
..    :alt: Test coverage
    
.. .. |docs| image:: https://github.com/gregkseno/master-thesis/workflows/docs/badge.svg
..    :target: https://intsystems.github.io/ProjectTemplate/
..    :alt: Docs status


.. class:: center

    :Title: Automatic Music Transcription
    :Type: Magister's Thesis
    :Author: Dmitry Protasov
    :Supervisor: Ivan Matveev


## Постановка задачи

Генеративные музыкальные модели довольно удобно строить в пространстве
MIDI-файлов. Проблема – нет большого количества таких MIDI-датасетов,
для большинства песен в интернете есть только их аудиоформат. Эту
проблему предлагается решать алгоритмом преобразования
аудио-представления песен в её MIDI-представление.

Целью работы является исследование и улучшение существующих алгоритмов извлечения MIDI из
песен

## Проведенные эксперименты

TODO: ноутбук с картинками спектрограмм получившиеся из demucs

## Usage

Install dependencies

```bash
# clone project
git clone https://github.com/Vosatorp/MusicNIR.git

# install requirements
pip install -r requirements.txt
