import speech_recognition as sr
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio= recognizer.listen(source)
        try:
            voice_data = recognizer.recognize_google(audio)
            print(f"you said : {voice_data}")
            return str(voice_data)
        except sr.UnknownValueError:
            print("sorry, I could not understand. please try agian")
            return""