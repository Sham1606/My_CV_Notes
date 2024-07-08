import cv2 as cv

# Way of reading images in cv2
img = cv.imread('D:/My_Data_Science/PycharmProjects/CV/1.Basics_of_CV/Photos/cat.jpg')

# Check if the image was successfully loaded
if img is None:
    print("Error: Could not read the image. Check the path.")
else:
    # To rescale image or video we are going to use rescale function
    def rescaleFrame(frame, scale=0.75):
        width = int(frame.shape[1] * scale)  # Width of the frame
        height = int(frame.shape[0] * scale)  # Height of the frame
        dimensions = (width, height)

        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  # Resizing the frame to a particular dimension

    # Rescale the image
    resized_image = rescaleFrame(img)

    # Display the resized image
    cv.imshow('Resized Image', resized_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
