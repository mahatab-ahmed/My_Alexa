import pyttsx3
import datefinder
import winsound
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
import time
from pprint import pprint
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
        engine.say(audio)
        engine.runAndWait()



def wishMe():
        speak("Welcome back sir")
        hour = int(datetime.datetime.now().hour)
        print(hour)
        year = int(datetime.datetime.now().year)
        month = int(datetime.datetime.now().month)
        date = int(datetime.datetime.now().day)
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        print(Time)
        print(date)
        print(month)
        print(year)
        speak("the current Time is")
        speak(Time)
        speak("the current Date is")
        speak(date)
        speak(month)
        speak(year)
        if hour >= 6 and hour < 12:
                speak("Good Morning Mahatab!")

        elif hour >= 12 and hour < 18:
                speak("Good Afternoon Mahatab!")

        elif hour >= 18 and hour < 24:
                speak("Good Evening Mahatab!")

        else:
                speak("Good Night Mahatab!")

        speak("Jarvis at your Service. Please tell me how can I help You ")


# wishMe()
def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"Mahatab Said:{query}\n")

        except Exception as e:
                print(e)
                print("Say that again Please...")
                speak("Say that again Please...")
                return "None"
        return query


def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Senderemail@gmail.com', 'Password')
        server.sendmail('Senderemail@gmail.com', to, content)
        server.close()


# def lighton():
#     driver = webdriver.Chrome('C:/Users/Username/Downloads/chromedriver.exe')add the location of the chrome Drivers
#     driver.get("https://Add here.000webhostapp.com/main.html")Add the webhost name
#     elem1 = driver.find_element_by_id("S1off")
#     elem1.click()

# def lightoff():
#     driver = webdriver.Chrome('C:/Users/HACKER47/Downloads/chromedriver.exe')
#     driver.get("https://Add here.000webhostapp.com/main.html")Add the webhost name
#     elem1 = driver.find_element_by_id("S1on")
#     elem1.click()
def alarm(text1):
        dtime = datefinder.find_dates(text1)
        for mat in dtime:
                print(mat)
        stringa = str(mat)
        timea = stringa[11:]
        houra = timea[:-6]
        houra = int(houra)
        mina = timea[3:-3]
        mina = int(mina)




        while True:
                if houra == datetime.datetime.now().hour:
                        if mina == datetime.datetime.now().minute:
                                print('alarm is running ')
                                winsound.PlaySound('D:\\song\\KGF_Monster_BGM_Ringtone__Hacker_vickky(128k).mp3',
                                                   winsound.SND_LOOP)
                        elif mina < datetime.datetime.now().minute:
                                break


def stopwatch(text):
        while True:
                try:
                        start_time =time.time()
                        print('stopwatch has started')

                        while True:
                                print(round(time.time() - start_time, 0), 'secs')
                                time.sleep(1)
                except KeyboardInterrupt:
                        print("stopwatch has sopped")
                        end_time=time.time()
                        print(round(end_time-start_time))
        



if __name__ == "__main__":
        wishMe()
        while True:
                query = takeCommand().lower()

                if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                elif 'search in chrome' in query:
                        speak("what should i search?")
                        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'  # Add the Location of the chrome browser

                        r = sr.Recognizer()

                        with sr.Microphone() as source:
                                print('say something!')
                                audio = r.listen(source)
                                print("done")
                        try:
                                text = r.recognize_google(audio)
                                print('google think you said:\n' + text + '.com')
                                wb.get(chrome_path).open(text + '.com')
                        except Exception as e:
                                print(e)

                elif 'how is the weather' and 'weather' in query:

                        url = 'https://api.openweathermap.org/'  # Open api link here

                        res = requests.get(url)

                        data = res.json()

                        weather = data['weather'][0]['main']
                        temp = data['main']['temp']
                        wind_speed = data['wind']['speed']

                        latitude = data['coord']['lat']
                        longitude = data['coord']['lon']

                        description = data['weather'][0]['description']
                        speak('Temperature : {} degree celcius'.format(temp))
                        print('Wind Speed : {} m/s'.format(wind_speed))
                        print('Latitude : {}'.format(latitude))
                        print('Longitude : {}'.format(longitude))
                        print('Description : {}'.format(description))
                        print('weather is: {} '.format(weather))
                        speak('weather is : {} '.format(weather))

                elif "open Google" in query:
                        wb.open('Google.com')

                elif "open Gmail" in query:
                        wb.open('Gmail.com')

                elif "open Github" in query:
                        wb.open('Github.com')

                elif "open stackoverflow" in query:
                        wb.open('stackoverflow.com')

                elif "play music" in query:
                        wb.open('spotify.com')

                elif "open facebook" in query:
                        wb.open('facebook.com')

                elif "open twitter" in query:
                        wb.open('twitter.com')

                elif 'open instagram' in query:
                        wb.open('instagram.com')

                elif 'what is the news for today' in query:
                        wb.open('timesofindia.com')

                elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"Sir, the time is {strTime}")

                elif 'set an alarm' in query:
                        speak("what is the time for alarm")
                        contents = takeCommand()
                        alarm(contents)
                        speak('your alarm is set')

                elif 'start stopwatch' in query:
                        speak('what is the timer that you want to set')
                        content1=takeCommand()
                        post=stopwatch(content1)
                        print(post)



                elif 'the date' in query:
                        year = int(datetime.datetime.now().year)
                        month = int(datetime.datetime.now().month)
                        date = int(datetime.datetime.now().day)
                        speak("the current Date is")
                        speak(date)
                        speak(month)
                        speak(year)





                elif 'email to harry' and 'send email' in query:
                        try:
                                speak("What should I say?")
                                content = takeCommand()
                                to = "ReciversEmail@gmail.com"
                                sendEmail(to, content)
                                speak("Email has been sent!")
                        except Exception as e:
                                print(e)
                                speak("Sorry my friend . I am not able to send this email")

                elif 'open code' in query:
                        codePath = "C:\\Users\\user account\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # ADD THE PATH OF THE PROGEM HERE
                        os.startfile(codePath)


                elif 'open' in query:
                        os.system('explorer C://{}'.format(query.replace('Open', '')))



                        # form here i start something new
                elif 'i love you' in query:
                        speak("Ghar me maa behan nhi hai kya be")
                elif 'are you single' in query:
                        speak("If you are interested than definitely not")
                elif 'what is your age' in query:
                        speak('I am too older than you')
                elif 'who is your creator' in query:
                        speak('professor Mahatab and professor Akram is our honorable creator')

                elif 'i want to marry you' in query:
                        speak("It's beyond your limit")

                # elif 'turn on lights' in query:
                #     speak("OK,sir turning on the Lights")
                #     lighton()
                #     speak("Lights are on")

                # elif 'turn off lights' in query:
                #     speak("OK,sir turning off the Lights")
                #     lightoff()
                #     speak("Lights are off")

                elif 'go offline' in query:
                        speak("good bye sir i am jarvis speed one tera heart memory one seta byte")
                        quit()
