# apple-harvesting-robot-vision-system
creating a vision system for apple harvesting robot using YOLO algorithm
# stepsto develop a custom detector

1.Create yolov4 and training folders in your google drive

2.Mount drive, link your folder and navigate to the yolov4 folder

3.Clone the Darknet git repository

4.Create & upload the files we need for training ( i.e. “obj.zip” , “yolov4- custom.cfg”, “obj.data”, “obj.names” and “process.py” ) to your drive

5.Make changes in the Makefile to enable OPENCV and GPU

6.Run make command to build darknet

7.Copy the files “obj.zip”, “yolov4-custom.cfg”, “obj.data”, “obj.names”, and “process.py” from the yolov4 folder to the darknet directory

8.Run the process.py python script to create the train.txt & test.txt files

9.Download the pre-trained YOLOv4 weights

10.Train the detector

11.Check performance

12.Test your custom Object Detector
