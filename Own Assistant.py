import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engin=pyttsx3.init()
voices=engin.getProperty('voices')
engin.setProperty('voice', voices[1].id)

def talk(text):
    engin.say(text)
    engin.runAndWait()

def take_command():
    try:
        with sr. Microphone() as source:
            print("Listening...")
            voice= listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_hasan():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk(time)

    elif 'who is the' in command:
        person=command.replace('who is the','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Can you Please say the command again')

while True:
    run_hasan()