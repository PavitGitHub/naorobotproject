# Guide dog robot for the visually impaired 

- [Project Background/Overview](#project-backgroundoverview)
- [Demo](#demo)
- [Features](#features)
- [Documentation](#documentation)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Changelog](#changelog)
- [Traceability Matrix](#traceability-matrix)
- [Contact](#contact)
- [License](#license)

## Project Background/Overview

<!-- Provide an overview of the project, its purpose, and objectives. -->
The Guide Dog Robot project is an innovative solution designed to assist visually impaired individuals in navigating their surroundings safely and independently. Built on the advanced NAO V5 humanoid robot platform, this project integrates multiple cutting-edge technologies to emulate the assistance provided by a guide dog.

Key technologies implemented in this project include:

- Text-to-Speech (TTS): Allows the robot to communicate verbally with the user, providing real-time updates about the environment, obstacles, and navigation instructions.
- Speech-to-Text (STT): Enables the robot to understand and process verbal commands from the user, facilitating seamless human-robot interaction.
- Computer Vision: Utilizes a YOLOv9 model for object detection and environment mapping, helping the robot identify obstacles, recognize landmarks, and make informed navigation decisions.
- Web-Based Control Interface: A user-friendly website that allows caregivers or users to remotely control the robot, adjust settings, and monitor its status in real-time.
By combining these technologies, the Guide Dog Robot aims to enhance the quality of life for visually impaired individuals, offering a reliable and interactive companion for daily activities.

## Demo

Have a look at this folder for [demo videos](https://drive.google.com/drive/folders/1g7xdTrDOXYPbarWvkWu9Pxx5UVu0v-n4) showing various aspects of the project!
<!-- Include a link to the hosted project or a demo video. -->

## Features

<!-- List the features or user stories, organized in sprints if applicable. -->

Our project incorporates a computer vision module that utilizes a training on a [**YOLOv9m**](https://docs.ultralytics.com/models/yolov9/#programmable-gradient-information-pgi) model for object detection and recognition tasks. The model is trained on a custom road objects dataset, [Lightweight_ObjDetect](https://universe.roboflow.com/derbyuniobjdet/lightweight_objdetect/browse) obtained from opensource website Roboflow to enhance accuracy for our specific use case. To test the model on a specific directory of images do the following: 

**Testing the Computer Vision Module:**

1. **Navigate to the Python directory:**
```
cd Python/3.12  
```
   
2.  **Run the computer vision controller script:**
```
python cv-controller.py
```
3. **Process images using the process_images function in the python shell:**
```
process_images("test")  # Or specify the path to your test directory in the code
```


## Documentation

<!-- Provide links to user stories, architecture diagrams, test cases, and other documents exported from Confluence as PDFs. -->

## System Requirements

<!-- List the tools, databases, and their versions required for the project. -->

## Installation Guide
**Installing Translation Module:**
pip install openai 
pip install --upgrade pip
pip install google-cloud-translate==2.0.1
pip install google-cloud-texttospeech
pip install playsound==1.2.2
install gcloud cli installer
gcloud auth application-default login

<!-- Provide setup and configuration details to install and run your code. -->

## Changelog

<!-- Include or link to the project's changelog detailing updates and changes. -->

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## Unreleased

<small>[Compare with latest](https://github.com/PavitGitHub/naorobotproject/compare/61aeb5441d176dc13c2253854e2a620f0d1a954f...HEAD)</small>

### Added

- added better output read functionality to handlers ([62e13c8](https://github.com/PavitGitHub/naorobotproject/commit/62e13c8814528b8268fcf0a432067ebb657b3c8c) by Joel Leifer).
- add audio recording part ([893ec9d](https://github.com/PavitGitHub/naorobotproject/commit/893ec9dc3c517fe2233ce747e939081813585df6) by coreshaw).
- add imu control part ([a0b79fe](https://github.com/PavitGitHub/naorobotproject/commit/a0b79fe62b2c9a4ae034444cfb7cc4bc92ca5d7a) by coreshaw).
- add esp32_imu_part ([a463707](https://github.com/PavitGitHub/naorobotproject/commit/a463707eabaddbc74de11de15900cc413f32200f) by coreshaw).
- added roboflow inference code and returning labels with position ([ce6a900](https://github.com/PavitGitHub/naorobotproject/commit/ce6a90049babaf5bddddb0be0b1bcfb045f1c6f9) by hannah_mac).
- added serverportforwarding on modem, added get request page with drumpad style post request inputs ([55063f3](https://github.com/PavitGitHub/naorobotproject/commit/55063f36323b5784fff650f0d55bd1104a5becaa) by Joel Leifer).
- added test routes and fixed reloading of controllers, added proper output and warns to reload and callback functions from controller classes ([9a27804](https://github.com/PavitGitHub/naorobotproject/commit/9a2780497cc73171e25bc1a8a908021d1c6d643b) by Chent).
- added cv-controller to nodejs python handler, updated routes to allow post request for manual yolo and nao controller restart ([4dab072](https://github.com/PavitGitHub/naorobotproject/commit/4dab072090b30a92db9b5b2b097fada56d422244) by Chent).
- added python controller support to nodejs server, added test route for feeding input to nao-controller ([a7fef8f](https://github.com/PavitGitHub/naorobotproject/commit/a7fef8ff3df595bd2831481f372a6e7394430e0a) by Joel Leifer).
- added skeleton for python 3.12 computer vision controller ([be6f767](https://github.com/PavitGitHub/naorobotproject/commit/be6f767e4b809f5e56345641a2ede6eb9a3525c7) by Joel Leifer).
- added upload of node modules for ease of use of other team members ([7b1a943](https://github.com/PavitGitHub/naorobotproject/commit/7b1a943abd220669dff3a6d476303f561cfc8a2b) by Joel Leifer).
- added file structure for python programs, added .gitignore, added server stubs for /feed and /videos viewing ([58e53cd](https://github.com/PavitGitHub/naorobotproject/commit/58e53cd9a41d6d65a6d79c85644873ba01b5b91e) by Joel Leifer).
- added basic nodejs express server function for file upload, new routes to be added soon for feed and view of exsiting files ([66a7683](https://github.com/PavitGitHub/naorobotproject/commit/66a768361914e690b07e5222fe034b074ad87ae3) by Joel Leifer).

### Fixed

- fixed server organisation ([1424bf8](https://github.com/PavitGitHub/naorobotproject/commit/1424bf8088479f1ed6d741bedacf3d5d8731caad) by Joel Leifer).
- fixed server usage, added ejs for drumpad automation, added proper route control, added ip util for automated server setup ([97f8480](https://github.com/PavitGitHub/naorobotproject/commit/97f848070596df73a9282d209cb757d1be69db9c) by Joel Leifer).

<!-- insertion marker -->

## Traceability Matrix

<!-- Include a traceability matrix linking requirements to test cases or other artifacts. -->

## Contact

<!-- Provide contact information for support or inquiries. -->
Please contact Hannah Bansal (hannah.bansal@student.unimelb.edu.au) for any pull requests or issues.

## License

<!-- Include licensing information for the project. -->

This project is released under the [MIT License](https://opensource.org/license/mit)
