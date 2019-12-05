import socket

class Client:
        # 클래스 선언하면 접속요청할 때 쓸 소켓 생성함
        # 클래스 생성할 때 인자로 유저로부터 서버아이피를 입력받아줘야함
        def __init__(self, serverIp):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = serverIp 
        self.port = 2818
        self.addr = (self.client, self.port)

    # 서버로부터 게임 정보를 받아옴
    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    # 서버로 내 클라의 게임 정보를 보냄
    def send(self, gameClass):
        try:
            self.client.send(str.encode(gameClass))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)