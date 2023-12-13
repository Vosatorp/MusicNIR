# Generating the contents for requirements.txt and install_dependencies.sh

# Contents for requirements.txt
requirements_txt = "\n".join([
    "scikits.audiolab",
    "torch==1.7.1",
    # Assuming the user will handle the local wheel file
    "git+https://github.com/FelixGSE/pypiano.git",
    "virtualenv",
    "sound_to_midi",
    "pydub",
    "python_speech_features",
    "pypiano",
    "yandex-music",
    "librosa",
    "mido[backends]",
    "timm",
    "mido",
    "pytube==12.1.3",
    "bytesep==0.1.1",
    "pretty_midi",
    # Assuming the user will handle the second local wheel file
    "audio-to-midi",
    "miditoolkit==0.1.13",
    "git+https://github.com/openai/whisper.git",
    "transformers",
    "crepe",
    "onnxruntime",
    "fluidsynth"
])

# Contents for install_dependencies.sh
install_dependencies_sh = "#!/bin/bash\nsudo apt-get install timidity"

# Saving the contents to files
requirements_txt_path = 'requirements.txt'
install_dependencies_sh_path = 'install_dependencies.sh'

with open(requirements_txt_path, 'w') as file:
    file.write(requirements_txt)

with open(install_dependencies_sh_path, 'w') as file:
    file.write(install_dependencies_sh)
