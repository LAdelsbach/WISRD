import cv2
import numpy as np

# Replace with the actual file path to your image
image_path = "image2.jpg"  # Change this to your image file path

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
    if area > 1000:
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

# ...[previous code]...

# Sort plant_centroids and plant_areas based on y-coordinates and then x-coordinates
sorted_indices = sorted(range(len(plant_centroids)), key=lambda k: (plant_centroids[k][1], plant_centroids[k][0]))
sorted_plant_centroids = [plant_centroids[i] for i in sorted_indices]
sorted_plant_areas = [plant_areas[i] for i in sorted_indices]

# Print the areas in order
for idx, area in enumerate(sorted_plant_areas):
    print(f"Area {idx+1}: {area} pixels")

# ...[remaining code]...


# Draw the outlines of the merged plant contours on the original image
outline_frame = frame.copy()
for contour in contours:
    cv2.drawContours(outline_frame, [contour], -1, (0, 255, 0), 2)

# Display the result (outlines of the merged plant contours)
cv2.imshow("Plant Leaves Detection", outline_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()