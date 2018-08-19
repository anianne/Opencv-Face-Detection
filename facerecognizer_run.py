import cv2

import os
import numpy as np


subjects = ["","subject1","subject2"]
face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer.read('models/FisherFacerecognizer')


def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    

def draw_text(img, text, x, y):

    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    if x == 0:
        img1 = img
        x = 1
    elif x == 1:
        img2 = img
    



def detect_face(img):
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    if (len(faces) == 0):
        return None, None
    

    (x, y, w, h) = faces[0]
    

    return gray[y:y+w, x:x+h], faces[0]
def predict(test_img):
    global label
    global x
    x = 0

    img = test_img.copy()

    face, rect = detect_face(img)
    if rect is None:
        return test_img

    label, confidence = face_recognizer.predict(face)
    if confidence is None:

    
        draw_rectangle(img, rect)

        draw_text(img, 'unknown', rect[0], rect[1]-5)        
    


    label_text = subjects[label]
    

    draw_rectangle(img, rect)

    draw_text(img, label_text, rect[0], rect[1]-5)
    
    print("The image is "+ label_text)
    return img



print("Predicting images...")


test_img1 = cv2.imread("test-data/test1.jpg")
test_img2 = cv2.imread("test-data/test2.jpg")

predicted_img1 = predict(test_img1)
predicted_img2 = predict(test_img2)#(edited)

print("Prediction complete")



#commented to supress graphics


cv2.imshow('test1', cv2.resize(predicted_img1, (400, 500)))
cv2.imshow('test2', cv2.resize(predicted_img2, (400, 500)))#(edited)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()
