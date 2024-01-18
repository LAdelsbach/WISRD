import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf

# Load the data
file_path = '/Users/lukeadelsbach/Desktop/WISRD/PaperAirplane/flight_test.txt'
df = pd.read_csv(file_path)

# Select features (t, x, z, theta) and target (x, z, theta at next time step)
features = df[['t', 'x', 'z', 'theta']]
target = df[['x', 'z', 'theta']].shift(-1)  # Shifted by one time step

# Drop the last row as it has NaN values after shifting
features, target = features[:-1], target[:-1]

# Normalize the features
scaler_features = MinMaxScaler()
features_scaled = scaler_features.fit_transform(features)

# Normalize the target
scaler_target = MinMaxScaler()
target_scaled = scaler_target.fit_transform(target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target_scaled, test_size=0.2, random_state=42)

# Reshape input to be [samples, time steps, features]
X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

# Define the RNN model
model = tf.keras.Sequential([
    tf.keras.layers.SimpleRNN(50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])),
    tf.keras.layers.Dense(3)  # Output layer with 3 neurons for x, z, and theta
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print('Test loss:', loss)
#2