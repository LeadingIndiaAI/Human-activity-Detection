import cv2
import numpy as np
import os
import sys

# Root directory of the project
ROOT_DIR = os.path.abspath("./../")

# Directory of dataset
DATA_DIR = os.path.join(ROOT_DIR, "dataset")

## =================== Mask RCNN ======================
# Directory of mask RCNN
MRCNN_DIR = os.path.join(ROOT_DIR, "dependencies/Mask_RCNN/")
# Import Mask RCNN
# sys.path.append(os.path.join("MRCNN_DIR")) # To find local version of the library
sys.path.append(MRCNN_DIR) # To find local version of the library
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

class WriteVideo():
    def __init__(self, destination):
        self.destination = os.path.join(DATA_DIR, destination)
        
    def writeFrame(self, frame):
        cv2.imwrite(self.destination, frame)
class ObjDetector:
    def __init__(self):
        class InferenceConfig(coco.CocoConfig):
            # Set batch size to 1 since we'll be running inference on
            # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
            GPU_COUNT = 1
            
            IMAGES_PER_GPU = 1

        config = InferenceConfig()
        config.display()
        # Create model object in inference mode.
        self.model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)
        # Load weights trained on MS-COCO
        self.model.load_weights(COCO_MODEL_PATH, by_name=True)
        self.class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']

    def apply_mask(self, image, mask):
        """Apply the given mask to the image.
        """
        for c in range(3):
            image[:, :, c] = np.where(mask == 0, 0, image[:, :, c])
        return image

    def detectPerson(self, image):
        results = self.model.detect([image], verbose=1)
        r = results[0]
        person_mask = np.array([])
        for i, class_id in enumerate(r['class_ids']):
            if self.class_names[class_id] == 'person':
                mask = r['masks'][:, :, i]
                if person_mask.size == 0:
                    person_mask = mask.copy()
                else:
                    person_mask += mask
        masked_img = self.apply_mask(image, person_mask)
        return masked_img
#if __name__ == '__main__':
    #vid = ReadVideo('HMDB51/1/1.avi')
    #frame = None
    #stack = None
    #success, frame = vid.getFrame()
    #cv2.imshow('frame', frame)
    #od = objDetector()
    #cv2.imshow(od.detectPerson(frame))
    #frameStack = vid.getFrameStack()
    #cv2.imshow('stack', frameStack[0])
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

