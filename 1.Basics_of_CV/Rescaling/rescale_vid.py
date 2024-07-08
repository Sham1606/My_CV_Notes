import cv2 as cv

# Rescaling Videos
capture = cv.VideoCapture('D:/My_Data_Science/PycharmProjects/CV/1.Basics_of_CV/Videos/dog.mp4')

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live videos
    width = int(frame.shape[1] * scale)  # width of the frame
    height = int(frame.shape[0] * scale)  # height of the frame
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  # resizing the frame to a particular dimension

# this function is possible only for videos not for images
def changeRes(width, height): # Used to change the resolution of the video
        # Live video
        capture.set(3, width)
        capture.set(4, height)


while True:
        isTrue, frame = capture.read()
        frame_resized = rescaleFrame(frame, scale=.2)

        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)
        
        if cv.waitKey(20) & 0xFF == ord('d'):
            break


cv.waitKey(0) # keyboard binding function, waits for a specific delay time in milliseconds time to be pressed