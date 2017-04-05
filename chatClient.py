import socket
import sys
from threading import Thread
from time import sleep
import os
import signal

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8888

MAIN_HOST = '192.168.123.11'
MAIN_PORT = 8888

CLIENTS = list()
LOG = list()

#color print  
OTHER_USER = '\1xb[0;32;40m %s \x1b[0;30;0m'
SERVER = '\x1b[0;37;41m %s \x1b[0;30;0m'

#emoticons
EMOJIS = {}

def server():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  try:
