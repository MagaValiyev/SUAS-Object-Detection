# Classification Models

Example of working models (Shape Detection, Shape Class., Ext. Color Class., Int.Color Class.) can be found [here](https://drive.google.com/file/d/1kMv3yhYnYlFYCnGEP3maxsYYmSHTDQRu/view?usp=sharing). (Redirection to Google Drive)

Example of working models (Shape Detection, Shape, Ext. Color, Int.Color and Character Classification) on Gazebo simulation can be found [here](https://drive.google.com/file/d/120ielb_8j4Ha78qDvazb6rKyFpcg2rcq/view?usp=sharing). (Redirection to Google Drive)

All Classification Models are trained using:
- Yolov8L-cls model with parameters:
  - imgsz = 320
  - batch = -1
  - epochs = 100

## Shape Classification
Total number of classes: 8

No missing classes

## External Color Classification
Total number of classes: 8

No missing classes

## Internal Color Classification
Total number of classes: 8

No missing classes

**Different Combinations for Colors**:
- Orange on Red
- Orange on Brown
- Purple on Black
- Blue on Black
- Brown on Orange
- Red on Orange


## Character Classification
Total number of classes: 36

Missing classes for now: 
- '1'
- '6'
- H

*All the instances are printed for **Sunday (04.02.2024)** flight.

Difficult scenarios:
- '6' vs '9'
- W vs M
- N vs Z
- '0' vs O
- '1' vs I

## General Overview
Real-life drone flight:
- 30 figure combinations are saved

Gazebo simulation flight:
- Extra 30 figure combinations are saved

For **Sunday (04.02.2024)** flight:
- 130 different combinations are printed
