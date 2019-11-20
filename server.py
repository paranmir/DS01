import socket
import threading

class Server:
    def __init__(self):
        #듣는 소켓 생성. ipv4 사용
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 서버 호스트 ip, 포트 지정 후 소켓과 포트 연결
        self.SERVER = '' # 모든 인터페이스에 바인딩, INADDR_ANY 즉 외부에서 볼 수 있게
        self.PORT = 2818

        try:
            self.serverSocket.bind((self.SERVER, self.PORT))
        except socket.error as e:
            print(str(e))
        
        # 서버객체를 만들면 연결요청 두개를 받을때까지 대기.
        self.serverSocket.listen(2)

        # 확장성을 위한 튜플
        self.connectedSocketList = []
        self.serverThreads = []


    #스레드 start시에 시작할 메소드
    def run(self):
        try:
            while True:
                #통신소켓 생성
                (connectedSocket, clientAddress) = self.serverSocket.accept()
                self.connectedSocketList.append(connectedSocket)
        except:
            pass
    # def getServerIp(self):
    #     # 서버 ip 스트링 반환.
    #     return self.gethostbyname(self.server)

server = Server()
server.run()
