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
awb = 0.040  # Wing area behind the center of mass (m^2)
aw = awn + awb  # Total wing area
#back is two grams
#front is two grams
mb = 0.0025  # Mass behind the center of mass of the plane (kg)
mn = 0.0025  # Mass in the nose side of the plane (kg)
inetia = 0.00005
    # 0.00005  # Moment of inertia about the center of mass (kg*m^2) (assumed)

# Initial conditions
theta = math.radians(45)  # Initial angle (converted to radians)
xfirst = 9  # Reasonable starting x speed (m/s)
zfirst = 9  # Initial positive z speed (m/s) - assuming it is launched with an upward component
thetafirst = 0  # Initial angular velocity (rad/s)

# Starting positions at a certain height above the ground
x, z, t = 0, 1, 0  # Starting at 1 meter above the ground

    # Drag force calculations and update velocities
thetaVelo = math.atan(zfirst/xfirst)
thetaDiff = theta - thetaVelo
xsecond = (-1) * ((0.5) * cf * p * (xfirst ** 2) * af * math.cos(thetaDiff)) / (m)

zsecond = ((-1) * m * g + (0.5) * cw * p * (zfirst ** 2) * math.sin(thetaDiff) * aw) / (m)  ##new Algo

thetasecond = (-1) * (0.5 * cw * p * (zfirst ** 2) * (awn - awb) * math.sin(thetaDiff) + g * abs(math.cos(theta)) * (mb - mn)) / (m)
for i in range(10):
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
    awb = 0.040  # Wing area behind the center of mass (m^2)
    aw = awn + awb  # Total wing area
    #back is two grams
    #front is two grams
    mb = 0.0025  # Mass behind the center of mass of the plane (kg)
    mn = 0.0025  # Mass in the nose side of the plane (kg)
    inetia = 0.00005
        # 0.00005  # Moment of inertia about the center of mass (kg*m^2) (assumed)

    # Initial conditions
    theta = math.radians(45)  # Initial angle (converted to radians)
    xfirst = 11 - i  # Reasonable starting x speed (m/s)
    zfirst = 11 - i  # Initial positive z speed (m/s) - assuming it is launched with an upward component
    thetafirst = 0  # Initial angular velocity (rad/s)

    # Starting positions at a certain height above the ground
    x, z, t = 0, 1, 0  # Starting at 1 meter above the ground

        # Drag force calculations and update velocities
    thetaVelo = math.atan(zfirst/xfirst)
    thetaDiff = theta - thetaVelo
    xsecond = (-1) * ((0.5) * cf * p * (xfirst ** 2) * af * math.cos(thetaDiff)) / (m)

    zsecond = ((-1) * m * g + (0.5) * cw * p * (zfirst ** 2) * math.sin(thetaDiff) * aw) / (m)  ##new Algo

    thetasecond = (-1) * (0.5 * cw * p * (zfirst ** 2) * (awn - awb) * math.sin(thetaDiff) + g * abs(math.cos(theta)) * (mb - mn)) / (m)
     
     # Open a file to save the data
    with open('/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/FinalAnalysis/SimulationsData/data' + str(i) + '.txt', 'w') as file:
        file.write("zfirst, xfirst, theta \n")
        file.write(f"{zfirst:.8f},{xfirst:.8f},{math.degrees(theta):.8f},\n")
        file.write("t,x,z,theta\n")  # Write the header

        # Simulation loop
        for i in range(totSteps):
            # Check if the plane has hit the ground
            if z <= 0 and t > 0:
                break  # Stop the simulation if the plane has hit the ground



            # Update velocities and angular velocity based on current accelerations
            # Replace the placeholder comments with your actual equations for xsecond, zsecond, and thetasecond
            thetaVelo = math.atan(zfirst / xfirst)
            thetaDiff = theta - thetaVelo

            xsecond = (-1) * ((0.5) * cf * p * (xfirst ** 2) * af * math.cos(thetaDiff)) / (m)

            zsecond = ((-1) * m * g  + (0.5) * cw * p * (zfirst ** 2) * math.sin(thetaDiff) * aw) / (m)  ##new Algo

            thetasecond = (0.5 * cw * p * (zfirst ** 2) * (awn - awb) * abs(math.sin(thetaDiff)) - g * (mb - mn)) / (m)

            # Update positions and angle based on current velocities and angular velocity


            xfirst += xsecond * delta
            zfirst += zsecond * delta
            thetafirst += thetasecond * delta


            x += delta * xfirst
            z += delta * zfirst
            theta += delta * thetafirst

            # Save the current state to the file
            file.write(f"{t:.8f},{x:.8f},{z:.8f},{math.degrees(theta):.8f}\n")

            # Increment time
            t += delta

        # The file will be automatically closed when the block ends
        print("Simulation" + str(i) + "complete. Data saved!!")
print("Simulation complete. Data saved!!")



