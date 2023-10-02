# import cv2
# import numpy as np
#
# # Replace with the actual file path to your image
# image_path = "image4.jpg"  # Change this to your image file path
#
# # Load your image
# frame = cv2.imread(image_path)
#
# # Convert the image to grayscale
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# # Threshold the image to create a binary mask for white pixels
# _, white_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
#
# # Convert the white mask to the inverted mask (to exclude white pixels)
# white_mask_inv = cv2.bitwise_not(white_mask)
#
# # Convert the image to the HSV color space
# hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
# # Define lower and upper bounds for green in HSV
# lower_green = np.array([20, 20, 20])
# upper_green = np.array([35, 255, 255])
#
# # Create a mask for green pixels
# green_mask = cv2.inRange(hsv_image, lower_green, upper_green)
#
# # Apply the white mask to exclude white pixels
# green_mask = cv2.bitwise_and(green_mask, white_mask_inv)
#
# # Apply morphological operations to close gaps between leaves
# kernel_size = 15  # Increase this value for a larger kernel
# kernel = np.ones((kernel_size, kernel_size), np.uint8)
# closed_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)
#
# # Find contours in the binary mask
# contours, _ = cv2.findContours(closed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize a list to store plant areas and centroids
# plant_areas = []
# plant_centroids = []
#
# # Define a minimum distance for merging contours (adjust as needed)
# min_distance = 250
#
#
# # Function to calculate the distance between two centroids
# def centroid_distance(c1, c2):
#     x1, y1 = c1
#     x2, y2 = c2
#     return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#
# # Merge contours based on proximity
# for contour in contours:
#     area = cv2.contourArea(contour)
#
#     # Filter out small noise by setting a minimum area threshold
#     if area > 1000:
#         # Calculate the centroid of the contour
#         M = cv2.moments(contour)
#         if M["m00"] > 0:
#             centroid_x = int(M["m10"] / M["m00"])
#             centroid_y = int(M["m01"] / M["m00"])
#             centroid = (centroid_x, centroid_y)
#
#             # Check if the contour is close to an existing plant
#             merged = False
#             for i, (existing_centroid, existing_area) in enumerate(zip(plant_centroids, plant_areas)):
#                 if centroid_distance(centroid, existing_centroid) < min_distance:
#                     # Merge the contour into the existing plant
#                     plant_areas[i] += area
#                     merged = True
#                     break
#
#             if not merged:
#                 # Create a new plant
#                 plant_areas.append(area)
#                 plant_centroids.append(centroid)
#
# # ...[previous code]...
#
# # Sort plant_centroids and plant_areas based on y-coordinates and then x-coordinates
# sorted_indices = sorted(range(len(plant_centroids)), key=lambda k: (plant_centroids[k][1], plant_centroids[k][0]))
# sorted_plant_centroids = [plant_centroids[i] for i in sorted_indices]
# sorted_plant_areas = [plant_areas[i] for i in sorted_indices]
#
# # Print the areas in order
# for idx, area in enumerate(sorted_plant_areas):
#     print(f"Area {idx+1}: {area} pixels")
#
# # ...[remaining code]...
#
#
# # Draw the outlines of the merged plant contours on the original image
# outline_frame = frame.copy()
# for contour in contours:
#     cv2.drawContours(outline_frame, [contour], -1, (0, 255, 0), 2)
#
# # Display the result (outlines of the merged plant contours)
# cv2.imshow("Plant Leaves Detection", outline_frame)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

# Replace with the actual file path to your image
image_path = "image4.jpg"

# Load your image
frame = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Define your boxes with top-left and bottom-right coordinates
boxes = [
    ((0, 0), (260, 260)),
    ((500, 50), (740, 260)),
    ((1100, 23), (1279, 250)),
    ((150, 352), (303, 481)),
    ((528, 348), (697, 502)),
    ((921, 387), (1129, 538))
]

# Create a black mask of the same size as the frame
combined_mask = np.zeros_like(gray)

# Set the regions for each box as white (255) in the combined mask
for box in boxes:
    top_left, bottom_right = box
    combined_mask[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = 255

# Apply the combined mask to the gray image
gray = cv2.bitwise_and(gray, gray, mask=combined_mask)

# Threshold the image to create a binary mask for white pixels
_, white_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Convert the white mask to the inverted mask (to exclude white pixels)
white_mask_inv = cv2.bitwise_not(white_mask)

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for green in HSV
lower_green = np.array([20, 20, 20])
upper_green = np.array([35, 255, 255])

# Create a mask for green pixels
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Apply the white mask to exclude white pixels
green_mask = cv2.bitwise_and(green_mask, white_mask_inv)

# Apply morphological operations to close gaps between leaves
kernel_size = 15
kernel = np.ones((kernel_size, kernel_size), np.uint8)
closed_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)

# Find contours
contours, _ = cv2.findContours(closed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Variables for storing plant areas and centroids
plant_areas = []
plant_centroids = []

min_distance = 250

def centroid_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Merge contours
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:
        M = cv2.moments(contour)
        if M["m00"] > 0:
            centroid = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            merged = False
            for i, existing_centroid in enumerate(plant_centroids):
                if centroid_distance(centroid, existing_centroid) < min_distance:
                    plant_areas[i] += area
                    merged = True
                    break
            if not merged:
                plant_areas.append(area)
                plant_centroids.append(centroid)

# Sort plants
sorted_indices = sorted(range(len(plant_centroids)), key=lambda k: (plant_centroids[k][1], plant_centroids[k][0]))
sorted_plant_centroids = [plant_centroids[i] for i in sorted_indices]
sorted_plant_areas = [plant_areas[i] for i in sorted_indices]

# Print areas
for idx, area in enumerate(sorted_plant_areas):
    print(f"Area {idx+1}: {area} pixels")

# Draw contours and boxes on the image
outline_frame = frame.copy()
for contour in contours:
    cv2.drawContours(outline_frame, [contour], -1, (0, 255, 0), 2)

for box in boxes:
    cv2.rectangle(outline_frame, box[0], box[1], (255, 0, 0), 2)  # Blue box for each region

# Display the result
cv2.imshow("Plant Leaves Detection", outline_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
