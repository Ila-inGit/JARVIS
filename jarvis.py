import pyttsx3
import wikipedia
import speech_recognition as sr
from helpers import *
import webbrowser
import datetime
import os
import sys
import smtplib
from OCR import OCR
from diction import search_meaning
from youtube import youtube
from sys import platform
import os
import getpass
import cv2
from news import speak_news, getNewsUrl

# engine = pyttsx3.init()
# voices = engine.getProperty('voices') #getting details of current voice
# engine.setProperty('voice', voices[0].id)

directory = os.path.dirname(os.path.abspath(__file__))

# print(voices[0].id)

class Jarvis:
    def __init__(self) -> None:
        if platform == "linux" or platform == "linux2":
            self.chrome_path = '/usr/bin/google-chrome'

        elif platform == "darwin":
            self.chrome_path = 'open -a /Applications/Google\ Chrome.app'

        elif platform == "win32":
            self.chrome_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register(
            'chrome', None, webbrowser.BackgroundBrowser(self.chrome_path)
        )

    def wishMe(self) -> None:
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak(directory + "\\recorded_voice\\good_morning.wav")
        elif hour >= 12 and hour < 18:
            speak(directory + "\\recorded_voice\\good_afternoon.wav")
        else:
            speak(directory + "\\recorded_voice\\good_evening.wav")

        ##weather()
        speak(directory + "\\recorded_voice\\hello.wav")

    def sendEmail(self, to, content) -> None:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('ilaria.c765@gmail.com', '#my')
        server.sendmail('email', to, content)
        server.close()

    def execute_query(self, query):
        # TODO: make this more concise
        if 'wikipedia' in query:
            speak( directory + "\\recorded_voice\\search_wiki.wav")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(f'{query}', sentences=2)
            speak(directory + "\\recorded_voice\\accoirdingTo_wiki.wav")
            print(results)
            model_create_file(results, directory + "\\recorded_voice\\results_wiki.wav")
            speak(directory + "\\recorded_voice\\results_wiki.wav")

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())
            
        # elif 'voice' in query:
        #     if 'female' in query:
        #         engine.setProperty('voice', voices[1].id)
        #     else:
        #         engine.setProperty('voice', voices[0].id)
        #     speak("Hello Sir, I have switched my voice. How is it?")

        if 'jarvis are you there' in query:
            speak(directory + "\\recorded_voice\\are_you_there.wav")

        if 'jarvis who made you' in query:
            speak(directory + "\\recorded_voice\\built_you.wav")
            
        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'search youtube' in query:
            speak(directory + "\\recorded_voice\\youtube_search.wav")
            youtube(takeCommand())
            
        elif 'open amazon' in query:
            webbrowser.get('chrome').open_new_tab('https://amazon.com')

        elif 'cpu' in query:
            cpu()

        elif 'notepad' in query:
            open_notepad()
        
        elif 'command prompt' in query:
            open_cmd()
        
        elif 'calculator' in query:
            open_calculator()

        elif 'screenshot' in query:
            speak(directory + "\\recorded_voice\\sreenshot.wav")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'stackoverflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            ## os.startfile("D:\\RoiNa.mp3")
            webbrowser.get('chrome').open_new_tab('https://open.spotify.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            model_create_file(f'Sir, the time is {strTime}', directory + "\\recorded_voice\\time.wav")
            speak(directory + "\\recorded_voice\\time.wav")

        elif 'search' in query:
            speak(directory + "\\recorded_voice\\search.wav")
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            model_create_file('Here is What I found for ' + search, directory + "\\recorded_voice\\result_search.wav")
            speak(directory + "\\recorded_voice\\result_search.wav")

        elif 'location' in query:
            speak(directory + "\\recorded_voice\\location.wav")
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            model_create_file('Here is the location ' + location, directory + "\\recorded_voice\\result_location.wav")
            speak(directory + "\\recorded_voice\\result_location.wav")

        elif 'your master' in query:
            speak(directory + "\\recorded_voice\\master.wav")

        elif 'your name' in query:
            speak(directory + "\\recorded_voice\\name.wav")
            
        elif 'who made you' in query:
            speak(directory + "\\recorded_voice\\built_you.wav")
            
        elif 'stands for' in query:
            speak(directory + "\\recorded_voice\\stands_for.wav")

        elif 'open code' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\gs935\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'shutdown the computer' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'your friend' in query:
            speak(directory + "\\recorded_voice\\friends.wav")

        elif 'joke' in query:
            joke()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/Ila-inGit')

        elif 'remember that' in query:
            speak(directory + "\\recorded_voice\\remember.wav")
            rememberMessage = takeCommand()
            speak("you said me to remember"+ rememberMessage)
            model_create_file("you said me to remember "+ rememberMessage, directory + "\\recorded_voice\\result_remember.wav")
            speak(directory + "\\recorded_voice\\result_remember.wav")
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak(directory + "\\recorded_voice\\result_remember.wav")

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' in query:
            speak(directory + "\\recorded_voice\\dictionary.wav")
            search_meaning(takeCommand())

        elif 'news' in query:
            speak( directory + "\\recorded_voice\\of_course.wav")
            speak_news()
            speak(directory + "\\recorded_voice\\full_news_ask.wav")
            test = takeCommand()
            if 'yes' in test:
                speak(directory + "\\recorded_voice\\open_browser.wav")
                webbrowser.open(getNewsUrl())
                speak(directory + "\\recorded_voice\\all_news.wav")
            else:
                speak(directory + "\\recorded_voice\\no_problem.wav")

        elif 'email to gaurav' in query:
            try:
                speak(directory + "\\recorded_voice\\email_what.wav")
                content = takeCommand()
                to = 'email'
                self.sendEmail(to, content)
                speak( directory + "\\recorded_voice\\email_success.wav")

            except Exception as e:
                speak( directory + "\\recorded_voice\\email_error.wav")


def wakeUpJARVIS():
    bot_ = Jarvis()
    bot_.wishMe()
    while True:
        query = takeCommand().lower()
        bot_.execute_query(query)
               

if __name__ == '__main__':
    
    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read(directory + '\\Face-Recognition\\trainer\\trainer.yml')   #load trained model
    cascadePath = directory + "\\Face-Recognition\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) # initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 3 #number of persons you want to Recognize


    names = ['','','ilaria']  #names, leave first empty bcz counter starts from 0


    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    # flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, loss = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

            # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (loss < 55):
                # Do a bit of cleanup
                speak(directory + "\\recorded_voice\\facial_yes.wav")
                cam.release()
                cv2.destroyAllWindows()
                wakeUpJARVIS()
            else:
                #speak(directory + "\\recorded_voice\\facial_no.wav")
                break


    
