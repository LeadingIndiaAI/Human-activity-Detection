import cv2
import numpy as np
import os
import sys

# Root directory of the project
ROOT_DIR = os.path.abspath("../")

# To find local versions of librarys
sys.path.append(ROOT_DIR)

# Directory of dataset
DATA_DIR = os.path.join(ROOT_DIR, "dataset")

class ReadVideo:
    def __init__(self, vidAddress):
        self.vidAddress = os.path.join(DATA_DIR, vidAddress)
        self.vid = cv2.VideoCapture(self.vidAddress)
        self.stack = []

    def getFrame(self):
        return self.vid.read()

    def getFrameStack(self):
        if not self.stack:
            vid = cv2.VideoCapture(self.vidAddress)
            while True:
                ret, frame = vid.read()
                if ret:
                    self.stack.append(frame)
                else:
                    break
        # return array(self.stack)
        return np.asarray(self.stack)

if __name__ == '__main__':
    vid = ReadVideo('HMDB51/1/1.avi')
    frame = None
    stack = None
    success, frame = vid.getFrame()
    cv2.imshow('frame', frame)
    frameStack = vid.getFrameStack()
    cv2.imshow('stack', frameStack[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

