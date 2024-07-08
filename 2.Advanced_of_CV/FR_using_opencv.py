#pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'D:/My_Data_Science/PycharmProjects/CV/2.Advanced_of_CV/train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = [] # image array of face
labels = [] # labelling every image it processes

def create_train(): # this function will loop over every folder in base folder
    # Loop over every folder in the base folder
    for person in people:
        # Construct the path to the current person's folder
        path = os.path.join(DIR, person)
        # Assign a label to the current person
        label = people.index(person)

        # Loop over each image in the current person's folder
        for img in os.listdir(path):
            # Construct the path to the current image file
            img_path = os.path.join(path,img) 

            # Read the image from the path
            img_array = cv.imread(img_path) 
            # Check if the image is not readable
            if img_array is None:
                # Continue to the next iteration if the image cannot be read
                continue 
                
            # Convert the color image to grayscale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Detect faces in the grayscale image
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) 

            # Loop over the bounding boxes of the detected faces
            for (x,y,w,h) in faces_rect:
                # Extract the region of interest (ROI) - the detected face
                faces_roi = gray[y:y+h, x:x+w] # cropping out the face in the image
                # Append the extracted face to the features list
                features.append(faces_roi)
                # Append the corresponding label to the labels list
                labels.append(label)
create_train()

#print(f'Length of features = {len(features)}')
#print(f'Length of labels = {len(labels)}')

print('Training done ---------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer.create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
