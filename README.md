# DroneFaceDetection

## 3.1	Preparing Environment

First of all, we ‘d prepared an environment that is compatible to artificial intelligence, in our Raspberry Pi B+ we ‘d installed an OS named “Respberrian Strach”, then we installed Cmake and OpenCV models.

## 3.2	Preparing Dataset
 
###### 3.2.1		Face Detection
In our artificial intelligent model, we imported libraries from OpenCV that is capable of detect faces in run time video. The inputs an image from real time video, detects a face through dark pixels, transform it to grayscale and then crop the area of detected face.

###### 3.2.2		Samples

In our model when a face is detected by OpenCV library, the program starting capturing the pictures of face detected area in grayscale it takes minimum 50 pictures an in interval of fewest seconds, the maximum limit is in our hand we can set the limit so that we gather quality data and it will result the most efficient results. It makes a square boundary of the only frontal face and only saves the boundary’s area in order to provide “Structured Data” to our model, and saves it to our dataset folder.

###### 3.2.3		Assigning Id’s

When the pictures are captured our program allots a unique id to every unique person, the pictures are saved along with its id in order to make every face different.

## 3.3	Training

We are training our classifier through papered dataset samples and generates an “yml” file of classifier, it’s like haarcascade, the data we are providing through dataset is a kind of structured data (Only frontal faces). The generated yml file has a matrix having the pixels of pictures presented in dataset, the number of rows is one and the number of columns depends upon the dataset’s data. The sample matrix, the yml file is being saved in trainer.

## 3.4	Recognition

The recognizer program reads all the data from the yml file that is produced by the trainer. We have an import detector that detects a face just like we ‘d stated above and then compare its pixels in the yml file’s matrix, after comparing it initialize the ids and assigns it a specified label. The recognition process is capable of recognizing any person in runtime video. If there is no label initialized the program will automatically allot a number to the person, or if person is not recognized it will show the “UNKOWN LABEL”.


The ratio of result accuracy is depending upon the provided data, the much the structured data results the higher accuracy in results. The model is also capable of detecting more than one person (multiple unwanted persons) in frame.


## 3.5	Location Specification

We ‘d used web scraping technique to get the current IP of detected person, and using same technique we obtain the real time latitude and longitude or preceding IP in order to get the exact location of that person.

## 3.6	Generating Email 

As soon as the model recognize the person, the classifier generates an automated email using “smtplib” to send the current location (latitude, longitude), name (label), picture and current date and time of the recognized person. The email will generate automatically after 50 captures (fewest seconds), in order to increase accuracy, and it will also trigger after 50 more captures.

