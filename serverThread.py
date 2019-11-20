import socket, threading
class serverThread(threading.Thread):
    def __init__(self, serverThreads, connectedSocketList, connectedSocket, clientAddress):
        threading.Thread.__init__(self)

        self.serverThreads = serverThreads
        self.connectedSocketList = connectedSocketList
        self.connectedSocket = connectedSocket
        self.clientAddress = clientAddress

    def run(self):
        try:
        # 게임 정보 클래스를 중계해서 전달하는 코드
        # ex) data = self.connectedSocket.recv()
        except:
            self.connectedSocketList.remove(self.connectedSocket)
            self.serverThreads.remove(self)
            exit(0)
        self.connectedSocketList.remove(self.connectedSocket)
        self.serverThreads.remove(self)

    def send(connectedSocket, gameClass) :
        print("sending from server")
        try:
            connectedSocket.sendall(gameClass)

        except:
            pass