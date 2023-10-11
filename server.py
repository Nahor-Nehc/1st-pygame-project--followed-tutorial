import socket
from _thread import *
import sys
from Components.bullet import Bullet, Bullets
from Components.format_data import convert
from Components.settings import *

server = "10.100.224.96" # local address!!!!!
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.bind((server, port))
except socket.error as e:
  print(e)

s.listen(2)  # how many things it is going to allow to connect
print("Server started, waiting for connection")



spaceship_pos = [(0, 0), (100, 100)]
bullets = [Bullets(), Bullets()]

def threaded_client(conn, current_player):
  conn.send(str.encode(convert(spaceship_pos[current_player])))
  reply = ""
  while True:
    try:
      data = conn.recv(2048) # receives the data
      data = data.decode("utf-8") # decode data, arg is the number of bits to receive
      data = convert(data) # convert string to tuple of positions
      #pos[current_player] = data

      
      if not data:
        print("disconnected")
        break
      
      else:
        if current_player == 1:
          pass
          #reply = pos[0]
        elif current_player == 0:
          pass
          #reply = pos[1]

        # print("Received:", data)
        # print("sending:", reply)
      
      conn.sendall(str.encode(convert(reply))) # encodes with utf-8
    
    except:
      print("error")
  
  print("lost connection")
  conn.close()

current_player = 0
while True:
  conn, addr = s.accept() # accepts incoming connections, address = ip address
  print("Connected to:", addr)
  
  start_new_thread(threaded_client, (conn, current_player)) # allows the program to continue to look for new connections while client program runs
  current_player += 1