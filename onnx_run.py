import onnxruntime
import cv2
import numpy as np
import utils


# preprocessing of image
img_file = 'img4.jpg'
img = cv2.imread(img_file)
img = cv2.resize(img, (416,416))
img = np.swapaxes(img, 0, 2)
img = np.swapaxes(img, 1, 2)/255.0
img = np.expand_dims(img, axis=0).astype('float32')

#print(img.shape)

session = onnxruntime.InferenceSession("yolov4_1_3_416_416_static.onnx") # onnx model
#print(session.get_inputs()[0])
inputs = {session.get_inputs()[0].name: img} 
results = session.run(None, inputs) # getting results

result = utils.post_processing(img, 0.4, 0.6, results) # img, conf, iou, output

with open('obj.names') as c: # getting all names from a file
    names = [name.replace('\n','') for name in c.readlines()]
    img = utils.plot_boxes_cv2(cv2.imread(img_file), result[0], savename=None, class_names=names, color=None) # plot bounding box

cv2.imwrite('test.jpg', img) # saving file
