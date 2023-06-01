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

def on_register(dan):
    print('register successfully')
    time.sleep(10)

def DummySensor_I():
# function to get plate number
    f = open("Q.txt", "r")
    tmp = f.read().splitlines()
    if len(tmp) == 0:
        return NoData
    print('tmp:', tmp)
    f.close()
    f = open("Q.txt", "w")
    try:
        for i in tmp[1:]:
            f.write(i + "\n")
    except:
        pass
    f.close()
    num = tmp[0]
    print(num)
    if num:
        return num

    # Or you want to return nothing.
    # Note that the object `None` is treated as normal data in IoTtalk
    #
    return NoData

def DummyControl_O(data: list):
    print(data[0])

            
