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
        f = open("can_leave.txt", "r")
        can_leave = f.read().splitlines()
        f.close()
        flag = False
        for i in can_leave:
            if data[0] in i:
                flag = True
                break
        if flag:
            response = '1'
            f = open("can_leave.txt", "w")
            for i in can_leave:
                if data[0] not in i:
                    f.write(i + '\n')
            f.close()
            f = open("num_in.txt", "r")
            nums = int(f.read())
            f.close()
            f = open("num_in.txt", "w")
            f.write(str(nums - 1))
            f.close()
            f = open("inside.txt", "r")
            inside = f.read().splitlines()
            f.close()
            f = open("inside.txt", "w")
            for i in inside:
                if data[0] not in i:
                    f.write(i + '\n')
            f.close()
            print("Car " + data[0] + " leaving")
            
            f = open("log.txt", "a")
            f.write("Car " + data[0] + " leaving\n")
            f.close()            
        else:
            response = '0'
            print("Car " + data[0] + " cannot leave")
        
        
                
            
