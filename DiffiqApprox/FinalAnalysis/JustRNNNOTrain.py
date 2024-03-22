import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/rnn_model.h5')


# loaded_model = model_from_json(loaded_model_json)
# load weights into new model
# loaded_model.load_weights('/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/rnn_model.h5')
print("Loaded model from disk")


def predict_for_new_t(new_t):
    new_t = np.array(new_t).reshape((1, 1, 4))  # Reshape new_t to fit the RNN input
    predicted_output = model.predict(new_t)
    return predicted_output[0]  # x, y, theta predictions

# Example prediction

new_t = [0.2, 2, 2, 45]  # New time step to predict x, y, theta
# t = np.reshape(new_t, (1, 1, 4))  # Reshape t to (samples, time steps, features(time, znot, xnot, thetanot))

predicted_x_y_theta = predict_for_new_t(new_t)
print(f'Predicted values for t={new_t}: x={predicted_x_y_theta[0]}, z={predicted_x_y_theta[1]}, theta={predicted_x_y_theta[2]}')
