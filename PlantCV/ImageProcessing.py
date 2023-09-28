
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
# # Apply the mask to the original image
# green_objects = cv2.bitwise_and(original_image, original_image, mask=green_mask)
#
# # Find contours in the mask
# contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize a list to store pixel counts for each plant
# plant_pixel_counts = []
#
# # Loop through each detected contour (plant) and calculate pixel count
# for contour in contours:
#     pixel_count = cv2.contourArea(contour)
#     plant_pixel_counts.append(pixel_count)
#
#     # Draw the contour on the masked image (green_objects)
#     cv2.drawContours(green_objects, [contour], -1, (0, 255, 0), 2)
#
# # Print pixel counts for each plant
# for i, pixel_count in enumerate(plant_pixel_counts):
#     if pixel_count > 1000:
#         print(f"Plant {i + 1} Pixel Count: {pixel_count}")
#
# # Display the original image with contours on the masked image
# cv2.imshow("Original Image with Contours", green_objects)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #
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
# # Apply the mask to the original image
# masked_image = cv2.bitwise_and(original_image, original_image, mask=green_mask)
#
# # Find contours in the mask
# contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Initialize a list to store bounding boxes
# bounding_boxes = []
#
# # Define a padding value to make the bounding boxes larger
# padding = 10  # Adjust this value to make the boxes larger or smaller
#
# # Loop through each detected contour (plant)
# for contour in contours:
#     # Find the bounding rectangle around the plant
#     x, y, w, h = cv2.boundingRect(contour)
#
#     # Expand the bounding rectangle by adding padding
#     x -= padding
#     y -= padding
#     w += 2 * padding
#     h += 2 * padding
#
#     bounding_boxes.append((x, y, x + w, y + h))
#
# # Combine overlapping bounding boxes
# combined_boxes, _ = cv2.groupRectangles(bounding_boxes, groupThreshold=1, eps=0.2)
#
# # Draw the combined bounding boxes (overlapping and larger than 10 pixels) on the masked image
# for (x, y, x2, y2) in combined_boxes:
#     cv2.rectangle(masked_image, (x, y), (x2, y2), (0, 255, 0), 2)
#
# # Display the original image with combined bounding rectangles
# cv2.imshow("Original Image with Combined Bounding Rectangles", masked_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Replace with the actual file path to your image
image_path = "image3.jpg"  # Change this to your image file path

# Load your image
frame = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
kernel_size = 15  # Increase this value for a larger kernel
kernel = np.ones((kernel_size, kernel_size), np.uint8)
closed_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)

# Find contours in the binary mask
contours, _ = cv2.findContours(closed_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize a list to store plant areas and centroids
plant_areas = []
plant_centroids = []

# Define a minimum distance for merging contours (adjust as needed)
min_distance = 30


# Function to calculate the distance between two centroids
def centroid_distance(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Merge contours based on proximity
for contour in contours:
    area = cv2.contourArea(contour)

    # Filter out small noise by setting a minimum area threshold
    if area > 100:
        # Calculate the centroid of the contour
        M = cv2.moments(contour)
        if M["m00"] > 0:
            centroid_x = int(M["m10"] / M["m00"])
            centroid_y = int(M["m01"] / M["m00"])
            centroid = (centroid_x, centroid_y)

            # Check if the contour is close to an existing plant
            merged = False
            for i, (existing_centroid, existing_area) in enumerate(zip(plant_centroids, plant_areas)):
                if centroid_distance(centroid, existing_centroid) < min_distance:
                    # Merge the contour into the existing plant
                    plant_areas[i] += area
                    merged = True
                    break

            if not merged:
                # Create a new plant
                plant_areas.append(area)
                plant_centroids.append(centroid)

# Draw the outlines of the merged plant contours on the original image
outline_frame = frame.copy()
for contour in contours:
    cv2.drawContours(outline_frame, [contour], -1, (0, 255, 0), 2)

# Display the result (outlines of the merged plant contours)
cv2.imshow("Plant Leaves Detection", outline_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
