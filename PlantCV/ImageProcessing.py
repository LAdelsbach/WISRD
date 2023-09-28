# #🩵🩷🤍🩷🩵🤍

# import cv2
# import numpy as np

# original_image = cv2.imread("image3.jpg")

# # Convert to HSV color space
# hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# lower_green = np.array([20, 20, 20])
# upper_green = np.array([35, 255, 255])

# #mask
# green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

# # Apply the mask
# green_objects = cv2.bitwise_and(original_image, original_image, mask=green_mask)

# # Display the original image and the result
# cv2.imshow("Original Image", original_image)
# cv2.imshow("Green Objects", green_objects)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

# Replace with the actual file path to your image
image_path = "image3.jpg"

# Load your image
original_image = cv2.imread(image_path)

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for green in HSV
lower_green = np.array([20, 20, 20])
upper_green = np.array([35, 255, 255])

# Create a mask for green pixels
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Apply the mask to the original image
green_objects = cv2.bitwise_and(original_image, original_image, mask=green_mask)

# Find contours in the mask
contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a list to store pixel counts for each plant
plant_pixel_counts = []

# Loop through each detected contour (plant) and calculate pixel count
for contour in contours:
    pixel_count = cv2.contourArea(contour)
    plant_pixel_counts.append(pixel_count)

    # Draw the contour on the masked image (green_objects)
    cv2.drawContours(green_objects, [contour], -1, (0, 255, 0), 2)

# Print pixel counts for each plant
for i, pixel_count in enumerate(plant_pixel_counts):
    if pixel_count > 1000:
        print(f"Plant {i + 1} Pixel Count: {pixel_count}")

# Display the original image with contours on the masked image
cv2.imshow("Original Image with Contours", green_objects)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# import cv2
# import numpy as np
#
# # Replace with the actual file path to your image
# image_path = "image3.jpg"
#
# # Load your image
# original_image = cv2.imread(image_path)
#
# # Convert the image to the HSV color space
# hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
#
# # Define lower and upper bounds for green in HSV
# lower_green = np.array([20, 20, 20])
# upper_green = np.array([35, 255, 255])
#
# # Create a mask for green pixels
# green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
#
# # Find contours in the mask
# contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize a list to store pixel counts for each plant
# plant_pixel_counts = []
#
# # Define a padding value to make the bounding boxes larger
# padding = 50  # Adjust this value to make the boxes larger or smaller
#
# # Loop through each detected contour (plant)
# for contour in contours:
#     # Calculate pixel count for the current plant
#     pixel_count = cv2.contourArea(contour)
#     plant_pixel_counts.append(pixel_count)
#
#     # Find the bounding rectangle around the plant
#     x, y, w, h = cv2.boundingRect(contour)
#
#     # Expand the bounding rectangle by adding padding
#     x -= padding
#     y -= padding
#     w += 2 * padding
#     h += 2 * padding
#
#     # Draw a bounding rectangle around the plant on the original image
#     cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# # Print pixel counts for each plant
# for i, pixel_count in enumerate(plant_pixel_counts):
#     print(f"Plant {i + 1} Pixel Count: {pixel_count}")
#
# # Display the original image with larger bounding rectangles
# cv2.imshow("Original Image with Larger Bounding Rectangles", original_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # Calculate pixel count for the current plant
# pixel_count = cv2.contourArea(contour)
# plant_pixel_counts.append(pixel_count)
#
#     # Find the bounding rectangle around the plant
# x, y, w, h = cv2.boundingRect(contour)
#
#     # Draw a bounding rectangle around the plant on the original image
# cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# # Print pixel counts for each plant
# for i, pixel_count in enumerate(plant_pixel_counts):
#     print(f"Plant {i + 1} Pixel Count: {pixel_count}")
#
# # Display the original image with bounding rectangles
# cv2.imshow("Original Image with Bounding Rectangles", original_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
