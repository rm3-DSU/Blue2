#TCP Server
import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn

clientList = "clients.txt" #file to store list of connected clients

class ClientThread(Thread): 

    def __init__(self,ip,port):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "Client connection: " + ip + ":" + str(port)
        #write new client connection to file
        file = open(clientList,"a") 
        file.write(ip + ":" + str(port) + "\n")
        file.close()
 
    def run(self): 
        while True: 
            data = conn.recv(2048) 
            print "Server received data: ", data,"\n"
            if data == "Connection Request":
              response = "Ok"
            elif data == "sendClientList":
              file = open(clientList,"r")
              response = file.read()
              file.close()    
            elif data == "sendServerCode":
              file = open("server.py","r")
              response = file.read()
              file.close()   
            else:
              response = "Command not found"
          
            conn.send(response)




TCP_IP = '192.168.10.100' 
TCP_PORT = 5500 
#BUFFER_SIZE = 32
MAX_QCONN = 5 #maximum number of queued connections

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
  server.listen(MAX_QCONN) 
  print "Listening for connections ..." 
  (conn, (ip,port)) = server.accept() 
  newthread = ClientThread(ip,port) 
  newthread.start() 
  threads.append(newthread) 
 
for t in threads: 
    t.join() 

