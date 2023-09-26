import socket
import json

# Server's IP address and port
server_ip = "192.168.1.1"  # Replace with the desired IP address
server_port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server's IP and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(5)

print("Server Raspberry Pi is waiting for connections...")

while True:
    # Accept a connection from a node
    node_socket, node_address = server_socket.accept()
    print(f"Connection established with {node_address}")
    
    # Receive a JSON-encoded list from the node
    json_data = node_socket.recv(1024).decode()
    
    # Deserialize the JSON data into a list
    received_list = json.loads(json_data)
    print(f"Received list from node: {received_list}")
    
    # Close the connection with the node
    node_socket.close()
