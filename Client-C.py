# Run on middle raspberry pi
import random
import time
import sys,os
import signal
from iottalkpy.dan import NoData
import RPi.GPIO as GPIO

api_url = 'https://iottalk2.tw/csm'  # default

device_model = 'Dummy_Device'

idf_list = ['DummySensor-I']
odf_list = ['DummyControl-O']

push_interval = 5  # global interval
interval = {
    'Dummy_Sensor-I': 5,  # assign feature interval
}

def on_register(dan):
    print('register successfully')
    time.sleep(10)

def DummySensor_I():
# function to get plate number
    #num = get number 
    os.system("raspistill -o entry.png -w 640 -h 480 -t 1 -q 100")
    os.system("python3 get_plate.py")
    f = open("result.txt", "r")
    tmp = f.read().splitlines()
    if len(tmp) == 0:
        return NoData
    print('tmp:', tmp)
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
    if data[0] == '1':
        pass
        #open gate
        import time
        import RPi.GPIO as GPIO

        CONTROL_PIN = 3
        PWM_FREQ = 50
        STEP=5
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(CONTROL_PIN, GPIO.OUT)

        pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
        pwm.start(0)

        def angle_to_duty_cycle(angle=0):
            duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
            return duty_cycle

        def switch2deg(deg):
            dc = angle_to_duty_cycle(deg)
            pwm.ChangeDutyCycle(dc)

        degrees = [50, 150]


        for deg in degrees:
            switch2deg(deg)
            time.sleep(3)

        pwm.stop()
        GPIO.cleanup()
    else:
        pass
        #cant leave

            
