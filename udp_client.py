import socket


SERVER_IP = 'localhost' 
SERVER_PORT = 55555 

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("UDP socket successfully")


while True:
    # Prompt the user for a message to send
    message = input("Enter a messageghjk: ")

    if message.lower() == 'exit':
        print("Exiting client...")
        break
    elif message:
        
        # Send the command to the server
        client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
        print("Massage sent success!!")

        # Receive the server's response
        data, server = client_socket.recvfrom(16100)
        print(f"Received from server: {data.decode()}")

client_socket.close()
print("Socket closed")