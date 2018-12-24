# Program To Read video 
# and Extract Frames 
import cv2 
import sys
import os
  
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path)
    os.system("mkdir "+sys.argv[2]) 
  
    # Used as counter variable 
    count = 0
    frameCount = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        if count % 6 == 0:
            # Saves the frames with frame-count 
            destination = sys.argv[2] + "/frame" + str(frameCount) +'.jpg'
            cv2.imwrite(destination, image) 
            frameCount += 1
  
        count += 1
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(sys.argv[1]) 
