import numpy as np
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense, LSTM
from keras.optimizers.legacy import Adam
# Import necessary library
import pandas as pd

# Define the file path
file_path = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/test1.txt'


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

    # Open and read the file
    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        
        # Read each line, split by comma, and append to lists
        for line in file:
            values = line.strip().split(',')
            t.append(float(values[0]))
            x.append(float(values[1]))
            z.append(float(values[2]))
            theta.append(float(values[3]))

    return t, x, z, theta


# Call the function and store the results
time, x, z, theta = read_and_parse_data(file_path)
# for i in range(len(time)):
#     time[i] = [time[i], x[i],z[i],theta[i]]



#TODO fix all that crap

# Reshape the data
t = np.reshape(time, (len(time), 1, 1))  # Reshape t to (samples, time steps, features)

outputs = np.column_stack((x, z, theta))  # Combine x, y, theta into a single matrix for output
print(t)
print(len(outputs))
# Define the RNN model
model = Sequential()
# model.add(SimpleRNN(units=64, input_shape=(1, 1), activation="relu"))  # RNN layer
model.add(LSTM(units=64, input_shape=(1, 1), activation="relu"))  # RNN layer
model.add(Dense(3))  # Output layer to predict x, y, and theta

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')
# Train the model
model.fit(t, outputs, epochs=20, batch_size=16, verbose=1)

model.save('/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/rnn_model.h5')


# Predict function (for new t values)
def predict_for_new_t(new_t):
    new_t = np.array(new_t).reshape((1, 1, 1))  # Reshape new_t to fit the RNN input
    predicted_output = model.predict(new_t)
    return predicted_output[0]  # x, y, theta predictions

# Example prediction
new_t = 0.2  # New time step to predict x, y, theta
predicted_x_y_theta = predict_for_new_t(new_t)
print(f'Predicted values for t={new_t}: x={predicted_x_y_theta[0]}, z={predicted_x_y_theta[1]}, theta={predicted_x_y_theta[2]}')

