import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import ctypes
from ecapture import ecapture as ec
import requests
from bs4 import BeautifulSoup

from django.shortcuts import render,redirect


recognizer = sr.Recognizer()

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def speak(text):
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am ela. Please tell me how may I help you")
    
def home(request):
    return render(request, 'ela/home.html')

def login_page(request):
    return render(request, 'ela/login.html')

def register_page(request):
    return render(request, 'ela/register.html')

def index(request):
    
    if request.method == 'POST' and 'task' in request.POST:
        
        task = request.POST['task']
        if task == 'perform_task':
            return perform_task(request)  # Call perform_task function
    return render(request, 'ela/index.html')

def process_speech():
    with sr.Microphone() as source:
        print("listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        # print(query)
        # speak(query)
        return query
    except Exception as e:
        speak("sorry sir i did not get that")
        print(e)
        return "None"



def perform_task(request): 
        
        query = process_speech().lower()
        print(query)
        
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org") 
        elif 'who are you'in query:
              speak("i'm Ela. Your desktop voice assistant") 
              exit()

        elif 'play music' in query:
            music_dir = './ela/song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\admin\Desktop\python project\assistant.py"
            os.startfile(codePath)
        
       
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by  vaishnavi and arati.")
       
        elif 'lock window' in query:
                # speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "ELA Camera ", "img.jpg")
        elif "shutdown the system" in query:
           speak("Are You sure you want to shutdown")
           shutdown = input("Do you wish to shutdown your computer? (yes/no)")
           if shutdown == "yes":
             os.system("shutdown /s /t 1")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = process_speech()
            file = open('Note.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = process_speech()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)

            else:
                file.write(note)
         
        elif "show notes" in query:
            speak("Showing Notes")
            file = open("Note.txt", "r")
            print(file.read())
            
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
            
        # elif 'send a mail' in query:
        #     try:
        #         speak("What should I say?")
        #         content = process_speech()
        #         speak("whom should i send")
        #         to = input()   
        #         sendEmail(to, content)
        #         speak("Email has been sent !")
        #     except Exception as e:
        #         print(e)
        #         speak("I am not able to send this email")
        elif "google search" in query:
             from .SearchNow import searchGoogle
             searchGoogle(query)
        elif "youtube search" in query:
            from .SearchNow import searchYoutube
            searchYoutube(query)
        elif " wikipedia search" in query:
            from .SearchNow import searchWikipedia
            searchWikipedia(query)
        elif "temperature" in query:
            search = "temperature in Pune"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
        # elif "weather" in query:
        #    search = "weather in Pune"
        #    url = f"https://www.google.com/search?q={search}"
        #    r = requests.get(url)
        #    data = BeautifulSoup(r.text, "html.parser")
        #    weather_condition = data.find("div", class_="BNeawe").text
        #    speak(f"The current {search} is {weather_condition}")
        elif "open" in query:
             from Dictapp import openappweb
             openappweb(query)
        elif "close" in query:
             from Dictapp import closeappweb
             closeappweb(query)
        # elif "set an alarm" in query:
        #     print("input time example:- 10 hr:10 min")
        #     speak("Set the time")
        #     a = input("Please tell the time :- ")
        #     alarm(a)
        #     speak("Done,sir")
        
        # elif "pause" in query:
        #     pyautogui.press("k")
        #     speak("video paused")
        # elif "play" in query:
        #     pyautogui.press("k")
        #     speak("video played")
        # elif "mute" in query:
        #     pyautogui.press("m")
        #     speak("video muted")

        # elif "volume up" in query:
        #     from keyboard import volumeup
        #     speak("Turning volume up,sir")
        #     volumeup()
        # elif "volume down" in query:
        #     from keyboard import volumedown
        #     speak("Turning volume down, sir")
        #     volumedown()
        
        # elif "remember that" in query:
        #   rememberMessage = query.replace("remember that","")
        #   rememberMessage = query.replace("ela","")
        #   speak("You told me to remember that"+rememberMessage)
        #   remember = open("Remember.txt","a")
        #   remember.write(rememberMessage)
        #   remember.close()
        # elif "what do you remember" in query:
        #   remember = open("Remember.txt","r")
        #   speak("You told me to remember that" + remember.read())
        
        # elif "news" in query:
        #   from NewsRead import latestnews
        #   latestnews()

        # elif "calculate" in query:
        #   from Calculatenumbers import WolfRamAlpha
        #   from Calculatenumbers import Calc
        #   query = query.replace("calculate","")
        #   query = query.replace("ela","")
        #   Calc(query)
  
        # elif "search for a file" in query:
        #     speak("What file are you looking for?")
        #     query = process_speech()  
        #     search_and_open_file(query)
        # elif "screenshot" in query:
        #     import pyautogui 
        #     im = pyautogui.screenshot()
        #     im.save("ss.jpg")
        # elif "translate" in query:
        #     from Translator import translategl
        #     query = query.replace("ela","")
        #     query = query.replace("translate","")
        #     translategl(query)
        elif  'bye' in query or 'stop' in query:
             hour = int(datetime.datetime.now().hour)
             if hour >= 21 and hour < 6:
                speak("Good night, take care!")
             else:
                speak('Have a good day !,')
             exit()
        return redirect('/start')
    
    

    