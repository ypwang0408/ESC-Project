import random
import time
import sys
from iottalkpy.dan import NoData

api_url = 'https://iottalk2.tw/csm' 

device_model = 'Dummy_Device'

idf_list = ['DummySensor-I']
odf_list = ['DummyControl-O']

push_interval = 5 
interval = {
    'Dummy_Sensor-I': 5, 
}

allow_in = False
f = open("num_in.txt", "w")
f.write("0")
f.close()
f = open("log.txt", "w")
f.write("")
f.close()
f = open("inside.txt", "w")
f.write("")
f.close()


def on_register(dan):
    print('register successfully')
    time.sleep(10)

def DummySensor_I():
    global allow_in
    if allow_in:
        allow_in = False
        return "True"
    else:
        return "False"
    return NoData

def DummyControl_O(data: list):
    global allow_in
    #print(str(data[0]))
    if data[0]:
        f = open("num_in.txt", "r")
        nums = int(f.read())
        print(nums)
        f.close()
        f = open("inside.txt", "r")
        inside = f.read().splitlines()
        f.close()
        for i in inside:
            if data[0] in i:
                print("Already inside")
                allow_in = True
                return
        if nums < 3:
            f = open("num_in.txt", "w")
            f.write(str(nums + 1))
            f.close()
            f = open("log.txt", "a")
            print(data[0] + "/" + str(int(time.time())) + "/in", file=f)
            f.close()
            f = open("inside.txt", "a")
            print(data[0] + "/" + str(int(time.time())), file=f)
            f.close()
            print("Allow in")
            allow_in = True
            # open door
        else:
            f.close()
            if nums == 3:
                print("Full")
            #print("Not allow in")
            allow_in = False
            # do nothing
    
            
