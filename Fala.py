import speech_recognition as Voz

Reconhecer = Voz.Recognizer()

with Voz.Microphone() as fonte:
    
    while True:
        audio = Reconhecer.listen(fonte)
        print(Reconhecer.recognize_google(audio, language='pt'))
