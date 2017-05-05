import os
import cv2
import numpy as np
import pickle

dirFolder = 'IMFDB_FIXED'
imgX = 64
imgY = 64

dirFolder += '/'
people = os.listdir(dirFolder)

for personName in people:
    personPath = dirFolder + personName
    personImgs = os.listdir(personPath)
    for imgName in personImgs:
        if imgName.endswith(".jpg"):
            imgPath = personPath + '/' + imgName
            print(imgPath)
            img = cv2.imread(imgPath,0)
            img_m = cv2.resize(img,(imgX,imgY))
            cv2.imwrite(personPath + '/mod_' + imgName, img_m)

print('done')
