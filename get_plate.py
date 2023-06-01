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
        headers={'Authorization': 'Token 91d4a6a4fdf8e7ae93abe8ceaae7b1b4d046be7a'})
#pprint(response.json())
try:
    plate = response.json()['results'][0]['plate']    
except:
    plate=""
    
print("plate: ", plate)
f = open("result.txt", "w")
f.write(plate)
f.close()

