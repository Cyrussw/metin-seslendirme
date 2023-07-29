from gtts import gTTS
import os

def seslendir(text):
    ses = gTTS(text=text, lang="tr", slow=False)
    ses.save("seslendirilmis-metin.mp3")
    os.system("seslendirilmis-metin.mp3")

dosya = open("metin.txt", "r").read()

seslendir(dosya)