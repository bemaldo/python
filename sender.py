import socket
import sys
from time import time

def runclient():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
    server_address = ('localhost', 5055)
	
	#connect the socket to the port where the server is listening
    sock.connect(server_address)
	
    try:
	sendTime = time()
	#send data
	message = "This is the message.  It will be repeated."
	sock.sendall(message)
	
	# Lookfor the reponse
	amount_received = 0
	amount_expected = len(message)
	
	#while amount_received < amount_expected:
		#data = sock.recv(16)
		#amount_received +=len(data)
		#print(sys.stderr, ('received "%s"') % data)
	data = sock.recv(16)
	print("[*]Received", data)
    finally:
	print('closing socket')
	sock.close()
	return float(data)-sendTime
	
if __name__ == '__main__':
	delay = runclient()
	print(delay)
