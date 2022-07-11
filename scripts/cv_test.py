import cv2
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

while True:
    im = cv2.imread('../images/01.jpg')

    imA = cv2.resize(im,(640,480))
    imA = cv2.cvtColor(imA,cv2.COLOR_RGB2GRAY)

    boxes, weights = hog.detectMultiScale(im,winStride=(2,2), padding = (8,8), scale=1.02)

    for i, (x, y, w, h) in enumerate(boxes):
        if weights[i] < 0.13:
            continue
        elif weights[i] < 0.3 and weights[i] > 0.13:
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 2)
        if weights[i] < 0.7 and weights[i] > 0.3:
            cv2.rectangle(im, (x, y), (x+w, y+h), (50, 122, 255), 2)
        if weights[i] > 0.7:
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 255, 0), 2)



    cv2.imshow('image',imA)
    cv2.imshow('original',im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
