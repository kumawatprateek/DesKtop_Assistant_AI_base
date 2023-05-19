# this project is made by Prateek kumawat on destop assest on python
#============================@prateekkumawat============================#
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# text to speach and use to speak
def speak(audio):
    '''
    This funtion is use to text to speech voice given by yser
    :param audio:
    :return:
    '''
    engine.say(audio)
    engine.runAndWait()
# remander of time and wish me about time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    strtime = datetime.datetime.now().strftime("%H:%M:%S")
    if 0<= hour<= 12:
        speak("Hello sir, Good Morning!")
    elif 12< hour<18:
        speak("hello sir, Good Afternoon!")
    elif 18<= hour <=19:
        speak("Hello sir, Good Evening!")
    else :
        speak("Good Night! Sir.")
    speak(f"Sir the time is {strtime}")
    speak("I am Tiger sir, Please tell me How may I help you ?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tiger is Listening...")
        r.pause_threshold = 1
        #audio = r.listen(source)
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        # here is all oprations
        if 'wikipedia' in query:# wikipedia oparation
            speak('Searching wikipedia....')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak(" According to Wikipedia ,")
            print(results)
            speak(results)
        elif "open youtude" in query:#youtube opration
            webbrowser.open("youtube.com")
        elif "the time" in query:# time query
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is {strtime}")
            speak(f"Sir the time is {strtime}")
        elif "play music" in query:# play music in this
            music_dir='D:\\All in One\\New folder'
            song= os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir, song[0]))

        elif "open notepad" in query:# open notpade++ of this command
            codePath= "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif "open spotify" in query:# open Spotify of this command
            codePath= "C:\\Users\\Prateek\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)

        elif "open dev c" in query:# open Dev c++ of this command
            codePath= "C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)

        elif "open google chrome" in query:# open Google Chrome of this command
            codePath=  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif "close google chrome" in query:
            codePath= "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.close(codePath)

        elif "open stream" in query:# open Stream app notpade++ of this command
            codePath=  "E:\\kali\\java\\Stream\\game\\Steam.exe"
            os.startfile(codePath)

        elif "open edge" in query:# open microsoft brawuser of this command
            codePath=  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(codePath)

        elif "close microsoft edge" in query:
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.close(codePath)

        elif "open firefox" in query:
            codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.close(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif "quit" or "exit" in query:
            exit()

        else :
            speak("Try again to speak sir")

# this project is made by Prateek kumawat on destop assest on python
#============================@prateekkumawat============================#
# copywrite: @2023 for prateek Kumawat