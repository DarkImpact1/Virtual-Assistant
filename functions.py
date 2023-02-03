import pyttsx3 as py
import datetime as dt
import speech_recognition as sp
import wikipedia as wp
import webbrowser as wb
import os
import random as rn
import smtplib as st
import functions as func


machine = py.init('sapi5')
voices = machine.getProperty("voices")
machine.setProperty('voice',voices[0].id)# setting male voice to change it in female voice replace 0 by 1
new_voice_address = 0

def takeorder():
    recogniser = sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening ......")
        recogniser.pause_threshold = 1
        recogniser.energy_threshold= 300
        audio = recogniser.listen(source)

    try:
        print("Recognizing...")
        query = recogniser.recognize_google(audio, language = "en-in")
        print(f"User said: {query}\n")

    except:
        print("say that again please...")
        return "none"
    return query

def speak(audio):
    machine.say(audio)
    machine.runAndWait()

def yourname(name):
    speak("My name is " + voices[new_voice_address].name)

def gender(voice_address):
    
    if voice_address == 0:
        speak("switching.... to female")
        new_voice_address = 1
    else:
        speak("switching to male ")
        new_voice_address = 0

    machine.setProperty("voice", voices[new_voice_address].id)
    speak("Hello sir, how may I help you ?")
    return new_voice_address

    
        # elif ("switch to female" in query) or ("female" in query):
        #     func.speak("switching to female")
        #     machine.setProperty('voice',voices[1].id)
        #     voice_add=1
        #     func.speak("Hello sir, I'm here to help you ")

        # elif ("switch to male" in query ) or ("male ai" in query):
        #     machine.setProperty('voice',voices[0].id)
        #     voice_add=0
        #     func.speak("Hello sir, I'm here to help you ")





def changeAIname(ainame):
    speak(f"OK, I'll remember {ainame} is my name")
    voices[new_voice_address].name=ainame
    return voices[new_voice_address].name

def myname(name):
    if len(name)==0:
        speak("Sorry! You didn't tell me your name but I will remember if you tell me your name ")
        speak("What is your name ?")
        name = takeorder()
        speak(f"I'll remember {name} is your name")
        name = name
        return name
    else:
        speak(f"Your name is {name}")
    

def changemyname(name):
    speak(f"Ok, now I'll remember your name is {name}")

def wishme():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!?")
    elif hour >= 12 and hour <=19:
        speak("Good Afternoon sir!?")
    else:
        speak("Good evening sir! ")

    speak("I'm Your assistant!")
    speak("How may I help you?")

def sendemail(to,content):
    try:
        server = st.SMTP('smtp@gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('ananonymousking1@gmail.com',"#@Anonymous1")
        server.sendmail('ananonymousking1@gmail.com',to,content)
        server.close()
    except Exception as e:
        print(e)
        speak("Sorry bhai, can't send an email to the address")


