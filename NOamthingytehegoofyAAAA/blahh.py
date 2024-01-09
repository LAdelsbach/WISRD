import tkinter as tk
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import board

kit = MotorKit(i2c=board.I2C())

def step_motor(motor, direction, steps):
    for _ in range(steps):
        motor.onestep(direction=direction, style=stepper.SINGLE)

def get_motor(motor_number):
    if motor_number == 1:
        return kit.stepper1
    elif motor_number == 2:
        return kit.stepper2
    elif motor_number == 3:
        return kit.stepper3
    else:
        return kit.stepper4

def step_command(motor_number, direction):
    motor = get_motor(motor_number)
    steps = int(step_entries[motor_number-1].get())
    step_motor(motor, direction, steps)

root = tk.Tk()
root.title("Stepper Motor Control")

step_entries = []

for motor_number in range(1, 5):
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=5)

    left_button = tk.Button(frame, text=f"Step Left Motor {motor_number}", command=lambda mn=motor_number: step_command(mn, stepper.BACKWARD))
    left_button.pack(side=tk.LEFT)

    right_button = tk.Button(frame, text=f"Step Right Motor {motor_number}", command=lambda mn=motor_number: step_command(mn, stepper.FORWARD))
    right_button.pack(side=tk.LEFT)

    step_entry = tk.Entry(frame, width=5)
    step_entry.pack(side=tk.LEFT)
    step_entries.append(step_entry)

root.mainloop()
