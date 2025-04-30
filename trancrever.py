import whisper

model = whisper.load_model("base")  


def transcrever(filename="1.wav"):
    print('\n')

    try: 
        result = model.transcribe(filename)
        print(f'{result["text"]}')
    except: 
        print(f"Não foi possivel transcrever \n")



transcrever()