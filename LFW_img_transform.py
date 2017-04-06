import os
import cv2
import pickle

dirFolder = 'IMFDB_final'
imgX = 64
imgY = 64

dirFolder += '/'
people = os.listdir(dirFolder)
# data structure to hold img information
imgData = []
# read through all images
for personName in people:
    personPath = dirFolder + personName
    if os.path.isdir(personPath):
        personMovies = os.listdir(personPath)
        for movie in personMovies:
            moviePath = personPath + '/' + movie + '/images/'
            if os.path.isdir(moviePath):
                personImgs = os.listdir(moviePath)
                for img in personImgs:
                    imgPath = moviePath + img
                    img = cv2.imread(imgPath,0)
                    img_m = cv2.resize(img,(imgX,imgY))
                    imgData += [img_m]
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



