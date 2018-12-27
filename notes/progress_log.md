# Progress log and Resource section
## 17 Dec:
* We have been assigned the project: **Human Activity Detection** (using video feed)
* Met Dr. Bishwas:
	* It would be best to limit the frame rate to 5 fps, as beyond this increase in data wouldn't result in increase in useful information.
## 18 Dec:
* Met Dr. Shreedhar for some insight upon our project:
	* First step would be human and object detection
	* Seems like Cafe is a heavily used framework (against my previous misconception)
	* According to him each framework is suited for particular kind for problem, e.g. pytorch for GANs and cafe for when we need speed.
* Started Coursera's deeplearning.ai CNN course by Andrew Ng
## 19 Dec:
* Got access to DGX (Nvidia supercomputer)
## 20 Dec:
* [CS231n Winter 2016: Lecture 4: Backpropagation, Neural Networks 1](https://www.youtube.com/watch?v=i94OvYb6noo): I you are like me and have learned most of DL from Deeplearningl.ai course then chances are you might not feel comfortable enough in back propagation. This video by Andrej Karpathy is an excellent resource to brush up this topic.
* Haven't been able to understand the use of docker for server, properly yet.
* **tmux** is used to create sessions in server which can be used to keep a process running even when disconnected. I might consider learning to work with it.
## 21 Dec:
* We have planed to lookup for research papers in the field.
* Adarsh came up with the idea to gray scale the background to increase the accuracy.
## 24 Dec:
* We have implemented an automated script for frame extraction and it took us 2 days to implement! (Most of the work done by Adarsh)
* Although Shreedhar sit (SD) told us to do human detection, but we are still confused, Why?
* We thought of specific objects such as comb in the frame. If there exists a comb in frame, it would increase the probability of the action combing. Although this might result in a increment in the accuracy on the given dataset but do we want a high accuracy on dataset or a general purpose algorithm?
* We are thinking of stacking frames at different time along an access and applying a 3D convolution along that axis. I believe this might tackle the problem of time and we might be able to produce some results only by applying conv. net.
## 25 Dec:
* I wanted to start implementing a CNN using keras but got stuck on importing data. No course ever taught the method to import data. So, I decided to contact SD sir for help.
* Following are the points that came up in the conversation with SD sir:
	* googling "video classification using python" resulted in good enough articles containing codes to learn to import such data.
	* My problem is totally different from video classification. Till today I considered video classification and human activity recognition different names for same problem, but they are not!
	* I need to do human detection and crop the relevant portion of frame and resize it to a constant frame size using openCV resize function and feed the output to NN.
	* Body part detection and finding relative distance between them could help.
## 26 Dec:
* Started learning openCV form YouTube [playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq). OpenCV is a great tool to learn, especially if you are into image and video processing.
* Learned to use tmux
* Tried to access dgx but the allocated memory is 100% full.
* Learned to import data, crop part of frame.
* By morning I implemented programs for foreground extraction and background reduction.
## 27 Dec:
* I are planing on using the tensorflow API for human detection task.
* We stumbled over [pose recognition API by CMU](https://github.com/CMU-Perceptual-Computing-Lab/openpose). Very cool, you should check it out!!
* We met Biswas sir and showed him our progress, he seems pleased. Also he told us to implement model only with CNN for now, and not use RNN.
* Everything seems messed up! We didn't knew about the facial expressions in the dataset (HMDB51).
* We also found out another relevant dataset UCF101
