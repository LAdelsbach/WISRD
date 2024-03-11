import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paper Airplane Trajectory")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Airplane properties
airplane_size = 20

# Scale factor for the coordinates
scale_factor = 100  # Adjust this as needed to fit your data

# Function to read trajectory data from a file
def read_trajectory(file_path):
    points = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            _, x, z, _ = line.split(',')  # Change here if format is different
            scaled_x = int(float(x) * scale_factor)
            scaled_z = int(float(z) * scale_factor)
            points.append((scaled_x, scaled_z))
    return points

# Read the trajectory data
file_path = '/Users/lukeadelsbach/Desktop/math/flight_test.txt'
trajectory_points = read_trajectory(file_path)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the trajectory
    for x, y in trajectory_points:
        pygame.draw.rect(screen, RED, (x, height - y, airplane_size, airplane_size))  # Inverting y for Pygame coordinates

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
