# apple-harvesting-robot-vision-system
creating a vision system for apple harvesting robot using YOLO algorithm
# stepsto develop a custom detector

1.Create yolov4 and training folders in your google drive

2.Mount drive, link your folder and navigate to the yolov4 folder

3.Clone the Darknet git repository
Create & upload the files we need for training ( i.e. “obj.zip” , “yolov4- custom.cfg”, “obj.data”, “obj.names” and “process.py” ) to your drive
Make changes in the Makefile to enable OPENCV and GPU
Run make command to build darknet
Copy the files “obj.zip”, “yolov4-custom.cfg”, “obj.data”, “obj.names”, and “process.py” from the yolov4 folder to the darknet directory
Run the process.py python script to create the train.txt & test.txt files
Download the pre-trained YOLOv4 weights
Train the detector
Check performance
Test your custom Object Detector
