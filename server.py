import socket
import threading
import select

HEADER_LENGTH = 10
class Server:
    def __init__(self):
        #서버 소켓 생성. ipv4 사용
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketList = []
        self.clients = {}

        #주소 재사용 가능하게 설정.
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 서버 호스트 ip, 포트 지정 후 소켓과 포트 연결
        self.SERVER = '' # ''인 이유는 모든 인터페이스에 바인딩, INADDR_ANY 즉 외부에서 볼 수 있게
        self.PORT = 2818
        
        try:
            self.serverSocket.bind((self.SERVER, self.PORT))
        except socket.error as e:
            print(str(e))
        
    def run(self):
        iothread = threading.Thread(target=serverIoThread)
        iothread.start()


    def serverIoThread(self):
        # 연결요청 받을때까지 대기.
        self.serverSocket.listen()
        self.socketList.append(self.serverSocket)
        while True:
            # I/O 멀티플렉싱을 위한 select. readSocket만 쓸거임.
            readSockets, _writeSockets, _exceptionSockets = select.select(self.socketList, [], self.socketList)

            #갱신된 소켓들만 처리
            for renewedSocket in readSockets:
                # 서버소켓으로 클라에서 연결요청 온 경우에는
                if renewedSocket == self.serverSocket:
                    clientSocket, clientAddress = self.serverSocket.accept()
                    
                    data = recvData(clientSocket)

                    if data is False:
                        continue
                    # save clients 
                    self.clients[clientSocket] = data
                    # select할 리스트에 클라 추가
                    self.socketList.append(clientSocket)

                    ################### 데이터 저장 ###################
                    # ex ) data = data
                    ##################################################

                # 이미 리스트에 있는 소켓에서 메세지 보낸거면
                else:
                    #receive data
                    data = recvData(renewedSocket)

                    #if False, client disconnected
                    if data is False:
                        print('closed connection form client')
                        self.socketList.remove(renewedSocket)
                        del clients[renewedSocket]
                        continue

                    print('received data from client')

                    for clientSocket in clients:
                        if clientSocket != renewedSocket:
                            sendData(clientSocket)

    def sendData(clientSocket):
        ########################데이터 보내기 #######################
        sendingData = pickle.dumps(''' 보낼 데이터(클래스/튜플/뭐든) ''')
        ############################################################
        sendingData = bytes(f"{len(sendingData):<{HEADER_LENGTH}}", 'utf-8')+sendingData
        clientSocket.send(sendingData)

    def recvData(clientSocket):
        try:
            # 바이너리로 저장.
            fullData = b''
            newData = True
                # 소켓으로 받는건 한번에 안오니까 전부 받을때까지 while로 대기.
            while True:
                data = s.recv(1024)
                #맨 처음 새로운 데이터를 받았을때에만 실행.
                if newData:
                    # 전부 받으려면 크기를 알아야함. HEADER_LENGTH가 데이터 앞에 데이터크기 붙여놓은 크기임.
                    # split 사용해서 그만큼만 잘라다가 씀.
                    print("new data len:",data[:HEADER_LENGTH])
                    datalen = int(msg[:HEADER_LENGTH])
                    new_msg = False

                print(f"full data length: {datalen}")
                fullData += data
                print("current received : ", len(fullData))

                if len(fullData)-HEADER_LENGTH == datalen:
                    print("full data recved")
                    ############## 게임 정보 클래스 리턴할 것 #########################
                    return pickle.loads(full_msg[HEADERSIZE:])
                    ##################################################################
                    

        except:
            return False