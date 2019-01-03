## Structure of the project:
* The datasets are expected to be in the structure as shown.
* The models will be with their respective names.
```
projectbu
|
|-- dataset
|   |-- UCF101
|   |-- HMDB51
|
|-- dependencies
|   |-- Mask_RCNN
|
|-- scripts
|
|-- CNN
```
* To extract the frames, run the command below:
```
bash frames.sh     # To extract just the frames
bash framesbr.sh   # To extract frames with Background Reduction
```
