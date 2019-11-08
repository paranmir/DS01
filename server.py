import socket
from _thread import *

class Server:

    def __init__(self):
        #소켓 생성. ipv4 사용
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 서버 호스트 ip, 포트 지정 후 소켓과 포트 연결
        self.server = '' # 모든 인터페이스에 바인딩, INADDR_ANY 즉 외부에서 볼 수 있게
        self.port = 2818
        self.server_ip = socket.gethostbyname(self.server)
        try:
            self.serverSocket.bind((server, port))
        except socket.error as e:
            print(str(e))
            
    def waitClient():
        self.socket.listen(1)

    def getServerIp(self):
        # 서버 ip 스트링 반환.
        return self.server_ip

    def sendHandsToClient('''클라이언트에서 받아야할 클라의 손패 정보''''):
        
    def getHandsFromClient():

    def sendBetToClient():
    
    def getBetFromClient():
    
