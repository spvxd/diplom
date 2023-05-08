import numpy as np
import cv2


cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input('\n Введите ID, под номером которого будет создана база')
print("\n Смотрите в камеру и ждите, пока программа будет завершена")
count = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale (gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1

        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff
    if k == 50:
        break
    elif count >= 55:
        break

print("\n Программа завершена")
cam.release()
cv2.destroyAllWindows()