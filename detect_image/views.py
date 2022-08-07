from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.files.temp import NamedTemporaryFile

import io
import os
from PIL import Image
import cv2
import numpy as np
from base64 import b64decode, b64encode
from .utils import *
from .darknet import Darknet
import urllib

@csrf_exempt
def yolo_detect_api(request):
    data = {'success':False}
    img = ''
    result = None

    if request.method == "POST":
        if request.FILES.get('img') is not None:
            inputImg = request.FILES.get('img')
            raw_image = inputImg.read()
            image = np.asarray(bytearray(raw_image))
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            result, img = yolo_detect(image)
    
        if result:
            data['success'] = True

    data['objects'] = result
    data['resultImage'] = img
    return JsonResponse(data)

def detect(request):
    return render(request, 'index.html')

def yolo_detect(original_image):
    cfg_file = './cfg/yolov3.cfg'
    weight_file = './weights/yolov3.weights'
    namesfile = 'data/coco.names'

    m = Darknet(cfg_file)
    m.load_weights(weight_file)
    class_names = load_class_names(namesfile)

    resized_image = cv2.resize(original_image, (m.width, m.height))

    nms_thresh = 0.6
    iou_thresh = 0.4

    boxes = detect_objects(m, resized_image, iou_thresh, nms_thresh)
    url = plot_boxes(original_image, boxes, class_names, plot_labels = True)
    objects = print_objects(boxes, class_names)
    return objects, url
