import os
import cv2
 #Do same for 
 #cap= cv2.VideoCapture('/Users/nambawan/Documents/dev/speedchallenge/data/train.mp4')
 #cv2.imwrite('/Users/nambawan/Documents/dev/speedchallenge/data/trainFrames/'+str(i)+'.jpg',frame)

trainVid= cv2.VideoCapture('/Users/nambawan/Documents/dev/speedchallenge/data/train.mp4')
testVid= cv2.VideoCapture('/Users/nambawan/Documents/dev/speedchallenge/data/test.mp4')

trainDir = '/Users/nambawan/Documents/dev/speedchallenge/data/trainFrames'
os.mkdir(trainDir)
 
testDir = '/Users/nambawan/Documents/dev/speedchallenge/data/testFrames'
os.mkdir(testDir)

i=1
while(trainVid.isOpened()):
    ret, frame = trainVid.read()
    if ret == False:
        break
    cv2.imwrite('/Users/nambawan/Documents/dev/speedchallenge/data/trainFrames/'+str(i)+'.jpg',frame)
    i+=1
 
i=1
while(testVid.isOpened()):
    ret, frame = testVid.read()
    if ret == False:
        break
    cv2.imwrite('/Users/nambawan/Documents/dev/speedchallenge/data/testFrames/'+str(i)+'.jpg',frame)
    i+=1

trainVid.release()
testVid.release()
cv2.destroyAllWindows()