import socket
import json

# Server's IP address and port
server_ip = "192.168.1.1"  # Replace with the server's IP address
server_port = 12345

# Create a socket object
node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
node_socket.connect((server_ip, server_port))

# Define the list to send
data_to_send = [1, 2, 3, 4, 5]

# Serialize the list to JSON
json_data = json.dumps(data_to_send)

# Send the JSON data to the server
node_socket.send(json_data.encode())

# Close the connection with the server
node_socket.close()
