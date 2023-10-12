import socket

class Network:
  def __init__(self):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server = "10.100.227.43" # local address!!!!!
    self.port = 5555
    self.addr = (self.server, self.port)
    self.init_pos = self.connect()
  
  def get_init_pos(self):
    return self.init_pos
    
  def connect(self):
    try:
      self.client.connect(self.addr)
      return self.client.recv(2048).decode("utf-8")
    except:
      pass
  
  def send(self, data):
    try:
      self.client.send(str.encode(data))
      return self.client.recv(2048).decode("utf-8") 
    except socket.error as e:
      print(e)
