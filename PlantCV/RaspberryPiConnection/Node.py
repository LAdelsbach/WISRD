import socket

# Coordinator's IP address and port
coordinator_ip = "192.168.1.1"  # Replace with the coordinator's IP address
coordinator_port = 12345

# Create a socket object
node_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the coordinator
node_socket.connect((coordinator_ip, coordinator_port))

# Define the code to send
code_to_send = """
print("Hello from the Node Raspberry Pi!")
"""

# Send the code to the coordinator
node_socket.send(code_to_send.encode())

# Receive a response from the coordinator
response = node_socket.recv(1024).decode()
print(f"Received response from coordinator: {response}")

# Close the connection with the coordinator
node_socket.close()
