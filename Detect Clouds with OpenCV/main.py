#import cv2     $ pip install opencv-python
#import numpy   $ pip install numpy
#import argparse (preinstalled)
import cv2
import numpy as np
import argparse

if __name__ == "__main__":
    #percentage calculator
    def percentage(percent, whole):
        return (percent * 100) / whole

    #text template
    def text(pos1, pos2, text):
        position = (pos1, pos2)
        cv2.putText(
        erosion, #numpy array on which text is written
        text, #text
        position, #position at which writing has to start
        cv2.FONT_HERSHEY_SIMPLEX, #font family
        1, #font size
        (209, 80, 0, 255), #font color
        3) #font stroke

    #--image command
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = vars(ap.parse_args())

    #set image
    img = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)

    #get reselution
    dimensions = img.shape
    height = img.shape[0]
    width = img.shape[1]

    #calculate pixel
    reselution = height * width

    #resize reselution
    if width > 1024:
        showheight =  height / 2
        showwidth = width / 2
    else:
        showheight =  height
        showwidth = width

    #get clouds
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)

    #paint clouds green 
    img[thresh == 255] = 124,252,0

    #get cloud pixel
    px = np.sum(gray >= 250)

    #stuff
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    erosion = cv2.erode(img, kernel, iterations = 1)

    #write text
    text(10, 50, "Clouds: " + str(percentage(px, reselution).round(2)) + "%")
    text(10, 90, "Reselution: " + str(width) + " * " + str(height))
    if width != showheight:
        text(10, 130, "Resized Reselution: " + str(int(showwidth)) + " * " + str(int(showheight)))

    #open image
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', int(showwidth), int(showheight))
    cv2.imshow("image", erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()