import RPi.GPIO as GPIO
import tkinter as tk
import time

# Pin definitions
# TODO change these pins
# Right Ascension(RA)
dir_pin0 = 20  # Change as per your connection
step_pin0 = 21  # Change as per your connection
# Declension
dir_pin1 = 20  # Change as per your connection
step_pin1 = 21  # Change as per your connection



# Setup
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(dir_pin0, GPIO.OUT)
GPIO.setup(step_pin0, GPIO.OUT)
GPIO.setup(dir_pin1, GPIO.OUT)
GPIO.setup(step_pin1, GPIO.OUT)

# Motor control parameters
steps = 200  # Number of steps to turn the motor
speed = 0.05  # Time between steps (lower is faster)

def step_once_declension():
    GPIO.output(step_pin1, GPIO.HIGH)
    time.sleep(speed)
    GPIO.output(step_pin1, GPIO.LOW)
    time.sleep(speed)

def step_once_ra():
    GPIO.output(step_pin0, GPIO.HIGH)
    time.sleep(speed)
    GPIO.output(step_pin0, GPIO.LOW)
    time.sleep(speed)

def rotate_motor_declension(direction, steps):
    GPIO.output(dir_pin1, GPIO.HIGH if direction == 'clockwise' else GPIO.LOW)
    for _ in range(steps):
        step_once_declension()

def rotate_motor_ra(direction, steps):
    GPIO.output(dir_pin0, GPIO.HIGH if direction == 'clockwise' else GPIO.LOW)
    for _ in range(steps):
        step_once_ra()
def display():
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=5)

    left_button = tk.Button(frame, text="Declension Motor", command=lambda dir='clockwise': step_command(dir, stepper.BACKWARD))
    left_button.pack(side=tk.LEFT)

    right_button = tk.Button(frame, text="Right Ascension Motor", command=lambda dir='counter clockwise': step_command(dir, stepper.FORWARD))
    right_button.pack(side=tk.LEFT)

    step_entry = tk.Entry(frame, width=5)
    step_entry.pack(side=tk.LEFT)
    step_entries.append(step_entry)

display()
root = tk.Tk()
root.title("Stepper Motor Control")


print("Rotating motor clockwise")
rotate_motor('clockwise', steps)

print("Rotating motor counterclockwise")
rotate_motor('counterclockwise', steps)

GPIO.cleanup()  # Clean up GPIO on normal exit