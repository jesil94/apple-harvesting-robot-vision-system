# apple-harvesting-robot-vision-system using YOLOv4
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

# Test results on images
![test4](https://user-images.githubusercontent.com/84291100/119716726-46221d00-be1a-11eb-92f3-283c6cdabd46.png)
![download (14)](https://user-images.githubusercontent.com/84291100/119716747-4de1c180-be1a-11eb-9ed3-ca0a8f76bb7f.png)
![test3](https://user-images.githubusercontent.com/84291100/119716768-533f0c00-be1a-11eb-8209-24dde8280820.png)
![download (12)](https://user-images.githubusercontent.com/84291100/119716817-6225be80-be1a-11eb-9a5a-99849cc0613c.png)

# Test results on webcam images
![download (11)](https://user-images.githubusercontent.com/84291100/119716958-8f726c80-be1a-11eb-8aec-34f000921e47.png)
![download (6)](https://user-images.githubusercontent.com/84291100/119716993-9bf6c500-be1a-11eb-966c-6469cfe3d1e0.png)


