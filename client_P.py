#socket library
import socket
import time


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
    
#send some data to Server
request = "GET / HTTP/1.0\r\nHost:%s\r\n\r\n" % HOST
print(request)
s.send(request.encode('UTF-8'))

def recv_timeout(the_socket,timeout=2):
    #make socket non blocking
    the_socket.setblocking(0)
    
    #total data partwise in an array
    total_data=[];
    data='';
    
    #beginning time
    begin=time.time()
    while 1:
        #if got some data,then break after tiemout
        if total_data and time.time()-begin > timeout:
            break
        #if got no data at all,wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
            
#receive all data from Server
        try:
            data= the_socket.recv(8192)
            if data:
                total_data.append(data)
                #sleep for sometime to indicate a gap
                begin=time.time()
            else:
                #sleep fo sometine to indicate a gap
                time.sleep(0.1)
        except:
            pass
    return b''.join(total_data)
 
#get reply and print
print (recv_timeout(s))

#close the socket
s.close()
