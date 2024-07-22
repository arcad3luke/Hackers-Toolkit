import sys

import pyttsx3
import os
import datetime
import speech_recognition as sr
from random import choice
import utils
import SwipeDown.SwipeDown.Menu.menu as online

USERNAME = os.getenv('USER')
BOTNAME = os.getenv('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices)

def speak(text):
    """Used to speak whatever is pass to it."""
    engine.say(text)
    engine.runAndWait()

def greetUser():

    """Greets according to time."""

    time = datetime.datetime.now()
    current_hour = time.hour
    if 6 >= current_hour <= 12:
        speak(f'Good Morning {USERNAME}! How may I be of assistance?')
    elif 12 >= current_hour <= 16:
        speak(f'Good Afternoon {USERNAME}! How may I be of assistance?')
    elif 16 >= current_hour <= 19:
        speak(f'Good Evening {USERNAME}! How may I be of assistance?')
    elif 19 >= current_hour <= 6:
        speak(f'Up late are we, {USERNAME}? How may I be of assistance?')
    else:
        print('What\'s the time?')

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        if not 'exit', 'stop', 'ok' in query:
            speak(choice(utils.opening_text))
            online.display_menu()
        else:
            current_hour = datetime.datetime.now().hour
            if 21 >= current_hour < 6:
                speak('Good night sire, take care!')
            else:
                speak('Have a good one sire!')
            sys.exit()
    except NotImplementedError:
        print(0)
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'

greetUser()
take_user_input()