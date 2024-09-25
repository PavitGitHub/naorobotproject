import os
import sys
# from ultralytics import YOLO
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
        return f"{vertical} {horizontal}"

def predict_and_draw_bboxes(image_path):
    """Predict the bounding boxes using an API client and draw them on the image."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found: {image_path}")
    
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="nNNDxwcGa4LCjLShqend"
    )
    
    # model = YOLO(model_path)
    # results = model.predict(image_path)
    
    results = CLIENT.infer(image_path,model_id="lightweight_objdetect/7")
    positions = []

    
    for box in results['predictions']:
        x1 = box['x'] - box['width'] / 2
        y1 = box['y'] - box['height'] / 2
        x2 = box['x'] + box['width'] / 2
        y2 = box['y'] + box['height'] / 2
        
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        # label = f"{box['class']} {box['confidence']:.2f}"
        label = f"{box['class']}"

        cv2.putText(img, label, (int(x1), int(y1) - 10), 0, 0.5, (255, 255, 255), 2)
        position = determine_position(img, x1, y1, x2, y2)
        
        positions.append((label, position))
    
    filename = "pred/pred" + os.path.basename(image_path)
    print(filename)
    cv2.imwrite(filename, img)
    return positions



def process_images(image_paths):
    """Process a list of image paths, making predictions and displaying results."""
    # use for local testing
    image_paths = glob.glob("test/*")
    # image_paths = glob.glob(image_path)
    for image_path in image_paths:
        print(f"Processing {image_path}...")
        results = predict_and_draw_bboxes(image_path)
        print(f"Results: {results}")

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
