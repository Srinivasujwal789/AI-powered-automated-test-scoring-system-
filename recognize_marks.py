import cv2
import numpy as np
import tensorflow as tf
from pytesseract import image_to_string

# Load pre-trained model
interpreter = tf.lite.Interpreter(model_path="models/digit_recognizer.tflite")
interpreter.allocate_tensors()

def preprocess_image(image, region):
    x, y, w, h = region
    roi = image[y:y+h, x:x+w]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28)) / 255.0
    return resized.reshape(1, 28, 28, 1).astype(np.float32)

def recognize_digit(image, region):
    input_data = preprocess_image(image, region)
    interpreter.set_tensor(interpreter.get_input_details()[0]['index'], input_data)
    interpreter.invoke()
    output = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])
    return np.argmax(output)

def recognize_usn(image, usn_region):
    x, y, w, h = usn_region
    roi = image[y:y+h, x:x+w]
    return image_to_string(roi, config='--psm 6').strip()

# Example usage
image = cv2.imread("captured_booklet.jpg")
mark_regions = [(100, 200, 50, 50), (160, 200, 50, 50)]  # Example regions
usn_region = (50, 50, 200, 50)
marks = [recognize_digit(image, region) for region in mark_regions]
usn = recognize_usn(image, usn_region)
print(f"USN: {usn}, Marks: {marks}")
