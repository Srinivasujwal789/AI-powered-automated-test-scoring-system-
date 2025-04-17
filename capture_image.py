import cv2
import RPi.GPIO as GPIO
import time

# Initialize camera and GPIO
camera = cv2.VideoCapture(0)
GPIO.setmode(GPIO.BCM)
PRESSURE_SENSOR_PIN = 18
GPIO.setup(PRESSURE_SENSOR_PIN, GPIO.IN)

def detect_booklet(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:  # Filter small contours
            return True
    return False

def capture_image():
    while True:
        if GPIO.input(PRESSURE_SENSOR_PIN):  # Booklet detected
            ret, frame = camera.read()
            if ret and detect_booklet(frame):
                cv2.imwrite("captured_booklet.jpg", frame)
                return frame
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        image = capture_image()
        print("Image captured successfully!")
    finally:
        camera.release()
        GPIO.cleanup()
