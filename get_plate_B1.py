import os 
import cv2

# load the input image
img = cv2.imread('entry.png')
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.waitKey(0)
cv2.imwrite("entry.png",img_cw_180)

from split_image import split_image
split_image("entry.png", 3, 3, True, False)


plate=""


import requests
from pprint import pprint
regions = ['mx', 'us-ca'] # Change to your country
with open('entry_3.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 91d4a6a4fdf8e7ae93abe8ceaae7b1b4d046be7a'})
with open('entry_4.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 91d4a6a4fdf8e7ae93abe8ceaae7b1b4d046be7a'})
with open('entry_5.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 91d4a6a4fdf8e7ae93abe8ceaae7b1b4d046be7a'})


#pprint(response.json())
try:
    plate += response.json()['results'][0]['plate']+'/'    
except:
    plate=""
    
print("plate: ", plate)
f = open("pos.txt", "w")
f.write(plate)
f.close()

