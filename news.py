import os
import time
import requests
import json
import pyttsx3
from helpers import tts, model_create_file, speak
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

directory = os.path.dirname(os.path.abspath(__file__))

import pygame

def speak_news():
    url = 'http://newsapi.org/v2/top-headlines?country=it&apiKey=0bd57861d4814db2843ceb30350849f9'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak("\\recorded_voice\\italy_check.wav")
    speak('\\recorded_voice\\italy_headlines.wav')
    for index, articles in enumerate(arts):
        model_create_file(phrase=articles['title'],file_path=directory + "\\recorded_voice\\news_stop.wav")
        speak(directory + "\\recorded_voice\\news_stop.wav")
        if index == len(arts)-1:
            break
        speak("\\recorded_voice\\italy_next.wav")
    speak("\\recorded_voice\\news_stop.wav")

def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?country=it&apiKey=0bd57861d4814db2843ceb30350849f9'

if __name__ == '__main__':
    speak_news()
