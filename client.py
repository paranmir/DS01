import socket

class Client:
        def __init__(self, serverIp):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = serverIp 
        self.port = 2818
        self.addr = (self.client, self.port)

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, gameClass):
        try:
            self.client.send(str.encode(gameClass))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)