import socket

# Define the server address and port
server_address = 'localhost',12347


# Create a TCP socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print(f"listening for incoming TCP connections on {server_address}")

while True:
	# Accept a connection from a clinet
	client_socket, client_address = server_socket.accept()
	print(f"Connected to {client_address}")

    # Define received message here
	received_message = ""

	while True:
		# Receive data from the client
		data = client_socket.recv(1024)
		if not data:
			break

		message = data.decode('utf-8')
		print(f"Received data: {message}")

		# Construct an appropriate response
		if message.startswith("TNE20003:"):
			received_message = message[len("TNE20003"):]
			if len(received_message)>=1:
				response = f"TNE20003:A{received_message}"
			else:
				response = "TNE20003:E: At least one character"
		else:
			response = "TNE20003:E:Invalid message"

		# Send data to the client
		client_socket.send(response.encode('utf-8'))

		# Check for an exit condition
		if received_message.lower() == "exit":
			break
        
print(f"connection to {client_address} closed")
client_socket.close()
        
# Close the server socket when it is doen
server_socket.close()





	