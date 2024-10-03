# -*- coding: utf-8 -*-
import sys
from naoqi import ALProxy
import time

def control_nao(command):
    try:
        motion = ALProxy("ALMotion", "localhost", 9559)
        posture = ALProxy("ALRobotPosture", "localhost", 9559)

        # Ensure stiffness is set to 1.0
        motion.setStiffnesses("Body", 1.0)

        # Ensure robot is in the correct posture
        posture.goToPosture("StandInit", 0.5)

        if command == "forward":
            motion.moveToward(0.5, 0, 0)  # Move forward
            print("Moving forward")

        elif command == "backward":
            motion.moveToward(-0.5, 0, 0)  # Move backward
            print("Moving backward")

        elif command == "left":
            motion.moveToward(0, 0, 0.5)  # Turn left in place
            print("Turning left in place")

        elif command == "right":
            motion.moveToward(0, 0, -0.5)  # Turn right in place
            print("Turning right in place")

        elif command == "stop":
            print("Stopping motion")
            success = False
            retries = 3  # Allow 3 retries
            while retries > 0 and not success:
                try:
                    motion.stopMove()
                    success = True
                    print("Motion stopped successfully")
                except Exception as e:
                    retries -= 1
                    print("Error stopping motion: {}. Retrying...".format(str(e)))
                    time.sleep(1)  # Wait 1 second before retrying

            if not success:
                print("Failed to stop motion after retries")

        else:
            print("Unknown command")

    except Exception as e:
        print("Error in control_nao: {}".format(str(e)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        control_nao(command)
    else:
        print("No command provided")
