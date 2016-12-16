import socket
import sys
from time import time

def runserver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5055)
	
    print('starting up on ',server_address)
    sock.bind(server_address)
	
    sock.listen(1)
	
    while True:
        print ('waiting for a connection')
        connection, client_address = sock.accept()
		
        try:
            while True:
		data = connection.recv(16)
		print("Received", data)
		if data:
			print("sending data back to the client")
			connection.sendall(str(time()))
			
		else:
			print('no more data from', client_address)
			break
				
        finally:
		connection.close()
		break
if __name__ == '__main__':
	runserver()
