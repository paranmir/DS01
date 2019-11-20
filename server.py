import socket
import threading

class Server(threading.thread):
    def __init__(self):
        threading.Thread.__init__(self)

        #듣는 소켓 생성. ipv4 사용
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 서버 호스트 ip, 포트 지정 후 소켓과 포트 연결
        self.SERVER = '' # 모든 인터페이스에 바인딩, INADDR_ANY 즉 외부에서 볼 수 있게
        self.PORT = 2818
        # self.server_ip = socket.gethostbyname(self.server)

        try:
            self.serverSocket.bind((SERVER, PORT))
        except socket.error as e:
            print(str(e))

        self.serverSocket.listen(2)

        # 확장성을 위한 튜플
        self.connectedSocketTuple = []
        #self.serverThreads = []


    #스레드 start시에 시작할 메소드
    def run(self):
        try:
            while True:
                #통신소켓 생성
                connectedSocket, clientAddress = self.serverSocket.accept()
                self.connectedSocketTuple.append(connectedSocket)

           
    # def getServerIp(self):
    #     # 서버 ip 스트링 반환.
    #     return self.server_ip

    # # 클라이언트에 정보 주고받는 메소드
    # def sendHandsToClient('''클라이언트에서 받아야할 클라의 손패 정보''''):
        
    # def getHandsFromClient():

    # def sendBetToClient():
    
    # def getBetFromClient():

