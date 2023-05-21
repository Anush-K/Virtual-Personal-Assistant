import pyttsx3
from decouple import config #User and VA
from datetime import datetime #Greet

import speech_recognition as sprg
from random import choice
from utils import working_text,thank_you,no_query

USERNAME = config('USER')
Vir_Asst = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 150)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#TextToSpeech
def speak(text): #To speak Text passed to it
    engine.say(text)
    engine.runAndWait()


#Greet
def greet_user():  #To Greets user
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour <=23):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {Vir_Asst}. How may I assist you?")

#Speech Recognition
def take_user_input(): #User input recognised and converted to text by Speech Recognition module
    r = sprg.Recognizer()
    with sprg.Microphone() as source:
        print('Listening....')
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source, duration=1)  
        r.dynamic_energy_threshold = True  
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not ('exit' in query or 'stop' in query or 'thanks' in query or 'thank you' in query):
            speak(choice(working_text))
        else:
            if ('thanks' in query or 'thank you' in query):
                speak(choice(thank_you))
            elif ('exit' in query or 'stop' in query):
                hour = datetime.now().hour
                if hour >= 21 or hour < 4:
                    speak(f"Good night {USERNAME}")
                else:
                    speak(f'Have a good day {USERNAME}!')
                exit()
            elif ('no query' in query):
                speak(choice(no_query))
    except Exception:
        speak('Sorry, I am not able to understand that. Could you please say that again?')
        query = 'no query'
    return query
