from datetime import datetime
from data import Observation
import cv2
import time



def run(observation: Observation) -> None:
    # define a video capture object
    vid = cv2.VideoCapture(0)
    vid.set(3,1920)
    vid.set(4,1080)
  
    while(True):
      
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()