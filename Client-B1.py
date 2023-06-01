# Run on middle raspberry pi
import random
import time
import sys
import signal
from iottalkpy.dan import NoData
import RPi.GPIO as GPIO

api_url = 'https://iottalk2.tw/csm'  # default

device_model = 'Dummy_Device'

idf_list = ['DummySensor-I']
odf_list = ['DummyControl-O']

push_interval = 3  # global interval
interval = {
    'Dummy_Sensor-I': 3,  # assign feature interval
}

R0 = 3
G0 = 5

R1 = 11
G1 = 13

R2 = 19
G2 = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(R0, GPIO.OUT)
GPIO.setup(G0, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(G1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(G2, GPIO.OUT)
GPIO.setup(R0, GPIO.HIGH)
GPIO.setup(G0, GPIO.HIGH)
GPIO.setup(R1, GPIO.HIGH)
GPIO.setup(G1, GPIO.HIGH)
GPIO.setup(R2, GPIO.HIGH)
GPIO.setup(G2, GPIO.HIGH)

def end(signum, frame):
    GPIO.setup(R0, GPIO.LOW)
    GPIO.setup(G0, GPIO.LOW)
    GPIO.setup(R1, GPIO.LOW)
    GPIO.setup(G1, GPIO.LOW)
    GPIO.setup(R2, GPIO.LOW)
    GPIO.setup(G2, GPIO.LOW)
    GPIO.cleanup()
    exit()
    
signal.signal(signal.SIGINT, end)

def on_register(dan):
    print('register successfully')
    time.sleep(10)

def DummySensor_I():
    # function to get plate number
    f = open("pos.txt", "r")
    data = f.read()
    tmp = data.split("/")
    print('tmp:', tmp)
    f.close()
    
    if tmp[0] == "":
        GPIO.setup(G0, GPIO.LOW)
        GPIO.setup(R0, GPIO.HIGH)
    else:
        GPIO.setup(G0, GPIO.HIGH)
        GPIO.setup(R0, GPIO.LOW)

    if tmp[1] == "":
        GPIO.setup(G1, GPIO.LOW)
        GPIO.setup(R1, GPIO.HIGH)
    else:
        GPIO.setup(G1, GPIO.HIGH)
        GPIO.setup(R1, GPIO.LOW)
        
    if tmp[2] == "":
        GPIO.setup(G2, GPIO.LOW)
        GPIO.setup(R2, GPIO.HIGH)
    else:
        GPIO.setup(G2, GPIO.HIGH)
        GPIO.setup(R2, GPIO.LOW)
    
    return data

def DummyControl_O(data: list):
    pass

            
