import socket
import sys
from threading import Thread

HOST = '192.168.123.11'
PORT = 8888

CLIENTS = list()
CLIENT_IPS = list()
CLIENT_NAMES = {}

def server():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print('socket created')
  
  try:
    s.bind((HOST,PORT))
  except socket.error as msg:
    print('bind failed.  error code: ' + str(msg[0]) + ' message ' + msg[1])
    sys.exit()
    
  print('socket bind complete')
  
  s.listen(100)
  
  print('listening')
  
  while 1:
    conn, addr = s.accept()
    CLIENTS.append(conn)
    CLIENT_IPS.append(addr[0])
    print('connected with ' + addr[0] + ':' + str(addr[1]))
    thrd = Thread(target = recvHandle, args = (conn,addr))
    thrd.start()
    
  print('closing the socket')
  s.close()
  
def recvHandle(connection, address):
  print('starting recvHandle for ', address)
  data = ''
  while 1:
    try:
      data = connection.recv(4096).decode('ascii')
    except:
      pass # connection removed
      
    if not data:
      print('removing connection with ' + address[0] + ':' + str(address[1]))
      msg = 'Left the chat.'
      mvh = Thread(target=broadcastMessage, args=(msg,connection, address[0]))
      mvh.start()
      
      CLIENTS.remove(connection)
      CLIENT_IPS.remove(address[0])
      
      break
      
    print(data)
    if data == '#online':
      data = '';
      
      cmdAnswr = Thread(target = answerOnlineCommand, args =(data,connection,address[0]))
      cmdAnswr.start()
      
    elif data.split('.',1)[0] == '#name':
      print('in name clause: ', data)
      nameChange = False
      if address[0] in CLIENT_NAMES.keys():
        print('name change detected')
        newName = data.split('.',1)[1]
        if newName in CLIENT_NAMES.values():
          data = newName
          nameChangeError = Thread(target=invalidNameChange, args=(data,connection,address[0]))
          nameChangeError.start()
          
        else:
          data = CLIENT_NAMES[address[0]] = newName
          userNameChange = Thread(target=broadcastMessage, args =(data,connection,address[0], True))
          userNameChange.start()
        nameChange = True
        
      if not nameChange:
        CLIENT_NAMES[address[0]] = data.split('.',1)[1]
        data = CLIENT_NAMES[ddress[0]] + ' entered the chat.'
        userEnter = Thread(target=notifyEntry, args = (data,connection, address[0]))
        userEnter.start()
        
      nameChange = False
    else:
      mvh = Thread(target = broadcastMessage, args=(data,connection, address[0]))
      mvh.start()
  connection.close()
     
    
def invalidNameChange(message, sender, ip):
    print('Reporting name selection already exists.')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, 8888)
    s.connect(server_address)
    s.sendall('[*] NameError: The name "' + message + '" is already in use.')
    
def notifyEntry(message, sender, ip):
  print('broadcasting entry...')
  ip_cursor = 0
  for connection in CLIENTS:
      if connection == sender:
          pass
      else:
          try:
            print('sending to ' + ip + ':8888')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('sent to other...')
            server_address = ((CLIENT_IPS[ip_cursors], 8888))
            s.connect(server_address)
            s.sendall('[*]'  + message)
          finally:
            s.close()
      ip_cursor += 1
      
def answerGetClientsCommand():
  pass

def answerOnlineCommand(message, sender, ip):
  try:
    message = list()
    for clnt in CLIENT_IPS:
      if not(clnt == ip):
        message.append(CLIENT_NAMES[clnt])
    if len(message) == 0:
      message = 'No Users online.'
    else:
      message = ','.join(message)
      message = 'Users Online: ' + message
    
    print('Replying online command to ' + ip + ':8888')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, 8888)
    s.connect(server_address)
    s.sendall('[*]' + message)
    print('Replied command')
  finally:
    s.close()
    
