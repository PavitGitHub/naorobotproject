import os
import sys
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
from inference_sdk import InferenceHTTPClient
# from inference import get_model
import glob

# def load_model(model_path='yolov8n.pt'):
#     """Load the YOLOv8 model from the specified path."""
#     model = YOLO(model_path)
#     return model

model_id = "lightweight_objdetect/7"
api_key = "nNNDxwcGa4LCjLShqend"

import cv2
import time

def extract_frames(video_source, output_folder, frames_per_second=2):
    # Start capturing video from the source
    cap = cv2.VideoCapture(video_source)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the frames per second of the video source
    source_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(source_fps / frames_per_second)

    current_frame = 0
    extracted_count = 0

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break  # Break the loop if no frame is captured

        if current_frame % frame_interval == 0:
            frame_name = f"{output_folder}/frame_{extracted_count}.jpg"
            cv2.imwrite(frame_name, frame)
            extracted_count += 1
            print(f"Extracted Frame: {frame_name}")

        current_frame += 1

        time.sleep(1 / source_fps)

    cap.release()
    print("Finished extracting frames.")

# Usage example:
# extract_frames(0, 'output_frames')  # for webcam, use 0 as video source

def determine_position(img, x1, y1, x2, y2):
    """Determine the position of the bounding box within the image."""
    height, width, _ = img.shape
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2

    if x_center < width / 3:
        horizontal = "left"
    elif x_center < 2 * width / 3:
        horizontal = "center"
    else:
        horizontal = "right"
        
    if y_center < height / 3:
        vertical = "top"
    elif y_center < 2 * height / 3:
        vertical = "center"
    else:
        vertical = "bottom"
        
    if vertical=="center" and horizontal == "center":
        return "center"
    else:
        return f"{horizontal}"

def predict_and_draw_bboxes(image_path):
    """Predict the bounding boxes using the YOLO model and return detected objects with their positions."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found: {image_path}")
    
    model_path = "best.pt"
    model = YOLO(model_path)
    results = model.predict(image_path, save=True, project='pred')
    
    # Initialize a list to store detected objects with positions
    detected_objects = []

    # Since results may contain multiple images, iterate over them
    for result in results:
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls[0].item())
            class_name = model.names[class_id]  # Using default class names

            # Get bounding box coordinates
            x1, y1, x2, y2 = box.xyxy[0].tolist()  # [x1, y1, x2, y2]

            # Determine position
            position = determine_position(img, x1, y1, x2, y2)

            # Append object name and position to the list
            detected_objects.append({'object': class_name, 'position': position})

    unique_objects = list({obj['object'] for obj in detected_objects})

    # print("Objects detected in the image:", [obj['object'] for obj in detected_objects])
    # print("Unique objects detected:", unique_objects)
        
    return detected_objects

def process_images(image_paths):
    """Process a list of image paths, making predictions and displaying results."""
    # Use for local testing
    image_paths = glob.glob("test/*")
    for image_path in image_paths:
        print(f"Processing {image_path}...")
        results = predict_and_draw_bboxes(image_path)
        print("Results:")
        for obj in results:
            print(f"Object: {obj['object']}, Position: {obj['position']}")




# def process_images(image_paths):
#     """Process a list of image paths, making predictions and displaying results."""
#     # use for local testing
#     image_paths = glob.glob("test/*")
#     # image_paths = glob.glob(image_path)
#     for image_path in image_paths:
#         print(f"Processing {image_path}...")
#         results = predict_and_draw_bboxes(image_path)
#         print(f"Results: {results}")

if __name__ == "__main__":
    print('Loading model . . .')
    # model = load_model()
    # COMMENTED OUT DURING TESTING
    print('intialising command loop . . .')
    while True:
        line = sys.stdin.readline().strip()
        if line:
            print(f'Executing command {line} . . .')
            eval(line)

    # image_filenames = ['C:/Users/joelm/Documents/GitHub/naorobotproject/uploads/images/image1.jpg']
    # print(f'Image files {image_filenames}')
    # # Ensure the images exist
    # image_paths = [filename for filename in image_filenames if os.path.isfile(filename)]

    # if not image_paths:
    #     print("No valid images to process.")
    # else:
    #     # Process images and display predictions
    #     process_images(image_paths, model)
