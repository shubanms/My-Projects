import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import webbrowser
import time
import random
import pywhatkit as pt

time = time.strftime("%M minutes past %I")

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate" , 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

url1 = 'youtube.com'
url2 = "gmail.com"
url3 = "github.com"
url6 = "primevideo.com"
url7 = "https://www.youtube.com/watch?v=IBFYsXhEQxc"
url5="https://www.youtube.com/watch?v=65OIWqsWoMw&list=PLc4jl5sV4zXQROG5dfv1aeeS3oy48olmH"
url9="https://cghs.nic.in/orsh"

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

engine.say("Hello shuban")
engine.say("Is there any work for me today")
engine.runAndWait()

def Listen():
    try:
        with sr.Microphone() as source:
            engine.say("i am listening sir")
            engine.runAndWait()
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()          
            if 'youtube' in command:
                webbrowser.get('chrome').open_new_tab(url1)         
            elif 'song' in command:
                engine.say("What kind of song do you want to listen to now?")
                engine.runAndWait()
                print("listening")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'anything' in command:
                    engine.say("ok sir playing a song")
                    engine.runAndWait()
                    webbrowser.get('chrome').open_new_tab(url7)
                elif 'playlist' in command:
                    engine.say("Here you go sir")
                    engine.runAndWait()
                    webbrowser.get('chrome').open_new_tab(url5)
                else:
                    engine.say("ok sir, then what do you want me to do?")
                    engine.runAndWait()
                    listen()      
            elif 'mail' in command:
                engine.say("checking for new mails sir")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab(url2)
                Listen()   
            elif 'time' in command:
                engine.say("The time is" + time)
                engine.runAndWait()
                engine.say("anything else sir")
                engine.runAndWait()
                Listen()
            elif 'nothing' in command:
                engine.say("Ok, have a good day")
                engine.runAndWait()
            elif 'movie' in command:
                engine.say("ok sir, opening amazon prime video")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab(url6)
            elif 'appointment' in command:
                engine.say("Opening cghs website")
                engine.runAndWait()
                webbrowser.get('chrome').open_new_tab(url9)
            elif 'message' in command:
                
                '''pt.sendwhatmsg("+919845515244", "Message sent by a bot!", 21, 36)'''
            else:
                engine.say("I am not sure i quite understand that sir")
                '''engine.say("could you repeat that")'''
                engine.runAndWait()
                Listen()
    except:
        engine.say("I am not sure i quite understand that sir")

while True:
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hello' in command:
                Listen()
            else:
                pass
    except:
        engine.say("I am not sure i quite understand that sir")























