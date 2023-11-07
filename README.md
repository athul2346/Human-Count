# Human Count
# Overview

The "Human Count" project is designed to detect and count the number of humans present in an image using the YOLO (You Only Look Once) model. This README provides an overview of the project and instructions on how to use the provided human-count.py script for human detection and counting.
# Project Details

The human-count.py script accepts an input image and detects the presence of humans. By default, the threshold is set to 2 humans. If more than two humans are detected in an image, the image is moved to an output folder.
# YOLO Model

The project utilizes the YOLO model for human detection. The necessary YOLO configuration files (yolo.cfg) and class names file (coco.names) are already included in this repository. However, to use the YOLO model effectively, you'll need to download the yolov4.weights file from the following link:

[Download YOLOv4 Weights](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiPm5GYzrGCAxVgTGwGHQm3AD0QFnoECAUQAQ&url=https%3A%2F%2Fgithub.com%2FAlexeyAB%2Fdarknet%2Freleases%2Fdownload%2Fdarknet_yolo_v3_optimal%2Fyolov4.weights&usg=AOvVaw30if4joxtTaS8DAh12vYQ4&opi=89978449)


Make sure to download the yolov4.weights file from the provided link and place it in the same directory as the project files.
# Usage

    Create two folders within your project directory:
        An "input" folder for providing input images to be processed.
        An "output" folder where images with more than two detected humans will be saved.

    Place your input images in the "input" folder.

    Run the human-count.py script. It will process the input images and move those with more than two detected humans to the "output" folder.

# Note

    Adjust the threshold for human detection by modifying the default value in the human-count.py script.

Thank you for using the "Human Count" project. If you encounter any issues or have questions, please feel free to reach out for assistance.
