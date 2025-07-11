import numpy as np
import face_recognition
import cv2

imgJohn = face_recognition.load_image_file('ImageBasic/JohnMulaneyTrain.jpg')
imgJohn = cv2.cvtColor(imgJohn, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImageBasic/SethMeyers.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgJohn)[0]
encodeJohn = face_recognition.face_encodings(imgJohn)[0]
cv2.rectangle(imgJohn, [faceLoc[3], faceLoc[0]],[faceLoc[1], faceLoc[2]], (0, 255, 0), 2)
faceLoc = face_recognition.face_locations(imgJohn)[0]

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, [faceLocTest[3], faceLocTest[0]],[faceLocTest[1], faceLocTest[2]], (0, 255, 0), 2)

results = face_recognition.compare_faces([encodeJohn], encodeTest)
faceDis = face_recognition.face_distance([encodeJohn], encodeTest)
print(results,faceDis)
cv2.putText(imgTest, f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imshow("John Mulaney", imgJohn)
cv2.imshow("John Test", imgTest)
cv2.waitKey(0)
