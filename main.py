import time
from pygame import mixer
mixer.init()
from PIL import Image
from pytesseract import  image_to_string
from gtts import gTTS
text = image_to_string(Image.open('text.png'))
gTTS(text).save('sound.mp3')
mixer.music.load('sound.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)