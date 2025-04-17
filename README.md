# AI-powered-automated-test-scoring-system-

# Project Overview 

The Neural Network-Based Test Marks Reader and Acquisition System is an AI-powered automated test scoring solution designed to streamline the grading process for handwritten test booklets in educational institutions. This system leverages computer vision and neural networks to capture, process, and validate test marks, reducing manual effort, minimizing errors, and providing rapid feedback. Key features include automated booklet placement detection, real-time mark display, robust validation mechanisms, and data export capabilities, making it scalable for large-scale assessments.

This project addresses the urgent need for efficient grading in educational settings, particularly for institutions transitioning to digital or hybrid learning environments. It was developed as an emergency solution to handle high-volume test grading with minimal latency, ensuring accuracy and reliability under tight deadlines.

# Technology Stack

The system is built using a combination of hardware and software technologies optimized for performance and cost-effectiveness:

# Hardware:

1. Raspberry Pi 4: Central processing unit for image acquisition, processing, and GUI rendering.
2. Raspberry Pi Camera Module V2 (8MP) or High Quality Camera (12.3MP): For capturing high-resolution images of test booklets.
3. LED Light Strips: Diffused lighting setup to ensure uniform illumination and minimize glare.
4. Pressure Sensor: Connected to Raspberry Pi GPIO for automatic booklet placement detection.
5. Touchscreen Monitor: Connected via HDMI for real diagramming and user interaction.

# Software:

1. Python 3.8+: Core programming language for system logic and integration.
2. OpenCV: For image processing, contour detection, and booklet boundary identification.
3. TensorFlow Lite: Lightweight neural network framework for handwritten digit recognition (e.g., marks and USN).
4. Tesseract OCR: For extracting handwritten text (University Seat Number and marks).
5. PyQt5: For designing a user-friendly graphical user interface (GUI).
6. pandas: For exporting marks and student data to CSV files.
7. NumPy: For numerical computations and image data handling.
8. RPi.GPIO: For interfacing with hardware sensors and GPIO pins.
   
# Development Tools:
1. Git: Version control for collaborative development.
2. VS Code: IDE for code development and debugging.
3. Raspbian OS: Operating system for Raspberry Pi.

# Implementation:
The system is implemented as a modular pipeline, ensuring scalability and maintainability. Below is an overview of the key components and their implementation:

1. Image Acquisition:
A Raspberry Pi Camera captures high-resolution images of test booklets placed in a custom enclosure.
Diffused LED lighting ensures consistent illumination, reducing shadows and glare.
A pressure sensor triggers image capture automatically when a booklet is detected.
2. Booklet Detection:
OpenCV's contour and edge detection algorithms (e.g., Canny edge detector) identify the booklet's boundaries against a contrasting background.
Hough transforms detect the rectangular shape of the booklet for precise alignment.
3. Handwritten Mark Recognition:
TensorFlow Lite runs a pre-trained convolutional neural network (CNN) model, fine-tuned on datasets like MNIST and custom handwritten mark samples, to recognize digits (0-9).
Tesseract OCR extracts the University Seat Number (USN) and validates it against a student database.
4. Mark Validation:
The system compares recognized marks against predefined maximum marks stored in a configuration files.
Total marks are verified by summing individual question marks and comparing them with the booklet's total.
Discrepancies trigger error messages on the GUI, with options for manual correction.
5. Real-Time Display:
A PyQt5-based GUI displays the captured USN, individual marks, and total marks on a touchscreen monitor.
Color-coded validation status (e.g., green for valid, red for errors) enhances user experience.
6. Data Export:
Recognized data (USN, marks) is exported to individual CSV files using pandas, named by USN for easy organization.
Fuzzy string matching links USNs to student names from a CSV database, handling minor OCR errors.
7. Feedback and Model Improvement:
Teachers can edit marks via the GUI, implicitly providing feedback for model retraining.
Corrected data is stored for periodic fine-tuning of the neural network using transfer learning.

# Application:

The system is designed for educational institutions, particularly those with large student cohorts or online learning platforms. Key applications include:

1. Automated Grading: Processes handwritten test booklets for courses with numerical marks, reducing grading time by up to 70%.
2. Scalable Assessments: Supports high-volume grading for semester exams, entrance tests, or certification programs.
3. Real-Time Feedback: Provides immediate mark validation and display, enabling quick corrections and feedback to students.
4. Data Management: Exports structured data for integration with Learning Management Systems (LMS) or student databases.
5. Continuous Improvement: Adapts to diverse handwriting styles through user feedback, ensuring long-term reliability.



