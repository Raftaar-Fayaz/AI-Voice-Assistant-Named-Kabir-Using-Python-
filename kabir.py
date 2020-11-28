import pyttsx3   #install pyttsx3 using pip
import speech_recognition as sr  #install speechRecognition using pip
import datetime
import pyaudio  #install pyaudio using pip installer
import wikipedia  #install Wikipedia usning pip installer
import webbrowser 
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")

    elif hour>=12 and hour<=15:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Kabir. Please tell me How May I Help You")

def takeCommand():
    #It Takes Microphone Input From The User And Returns STRING Output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning.....")
        #r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User Said : {query}\n")
        
    except Exception as e:
        #print(e)
        print("Say that Again Please.....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail39@gmai.com', 'your-password')
    server.sendmail('youremail39@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # takeCommand()
    while True:
    # if 1:
        query = takeCommand().Lower()

        # Logics For Executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("Wikipedia","")
            results = wikipedia.summery(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'D:\\Raftaar Fayaz\\MY MUSIC\\Mood Changing'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime().now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The Time Is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\91798\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open photoshop' in query:
            psPath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
            os.startfile(psPath)

        elif 'email to raftaar' in query:
            try:
                speak("What Should I say ?")
                content = takeCommand()
                to = "raftarfayaz@gmail.com"
                sendEmail(to, content)
                speak("Email Sent Sucessful")

            except Exception as e:
                print(e)
                speak("Sorry!, My Friend. I am not able to send this mail right now")



