import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import sys
import smtplib
import wolframalpha
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Jarvis : Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Jarvis : Good Afternoon!")   
        speak("Good Afternoon!")   

    else:
        print("Jarvis : Good Evening!")  
        speak("Good Evening!")  

    print("Jarvis : I am Jarvis Sir. Please tell me how may I help you")       
    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Jarvis : Say that again please...")  
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anjalissingh@gmail.com', 'anjali15080203')
    server.sendmail('anjalissingh@gmail.com', to, content)
    server.close()

def DownloadVideo():
    from pytube import YouTube
    link_video = input("Enter the link of video to download: ").strip()
    def Download(l):
        url = YouTube(l)
        video = url.streams.first()
        video.download('D:\\YouTube-Videos\Downloads\\')

    Download(link_video)
    print("Jarvis : Video Downloaded succesfully")
    speak("Video Downloaded succesfully")

def My_Location():
    global geo_d
    global city
    global cont
    ip_add = requests.get("https://api.ipify.org").text
    url = "https://get.geojs.io/v1/ip/geo/" + ip_add + ".json"
    geo_q = requests.get(url)
    geo_d = geo_q.json()

    city = geo_d['city']
    cont = geo_d['country']

def GoogleMap(place):
    url = "https://www.google.com/maps/place/"
    url+=place
    try:
        webbrowser.open(url)
    except:
        print("Jarvis : There is No such place in google maps")
        speak("There is No such place in google maps")

def Wolfram(query):
    api_key = "4HP849-WQUXKLXWX2"
    requestser = wolframalpha.Client(api_key)
    requetsted = requestser.query(query)

    Answer = next(requetsted.results).text
    print(f"Jarvis : {Answer}")
    speak(Answer)

def AI(conversation):
    # import the module
    from prsaw import RandomStuffV2

    # initiate the object
    rs = RandomStuffV2() 

    # get a response from an endpoint
    response = rs.get_ai_response(conversation)
    print(f"Jarvis : {response['message']}")
    speak(response['message'])

    # close the object once done (recommended)
    rs.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(f"Jarvis : {results}")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Jarvis : Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                print("Jarvis : What should I say?")
                speak("What should I say?")
                content = takeCommand()
                to = input("Enter the email address: ").strip()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry my friend harry bhai. I am not able to send this email")
        elif 'quit jarvis' in query:
            print("Jarvis : Quitting sir thanks for your time!")
            speak("Quitting sir thanks for your time!")
            break
            sys.exit()

        elif 'open file' in query:
            print("Jarvis : Which file to open sir?")
            speak("Which file to open sir?")
            file = input("Enter the path of the file: ").strip()
            try:
                os.startfile(file)
            except:
                print("Jarvis : Could not open the file sir")
                speak("Could not open the file sir", file)

        elif 'open website' in query:
            print("Jarvis : Which website to open sir?")
            speak("Which website to open sir?")
            url = input("Enter the URL of the website: ").strip()
            try:
                webbrowser.open(url)
            except:
                print("Jarvis : Could not open", url)
                speak("Could not open", url)

        elif 'play music' in query:
            song = r"D:\song.mp3"
            os.startfile(song)

        elif 'what is my ip' in query:
            My_Location()
            print(geo_d['ip'])
            speak(geo_d['ip'])

        elif 'google map of' in query:
            query = query.replace("google map of","")
            query = query.strip()
            GoogleMap(query)

        elif 'google' in query:
            link_g = 'https://www.google.com/search?q='
            query = query.replace('google','')
            query = query.strip()
            query = query.replace(' ', '+')
            link_g+=query
            webbrowser.open(link_g)

        elif 'search youtube' in query:
            link_y = 'https://www.youtube.com/results?search_query='
            query = query.replace('search youtube','')
            query = query.strip()
            query = query.replace(' ', '+')
            link_y+=query
            webbrowser.open(link_y)

        elif 'download youtube video' in query:
            DownloadVideo()

        elif 'my location' in query:
            My_Location()
            print(f"Jarvis : Sir, you are now in {city} in {cont} country")
            speak(f"Sir, you are now in {city} in {cont} country")

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        else:
            try:
                Wolfram(query)
            except:
                AI(query)
