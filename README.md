# SUAS 2024 Object Detection Task

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
**General procedure - Object Detection-Localization-Classification (ODLC):**

- We detect an object on the ground
- Verify whether it coincides with given parameters
- If yes, drop at the location

**Manikin Recognition:**
- Gather images with drone
- Automatic labelling with SAM
- Train YOLOv8 model

**Standard Objects Detection** includes 4 sub-tasks:
- Shape Detection
- Character Detection
- Color Detection for Shape
- Color Detection for Character

## Detailed Standard Objects Detection
**Final Decision:**

For manikin detection:

- Gather dataset with human from birdseye view
- Train YOLOv8 model

For shapes detection:
- Train general YOLOv8 model for paper detection on ground
- Train 4 models for classification of:
  - Shape
  - Shape color
  - Character
  - Character Color
- Save detection results into the database (SQLIte)
- Choose the most frequent detection

Localization (identifying geolocation):
- Save location points into the database (SQLLite) when detecting
- Height: using Lidar
- Location: using GPS
  

