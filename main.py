import numpy as np
import cv2


cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret, img = cam.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=2.8,
            minNeighbors=2

        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
cam.release()
cv2.destroyAllWindows()
