import numpy as np
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense, LSTM
from keras.optimizers.legacy import Adam
import pandas as pd

# Define the file path



# Placeholder for loading your dataset
# Assuming the dataset is loaded and has the following structure:
# t: time steps (input)
# x, y, theta: coordinates and angle (outputs)

# Read and parse the data from the file
def read_and_parse_data(file_path):
    # Initialize lists for each variable
    t = []
    x = []
    z = []
    theta = []

    znot = 0
    xnot = 0
    thetanot = 0


    # Open and read the file
    # def read_data(file_path):
    # Initialize the lists for storing data
    
    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        # Read the second line to get initial values
        values = file.readline().strip().split(',')

        znot = float(values[0])
        xnot = float(values[1])
        thetanot = float(values[2])

        # Skip the next line (assuming you want to skip one more line here, if not, remove this next(file))
        next(file)

        # Read each subsequent line, split by comma, and append to lists
        for line in file:
            values = line.strip().split(',')
            t.append(float(values[0]))
            x.append(float(values[1]))
            z.append(float(values[2]))
            theta.append(float(values[3]))

    return znot, xnot, thetanot, t, x, z, theta


# Call the function and store the results

# for i in range(10):
#     filena = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/FinalAnalysis/data0.txt'
#     znot, xnot, thetanot, time, x, z, theta = read_and_parse_data(filena)
#     # for i in range(len(time)):
#     #     time[i] = [time[i], x[i],z[i],theta[i]]
test = []
znot = []
xnot = []
thetanot = []
x = []
z = []
theta = []
print("starting" + "\n")

for i in range(100):
    print("Step: " + str(i) + "\n")
    filena = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/FinalAnalysis/SimulationsData/data' + str(i) + '.txt'
    znot1, xnot1, thetanot1, time, x1, z1, theta1 = read_and_parse_data(filena)
    for i in range(len(time)):
        blah = [time[i], znot1, xnot1, thetanot1]
        test.append(blah)
        znot.append(znot1)
        xnot.append(xnot1)
        thetanot.append(thetanot1)
        z.append(z1[i])
        x.append(x1[i])
        theta.append(theta1[i])
    #TODO fix all that crap
    # Reshape the data

# print(test)
print("Beggining reshaping")
t = np.reshape(test, (len(test), 1, 4))  # Reshape t to (samples, time steps, features(time, znot, xnot, thetanot))

outputs = np.column_stack((x, z, theta))  # Combine x, y, theta into a single matrix for output
# print(t)
print(len(outputs))
# Define the RNN model
model = Sequential()
# model.add(SimpleRNN(units=64, input_shape=(1, 1), activation="relu"))  # RNN layer
model.add(LSTM(units=64, input_shape=(1, 4), activation="relu"))  # RNN layer
model.add(Dense(3))  # Output layer to predict x, y, and theta

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0005), loss='mean_squared_error')
# Train the model
model.fit(t, outputs, epochs=20, batch_size=1028, verbose=1)

model.save('/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/rnn_model.h5')


# Predict function (for new t values)
def predict_for_new_t(new_t):
    new_t = np.array(new_t).reshape((1, 1, 4))  # Reshape new_t to fit the RNN input
    predicted_output = model.predict(new_t)
    return predicted_output[0]  # x, y, theta predictions

# Example prediction

new_t = [0.2, 2, 2, 45]  # New time step to predict x, y, theta
# t = np.reshape(new_t, (1, 1, 4))  # Reshape t to (samples, time steps, features(time, znot, xnot, thetanot))

predicted_x_y_theta = predict_for_new_t(new_t)
print(f'Predicted values for t={new_t}: x={predicted_x_y_theta[0]}, z={predicted_x_y_theta[1]}, theta={predicted_x_y_theta[2]}')



