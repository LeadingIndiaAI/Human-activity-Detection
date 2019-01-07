import cv2
import numpy as np
import os
import sys

# Root directory of the project
ROOT_DIR = os.path.abspath("../")

# Directory of dataset
DATA_DIR = os.path.join(ROOT_DIR, "dataset")

## =================== Mask RCNN ======================
# Directory of mask RCNN
MRCNN_DIR = os.path.join(ROOT_DIR, "dependencies/Mask_RCNN/")
# Import Mask RCNN
sys.path.append(os.path.join("MRCNN_DIR")) # To find local version of the library
from mrcnn import utils
import mrcnn.model as modellib
# Import COCO config
sys.path.append(os.path.join(MRCNN_DIR, "samples/coco/"))  # To find local version
import coco

# Directory to save logs and trained model
MODEL_DIR = os.path.join(MRCNN_DIR, "logs")

# Local path to trained weights file
COCO_MODEL_PATH = os.path.join(MRCNN_DIR, "mask_rcnn_coco.h5")
# Download COCO trained weights from Releases if needed
if not os.path.exists(COCO_MODEL_PATH):
    utils.download_trained_weights(COCO_MODEL_PATH)

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

class objDetector:
    def __init__(self):
        # Create model object in inference mode.
        model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
        # Load weights trained on MS-COCO
        model.load_weights(COCO_MODEL_PATH, by_name=True)


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

