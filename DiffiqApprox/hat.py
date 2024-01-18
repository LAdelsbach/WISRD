import tkinter as tk
from adafruit_motorkit import MotorKit
import board

# Initialize MotorKit
kit = MotorKit(i2c=board.I2C())

def step_left():
    """Turn the stepper motor a little to the left."""
    kit.stepper1.onestep(direction=1, style=2)

def step_right():
    """Turn the stepper motor a little to the right."""
    kit.stepper1.onestep(direction=0, style=2)

# Create the main window
root = tk.Tk()
root.title("Stepper Motor Control")

# Create buttons for left and right movement
left_button = tk.Button(root, text="Step Left", command=step_left)
left_button.pack(side=tk.LEFT)

right_button = tk.Button(root, text="Step Right", command=step_right)
right_button.pack(side=tk.RIGHT)

# Start the GUI event loop
root.mainloop()
