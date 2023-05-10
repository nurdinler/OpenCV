import cv2 as cv
import matplotlib as plt

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

def rescaleFrame(frame,scale=0.15): # works for videos,images and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale) # 0 is basically the height of the image
    dimension  = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

model = cv.dnn_DetectionModel(frozen_model, config_file)
classLabels = []
file_name = 'Labels.txt'
with open(file_name,'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')
cap = cv.VideoCapture('peoplecount1.mp4')
font_scale = 3
font = cv.FONT_HERSHEY_PLAIN
while True:
    ret,theframe = cap.read()
    frame = rescaleFrame(theframe)
    ClassIndex, confidece, bbox = model.detect(frame,confThreshold=0.55)
    print(ClassIndex)
    if (len(ClassIndex)!=0):
        for ClassInd,conf, boxes in zip(ClassIndex.flatten(), confidece.flatten(), bbox):            
            if(ClassInd <= 80):
                cv.rectangle(frame,boxes,(255,0,0),2)
                cv.putText(frame,classLabels[ClassInd-1],boxes[0]+10,boxes[1]+40,font,font_scale=(0,255,0))
    cv.imshow('CCTV',frame)    
    if cv.waitKey(2) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
cv.waitKey(0)