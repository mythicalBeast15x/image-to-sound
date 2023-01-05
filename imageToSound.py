import os.path
import time
from pygame import mixer
mixer.init()
from PIL import Image
from pytesseract import  image_to_string
from gtts import gTTS
from os.path import exists

def get_filepath():
    image_file = input("filepath: ")
    ext_list = ['.jpeg', '.jpg', '.png']
    if exists(image_file):
        ext = os.path.splitext(image_file)[-1].lower()
        if ext in ext_list:
            return image_file
        else:
            path = get_filepath()
            return path
    else:
        path = get_filepath()
        return path

def image_to_sound():
    image = get_filepath()
    text = image_to_string(Image.open(image))
    try:
        gTTS(text).save('sound.mp3')
    except:
        gTTS('No Sound to Speak').save('sound.mp3')
    mixer.music.load('sound.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

image_to_sound()

