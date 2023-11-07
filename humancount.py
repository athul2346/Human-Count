import cv2
import os

def count_humans(image_path):
    # Load the YOLOv4 model and configuration
    net = cv2.dnn_DetectionModel('F:\\my code\\human count\\yolov4.cfg', 'F:\\my code\\human count\\yolov4.weights')
    net.setInputSize(608, 608)
    net.setInputScale(1.0 / 255)
    net.setInputSwapRB(True)

    # Load the COCO class labels
    with open('F:\\my code\\human count\\coco.names', 'r') as f:
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

input_folder='F:\\my code\\human count\\BRanch Snaps\\'
output_folder='F:\\my code\\human count\\above 2\\'


for item in os.listdir(input_folder):
    image_path=os.path.join(input_folder,item)
    out_path=os.path.join(output_folder,item)
    num_humans=count_humans(image_path)
    if num_humans>2:
        print("more than two persons detected")
        os.replace(image_path,out_path)

# Path to the image you want to analyze
# image_path = '10.17.219.200_01_20230705153351581_LINE_CROSSING_DETECTION.jpg'

# # Count the number of humans in the image
# num_humans = count_humans(image_path)

# print(f"Number of humans detected: {num_humans}")
