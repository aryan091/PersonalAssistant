import datetime
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import smtplib
import requests
from bs4 import BeautifulSoup
from covid import Covid

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def weatherststus(cityname):
    url = "https://www.google.com/search?q="+cityname+"+" "weather/"
    r=requests.get(url=url)
    s=BeautifulSoup(r.text,'html.parser')
    w=s.find_all("div",class_="BNeawe iBp4i AP7Wnd")
    data=list(w)
    return data[1].text.strip()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    print("I am Jarvis Sir...How may I help you?")
    speak("I am Jarvis Sir...How may I help you? ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aryandaftari7@gmail.com', 'aryan@1234')
    server.sendmail('aryandaftari7@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open javatpoint' in query:
            webbrowser.open("javatpoint.com")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.com")

        elif 'play music' in query:
            music_dir = 'D:\\OFFICIAL BHAGAT BBI'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, The time is {strtime}")

        elif 'open pycharm' in query:
            codepath = "D:\\PyCharm Community Edition 2019.2.2\\bin\pycharm64.exe"
            os.startfile(codepath)

        elif 'email to aryan' in query:
            try:
                speak("What should I Say..?")
                content = takecommand()
                to = "aryandaftari89@gmail,com"
                sendEmail(to, content)
                print("Email has been Sent!..")
                speak("Email has been Sent!..")
            except Exception as e:
                print(e)
                print("Sorry Aryan I am not able to send an email at the moment")
                speak("Sorry Aryan I am not able to send an email at the moment")

        elif 'corona virus  in world' in query:
            url = "https://www.worldometers.info/coronavirus/"
            r = requests.get(url)
            myhtml = r.text

            soup = BeautifulSoup(myhtml, 'html.parser')
            print(soup.prettify())

            details = soup.find_all("div", class_="maincounter-number")
            print("       WORLDOMETER                    ")
            print("TOTAL CASES :", details[0].text.strip())
            print("TOTAL DEATHS :", details[1].text.strip())
            print("TOTAL RECOVERED :", details[2].text.strip())
            tot_cases=details[0].text.strip()
            tot_deaths=details[1].text.strip()
            tot_rec=details[2].text.strip()
            speak("TOTAL CONFIRMED CASES IN WORLD IS"+str(tot_cases))
            speak("TOTAL DEATHS CASES IN WORLD IS"+str(tot_deaths))
            speak("TOTAL RECOVERED CASES IN WORLD IS"+str(tot_rec))

        elif 'weather' in query:
            speak("please tell city name")
            cityname = takecommand().capitalize()
            status=weatherststus(cityname=cityname)
            print(status)
            speak(str(status))

        elif 'covid cases' in query:
            speak("please tell country name")
            country = takecommand().capitalize()
            covid = Covid()
            data = covid.get_status_by_country_name(country)

            Country_Name = data['country']
            Confirmed_Cases = data['confirmed']
            Active_Cases = data['active']
            Deaths = data['deaths']
            Recovered = data['recovered']
            print(" Country Name : ", Country_Name)
            print("Confirmed Cases : ", Confirmed_Cases)
            print(" Active Cases : ", Active_Cases)
            print("Deaths : ", Deaths)
            print("Recovered : ", Recovered)
            speak(" Country Name : "+str(Country_Name))
            speak("Confirmed Cases : "+str(Confirmed_Cases))
            speak(" Active Cases : "+str(Active_Cases))
            speak("Deaths : "+str(Deaths))
            speak("Recovered : "+str(Recovered))




