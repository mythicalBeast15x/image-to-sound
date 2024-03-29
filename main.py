import time
from pygame import mixer
mixer.init()
from PIL import Image
from pytesseract import  image_to_string
from gtts import gTTS

def image_to_sound():
    text = image_to_string(Image.open('text.png'))
    try:
        gTTS(text).save('sound.mp3')
    except:
        gTTS('No Sound to Speak').save('sound.mp3')

    mixer.music.load('sound.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

image_to_sound()