# Human Activity Recognition Report (13 Jan 2018)

## by Dhruv Garg and Adarsh Kumar - Thapar University

### Dataset:
Following are the deductions about dataset
* **UCF101**
	* Camera static
	* Whole frame consists of moving objects
* **HMDB51**
	* Camera moving
	* Human in main focus
	* Facial actions involved

### Progress:

#### Pre-process
We coded a script for frame extraction from the video and droped the frame rate to around 6 fps. We tested code for Foreground Extraction (not so useful) and Background Subtraction. We also implemented code for human detection and extracting it from frame using Mask RCNN. Although we were able to use Mask RCNN on single images but running a script for full dataset results in memory full error on laptop.

Since the dataset involves facial actions like smiling, laugh, talk, hence face an be extracted using face detection and a separate neural network can be implemented for it, resulting in an hybrid network.

Other pre-processing techniques that can be used:
* CMU pose detection: this API outputs stick figures representing human body posture
* Crop and resize human from the frame
* Optical flow (as suggested by Dr. Shridhar)

#### Neural Network
We came up with the following ideas for neural network (need some time to implement them):
* 3D CNN with time axis
** Was the first idea we wanted to implement, however due to difference in no. of frames, we were having some difficulties
* CNN to RNN combination
** We used a pretrained inception v3 model right until the softmax layer and then used the features extracted to feed into a simgle layer LSTM followed by 101 output nodes.
** achieved accuracy of 67.83 % but we need to work a bit more on it to shoot the accuracy.
* Autoencoders to RNN
