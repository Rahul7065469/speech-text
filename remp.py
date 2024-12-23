
 
import speech_recognition as sr
import pyttsx3


def text_to_audio(audio):
    engine = pyttsx3.init()
    rate=engine.getProperty("rate")
    voices = engine.getProperty("voices")
    volume =engine.getProperty("volume")

    engine.setProperty("volumw",0.5)
    engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate",150)
    engine.say(audio)
    engine.runAndWait()



while True:

    r = sr.Recognizer()

    with sr.Microphone() as data:
        try:
            print("say somthing:")
            audio = r.listen(data,timeout=120,phrase_time_limit=2.5)
            audio = r.recognize_google(audio)
            print("finish")
            print(f"you siad:{audio}")

            text_to_audio(audio)
        except:
            print("unable to recognize")
        input1= input("want to do again: (Y/N): ")
        input1 = input1.upper()
        print(input1)
        if input1 == "N":
            break


   