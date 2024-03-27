import os 
import cv2
import time
# load the input image
img = cv2.imread('entry.png')
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.waitKey(0)
cv2.imwrite("entry.png",img_cw_180)

from split_image import split_image
split_image("entry.png", 2, 3, True, False)



plate=""
plate_all=""
flag_all=""
f = open("last_flag.txt", "r")
data = f.read()
last_flag = data.split("/")
now_flag=""
f = open("pos.txt", "r")
data = f.read()
last_plate = data.split("/")


print(last_flag)

import requests
from pprint import pprint
regions = ['mx', 'us-ca'] # Change to your country

with open('entry_3.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token fb29a7f05f1a5cd8147e6312fc97e7c70b5c81be'})
try:
	plate=response.json()['results'][0]['plate']
except:
	plate=""
 

if(plate=="" and last_flag[0]=='0'):
    now_flag='0'
    plate=""
elif(plate=="" and last_flag[0]=='1'):
    now_flag='0'
    plate=last_plate[0]
elif(plate!="" and last_flag[0]=='0'):
    now_flag='1'
    # plate=last_plate[0]
elif(plate!="" and last_flag[0]=='1'):
    now_flag='1'

    # plate=last_plate[0]


plate_all+=plate+"/"
flag_all+=now_flag+"/"
print("now f0 ",now_flag)
# time.sleep(1)

with open('entry_4.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 5a97668b81e0b6969a3445d65b68798d1f70b93b'})
try:
	plate=response.json()['results'][0]['plate']
except:
	plate=""




if(plate=="" and last_flag[1]=='0'):
    now_flag='0'
    plate=""
elif(plate=="" and last_flag[1]=='1'):
    now_flag='0'
    plate=last_plate[1]
elif(plate!="" and last_flag[1]=='0'):
    now_flag='1'
    # plate=last_plate[0]
elif(plate!="" and last_flag[0]=='1'):
    now_flag='1'
    pass
    # plate=last_plate[0]

print("now f2 ",now_flag)
plate_all+=plate+"/"
flag_all+=now_flag+"/"
# time.sleep(1)

with open('entry_5.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 91d4a6a4fdf8e7ae93abe8ceaae7b1b4d046be7a'})
try:
	plate=response.json()['results'][0]['plate']
except:
	plate=""

if(plate=="" and last_flag[2]=='0'):
    now_flag='0'
    plate=""
elif(plate=="" and last_flag[2]=='1'):
    now_flag='0'
    plate=last_plate[2]
elif(plate!="" and last_flag[2]=='0'):
    now_flag='1'
    # plate=last_plate[0]
elif(plate!="" and last_flag[2]=='1'):
    now_flag='1'
    pass
    # plate=last_plate[0]
print("now f3 ",now_flag)

plate_all+=plate
flag_all+=now_flag

#pprint(response.json())
# try:
#     plate += response.json()['results'][0]['plate']+'/'    
# except:
#     plate=""
    
print("plate: ", plate_all)
f = open("pos.txt", "w")
f.write(plate_all)
f.close()

print("flag: ", flag_all)

f = open("last_flag.txt", "w")
f.write(flag_all)
f.close()
