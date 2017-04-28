import os
import cv2
import numpy as np
import pickle

dirFolder = 'IMFDB_FIXED'
imgX = 64
imgY = 64

dirFolder += '/'
people = os.listdir(dirFolder)
# data structure to hold img information
# imgData = []
# read through all images
for personName in people:
    personPath = dirFolder + personName
    personImgs = os.listdir(personPath)
    for imgName in personImgs:
        if imgName[len(imgName)-4:] == '.jpg' and imgName[len(imgName)-6:len(imgName)-4] != '_m' :
            imgPath = personPath + '/' + imgName
            img = cv2.imread(imgPath,0)
            img_m = cv2.resize(img,(imgX,imgY))
            # imgData += [img_m]
            cv2.imwrite((imgPath[:len(imgPath)-4]) + '_m.jpg' ,img_m)


# pickle image data into file
# out = open('data.pkl','wb')
# pickle.dump(imgData, out)
# out.close()

#open data from pickle folder
# f = open('data.pkl','rb')
# A = pickle.load(f)
# f.close()
# for img in A:
#     cv2.imshow('img',img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


print('done')



