import os
import pyttsx3
import pyautogui
import psutil
import pyjokes
import speech_recognition as sr
import json
import requests
import geocoder
from difflib import get_close_matches
from io import BytesIO
import pygame
import time
from TTS.api import TTS


# engine = pyttsx3.init()
# voices = engine.getProperty('voices') #getting details of current voice
# engine.setProperty('voice', voices[0].id)
pygame.init()
pygame.mixer.init()

g = geocoder.ip('me')
data = json.load(open('data.json'))
device = "cpu"
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
directory = os.path.dirname(os.path.abspath(__file__))

import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def wait():
    while pygame.mixer.get_busy():
        time.sleep(1)

def speak(file_name):
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_name)
    sound.play()
    wait()

def model_create_file(phrase, file_path):
    tts.tts_to_file(phrase, speaker_wav=directory + "\\OUTPUT.wav", language="en", file_path= file_path )


def screenshot() -> None:
    img = pyautogui.screenshot()
    img.save('C:\\Users\\ecapila\\Pictures\\j.a.r.v.i.s\\screenshot.png')

def cpu() -> None:
    usage = str(psutil.cpu_percent())
    model_create_file("CPU is at "+ usage, directory + "\\recorded_voice\\cpu.wav")
    speak(directory + "\\recorded_voice\\cpu.wav")

    battery = psutil.sensors_battery()
    model_create_file("battery is at "+ str(battery.percent), directory + "\\recorded_voice\\battery.wav")
    speak(directory + "\\recorded_voice\\battery.wav")

def joke() -> None:
    for i in range(2):
        model_create_file(pyjokes.get_jokes()[i], directory + f"\\recorded_voice\\joke{i}.wav")
        speak(directory + f"\\recorded_voice\\joke{i}.wav")

def takeCommand() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query

def weather():
    API_key = "0e6a1fc2664ff90f80819284472085ed"
    city_name =  "Milan,it"

    api_url_city = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

    data = requests.get(api_url_city)
    data_json = data.json()
    if data.status_code == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        # speak(str(data_json['coord']['lat']) + 'latitude' + str(data_json['coord']['lon']) + 'longitude')
        model_create_file('Current location is ' + data_json['name'] + data_json['sys']['country'], directory + "\\recorded_voice\\current_loc.wav")
        speak(directory + "\\recorded_voice\\current_loc.wav")

        model_create_file('The weather type is ' + weather_desc['main'], directory + "\\recorded_voice\\current_weather.wav")
        speak(directory + "\\recorded_voice\\current_weather.wav")

        model_create_file('The wind speed is ' + str(wind['speed']) + ' metre per second', directory + "\\recorded_voice\\current_wind.wav")
        speak(directory + "\\recorded_voice\\current_wind.wav")

        model_create_file('Temperature: ' + str(main['temp']) + 'degree celcius', directory + "\\recorded_voice\\current_temp.wav")
        speak(directory + "\\recorded_voice\\current_temp.wav")

        model_create_file('Humidity is ' + str(main['humidity']), directory + "\\recorded_voice\\current_hum.wav")
        speak(directory + "\\recorded_voice\\current_hum.wav")

    else:
        speak( directory + "\\recorded_voice\\weather_error.wav")

def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])