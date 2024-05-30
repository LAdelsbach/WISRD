import numpy as np
import os
from keras.models import load_model
from sklearn.metrics import mean_squared_error

# Define a function to calculate Mean Absolute Percentage Error
def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    non_zero_mask = y_true != 0  # Avoid division by zero
    if np.any(non_zero_mask):
        return np.mean(np.abs((y_true[non_zero_mask] - y_pred[non_zero_mask]) / y_true[non_zero_mask])) * 100
    else:
        return np.nan  # Return NaN if all y_true values are zero

# Function to read and parse the test data
def read_and_parse_data(file_path):
    with open(file_path, 'r') as file:
        next(file)  # Skip the header
        init_values = file.readline().strip().split(',')
        znot, xnot, thetanot = float(init_values[0]), float(init_values[1]), float(init_values[2])
        next(file)  # Skip the second header
        t, x, z, theta = [], [], [], []
        for line in file:
            values = line.strip().split(',')
            t.append(float(values[0]))
            x.append(float(values[1]))
            z.append(float(values[2]))
            theta.append(float(values[3]))
    return znot, xnot, thetanot, t, x, z, theta

# Directory containing test data files
data_directory = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/FinalAnalysis/TestingData/'
model_path = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/rnn_model.h5'

# Load the trained model
model = load_model(model_path)

# Prepare to aggregate MSE and MAPE
mse_x_list, mse_z_list, mse_theta_list = [], [], []
mape_x_list, mape_z_list, mape_theta_list = [], [], []

# Process each test data file
for filename in os.listdir(data_directory):
    if filename.startswith("data") and filename.endswith(".txt"):
        file_path = os.path.join(data_directory, filename)

        # Load the test data
        znot, xnot, thetanot, t, x_actual, z_actual, theta_actual = read_and_parse_data(file_path)

        # Prepare the test inputs
        test_input = np.array([[time_step, znot, xnot, thetanot] for time_step in t])
        test_input = np.reshape(test_input, (len(test_input), 1, 4))

        # Predict using the model
        predictions = model.predict(test_input)
        x_pred, z_pred, theta_pred = predictions[:, 0], predictions[:, 1], predictions[:, 2]

        # Calculate MSE for each output
        mse_x = mean_squared_error(x_actual, x_pred)
        mse_z = mean_squared_error(z_actual, z_pred)
        mse_theta = mean_squared_error(theta_actual, theta_pred)

        # Calculate MAPE for each output
        mape_x = mean_absolute_percentage_error(x_actual, x_pred)
        mape_z = mean_absolute_percentage_error(z_actual, z_pred)
        mape_theta = mean_absolute_percentage_error(theta_actual, theta_pred)

        # Store results
        mse_x_list.append(mse_x)
        mse_z_list.append(mse_z)
        mse_theta_list.append(mse_theta)
        mape_x_list.append(mape_x)
        mape_z_list.append(mape_z)
        mape_theta_list.append(mape_theta)

# Calculate average MSE and MAPE across all files
avg_mse_x = np.mean(mse_x_list)
avg_mse_z = np.mean(mse_z_list)
avg_mse_theta = np.mean(mse_theta_list)
avg_mape_x = np.mean(mape_x_list)
avg_mape_z = np.mean(mape_z_list)
avg_mape_theta = np.mean(mape_theta_list)

# Print average MSE and MAPE results
print(f"Average Mean Squared Error for x: {avg_mse_x:.4f}, Average MAPE: {avg_mape_x:.2f}%")
print(f"Average Mean Squared Error for z: {avg_mse_z:.4f}, Average MAPE: {avg_mape_z:.2f}%")
print(f"Average Mean Squared Error for theta: {avg_mse_theta:.4f}, Average MAPE: {avg_mape_theta:.2f}%")