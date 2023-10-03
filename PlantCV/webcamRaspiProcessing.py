import cv2
import numpy as np
import time

# Initialize the webcam (you may need to change the device index)
cam = cv2.VideoCapture(0)  # Use 0 as the device index for the default webcam

# Check if the webcam is opened successfully
if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Define your boxes with top-left and bottom-right coordinates
boxes = [
    ((0, 0), (260, 260)),
    ((500, 50), (740, 260)),
    ((1100, 23), (1279, 250)),
    ((150, 352), (303, 481)),
    ((528, 348), (697, 502)),
    ((921, 387), (1129, 538))
]

while True:
    # Capture a frame from the webcam
    ret, frame = cam.read()

    if not ret:
        print("Error: Could not read a frame from the webcam.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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

    # Convert the frame to the HSV color space
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
        print(f"Area {idx + 1}: {area} pixels")

    # Wait for 2 minutes before capturing the next image
    time.sleep(120)

# Release the webcam and close all windows
cam.release()
cv2.destroyAllWindows()
