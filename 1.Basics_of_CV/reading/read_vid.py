import cv2 as cv

#Reading videos
capture = cv.VideoCapture('D:/My_Data_Science/PycharmProjects/CV/1.Basics_of_CV/Videos/dog.mp4') # can also provide the path to the video

#now we are passing the video frame by frame such that it will be played as video
while True:
       isTrue, frame = capture.read()

       #displaying each frame using imshow method
       cv.imshow('Video',frame) 

       # to stop the video from playing again we need to
       if cv.waitKey(20) & 0xFF==ord('d'): # basically says if letter d is pressed then video will be paused
              break
       
capture.release()
cv.destroyAllWindows()
