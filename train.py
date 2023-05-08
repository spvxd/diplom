import numpy as np
import cv2
from PIL import Image
import os

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getImageAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')

        img_numpy = np.array(PIL_img, 'uint8')

        id = int (os.path.split(imagePath)[-1].split(".")[1])
        faces =  detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h , x:x+w])
            ids.append(id)

    return faceSamples, ids
print("\n Дождитесь обработки")
faces,ids = getImageAndLabels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')
print("\n Программа завершена".format(len(np.unique(ids))))