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
      
      
    
