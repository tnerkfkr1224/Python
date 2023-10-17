import socket

SERVER_IP = "localhost" 
SERVER_PORT = 55555  

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("UDP socket created")

# Bind the socket to the server address
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")


while True:
    data, addr = server_socket.recvfrom(16100)
    received_message = data.decode()
    
    # Check if the received message starts with the protocol header
    if received_message.startswith('TNE20003:'):
      
        response = f"A:{received_message}"
        actual_message = received_message[9:]
        # Check if the actual message is at least one character long
        if len(actual_message) >= 1:
            response = f"TNE20003:A:{actual_message}"
        else:
            response = "TNE20003:E:EMessage should be there"
    else:
        response = "NE20003:E:ERROR"


    server_socket.sendto(response.encode(), addr)