#import stuff
import cv2 as cv
import pyautogui
import numpy as np

#width and height
screen_size = pyautogui.size()

#inisializing object
video = cv.VideoWriter('Recording.avi',
                       cv.VideoWriter_fourcc(*'MJPG'),
                       20,screen_size)

print("Recording This...")
while True:
    #screenshot
    screen_shot_image = pyautogui.screenshot()

    #convert to array
    frame = np.array(screen_shot_image)

    #change from BGR to RGB
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)

    #write frame
    video.write(frame)

    #display the live recording
    cv.imshow("Recording Frame(Minimize it)", frame)    
    if cv.waitKey(1) == ord("q"):
        break

cv.destroyAllWindow()
video.release()

#credits to https://www.techgeekbuzz.com/how-to-make-a-screen-recorder-in-python/

