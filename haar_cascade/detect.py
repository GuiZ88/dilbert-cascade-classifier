import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
 
 
# Read in the cascade classifiers
dilbert_cascade = cv2.CascadeClassifier('data/cascade.xml')
   
def detect_dilbert(img):
     
    dilbert_img = img.copy()   
    dilbert_rect = dilbert_cascade.detectMultiScale(dilbert_img,
                                            scaleFactor = 1.2,
                                            minNeighbors = 5)   
    #print(dilbert_rect)
    for (x, y, w, h) in dilbert_rect:
        cv2.rectangle(dilbert_img, (x, y),
                      (x + w, y + h), (0, 0, 255), 2)       
    return dilbert_img
 

directory = "undefined/"
for filename in os.listdir(directory):
    f_read = os.path.join(directory, filename)
    f_write = os.path.join("detected_gilbert/", filename)
    img = cv2.imread(f_read)
    face = detect_dilbert(img)
    #plt.imshow(face)
    #print(len(face))
    cv2.imwrite(f_write, face)