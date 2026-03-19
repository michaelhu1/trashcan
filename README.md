# AI Recycling Bin

A Raspberry Pi-powered recycling bin that automatically sorts waste using computer vision.
When an object is placed in front of the bin, it captures an image, classifies the waste type,
and physically opens the correct compartment using servo motors.

## How it works

An ultrasonic sensor detects when something is nearby and triggers the camera. The image is
sent to a Roboflow-hosted classification model trained on waste categories. Based on the result,
a servo motor opens the correct bin compartment. A local on-device model handles basic cases
for low-latency response; ambiguous items fall back to the cloud model at 98% accuracy.

## Architecture
```
Ultrasonic sensor → Raspberry Pi → PiCamera2 capture
                                 → Roboflow API (cloud, 98% accuracy)
                                 → Servo motor control → bin opens
```

## Stack

Python · OpenCV · TensorFlow · PiCamera2 · Roboflow · RPi.GPIO

## Hardware

- Raspberry Pi
- Raspberry Pi Camera
- Ultrasonic distance sensor
- Servo motor (compartment control)

## Results

- Local on-device model: ~50% accuracy (fast, no network required)
- Cloud model via Roboflow API: 98% accuracy
