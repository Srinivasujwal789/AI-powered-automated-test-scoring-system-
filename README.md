# AI-powered-automated-test-scoring-system-

##Project Overview##

The Neural Network-Based Test Marks Reader and Acquisition System is an AI-powered automated test scoring solution designed to streamline the grading process for handwritten test booklets in educational institutions. This system leverages computer vision and neural networks to capture, process, and validate test marks, reducing manual effort, minimizing errors, and providing rapid feedback. Key features include automated booklet placement detection, real-time mark display, robust validation mechanisms, and data export capabilities, making it scalable for large-scale assessments.

This project addresses the urgent need for efficient grading in educational settings, particularly for institutions transitioning to digital or hybrid learning environments. It was developed as an emergency solution to handle high-volume test grading with minimal latency, ensuring accuracy and reliability under tight deadlines.

#Technology Stack#

The system is built using a combination of hardware and software technologies optimized for performance and cost-effectiveness:
#Hardware:#

Raspberry Pi 4: Central processing unit for image acquisition, processing, and GUI rendering.
Raspberry Pi Camera Module V2 (8MP) or High Quality Camera (12.3MP): For capturing high-resolution images of test booklets.
LED Light Strips: Diffused lighting setup to ensure uniform illumination and minimize glare.
Pressure Sensor: Connected to Raspberry Pi GPIO for automatic booklet placement detection.
Touchscreen Monitor: Connected via HDMI for real diagramming and user interaction.
#Software:#

Python 3.8+: Core programming language for system logic and integration.
OpenCV: For image processing, contour detection, and booklet boundary identification.
TensorFlow Lite: Lightweight neural network framework for handwritten digit recognition (e.g., marks and USN).
Tesseract OCR: For extracting handwritten text (University Seat Number and marks).
PyQt5: For designing a user-friendly graphical user interface (GUI).
pandas: For exporting marks and student data to CSV files.
NumPy: For numerical computations and image data handling.
RPi.GPIO: For interfacing with hardware sensors and GPIO pins.
#Development Tools:#
Git: Version control for collaborative development.
VS Code: IDE for code development and debugging.
Raspbian OS: Operating system for Raspberry Pi.

