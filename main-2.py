from gtts import gTTS
import smtplib
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os, sys, subprocess
import random
import wikipedia
import wikipediaapi
from instabot import Bot
import shutil
from voiceBiometrics import authenticate_user
from interface import speak

# Setting up pyttsx3 for Windows
if sys.platform != 'darwin':
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)  # Female voice. To switch to female voice, use: voice[0].id


if __name__ == "__main__":

    speak("Hello how are you today? I am your virtual assistant")

    authenticated = authenticate_user()
    if authenticated:
        print("You are authorized!")
        speak("You are authorized!")
        #if authorized start interacting and launch voice assistant
        exec(open(f"interface.py").read())
    else:
        print("Unauthorized !!")
        speak("You are unauthorized")
