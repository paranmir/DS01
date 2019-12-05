import socket
import pickle
HEADER_LENGTH = 10

class Client:
        # 클래스 선언하면 접속요청할 때 쓸 소켓 생성함
        # 클래스 생성할 때 인자로 유저로부터 서버아이피를 입력받아줘야함
        def __init__(self, serverIp):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = serverIp 
        self.port = 2818
        self.addr = (self.client, self.port)
        self.locking = threading.Lock()

    # 서버로 내 클라의 게임 정보를 보냄
    def send(self, gameClass):
        try:
            self.client.send(str.encode(gameClass))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)

    def run(self):
        #서버랑 연결
        self.client.connect(self.addr)

        # 계속 io해줌
        sendThread = Threading.Thread(target= sThread)
        readThread = Threading.Thread(target= rThread)
        sendThread.start()
        readThread.start()

    def sThread(self):
        while True:
            #send my data
            self.locking.acquire()
            sendingData = pickle.dump(''' data class to send ''' )
            sendingData = bytes(f"{len(sendingData):<{HEADER_LENGTH}}", 'utf-8')+sendingData
            clientSocket.send(sendingData)
            self.locking.release()

    def rThread(self):
        #get data

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
                # print("new data len:",data[:HEADER_LENGTH])
                datalen = int(msg[:HEADER_LENGTH])
                new_msg = False

            fullData += data

            if len(fullData)-HEADER_LENGTH == datalen:
                print("full data recved")
                ############## 게임 정보 클래스 저장할 것 #########################
                self.locking.acquire()
                '''data class to save  = ''' pickle.loads(full_msg[HEADERSIZE:])
                self.locking.release()
                ##################################################################
                break
