from naoqi import ALProxy
import sys
import vision_definitions
import numpy as np
import cv2
import time  # For recording functionality

# Initialize TTS proxy
tts = ALProxy("ALTextToSpeech", "192.168.0.170", 9559)

def check_if_simulator(robot_ip, port=9559):
    """Check if the environment is a simulator or a real robot."""
    try:
        # Create a proxy to ALMemory to check simulator status
        memoryProxy = ALProxy("ALMemory", robot_ip, port)

        # Try to get the robot's head pitch sensor value
        head_pitch_sensor = memoryProxy.getData("Device/SubDeviceList/HeadPitch/Position/Sensor/Value")

        if head_pitch_sensor is not None:
            print("Real robot detected. Head pitch sensor value: {}".format(head_pitch_sensor))
            return False  # False means it's a real robot
        else:
            print("Simulator detected.")
            return True  # True means it's a simulator

    except Exception as e:
        # If we cannot retrieve sensor data, assume it's a simulator
        print("Simulator likely detected. Error: {}".format(e))
        return True

def get_camera_image(robot_ip, port=9559):
    """Capture an image from the robot's camera."""
    try:
        # Create a proxy to ALVideoDevice
        camProxy = ALProxy("ALVideoDevice", robot_ip, port)

        # Define resolution, color space, and frame rate
        resolution = vision_definitions.kQVGA  # 320x240 resolution
        colorSpace = vision_definitions.kBGRColorSpace  # Use BGR color space
        fps = 30

        # Subscribe to the video stream
        nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)

        # Capture an image
        image = camProxy.getImageRemote(nameId)

        # Unsubscribe from the video stream
        camProxy.unsubscribe(nameId)

        if image is None:
            print("Failed to retrieve image from the robot.")
            return None

        # Extract image width, height, and the image data array
        width = image[0]
        height = image[1]
        array = image[6]

        # Convert the image to a numpy array
        img_array = np.frombuffer(array, dtype=np.uint8).reshape((height, width, 3))

        print("Image captured successfully: Resolution {}x{}".format(width, height))
        return img_array

    except Exception as e:
        print("Error while capturing image: {}".format(e))
        return None

def display_image(image_array):
    """Display the captured image in a window."""
    # Convert the image from BGR to RGB, as OpenCV uses BGR by default
    rgb_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
    
    # Display the image in a window
    cv2.imshow('Captured Image', rgb_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close the window after key press

def save_image(image_array, filename='captured_image.png'):
    """Save the captured image to a file."""
    # Save the image as a file (no need to convert the color for saving)
    cv2.imwrite(filename, image_array)
    print("Image saved as {}".format(filename))

def get_frame():
    """Capture, display, and save an image from the robot's camera."""
    img = get_camera_image('192.168.0.170')
    if img is not None:
        display_image(img)
        save_image(img)
    else:
        print("Failed to retrieve image.")

def send_tts(text="This command has been sent from the server"):
    """Send a text-to-speech command to the robot."""
    error = False
    try:
        tts.say(text)
    except Exception as e:
        print("Error in TTS: {}".format(e))
        error = True
    finally:
        return error

def test_input_from_nodejs():
    """Test function to confirm input from Node.js."""
    print("Python function called!")

def start_recording(duration=5, filename="/home/nao/audio.wav"):
    """Start recording audio from the robot's microphones."""
    try:
        audioProxy = ALProxy("ALAudioRecorder", "192.168.0.170", 9559)
        channels = [0, 0, 1, 0]  # Use microphone channel 2
        audioProxy.startMicrophonesRecording(filename, "wav", 16000, channels)
        print("Recording started, saving to {}".format(filename))
        time.sleep(duration)
        audioProxy.stopMicrophonesRecording()
        print("Recording stopped.")
    except Exception as e:
        print("Error while recording audio: {}".format(e))

if __name__ == "__main__":
    print('Initializing NAO controller . . .')
    command_map = {
        'get_frame': get_frame,
        'send_tts': send_tts,
        'test_input_from_nodejs': test_input_from_nodejs,
        'start_recording': start_recording,
    }
    while True:
        line = sys.stdin.readline().strip()
        if line:
            # Check if the command includes arguments
            if ' ' in line:
                cmd_parts = line.split(' ', 1)
                command = cmd_parts[0]
                args = cmd_parts[1]
                if command in command_map:
                    if command == 'send_tts':
                        send_tts(args)
                    elif command == 'start_recording':
                        try:
                            duration = float(args)
                            start_recording(duration=duration)
                        except ValueError:
                            print("Invalid duration. Please enter a number.")
                    else:
                        print("Command {} does not accept arguments.".format(command))
                else:
                    print("Unknown command: {}".format(command))
            else:
                if line in command_map:
                    command_map[line]()
                else:
                    print("Unknown command: {}".format(line))
