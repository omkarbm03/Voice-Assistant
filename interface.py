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

global language
language = 'en-in'

# Setting up pyttsx3 for Windows
if sys.platform != 'darwin':
    engine = pyttsx3.init(driverName='sapi5')
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)  # Female voice. To switch to female voice, use: voice[0].id


def chooseLanguage():
    global language

    speak("Choose English or Hindi")
    query = takeCommand().lower()
    print(f"User chose: {query}\n")

    if 'english' in query:
        language = 'en-in'  # default language
        speak("You chose English")
    else:
        language = 'hi-In'
        speak("You chose Hindi")

    return


def open_file(filename):
    # Opens a file in Mac / Windows / Linux

    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def speak(audio):
    if sys.platform == 'darwin':
        os.system('say ' + audio)
    else:
        engine.say(audio)
        engine.runAndWait()  # Without this command, speech will not be audible to us.


def takeCommand():
    # Takes a microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # speak("Start")
        r.pause_threshold = 1
        audio = r.listen(source)

        # query = r.recognize_google(audio, language='hi-Ind')
        # print(f"User said: {query}\n")

    try:
        print("Recognizing...")
        print(f"language is: {language}")
        query = r.recognize_google(audio, language=language)  # Using Google for voice recognition
        # query = r.recognize_google(audio, language='hi-In')
        print(f"User said: {query}\n")  # User query will be printed
    except Exception as e:
        print("Say that again please...")  # In case of improper voice
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # server.login('class.email.gwu@gmail.com', 'XPalpERL')
    server.login('class.email.gwu@gmail.com', 'egzw bixl sbjb knzw')
    server.sendmail('class.email.gwu@gmail.com', to, content)
    server.close()


def move_images_last_week(src, dest):
    source_directory = f'/Users/jdo/MyDocuments/GWU/CS6221/pythonProject/{src}'

    destination_directory = f'/Users/jdo/MyDocuments/GWU/CS6221/pythonProject/{dest}'
    os.makedirs(destination_directory, exist_ok=True)

    for file in os.listdir(source_directory):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):  # Check for image files
            shutil.move(os.path.join(source_directory, file), os.path.join(destination_directory, file))


if __name__ == "__main__":

    chooseLanguage()

    new_dir_path = os.getcwd()

    if language == 'en-in':
        while True:
            # if 1:
            query = takeCommand().lower()  # Convert user query into lower case

            print(query)
            # Logic for executing tasks based on query

            if 'wikipedia' in query:
                # Query: Virginia, Thanksgiving
                # Only query that does not have "(" in results work
                # Task 1: Search something on Wikipedia

                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                # wiki_=wikipediaapi.wikipedia('en')
                # page=wikipedia.page(query)
                results = wikipedia.summary(query,
                                            sentences=2)  # fetch two sentences from the summary of the Wikipedia page
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'youtube' in query:
                # Task 2: Open YouTube site in a web-browser
                # webbrowser.open("https://www.youtube.com/")

                query = query.replace("youtube", "")
                url = "https://www.youtube.com/results?search_query={}".format(query)
                webbrowser.open(url)


            elif 'google' in query:
                # Task 3: Open Google site in a web-browser
                # webbrowser.open("https://www.google.com/")

                query = query.replace("google", "")
                url = "https://www.google.com.tr/search?q={}".format(query)
                webbrowser.open(url)

            elif 'play music' in query:
                # Task 4: Play music

                music_dir = f'{new_dir_path}/music'
                songs = os.listdir(music_dir)

                # Play a random song
                n = random.randint(0, len(songs) - 1)
                open_file(os.path.join(music_dir, songs[n]))

            elif 'the time' in query:
                # Task 5: Tell  current time
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                # Task 6: Open VS Code Program
                codePath = "/Applications/Visual Studio Code.app"
                open_file(codePath)

            elif 'email professor' in query:
                # Task 7: Send Email
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = ['thanh.chau.do.522@gmail.com', 'omkarbm03@gmail.com']
                    sendEmail(to, content)
                    speak("Email has been sent!")

                except Exception as e:

                    print(e)
                    speak("Sorry my friend, I am not able to send this email.")

            elif 'instagram message' in query:
                shutil.rmtree("./config")
                bot = Bot()
                bot.login(username="voicebot99", password="Voicebot@99")
                urer_ids = ["omkar.0_o"]
                speak("What should I say?")
                content = takeCommand()
                # text = "Hi how are you?"
                bot.send_messages(content, urer_ids)

            elif 'move images' in query:
                speak("Which folder do you want to move from")
                srcFolder = takeCommand()
                speak("Which folder do you want to move to")
                destFolder = takeCommand()
                folderName = takeCommand()
                move_images_last_week(srcFolder, destFolder)
                speak("Images are moved!")

            elif 'stop' in query:
                break

    elif language == 'hi-In':
        query = takeCommand().lower()  # Convert user query into lower case
        print(query)

        while True:
            if 'विकिपीडिया' in query:
                # Task 1: Search something on Wikipedia

                speak('विकिपीडिया खोज रहा हूँ ')
                query = query.replace("विकिपीडिया", "")
                results = wikipedia.summary(query,
                                            sentences=2)  # fetch two sentences from the summary of the Wikipedia page
                speak("विकिपीडिया के अनुसार ")
                print(results)
                speak(results)

            elif 'यूट्यूब' in query:
                # Task 2: Open YouTube site in a web-browser
                # webbrowser.open("https://www.youtube.com/")

                query = query.replace("यूट्यूब", "")
                url = "https://www.youtube.com/results?search_query={}".format(query)
                webbrowser.open(url)

            elif 'गूगल' in query:
                # Task 3: Open Google site in a web-browser
                # webbrowser.open("https://www.google.com/")
                query = query.replace("गूगल", "")
                url = "https://www.google.com.tr/search?q={}".format(query)
                webbrowser.open(url)

            elif 'संगीत बजाना' in query:
                # Task 4: Play music
                music_dir = f'/{new_dir_path}/music'
                songs = os.listdir(music_dir)

                # Play a random song
                n = random.randint(0, len(songs) - 1)
                open_file(os.path.join(music_dir, songs[n]))

            elif 'समय' in query:
                # Task 5: Tell  current time
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"{strTime}")

            elif 'कोड खोलें ' in query:
                # Task 6: Open VS Code Program
                codePath = "/Applications/Visual Studio Code.app"
                open_file(codePath)

            elif 'प्रोफेसर को ईमेल करें ' in query:
                # Task 7: Send Email
                try:
                    speak("What should I say?")
                    # speak("क्या कहूँ ")
                    content = takeCommand()
                    to = ['thanh.chau.do.522@gmail.com', 'omkarbm03@gmail.com']
                    sendEmail(to, content)
                    # speak("ईमेल भेज दिया गया है ")

                except Exception as e:
                    print(e)
                    speak("क्षमा करे मेरे मित्र , में यह ईमेल भेजने में समक्ष नई हूँ ")

            elif 'इंस्टाग्राम संदेश' in query:
                shutil.rmtree("./config")
                bot = Bot()
                bot.login(username="voicebot99", password="Voicebot@99")
                urer_ids = ["omkar.0_o"]
                speak("क्या कहुँ")
                content = takeCommand()
                # text = “हेलो, आप  कैसे है ?"
                bot.send_messages(content, urer_ids)

            elif 'रुकना' in query:
                break

