import socket
import threading

bind = '0.0.0.0'
port = 5055

def handle_client(client_socket):
    request = client_socket.recv(1024)
    client_socket.send('ACK')
    client_socket.close()
def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind,port))
    print("[*]Listening on %s:%d"%(bind,port))
    
    while True:
        client, addr = server.accept()
        print("[*]Accepted connection from %s:%d" %(addr[0],addr[1]))
        client_handler = threading.Thread(target=handle_client, args =(client,))
        client_handler.start()
if __name == '__name__':
    tcp_server()
