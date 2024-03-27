# Get car's position
import random
import time
import sys
from iottalkpy.dan import NoData

api_url = 'https://iottalk2.tw/csm' 

device_model = 'Dummy_Device'

idf_list = ['DummySensor-I']
odf_list = ['DummyControl-O']
push_interval = 3 
interval = {
    'Dummy_Sensor-I': 3,
}


def on_register(dan):
    print('register successfully')
    time.sleep(10)

def DummySensor_I():
    return NoData

def DummyControl_O(data: list):
    print(str(data[0]))
    if data[0]:
        f = open("car_pos.txt", "w")
        print(data[0], file=f)
        f.close()
        
            
