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

# def predict_and_draw_bboxes(image_path):
#     """Predict the bounding boxes and draw them on the image."""
#     # Load the image
#     img = cv2.imread(image_path)
#     if img is None:
#         raise ValueError(f"Image not found: {image_path}")
    
#     # results = model.predict(image_path)

#     # for box in results[0].boxes:
#     #     x1, y1, x2, y2 = box.xyxy[0]
#     #     conf = box.conf[0]
#     #     cls = box.cls[0]
        
#     #     cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
#     #     label = f"{model.names[int(cls)]} {conf:.2f}"
#     #     cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # plt.figure(figsize=(10, 10))
#     # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#     # plt.axis('off')
#     # plt.show()

    
#     results = CLIENT.infer(img, )
#     return results

def predict_and_draw_bboxes(image_path):
    """Predict the bounding boxes using an API client and draw them on the image."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found: {image_path}")
    
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="nNNDxwcGa4LCjLShqend"
    )
    # get_model( model_id="lightweight_objdetect/7")
    
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

        # cv2.putText(img, label, (int(x1), int(y1) - 10), cv2., 0.5, (255, 255, 255), 1)
        position = determine_position(img, x1, y1, x2, y2)
        
        positions.append((label, position))
        
    # uncomment to show the annotated images
    # cv2.imshow("Detected Objects", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
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
