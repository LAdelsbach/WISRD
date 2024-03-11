import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

# Load the saved model
model_path = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/modelTest.keras'  # Adjust path as needed
model = keras.models.load_model(model_path)
print("Model loaded successfully.")

# Example new data for prediction
new_data = {
    't': [0.00021600],
    'x': [0.00200990],
    'z': [1.00201125],
    'theta': [44.99999995]
}

new_df = pd.DataFrame(new_data)
print("New data prepared:", new_df)

# Assuming you have saved your scaler or you're fitting it again for demonstration
# In practice, you should save and load your scaler
scaler_features = MinMaxScaler()

# Fit scaler to some example features (this should ideally be the same data used for training)
# For the purpose of this demonstration, using new_df as a placeholder
scaler_features.fit(new_df)  # Fit scaler to the features
print("Feature scaler fitted.")

# Scale the new data
new_features_scaled = scaler_features.transform(new_df)
print("New features scaled:", new_features_scaled)

# Reshape for the RNN input
new_features_scaled = new_features_scaled.reshape((new_features_scaled.shape[0], 1, new_features_scaled.shape[1]))

# Make predictions
predictions_scaled = model.predict(new_features_scaled)
print("Predictions (scaled):", predictions_scaled)

# Assuming this scaler was fitted to the target during training
# For demonstration, using the same scaler as a placeholder
scaler_target = MinMaxScaler()
scaler_target.fit(new_df[['x', 'z', 'theta']])  # Fit scaler to the target

# Inverse transform the predictions to original scale
predictions = scaler_target.inverse_transform(predictions_scaled)
print("Predicted x, z, theta:", predictions)

