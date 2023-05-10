# Алгоритм распознавания лиц для дипломной работы
___
## Как установить?
+ Сделайте клон проекта, затем извлеките файлы в систему.
+ Создайте виртуальное окружение путем ```python -m venv env_name```
+ Активируйте виртуальное окружение командой ```env_name/Scripts/activate```
+ Установите необходимые библиотеки, прописав в терминале ```pip install -r req.txt```
___
## Как работать?
+ Запустите файл ***main.py***. Данный файл отвечает за обнаружение лица в реальном
времени, однако не позволяет обнаружить конкретного человека. Если веб-камера не открывается
  (или если у вас несколько камер), попробуйте поменять параметр **cv2.VideoCapture(x)**, где x -
порядковый номер вашей камеры в системе (по умолчанию 0). 
+ Запустите файл ***baza.py***. Данный файл отвечает за создание базы лиц. Каждый раз, распознав лицо,
алгоритм сохранит изображения как **User.face_id.count.jpg**, где **face_id** пользователь
вводит самостоятельно, а **count** - порядковый номер созданного изображения. Как только алгоритм
сделает 50 снимков, он завершит работу.
+ Запустите файл ***train.py.*** Функция **getImagesAndLabels(path)** будет принимать все фотографии в 
каталоге: **«dataset /»**, возвращая 2 массива: «Идентификаторы(lds)» и «Лица(Faces)». С этими массивами 
в качестве входных данных будет обучен распознаватель.
В результате файл с именем ***«trainer.yml»*** будет сохранен в каталоге тренера, который был ранее
предварительно создан. 
+ Запустите файл ***final.py***. Функция **recognizer.predict()** принимает в качестве параметра захваченную
часть лица, подлежащую анализу, и возвращает своего вероятного владельца, указывая его идентификатор и
степень уверенности распознавателя в связи с этим совпадением. В списке **names** содержатся имена людей,
которые были занесены в базу под соответствующими ID.
Алгоритм не только старается определить лицо, но и проинформировать пользователя о степени своей уверенности,
при том выводится погрешность, то есть 0% - это 100% уверенность алгоритма.
___
# Algorithm for face recognition for the thesis
___
## How to install?
+ Make a clone of the project, then extract the files to the system.
+ Create a virtual environment by ```python -m venv env_name```
+ Activate the virtual environment with ```env_name/Scripts/activate```
+ Install the necessary libraries by typing ```pip install -r req.txt``` in the terminal
___
## How to work?
+ Run the file ***main.py***. This file is responsible for face detection in real life.
time, however, does not allow to detect a specific person. If the webcam does not open
(or if you have multiple cameras), try changing the **cv2.VideoCapture(x)** parameter, where x is
serial number of your camera in the system (0 by default).
+ Run the file ***baza.py***. This file is responsible for creating a database of faces. Every time I recognize a face
the algorithm will save the images as **User.face_id.count.jpg** where **face_id** is the user
enters independently, and **count** is the sequence number of the created image. Once the algorithm
will take 50 shots, it will complete the job.
+ Run the file ***train.py.*** The **getImagesAndLabels(path)** function will take all the photos in
directory: **"dataset /"**, returning 2 arrays: "Identifiers (lds)" and "Faces (Faces)". With these arrays
the recognizer will be trained as input.
As a result, a file named ***"trainer.yml"*** will be saved in the trainer directory that was previously
pre-created.
+ Run the file ***final.py***. The **recognizer.predict()** function takes as a parameter the captured
part of the face to be analyzed and returns its probable owner, indicating its identifier and
the degree of confidence the resolver has about this match. The **names** list contains the names of people
which were entered into the database under the corresponding IDs.
The algorithm not only tries to identify the face, but also informs the user about the degree of his confidence,
while the error is displayed, that is, 0% is 100% confidence of the algorithm.
