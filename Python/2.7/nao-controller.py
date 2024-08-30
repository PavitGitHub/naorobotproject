#from naoqi import ALProxy

import sys

def test_input_from_nodejs():
    print("Python function called!")

if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().strip()
        if line:
            eval(line)