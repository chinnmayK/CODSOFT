# Face Recognition Project

This project implements a face recognition system using OpenCV for face detection and a machine learning model for recognition. It allows users to create a dataset, train a recognition model, and use that model to recognize faces in images or real-time video.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **Required Libraries**: 
  - OpenCV
  - NumPy
  - TensorFlow or Keras
  - Matplotlib

You can install these dependencies using pip.

---

## Project Structure

The project consists of the following key files:

- **`task5_dataset.py`**: Prepares and processes the face dataset.
- **`task5_trainer.py`**: Trains the face recognition model.
- **`task5_recog.py`**: Recognizes faces in new images or video.
- **`task5_haarcascade.xml`**: Haar Cascade model for detecting faces.
- **`docs/`**: Contains additional documentation and reports.

---

## Installation Instructions

1. **Clone the repository**:
   Download or clone this repository to your local machine.

2. **Install the required libraries** using pip.

---

## Workflow

### 1. Dataset Preparation

Run `task5_dataset.py` to create and preprocess your dataset.

### 2. Model Training

Run `task5_trainer.py` to train your face recognition model.

### 3. Face Recognition

Run `task5_recog.py` to recognize faces in images or videos. You can also modify it for real-time webcam recognition.

---

## Acknowledgments

- **OpenCV**: For the Haar Cascade Classifier used in face detection.
- **TensorFlow/Keras**: For the machine learning models.

---
