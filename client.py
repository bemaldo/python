import socket
import sys
import time

host = '127.0.0.1'

port = 4044
addr = (host,port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)
sending = 'some text'
client.send(sneding)
client.close()
