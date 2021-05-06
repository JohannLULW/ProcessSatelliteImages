import cv2
from datetime import date
import os

def takepicture():
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        date = today.strftime("%d-%m-%Y") + ".jpg"
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-"*60 + "\n Take a picture by pressing \"W\" \n" + "\n Close the programm by pressing \"Q\"\n" + "\nPicture saved: " + date + "\n" + "-"*60) #Keybinds
        if os.path.exists(date):
            os.remove(date)
        cv2.imwrite(date, frame)
        result = False
    schowWindow()

def schowWindow():
    ret,frame = videoCaptureObject.read()
    cv2.imshow('Take a picture',frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        cv2.destroyAllWindows()
    if(cv2.waitKey(1) & 0xFF == ord('w')):
        takepicture()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-"*60 + "\n Take a picture by pressing \"W\" \n" + "\n Close the programm by pressing \"Q\"\n" + "-"*60) #Keybinds
    videoCaptureObject = cv2.VideoCapture(0)
    today = date.today()
    while True:
        schowWindow()