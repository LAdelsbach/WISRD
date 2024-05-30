import RPi.GPIO as GPIO
import tkinter as tk
import time
#TODO: if change these pins
# Pin Definitions
DIR_PIN_DEC = 24  # Direction GPIO Pin
PUL_PIN_DEC = 23  # Pulse GPIO Pin
STEPS_PER_REV_DEC = 200  # Adjust this to your stepper motor specs

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN_DEC, GPIO.OUT)
GPIO.setup(PUL_PIN_DEC, GPIO.OUT)

# Pin Definitions
DIR_PIN_RA = 24  # Direction GPIO Pin
PUL_PIN_RA = 23  # Pulse GPIO Pin
STEPS_PER_REV_RA = 200  # Adjust this to your stepper motor specs

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN_RA, GPIO.OUT)
GPIO.setup(PUL_PIN_RA, GPIO.OUT)





def move_to_position_dec(steps, direction):
    # Set the direction
    GPIO.output(DIR_PIN_DEC, GPIO.HIGH if direction else GPIO.LOW)

    # Step to position
    for _ in range(steps):
        GPIO.output(PUL_PIN_DEC, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(PUL_PIN_DEC, GPIO.LOW)
        time.sleep(0.001)

def rotate_to_angle_dec(angle):
    # Calculate the number of steps needed
    steps = int(angle / 360.0 * STEPS_PER_REV_DEC)
    direction = angle >= 0
    move_to_position_dec(abs(steps), direction)





def move_to_position_ra(steps, direction):
    # Set the direction
    GPIO.output(DIR_PIN_RA, GPIO.HIGH if direction else GPIO.LOW)

    # Step to position
    for _ in range(steps):
        GPIO.output(PUL_PIN_RA, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(PUL_PIN_RA, GPIO.LOW)
        time.sleep(0.001)

def rotate_to_angle_ra(angle):
    # Calculate the number of steps needed
    steps = int(angle / 360.0 * STEPS_PER_REV_RA)
    direction = angle >= 0
    move_to_position_ra(abs(steps), direction)



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