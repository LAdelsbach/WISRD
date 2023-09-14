
import cv2
import numpy as np

original_image = cv2.imread("image3.jpg")

# Convert to HSV color space
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

lower_green = np.array([20, 20, 20])
upper_green = np.array([80, 255, 255])

#mask
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Apply the mask
green_objects = cv2.bitwise_and(original_image, original_image, mask=green_mask)

# Display the original image and the result
cv2.imshow("Original Image", original_image)
cv2.imshow("Green Objects", green_objects)
cv2.waitKey(0)
cv2.destroyAllWindows()
