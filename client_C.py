#socket library
import socket

#server's hostname or IP address
HOST = "www.google.com"  
#port number used by google
PORT = 80 

#creating socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

#connecting to the Remote Server
s.connect((HOST, PORT))
print("successfully connected")
    
#send HTTP GET request (to fetch the data from the server)
request = "GET / HTTP/1.0\r\nHost:%s\r\n\r\n" % HOST
s.send(request.encode('UTF-8'))
print('success!!')

#Receive the response
response = b""
data = s.recv(8192)
response += data

#Close the socket
s.close()

# Split the response into HTTP response, headers, and HTML content
response_str = response.decode('utf-8')
parts = response_str.split('\n',2)
http_response,header,contents = parts[0],parts[1],parts[2]

# Extract response code and message
response_parts = http_response.split(' ',2)
code = int(response_parts[1])
message = response_parts[2]

#store header content in the dictionary
for a in header:
    if ':' in a:
        parameter , value = a.split(':',1)

#initialize dictionary
dict = {}
   
if code == 200:
  print("HTTP Response-->",http_response)
  print("HTTP Header-->",header)
  print("HTTP contents-->",contents)
  
else:
    print("Request failed")


