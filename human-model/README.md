# Human Detection Model

## Introduction
 This is a preliminary model trained for detecting human (**manikin** in the competition) from birdseye view. A complete model will be able to detect **manikin** and **shapes** (printed on A4 and cut out).

## Procedure
- Downloading 27k images dataset
- Separating images with humans
- Deleting labels of other objects (cars, trucks, etc.)
- Converting PASCAL VOC labels to YOLO labels
- Manual inspection of some corrupted images
- Random shuffling for manual review of ~ 100 labeled images
- Training using Yolov8

## Current State
- 10.555 training set images
- 1000 validation set images
- Yolov8 Model: 24/100 epochs ...

## Future Plan
- Gather images of **shapes** using drone
- Label gathered images
- Train a model for object detection of 2 classes: **human** and **shapes**
