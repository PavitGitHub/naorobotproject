#from naoqi import ALProxy

import sys

def test_input_from_nodejs():
    print("Python function called!")

if __name__ == "__main__":
    print('initalising nao controller . . .')
    while True:
        print('intialising command loop . . .')
        line = sys.stdin.readline().strip()
        if line:
            eval(line)