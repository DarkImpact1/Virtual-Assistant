import pyttsx3 as py#--- for sending mail
import datetime as dt  # to extract date and rime

import speech_recognition as sp # for speech recognition
import wikipedia as wp
import webbrowser as wb
import os
import random as rn
import smtplib as st
import functions as func

machine = py.init('sapi5')
voices = machine.getProperty("voices")
machine.setProperty('voice',voices[0].id)# setting male voice to change it in female voice replace 0 by 1
voice_add=0
name=""


if __name__ == "__main__":
    func.wishme()
    start = True
    while start:
        query  = func.takeorder().lower()
        if "wikipedia" in query:
            func.speak("here's what I got from wikipedia ")
            query = query.replace("wikipedia","")
            result = wp.summary(query, sentences = 2)
            func.speak("According to wikipedia")
            func.speak(result)
        elif "wish me in" in query:
            func.wishme()

        elif "open youtube" in query:
            you = wb.open("youtube.com",2)
        elif "fuck" in query:
            func.speak("Being an honourable person, You should not abuse")
        
        elif "open google" in query:
            goo = wb.open("google.com",2)

        elif "open github" in query:
            git = wb.open("github.com",2)

        elif "open linkedin" in query:
            link = wb.open("linkedin.com",2)

        elif "music online" in query:
            gana = wb.open("gaana.com",2)

        elif "play music offline" in query:
            music_dir = "D:\\MUSIC"  
            songs = os.listdir(music_dir)
            if len(songs) == 0:
                func.speak("Sorry! You don't have any song on your PC")
            else:
                os.startfile(os.path.join(music_dir,songs[rn.randint(0,len(songs))])) 


        elif "close music" in query:
            os.close(os.path.join("D\\MUSIC",))
        elif "time" in query:
            time = dt.datetime.now().strftime("%H:%M:%S")
            func.speak(f"sir, The time is {time}")

        elif "screenshot" in query:
            os.startfile(("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Snipping Tool.lnk"))

        elif "thank you" in query:
            reply=["you welcome!","welcome whole Heartedly","My pleasure","I'm glad to help you",]
            func.speak(reply[rn.randint(0,len(reply)-1)])

        elif "vs code" in query:
            codepath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif "send email" in query:
            func.speak("Whom you want to send an an email")
            to = func.takeorder()
            func.speak("tell me the message to be sent")
            content = func.takeorder()
            func.speak("sending.... please wait!")
            func.sendemail(to,content)
            func.speak(f" sir, email sent to {to}")

# --------------------- changeing ai ----------------------------------------

        elif ("switch to female" in query) or ("female" in query):
            func.speak("switching to female")
            machine.setProperty('voice',voices[1].id)
            voice_add=1
            func.speak("Hello sir, I'm here to help you ")

        elif ("switch to male" in query ) or ("male ai" in query):
            machine.setProperty('voice',voices[0].id)
            voice_add=0
            func.speak("Hello sir, I'm here to help you ")


        elif "change your name" in query:
            func.speak("what do want to call me?")
            ainame = func.takeorder()
            func.changeAIname(ainame)

        elif "your name" in query:
            func.yourname()

        elif "change my name" in query:
            func.speak("What should I call you ?")
            name = func.takeorder()
            func.changemyname(name)

        elif "my name" in query:
            func.myname(name)
        
        elif "mata" in query:
            func.speak("Hello, Mai tumhari mata bol rhi hu")
            func.speak("Aur beta kaise ho?")

        elif "wait" in query or ("next command " in query):
            func.speak("Ok sir, I'm waitting")
            


        elif ("quit" in query) or ("exit" in query) or ("bye" in query) or ("good bye in query"):
            func.speak("Good bye sir, ... It was nice to meet you ")
            start = False
        
