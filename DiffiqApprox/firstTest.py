import math

# Constants
g = 9.80665  # Acceleration due to gravity (m/s^2)

# Simulation parameters
time = 10000  # Maximum simulation time in seconds
max_flight_time = 15  # Estimated time until the plane lands (s)
step = int(1e7)  # A very high number of steps for finer resolution
totSteps = step * time
delta = max_flight_time / step  # Time step

# Paper plane properties
cf = 1.28  # Coefficient of friction for paper in air (assumed)
p = 1.225  # Air density at sea level (kg/m^3)
af = 0.005  # Frontal area of the paper plane (m^2)
m = 0.005  # Total mass of the paper plane (kg)
cw = 0.3  # Drag coefficient (typical for flat plates)
awn = 0.025  # Wing area in the nose side of the center of mass (m^2)
awb = 0.030  # Wing area behind the center of mass (m^2)
aw = awn + awb  # Total wing area
#back is two grams
#front is two grams
mb = 0.0027  # Mass behind the center of mass of the plane (kg)
mn = 0.0025  # Mass in the nose side of the plane (kg)
inetia = 0.0000354
    # 0.00005  # Moment of inertia about the center of mass (kg*m^2) (assumed)

# Initial conditions
theta = 45  # Initial angle (converted to radians)
xfirst = 9  # Reasonable starting x speed (m/s)
zfirst = 9  # Initial positive z speed (m/s) - assuming it is launched with an upward component
thetafirst = 0  # Initial angular velocity (rad/s)

# Starting positions at a certain height above the ground
x, z, t = 0, 1, 0  # Starting at 1 meter above the ground
theta_radians = math.radians(theta)

    # Drag force calculations and update velocities
xsecond = (cf * p * (xfirst ** 2) * af * math.cos(theta_radians)) / (2 * m)
zsecond = ((p * (zfirst ** 2) * (cw * aw * math.cos(theta_radians) + (cf * af * math.sin(theta_radians)))) / (
        2 * m))
thetasecond = ((0.5) * p * cw * (zfirst ** 2) * math.cos(theta_radians) * (awn - awb) + g * (mb - mn)) / inetia

# Open a file to save the data
with open('/Users/lukeadelsbach/math/flight_test.txt', 'w') as file:
    file.write("t,x,z,theta\n")  # Write the header

    # Simulation loop
    for i in range(totSteps):
        # Check if the plane has hit the ground
        if z <= 0 and t > 0:
            break  # Stop the simulation if the plane has hit the ground

        # Update positions and angle based on current velocities and angular velocity
        x += delta * xfirst
        z += delta * zfirst
        theta += delta * thetafirst


        # Update velocities and angular velocity based on current accelerations
        # Replace the placeholder comments with your actual equations for xsecond, zsecond, and thetasecond

        theta_radians = math.radians(theta)

        # Drag force calculations and update velocities
        xsecond = -(cf * p * (xfirst ** 2) * af * math.cos(theta_radians)) / (2 * m)

        if zfirst > 0:
            zsecond = ((p * (zfirst ** 2) * (cw * aw * math.cos(theta_radians) + (-1 * cf * af * abs(math.sin(theta_radians))))) / (
                    2 * m))

        else:
            zsecond = ((p * (zfirst ** 2) * (cw * aw * math.cos(theta_radians) + (cf * af * abs(math.sin(theta_radians))))) / (
                    2 * m))

        # zsecond = ((p * (zfirst ** 2) * (cw * aw * math.cos(theta_radians) + (cf * af * math.sin(theta_radians)))) / (
        #             2 * m)) - g
        thetasecond = ((0.5) * p * cw * (zfirst ** 2) * math.cos(theta_radians) * (awn - awb) + g * (mb - mn)) / inetia

        #
        # ... [

        xfirst += xsecond * delta
        zfirst += zsecond * delta
        thetafirst += thetasecond * delta

        # Apply gravitational acceleration to the z velocity
        zfirst -= g * delta  # Subtract because gravity is in the negative z direction

        # Save the current state to the file
        file.write(f"{t:.8f},{x:.8f},{z:.8f},{theta:.8f}\n")

        # Increment time
        t += delta

# The file will be automatically closed when the block ends
print("Simulation complete. Data saved!!")
