import socket

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
    
    # Receive code from the node
    received_code = node_socket.recv(1024).decode()
    
    # Execute the received code
    try:
        exec(received_code)
        response = "Code execution successful."
    except Exception as e:
        response = f"Code execution failed: {str(e)}"
    
    # Send a response back to the node
    node_socket.send(response.encode())
    
    # Close the connection with the node
    node_socket.close()
