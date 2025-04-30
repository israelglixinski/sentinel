import whisper

model = whisper.load_model("base")  


def transcrever(filename="gravacao_sistema.wav"):
    print('\n')

    try: 
        result = model.transcribe(filename)
        print(f'{result["text"]}')
        Thread(target=lambda:traduzir(result["text"])).start()
    except: 
        print(f"Não foi possivel transcrever \n")

