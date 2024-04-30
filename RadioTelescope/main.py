import RPi.GPIO as GPIO
import time

# Pin definitions
dir_pin = 20  # Change as per your connection
step_pin = 21  # Change as per your connection

# Setup
GPIO.setmode(GPIO.BCM)  # Broadcom pin-numbering scheme
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)

# Motor control parameters
steps = 200  # Number of steps to turn the motor
speed = 0.005  # Time between steps (lower is faster)

def step_once():
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(speed)
    GPIO.output(step_pin, GPIO.LOW)
    time.sleep(speed)

def rotate_motor(direction, steps):
    GPIO.output(dir_pin, GPIO.HIGH if direction == 'clockwise' else GPIO.LOW)
    for _ in range(steps):
        step_once()

try:
    print("Rotating motor clockwise")
    rotate_motor('clockwise', steps)

    print("Rotating motor counterclockwise")
    rotate_motor('counterclockwise', steps)

finally:
    GPIO.cleanup()  # Clean up GPIO on normal exit




def runClockWise():


    ##
    return 0

def runCounterClock():

    ##code changeds
    return 0




##Main While Loop

isRunning = True
while(isRunning):
