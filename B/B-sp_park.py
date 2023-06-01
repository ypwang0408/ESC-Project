import os 
import cv2

# load the input image
img = cv2.imread('test.png')
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.waitKey(0)
cv2.imwrite("test.png",img_cw_180)

from split_image import split_image
split_image("test.png", 3, 3, True, False)
