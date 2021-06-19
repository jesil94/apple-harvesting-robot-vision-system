# vision system for apple harvesting robot YOLOv4
creating a vision system for apple harvesting robot using YOLO algorithm
# steps to develop a custom detector

# 1.Create yolov4 and training folders in your google drive
received gpu
![image](https://user-images.githubusercontent.com/84291100/122655101-d6dfd600-d104-11eb-984f-62ff5af4d259.png)


# 2.Mount drive, link your folder and navigate to the yolov4 folder

# 3.Clone the Darknet git repository

# 4.Create & upload the files we need for training ( i.e. “obj.zip” , “yolov4- custom.cfg”, “obj.data”, “obj.names” and “process.py” ) to your drive
# Data set construction 
Single object with no occlusion,
Multiple objects with occlusion,
Clusters of apples,
Illumination variation,
Shading conditions,
Multiple objects with or without occlusion


# 5.Make changes in the Makefile to enable OPENCV and GPU

# 6.Run make command to build darknet

# 7.Copy the files “obj.zip”, “yolov4-custom.cfg”, “obj.data”, “obj.names”, and “process.py” from the yolov4 folder to the darknet directory

# 8.Run the process.py python script to create the train.txt & test.txt files

# 9.Download the pre-trained YOLOv4 weights

# 10.Train the detector

# 11.Check performance


# performence graph
![image](https://user-images.githubusercontent.com/84291100/122654991-e27ecd00-d103-11eb-921e-fa2e3178d984.png)

# performence check by mean average precision(mAP)
![image](https://user-images.githubusercontent.com/84291100/122655007-004c3200-d104-11eb-9403-4f90f2d86c73.png)

# 12.Test your custom Object Detector 
# Test results on images
![test4](https://user-images.githubusercontent.com/84291100/119716726-46221d00-be1a-11eb-92f3-283c6cdabd46.png)
![download (14)](https://user-images.githubusercontent.com/84291100/119716747-4de1c180-be1a-11eb-9ed3-ca0a8f76bb7f.png)
![test3](https://user-images.githubusercontent.com/84291100/119716768-533f0c00-be1a-11eb-8209-24dde8280820.png)
![download (12)](https://user-images.githubusercontent.com/84291100/119716817-6225be80-be1a-11eb-9a5a-99849cc0613c.png)

# Test results on webcam images
![download (11)](https://user-images.githubusercontent.com/84291100/119716958-8f726c80-be1a-11eb-8aec-34f000921e47.png)
![image](https://user-images.githubusercontent.com/84291100/122654905-4ce33d80-d103-11eb-969c-638044b78fc5.png)
Testing on a higher illumination condtion
![image](https://user-images.githubusercontent.com/84291100/122654923-6ab0a280-d103-11eb-8239-5584d5c2c60d.png)
Testing on a highershading condtion

# Test results on videos



https://user-images.githubusercontent.com/84291100/119975186-62cd6a80-bf6a-11eb-94e6-0027398e7793.mp4


https://user-images.githubusercontent.com/84291100/119975223-6cef6900-bf6a-11eb-8738-05ff0c62b581.mp4


https://user-images.githubusercontent.com/84291100/119975241-724cb380-bf6a-11eb-9838-345b6531cdc1.mp4



