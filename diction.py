from difflib import get_close_matches
import os
from helpers import speak, model_create_file
import json
import speech_recognition as sr

directory = os.path.dirname(os.path.abspath(__file__))
data = json.load(open('data.json'))
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


def takeCommand():
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


def search_meaning(word):
    word = word.lower()
    if word in data:
        model_create_file(data[word], directory + "\\recorded_voice\\word_to_search.wav")
        speak(directory + "\\recorded_voice\\word_to_search.wav")
        
    elif len(get_close_matches(word, data.keys())) > 0:
        x = get_close_matches(word, data.keys())[0]
        model_create_file('Did you mean ' + x + '? respond with Yes or No.', directory + "\\recorded_voice\\did_you_mean.wav")
        speak(directory + "\\recorded_voice\\did_you_mean.wav")
        ans = takeCommand().lower()
        if 'yes' in ans:
            model_create_file(data[x], directory + "\\recorded_voice\\dict_results.wav")
            speak(directory + "\\recorded_voice\\dict_results.wav")
        elif 'no' in ans:
            speak(directory + "\\recorded_voice\\no_word_found.wav")
        else:
            #changed from we to I
            speak(directory + "\\recorded_voice\\no_understand.wav")

    else:
        speak( directory + "\\recorded_voice\\dict_error.wav")


if __name__ == '__main__':
    search_meaning()
