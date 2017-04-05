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
    s.bind((HOST,PORT))
  except socket.error as msg:
    print('bind failed. error code: ' + str(msg[0]) + ' message ' + msg[1])
    print('[*] YOU MUST RUN YOUR CLIENT FROM A LOCAL TERMINAL.')
    sys.exit()
    
  s.listen(100)
  
  while 1:
    conn, addr = s.accept()
    CLIENTS.append(conn)
    thrd = Thread(target=recvHandle, args=(conn,addr))
    thrd.start()
  s.close()

def recvHandle(connection, address):
  data = ''
  while 1:
    try:
      data = connection.recv(4096).decode('ascii')
    except:
      pass
    
    if not data:
      CLIENTS.remove(connection)
      break
    data = processEmoji(data)
    if data.startswith('[*]'):
      data = SERVER%data
    else:
      data = OTHER_USER % data
    os.system('clear')
    LOG.append(data)
    for l in LOG:
      print(l+'\n')
  connection.close()
  
def client(name):
  os.system('clear')
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = ((MAIN_HOST, MAIN_PORT))
  s.connect(server_address)
  
  s.sendall('#name' + '.' + name)
  sleep(1) #delay to send the online message because it is receieving and must stop before next receive
  s.sendall('#online') 
  
  try:
    message = ''
    while True:
      message = raw_input('')
      if not(message == ''):
        if message == 'exit':
          break
        s.sendall(message)
        os.system('clear')
        message = processEmoji(message)
        
        if not(message == '#online'):
          LOG.append(' You: ' + message)
        for l in LOG:
          print(l + '\n')
  finally:
    s.close()
    os.system('clear')
    os.kill(os.getpid(), signal.SIGTERM)
    
def processEmoji(string):
  for key in EMOJIS:
    if key in string:
      string = string.replace(key, EMOJIS[key])
  return string

def initEmojis(): # add emojis here
  EOMJIS[':D'] = u'\U0001F600'
  EOMJIS['|D'] = u'\U0001F601'
  EOMJIS['%D'] = u'\U0001F602'
  EOMJIS['8D'] = u'\U0001F603'
  EOMJIS['|D'] = u'\U0001F604'
  EOMJIS['XD'] = u'\U0001F605'
  EOMJIS['xD'] = u'\U0001F606'
  EOMJIS[':p'] = u'\U0001F607'
  EOMJIS[':('] = u'\U0001F608'

if __name__ == '__main__':
  initEmojis()
  serve = Thread(target=server, args=[])
  serve.start()
  name = raw_input('Enter your name: ')
  sleep(2)
  clnt = Thread(target=client, args=(name,))
  clnt.start()
