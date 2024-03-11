# Import necessary library
import pandas as pd

# Define the file path
file_path = '/Users/lukeadelsbach/Desktop/WISRD/DiffiqApprox/test1.txt'

# Read and parse the data from the file
def read_and_parse_data(file_path):
    # Initialize lists for each variable
    t = []
    x = []
    z = []
    theta = []

    # Open and read the file
    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        
        # Read each line, split by comma, and append to lists
        for line in file:
            values = line.strip().split(',')
            t.append(float(values[0]))
            x.append(float(values[1]))
            z.append(float(values[2]))
            theta.append(float(values[3]))

    return t, x, z, theta

# Call the function and store the results
t, x, z, theta = read_and_parse_data(file_path)

# Print the results
print("t:", t[0])
print("x:", x[0])
print("z:", z[0])
print("theta:", theta[0])
