import socket

# Define the server address and port
server_address = ('localhost', 12347)

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(server_address)

while True:
    # Prompt the user to input a message
    message = input("Enter a message:")
    
    # Send the message to the server
    client_socket.send(message.encode('utf-8'))
    
    # Receive data from the server
    response = client_socket.recv(1024)
    print(f"Received response: {response.decode('utf-8')}")

    # Check for an exit condition
    if message.lower() == "exit":
        break

# Close the client socket when done
client_socket.close()
