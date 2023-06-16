import sys, signal, time
import subprocess
import snowboydecoder
import speech_recognition as sr
import numpy as np
from gtts import gTTS
from difflib import SequenceMatcher

interrupted = False
def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sys.stdout.reconfigure(encoding="utf-8")
if len(sys.argv) == 1:
    print("Usage: python main.py your.model")
    sys.exit(-1)

def detect_callback():
    subprocess.run(["mpg123", "-d", "4" , "-h" , "3",  "-a", "hw:2", './voice_files/ask_car_num.mp3'])
    r = sr.Recognizer() 
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1) #listen for 1 seconds and create the ambient noise energy level 
                audio = r.listen(source)
            text = r.recognize_google(audio, language = 'zh-TW')
            print('Speech Recognition:', text)
            text = text.lower()
            
            f = open('pos.txt', 'r')
            car_set = f.read().split('/')
            f.close()

            matchers = [SequenceMatcher(None, car_num, text) for car_num in car_set]
            score = np.array([matcher.ratio() for matcher in matchers])
            print(car_set)
            print(score)

            if sum(score) == 0.0:
                subprocess.run(["mpg123", "-d", "4" , "-h" , "3",  "-a", "hw:2", './voice_files/no_car.mp3'])
                subprocess.run(["mpg123", "-a", "hw:2", './voice_files/repeat.mp3'])
                break
            
            text = car_set[score.argmax()]
            
            f = open("Q.txt", "w")
            f.write(text)
            f.close()

            text = ' '.join(text)
            # if text == 'eat':
            #     text = 'e a t'
            # if text == 'pqk':
            #     text = 'p q k'
            # if text=='fuy':
            #     text = 'f u y'
            f = open('info.txt', "r+")
            while True:
                try:
                    time.sleep(1)
                    pos, sec, = f.read().split('/')
                    min, sec = int(sec) // 60, int(sec) % 60
                    f.truncate(0)
                    f.close()
                    break
                except:
                    pass
            tts = gTTS(text="您的車牌號碼是"+text+"，您的愛車在"+pos+"號車位停了"+str(min)+"分"+str(sec)+"秒", lang='zh-TW')
            tts.save("./voice_files/info.mp3")
            subprocess.run(["mpg123", "-d", "4", "-h", "3", "-a", "hw:2", './voice_files/info.mp3'])
            subprocess.run(["mpg123", "-d", "4", "-h", "3", "-a", "hw:2", './voice_files/bye.mp3'])
            break
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            subprocess.run(["mpg123", "-a", "hw:2", './voice_files/repeat.mp3'])
        except sr.RequestError as e:
            print("No response from Google Speech Recognition service: {0}".format(e))
    return

model = sys.argv[1]
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.55)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detect_callback,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)
detector.terminate()
