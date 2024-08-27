import sys
sys.path.append('/Users/xiaokan/Desktop/it project/naorobotproject/Python/2.7/pynaoqi-python2.7-2.8.6.23-mac64-20191127_144231 2/lib/python2.7/site-packages')
from naoqi import ALProxy
import vision_definitions
import numpy as np

def get_camera_image():
    # Create a proxy to the ALVideoDevice module
    camProxy = ALProxy("ALVideoDevice", "nao.local", 9559)

    # Define resolution, color space, and frame rate
    resolution = vision_definitions.kQVGA  # 320x240 resolution
    colorSpace = vision_definitions.kYUVColorSpace
    fps = 30

    # Subscribe to the video stream
    nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)

    # Capture an image
    image = camProxy.getImageRemote(nameId)

    # Unsubscribe from the video stream
    camProxy.unsubscribe(nameId)

    return image

def simulate_camera_image():
    # Simulate a 320x240 grayscale image
    width, height = 320, 240
    simulated_image = np.random.randint(0, 255, (height, width), dtype=np.uint8)
    return simulated_image

def test_camera_functionality():
    # Test using simulated image data
    image = simulate_camera_image()
    if image is None:
        print "Failed to retrieve image."
    else:
        print "Simulated image data successfully retrieved."

if __name__ == "__main__":
    test_camera_functionality()
