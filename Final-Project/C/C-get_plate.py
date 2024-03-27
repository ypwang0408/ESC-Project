import os 
import cv2

# load the input image
img = cv2.imread('entry.png')
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.waitKey(0)
cv2.imwrite("entry.png",img_cw_180)





import requests
from pprint import pprint
regions = ['mx', 'us-ca'] # Change to your country
with open('entry.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 96317985db62da5e9ac0afb7d2d82c7fc7622821'})
#pprint(response.json())
try:
    plate = response.json()['results'][0]['plate']    
except:
    plate=""
    
print("plate: ", plate)
f = open("result.txt", "w")
f.write(plate)
f.close()

