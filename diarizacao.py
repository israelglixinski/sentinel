from pyannote.audio import Pipeline
import os

# Substitua pelo seu token pessoal do Hugging Face
HUGGINGFACE_TOKEN = ""

# Carrega o pipeline de diarização
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=HUGGINGFACE_TOKEN)

# Caminho do arquivo de áudio (formato .wav preferido)
audio_file = "brasil2.wav"

# Executa a diarização
diarization = pipeline(audio_file)

# Exibe quem falou quando
for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{speaker} falou de {turn.start:.1f}s até {turn.end:.1f}s")
