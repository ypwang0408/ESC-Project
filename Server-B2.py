# Get car's position and park time
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

response = ''

def on_register(dan):
    print('register successfully')
    time.sleep(10)

def DummySensor_I():
    global response
    if response:
        tmp = response
        response = ''
        return tmp
    return NoData

def DummyControl_O(data: list):
    global response
    print(str(data[0]))
    if data[0]:
        f = open("inside.txt", "r")
        inside = f.read().splitlines()
        target = ''
        for i in inside:
            if data[0] in i:
                target = i
                break
        f.close()
        f = open("car_pos.txt", "r")
        car_pos = f.read().strip().split('/')
        print(car_pos)
        f.close()
        pos = car_pos.index(data[0])
        start_time = target.split('/')[1]
        park_time = int(time.time()) - int(start_time)
        print("Car " + data[0] + " has parked for " + str(park_time) + " seconds")
        response = str(pos) + '/' + str(park_time)
        f = open("can_leave.txt", "w")
        f.write(data[0])
        f.close()
        
                
            
