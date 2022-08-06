# Object-Detection-API

The django web-app detects object using YOLOv3 and acts as an API.

You can download the weights by - 
```
    $ wget https://pjreddie.com/media/files/yolov3.weights
```


#### Input

You can send either of the following parameters -

Parameter | Type                           | Description
--------- | ------------------------------ | ---------------------------------------------------------------------------------
image     | file                           | Image file that you want to detect.

#### Result

Parameter | Type                | Description
--------- | ------------------- | -----------------------------------------------
success   | bool                | Whether classification was successful or not 
detect    | class label, float  | pair of label and its confidence
image     | image               | Result image with bounding boxes

Example:  {"success": true, "detect": {  "dog": 0.9989, "truck": 0.9999 }, 'image':"image.png"}<br>
"detect" will be empty if no objects are detected.
