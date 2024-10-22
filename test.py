from io import BytesIO
import os
import time
from TTS.api import TTS

device = "cpu"
directory = os.path.dirname(os.path.abspath(__file__))

## download on C:\Users\ecapila\AppData\Local\tts\tts_models--de--thorsten--tacotron2-DDC

OUTPUT_PATH = directory + "\\recorded_voice\\prova.wav"

# Init TTS with the target model name
## tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False).to(device)

# Run TTS
## tts.tts_to_file(text="Sir, I checked what happened in Italy", file_path=OUTPUT_PATH)


tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
tts.tts_to_file("Good evening, SIR!", speaker_wav=directory + "\\OUTPUT.wav", language="en", file_path= directory + "\\recorded_voice\\good_evening.wav")


# import pygame

# def wait():
#     while pygame.mixer.get_busy():
#         time.sleep(1)


# pygame.init()
# pygame.mixer.init()
# sound = pygame.mixer.Sound(directory + "\\eng_output.wav")
# sound.play()
# wait()
