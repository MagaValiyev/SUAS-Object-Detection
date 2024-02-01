# SUAS 2024 Object Detection Task 

state of the project as for 01.02.2024 ...

## Introduction

This is a GitHub repository aimed to give information about the Object Detection systems designed for the [SUAS (Student Unmanned Aerial Systems) 2024](https://suas-competition.org/) Competition. 

## Object Types

The **Object Detection Task** consists of detecting a set of standard objects and an emergent object.

The **standard objects** are geometric shapes, namely:

1. Triangle [(view)](images/triangle.jpg)
2. Circle [(view)](images/circuit.jpg)
3. Semi-circle [(view)](images/semi-circuit.jpg)
4. Quarter-circle [(view)](images/quarter-circle-edited.jpg)
5. Rectangle [(view)](images/rectangle.jpg)
6. Pentagon [(view)](images/pentagon.jpg)
7. Star ([view)](images/star.jpg)
8. Cross [(view)](images/cross.jpg)

The standard objects can be of **colours**:

1. White
2. Black
3. Red
4. Blue
5. Green
6. Purple
7. Brown
8. Orange

The **emergent object** is a manikind dressed in clothes lying on the ground [view](images/manikind.jpg).

| Object Types | Images | Color | Description |
| ---------|----------|----------|----------|
| Triangle | <img src="images/triangle.jpg" width="40"> | white-orange | contains (A-Z) or (0-9) |
| Circle | <img src="images/circuit.jpg" width="40">  | white-orange | contains (A-Z) or (0-9) |
| Semi-circle | <img src="images/semi-circuit.jpg" width="40">  | white-orange | contains (A-Z) or (0-9) |
| Quarter-circle | <img src="images/quarter-circle-edited.jpg" width="40">  | white-orange | contains (A-Z) or (0-9) |
| Rectangle | <img src="images/rectangle.jpg" width="40"> | white-orange | contains (A-Z) or (0-9) |
| Pentagon | <img src="images/pentagon.jpg" width="40">  | white-orange | contains (A-Z) or (0-9) |
| Star | <img src="images/star.jpg" width="40">  | white-orange | contains (A-Z) or (0-9) |
| Cross | <img src="images/cross.jpg" width="40">  | white-orange | contains (A-Z) or (0-9) |
| Manikin | <img src="images/manikin.jpg" width="40"> | **unkown** | dressed |

## Target Goal

To make a control flight, during which:
- Detect all the objects on the ground
- If one object detected:
  - Get geolocation
  - Save frame of the object
  - If manikin: save to database
  - If figure:
    - Classify shape
    - Classify character
    - Classify external color
    - Classify internal color
    - Save to database

## Difficulties Encountered
Drone flight was **banned** by university
- Approximate permission date from: 02.02.2024
- Alternative solutions:
  - Gather synthetic data (Canva, Gazebo)
  - Simulate different scenarios in Gazebo
  - Save videos of these scenarios
  - Test detection and classification models on test video
  - Work on imporvements (simulate GenAI)
- Character classification model not trained:
  - High number of classes: 36
  - Insufficient data (not any frames for 19 classes)

## Timeline

1. A4 or Manikin Detection Model:
   - [x] Cleaning of 25k dataset (1 week)
   - [x] Collection of images (drone will be ready in ~1 week) 
   - [ ] 40k objects per class
   - [ ] Labelling (SAM, by hand, and own model)
   - [x] Training model 
   - [x] Checking on validation dataset 
   - [ ] Ready model (end of January)

P.S. Checkmarks are for the **demo** models. As for now:
- 1306 images are taken by drone
- 7600 labeled objects
  - Shapes: 7055
  - Person: 545
- Demo model for human detection is trained and tested (find futher information in **human-model** repository)
- Demo model for shape detection is trained and tested (find futher information in **shape-detection** repository)

2. Classification Models:
   - [x] Use gathered images (40k for this class)
   - [X] Separate images (manually, after certain time with model)
   - [X] Training model
   - [X] Checking on validation dataset
   - [ ] Ready Models (end of February)

P.S. Checkmarks are for the **demo** models. Checkmarks are for 3 classification models (shape, external color, internal color). Character classification model not trained (lack of data).
- Demo classification models (shape, external color, internal color) are trained and tested (find further information in **classification-models** repository)
