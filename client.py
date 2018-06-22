#TCP Client
import socket 

host = "192.168.10.100" 
port = 5500
buffer_len = 2048 
command = "Connection Request"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((host, port))

while command != 'exit':
    client.send(command)     
    data = client.recv(buffer_len)
    print "received data:", data
    command = raw_input("Enter command or 'exit' to quit:")

client.close()