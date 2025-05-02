import whisper
import json

model = whisper.load_model("medium")  # ou "large"

def transcrever(filename="1.wav"):
    print('\n')

    try: 
        result = model.transcribe(filename, word_timestamps=True)
        
        palavras = []
        for segmento in result["segments"]:
            for palavra in segmento["words"]:
                palavras.append({
                    "palavra": palavra["word"].strip(),
                    "tempo": round(palavra["start"], 3)  # em segundos
                })

        print(json.dumps(palavras, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"❌ Não foi possível transcrever.\nErro: {e}")


transcrever()
