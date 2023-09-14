
import cv2
from plantcv import plantcv as pcv

image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Start a PlantCV session
pcv.params.debug = "plot"
pcv.params.debug_outdir = "."  # Output directory for debug images (current directory)

# Apply a threshold to segment the plant from the background
binary_image = pcv.threshold.binary(gray_image, threshold=120, object_type="dark")

# Find plant contours
contours, _ = pcv.find_objects(binary_image, gray_image)

# Measure plant properties
plant_measurements = pcv.report_size_shape(contours)

# Print the results
print("Plant Measurements:")
print(plant_measurements)

# Save debug images (if debug mode is enabled)
pcv.print_image(binary_image, "binary_image.png")
pcv.print_image(gray_image, "gray_image.png")

# Close the PlantCV session
pcv.params.debug = "print"
pcv.outputs.clear()

# Display the original image with plant contours (for visualization purposes)
cv2.drawContours(image, contours, 1, (0, 255, 0), 2)
cv2.imshow("Plant Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
