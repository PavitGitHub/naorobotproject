import os
import sys
# from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
from inference_sdk import InferenceHTTPClient

# def load_model(model_path='yolov8n.pt'):
#     """Load the YOLOv8 model from the specified path."""
#     model = YOLO(model_path)
#     return model

def predict_and_draw_bboxes(image_path):
    """Predict the bounding boxes and draw them on the image."""
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found: {image_path}")
    
    # results = model.predict(image_path)

    # for box in results[0].boxes:
    #     x1, y1, x2, y2 = box.xyxy[0]
    #     conf = box.conf[0]
    #     cls = box.cls[0]
        
    #     cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    #     label = f"{model.names[int(cls)]} {conf:.2f}"
    #     cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # plt.figure(figsize=(10, 10))
    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.axis('off')
    # plt.show()

    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="nNNDxwcGa4LCjLShqend"
    )

    results = CLIENT.infer(img, model_id="lightweight_objdetect/7")
    return results

def process_images(image_paths):
    """Process a list of image paths, making predictions and displaying results."""
    for image_path in image_paths:
        print(f"Processing {image_path}...")
        results = predict_and_draw_bboxes(model, image_path)
        print(f"Results: {results}")

if __name__ == "__main__":
    print('Loading model . . .')
    # model = load_model()
    # COMMENTED OUT DURING TESTING
    print('intialising command loop . . .')
    
    # image_filenames = ['C:/Users/joelm/Documents/GitHub/naorobotproject/uploads/images/image1.jpg']
    # print(f'Image files {image_filenames}')
    # # Ensure the images exist
    # image_paths = [filename for filename in image_filenames if os.path.isfile(filename)]

    # if not image_paths:
    #     print("No valid images to process.")
    # else:
    #     # Process images and display predictions
    #     process_images(image_paths, model)
