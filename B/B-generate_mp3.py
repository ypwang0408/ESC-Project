from gtts import gTTS #creating speech files using the Google Text-to-Speech API. 
import argparse       #With this module, you can convert text to speech and save the output as an MP3 file.
import os

parser = argparse.ArgumentParser()
parser.add_argument('--text', type=str, default='查無此車牌')
parser.add_argument('--file_o', type=str, default='book.mp3')
parser.add_argument('--lang', type=str, default='zh-TW')
opt = parser.parse_args()

tts = gTTS(text=opt.text, lang=opt.lang, slow=False)
tts.save(opt.file_o)
