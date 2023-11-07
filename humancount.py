import cv2
import os

def count_humans(image_path):
    # Load the YOLOv4 model and configuration
    net = cv2.dnn_DetectionModel('.\\yolov4.cfg', '.\\yolov4.weights')
    net.setInputSize(608, 608)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)

    # Load the COCO class labels
    with open('.\\coco.names', 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    # Read the image
    image = cv2.imread(image_path)

    # Perform object detection
    class_ids, confidences, boxes = net.detect(image, confThreshold=0.5, nmsThreshold=0.4)

    # Initialize variables
    num_humans = 0

    # Loop over the detections
    if len(class_ids) > 0:
        for class_id, confidence, box in zip(class_ids.flatten(), confidences.flatten(), boxes):
            # Check if the detected object is a human
            if classes[class_id] == 'person' and confidence > 0.3:
                num_humans += 1

    return num_humans

input_folder='.\\input\\'
output_folder='.\\output\\'


for item in os.listdir(input_folder):
    image_path=os.path.join(input_folder,item)
    out_path=os.path.join(output_folder,item)
    num_humans=count_humans(image_path)
    if num_humans>2:
        print("more than two persons detected")
        os.replace(image_path,out_path)


