# Guide dog robot for the visually impaired 

## Table of Contents

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

## Demo

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

<!-- Provide setup and configuration details to install and run your code. -->

## Changelog

<!-- Include or link to the project's changelog detailing updates and changes. -->

## Traceability Matrix

<!-- Include a traceability matrix linking requirements to test cases or other artifacts. -->

## Contact

<!-- Provide contact information for support or inquiries. -->

## License

<!-- Include licensing information for the project. -->

