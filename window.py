# -*- Coding: UTF-8 -*-
'''
Project name: LANPoker
FIle name: window.py
File info: Program GUI source code.
Written by: pinkrabbit412 
Written at: 2019.10.21.
Version: v0.0.0.dev191021A.alpha

Copyright 2019. 악동분홍토끼(pinkrabbit412@daum.net). All rights reserved.
'''

#모듈 Import
import tkinter
import tkinter.font as font
import tkinter.messagebox as msgPop
import tkinter.simpledialog as inpPop
import PIL
from PIL import Image
from PIL import ImageTk
from time import sleep

#직접 만든 소스코드 Import
import threading
import cardImages
import game_class1
import game_class2
import game_jokbo

#전역변수의 선언
version = "0.0.0.dev191021A.alpha"
programName = "LANPoker: Client"
programIcon = ""
resolution = "1600x900"
backgroundColor = "#252830"
나눔스퀘어_16pt = "-family 나눔스퀘어 -size 16 -weight normal -slant roman "
나눔스퀘어EB_24pt = "-family {나눔스퀘어 ExtraBold} -size 24 -weight bold "

class Window:
    def disableBetButtonsForStart(self):
        sleep(0.5) #GUI 생성 전에 쓸데없이 반복 실행되지 않도록 0.5초의 딜레이를 줌.
        try:
            self.Betting_CALL.configure(image=self.시작)
            self.Betting_CALL.configure(command=self.askRunGame)
            self.Betting_CALL.image=self.시작
            self.Betting_RAISE.config(state = tkinter.DISABLED)
            self.Betting_CHECK.config(state = tkinter.DISABLED)
            self.Betting_FOLD.config(state = tkinter.DISABLED)
        except:
            self.disableBetButtons()

    def disableBetButtons(self):
        sleep(0.5) #GUI 생성 전에 쓸데없이 반복 실행되지 않도록 0.5초의 딜레이를 줌.
        try:
            self.Betting_CALL.configure(image=self.베팅)
            self.Betting_CALL.configure(command=self.askInitBetting)
            self.Betting_CALL.image=self.베팅
            self.Betting_RAISE.config(state = tkinter.DISABLED)
            self.Betting_CHECK.config(state = tkinter.DISABLED)
            self.Betting_FOLD.config(state = tkinter.DISABLED)
        except:
            self.disableBetButtons()

    def enableBetButtons(self):
        try:
            self.Betting_CALL.configure(image=self.콜)
            self.Betting_CALL.configure(command=self.askCall)
            self.Betting_CALL.image=self.콜
            self.Betting_RAISE.config(state = "normal")
            self.Betting_CHECK.config(state = "normal")
            self.Betting_FOLD.config(state = "normal")
        except:
            self.enableBetButtons()

    def updateMoney(self):
        self.Player1Account.configure(text=(str(self.gameProgress1.moneyOfPlayer1) + "$"))
        self.Player2Account.configure(text=(str(self.gameProgress1.moneyOfPlayer2) + "$"))
        self.BettingText.configure(text=str(self.gameProgress1.collectedBet) + "$ 베팅됨")
            
    ########## [한 세트] 시작 ##########
    def newThread(self):
        newT = threading.Thread(target=self.longTime1)
        newT.start()
        
    def longTime1(self):
        #오래 걸리는 코드
        sleep(2)
        msgPop.showinfo("앙", "김옥지");
    ########## [한 세트] 종료 ##########

    ########## [한 세트] 시작 ##########
    def gameThread(self):
        gameT = threading.Thread(target=self.game_main)
        gameT.start()
        
    def game_main(self):
        import random
        import poker
        from poker import Suit
        from poker import Rank
        from poker import Card
        from poker.hand import Hand, Combo
        self.gameProgress1=game_class2.GameProgress("아귀", "고니", 10000, 10000)
        sleep(0.25) #GUI가 생성되기 전에 동기화되는 것을 방지
        
        while True:
            deck = list(Card)
            random.shuffle(deck)

            #게임을 시작했는지를 감지
            while True:
                try:
                    ##########[ 게임 시작 입력 대기 ]###########
                    self.runGame = False
                    self.disableBetButtonsForStart()
                    while (self.runGame == False):
                        pass
                    self.enableBetButtons()
                    ####################################
                    break
                except:
                    sleep(0.1)
                    continue

            #플레이어 이름 및 소지금 동기화
            self.Player1Name.configure(text=self.gameProgress1.nameOfPlayer1) #위쪽 플레이어
            self.Player2Name.configure(text=self.gameProgress1.nameOfPlayer2) #아래쪽 플레이어 (나)
            self.updateMoney()
            
            #손패 카드 뽑기
            self.gameProgress1.update_notice("[Preflop round]")
            hands1=[deck.pop() for i in range(2)]
            self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer1 + "님이 2장의 카드를 뽑았습니다.")
            self.gameProgress1.append_handsOfPlayer1(hands1)
            self.MyLeftHandData = "" + str(self.gameProgress1.handsOfPlayer1[0].rank) + str(self.gameProgress1.handsOfPlayer1[0].suit)
            self.MyLeftHand_png = Image.open(cardImages.getImage(self.MyLeftHandData))
            self.MyLeftHand = ImageTk.PhotoImage(self.MyLeftHand_png)
            self.MyHand1.configure(image=self.MyLeftHand)#내 왼쪽 손패 보이기
            self.MyRightHandData = "" + str(self.gameProgress1.handsOfPlayer1[1].rank) + str(self.gameProgress1.handsOfPlayer1[1].suit)
            self.MyRightHand_png = Image.open(cardImages.getImage(self.MyRightHandData))
            self.MyRightHand = ImageTk.PhotoImage(self.MyRightHand_png)
            self.MyHand2.configure(image=self.MyRightHand) #내 오른쪽 손패 보이기
            hands2=[deck.pop() for i in range(2)]
            self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer2 + "님이 2장의 카드를 뽑았습니다.")
            self.gameProgress1.append_handsOfPlayer2(hands2)
            ##########[ 플레이어 1 베팅 ]#############
            self.Betting = False
            self.disableBetButtons() #초기베팅용
            while (self.Betting == False):
                pass
            self.Betting = False
            self.enableBetButtons() #초기베팅용
            self.gameProgress1.betting_1(self.toBet)
            self.updateMoney()
            ####################################
            ##########[ 플레이어 2 베팅 ]#############
            self.Betting = False
            while (self.Betting == False):
                pass
            self.Betting = False
            self.gameProgress1.afterBetting_1(self.playerChoice, self.toBet)
            self.updateMoney()
            #####################################

            #공유 카드 세 장 뽑기
            self.gameProgress1.update_notice("[Flop round]")
            self.gameProgress1.update_notice("3장의 공유 카드를 뽑습니다.")
            flop=[deck.pop() for i in range(3)]
            self.gameProgress1.append_communityCards(flop)
            self.OpenCard1Data = "" + str(self.gameProgress1.communityCards[0].rank) + str(self.gameProgress1.communityCards[0].suit)
            self.OpenCard1Image_png = Image.open(cardImages.getImage(self.OpenCard1Data))
            self.OpenCard1Image = ImageTk.PhotoImage(self.OpenCard1Image_png)
            self.OpenCard1.configure(image=self.OpenCard1Image) #첫 번째 공유카드 보이기
            self.OpenCard2Data = "" + str(self.gameProgress1.communityCards[1].rank) + str(self.gameProgress1.communityCards[1].suit)
            self.OpenCard2Image_png = Image.open(cardImages.getImage(self.OpenCard2Data))
            self.OpenCard2Image = ImageTk.PhotoImage(self.OpenCard2Image_png)
            self.OpenCard2.configure(image=self.OpenCard2Image) #두 번째 공유카드 보이기
            self.OpenCard3Data = "" + str(self.gameProgress1.communityCards[2].rank) + str(self.gameProgress1.communityCards[2].suit)
            self.OpenCard3Image_png = Image.open(cardImages.getImage(self.OpenCard3Data))
            self.OpenCard3Image = ImageTk.PhotoImage(self.OpenCard3Image_png)
            self.OpenCard3.configure(image=self.OpenCard3Image) #세 번째 공유카드 보이기
            ##########[ 플레이어 1 베팅 ]#############
            self.Betting = False
            while (self.Betting == False):
                pass
            self.Betting = False
            self.gameProgress1.betting_2(self.playerChoice, self.toBet)
            self.updateMoney()
            #####################################
            ##########[ 플레이어 2 베팅 ]#############
            self.Betting = False
            while (self.Betting == False):
                pass
            self.Betting = False
            self.gameProgress1.afterBetting_2(self.playerChoice, self.toBet)
            self.updateMoney()
            #####################################

            #공유 카드 한 장 뽑기
            
            self.gameProgress1.update_notice("[turn round]")
            self.gameProgress1.update_notice("1장의 공유 카드를 뽑습니다.")
            turn=[deck.pop() for i in range(1)]
            self.gameProgress1.append_communityCards(turn)
            self.OpenCard4Data = "" + str(self.gameProgress1.communityCards[3].rank) + str(self.gameProgress1.communityCards[3].suit)
            self.OpenCard4Image_png = Image.open(cardImages.getImage(self.OpenCard4Data))
            self.OpenCard4Image = ImageTk.PhotoImage(self.OpenCard4Image_png)
            self.OpenCard4.configure(image=self.OpenCard4Image) #네 번째 공유카드 보이기
            ##########[ 플레이어 1 베팅 ]#############
            self.Betting = False
            while (self.Betting == False):
                pass
            self.Betting = False
            self.gameProgress1.betting_2(self.playerChoice, self.toBet)
            self.updateMoney()
            #####################################
            ##########[ 플레이어 2 베팅 ]#############
            self.Betting = False
            while (self.Betting == False):
                pass
            self.Betting = False
            self.gameProgress1.afterBetting_2(self.playerChoice, self.toBet)
            self.updateMoney()
            #####################################

            #공유 카드 한 장 뽑기
            self.gameProgress1.update_notice("[river round]")
            self.gameProgress1.update_notice("1장의 공유 카드를 뽑습니다.")
            river=[deck.pop() for i in range(1)]
            self.gameProgress1.append_communityCards(river)
            self.OpenCard5Data = "" + str(self.gameProgress1.communityCards[4].rank) + str(self.gameProgress1.communityCards[4].suit)
            self.OpenCard5Image_png = Image.open(cardImages.getImage(self.OpenCard5Data))
            self.OpenCard5Image = ImageTk.PhotoImage(self.OpenCard5Image_png)
            self.OpenCard5.configure(image=self.OpenCard5Image) #다섯 번째 공유카드 보이기
            ##########[ 플레이어 1 베팅 ]#############
            self.Betting = False
            while (self.Betting == False):
                pass
            self.Betting = False
            self.gameProgress1.betting_2(self.playerChoice, self.toBet)
            self.updateMoney()
            #####################################
            ##########[ 플레이어 2 베팅 ]#############
            self.Betting = False
            while (self.Betting == False):
                pass
            self.Betting = False
            self.gameProgress1.afterBetting_2(self.playerChoice, self.toBet)
            self.updateMoney()
            #####################################

            # 승패 판정
            player1=self.gameProgress1.handsOfPlayer1+self.gameProgress1.communityCards
            player1.sort()
            player1=game_jokbo.evaluateMax(game_jokbo.combination(player1))

            player2=self.gameProgress1.handsOfPlayer2+self.gameProgress1.communityCards
            player2.sort()
            player2=game_jokbo.evaluateMax(game_jokbo.combination(player2))

            self.gameProgress1.update_notice("[결과]\n(" + self.gameProgress1.nameOfPlayer1 + ")의 최종 패:" +" <"+ game_jokbo.printEvaluate(player1) +"> "+ str(player1)+ "\n(" + self.gameProgress1.nameOfPlayer2 + ")의 최종 패: " + "<" + game_jokbo.printEvaluate(player2)+"> " + str(player2))
            self.gameProgress1.print1()
            
            self.OpHand1Data = "" + str(self.gameProgress1.handsOfPlayer1[0].rank) + str(self.gameProgress1.handsOfPlayer1[0].suit)
            self.OpHand1Image_png = Image.open(cardImages.getImage(self.OpHand1Data))
            self.OpHand1Image = ImageTk.PhotoImage(self.OpHand1Image_png)
            self.OpHand1.configure(image=self.OpHand1Image) #상대의 좌측 패 보이기
            self.OpHand2Data = "" + str(self.gameProgress1.handsOfPlayer1[1].rank) + str(self.gameProgress1.handsOfPlayer1[1].suit)
            self.OpHand2Image_png = Image.open(cardImages.getImage(self.OpHand2Data))
            self.OpHand2Image = ImageTk.PhotoImage(self.OpHand2Image_png)
            self.OpHand2.configure(image=self.OpHand2Image) #상대의 우측 패 보이기
                    
            if game_jokbo.compare(player1,player2) == True:
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer1+" 승리")
                self.gameProgress1.print1()
                self.gameProgress1.append_moneyOfPlayer1(self.gameProgress1.collectedBet)
                self.updateMoney()
                self.gameProgress1.reset()
                    
            elif game_jokbo.compare(player1,player2) == False:
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer2+" 승리")
                self.gameProgress1.print1()
                self.gameProgress1.append_moneyOfPlayer2(self.gameProgress1.collectedBet)
                self.updateMoney()
                self.gameProgress1.reset()

            else:
                self.gameProgress1.update_notice("무승부")
                self.gameProgress1.print1()
                self.gameProgress1.append_moneyOfPlayer1(self.gameProgress1.bet1)
                self.gameProgress1.append_moneyOfPlayer2(self.gameProgress1.bet2)
                self.updateMoney()
                self.gameProgress1.reset()
                
            self.gameProgress1.print1()
            self.BettingText.configure(text="0$ 베팅됨")
            deck.clear()		

            if(self.gameProgress1.moneyOfPlayer1<=0):
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer1+"님께서 파산하셨습니다.")
                self.gameProgress1.print1()
                break
                
            if(self.gameProgress1.moneyOfPlayer2<=0):
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer2+"님께서 파산하셨습니다.")
                self.gameProgress1.print1()
                break
    ########## [한 세트] 종료 ##########

    ########## [새로운 게임] 시작 ##########
    def askRunGame(self):
        self.goNext = msgPop.askquestion(programName, "새 게임을 시작할까요?", parent = self.mainWindow)
        if (self.goNext == "no"
            ):
            return
        self.runGame = True
    ########## [새로운 게임] 부분의 종료 ######

    ########## [초기 베팅] 시작 ##########
    def askInitBetting(self):
        self.goNext = msgPop.askquestion(programName, "베팅할까요?", parent = self.mainWindow)
        if (self.goNext == "no"):
            return
        self.toBet = inpPop.askinteger(programName, "베팅할 액수를 입력하세요. (단위: $)", parent = self.mainWindow)
        self.Betting = True
    ########## [초기 베팅] 종료 ##########

    ########## [베팅: 콜] 시작 ##########
    def askCall(self):
        self.goNext = msgPop.askquestion(programName, "베팅에 응할까요?", parent = self.mainWindow)
        if (self.goNext == "no"):
            return
        self.playerChoice = 1 #1이 콜임
        self.toBet = -1
        self.Betting = True
    ########## [베팅: 콜] 종료 ##########

    ########## [베팅: 레이즈] 시작 ##########
    def askRaiseValue(self):
        self.goNext = msgPop.askquestion(programName, "베팅에 응하고, 추가베팅 할까요?", parent = self.mainWindow)
        if (self.goNext == "no"):
            return
        self.toBet = inpPop.askinteger(programName, "추가 베팅할 액수를 입력하세요. (단위: $)", parent = self.mainWindow)
        if (self.toBet is None):
            return
        self.playerChoice = 2 #2가 레이즈임
        self.Betting = True
    ########## [베팅: 레이즈] 종료 ##########

    ########## [베팅: 레이즈] 시작 ##########
    def askCheck(self):
        self.goNext = msgPop.askquestion(programName, "베팅하지 않고, 턴을 넘길까요?", parent = self.mainWindow)
        if (self.goNext == "no"):
            return
        self.toBet = -1
        self.playerChoice = 3 #3이 체크임
        self.Betting = True
    ########## [베팅: 레이즈] 종료 ##########

    ########## [베팅: 폴드] 시작 ##########
    def askFold(self):
        self.goNext = msgPop.askquestion(programName, "베팅을 포기할까요?", parent = self.mainWindow)
        if (self.goNext == "no"):
            return
        self.toBet = -1
        self.playerChoice = 4 #4가 폴드임
        self.Betting = True
    ########## [베팅: 폴드] 종료 ##########
        
    def main(self):
        self.subT1 = threading.Thread()
        self.gameThread()
        
        self.mainWindow = tkinter.Tk()
        #self.mainWindow.iconbitmap(programIcon)
        self.mainWindow.title(programName)
        self.mainWindow.resizable(False, False)
        self.mainWindow.geometry(resolution)
        self.mainWindow.configure(background = "#252830")

        #플레이어 프로필 사진
        아귀_png = Image.open("./resources/아귀.png")
        고니_png = Image.open("./resources/고니.png")
        플레이어1프사 = ImageTk.PhotoImage(아귀_png)
        플레이어2프사 = ImageTk.PhotoImage(고니_png)

        #베팅 버튼 이미지
        시작_png = Image.open("./resources/START.png")
        베팅_png = Image.open("./resources/BET.png")
        콜_png = Image.open("./resources/CALL.png")
        레이즈_png = Image.open("./resources/RAISE.png")
        체크_png = Image.open("./resources/CHECK.png")
        폴드_png = Image.open("./resources/FOLD.png")
        self.시작 = ImageTk.PhotoImage(시작_png)
        self.베팅 = ImageTk.PhotoImage(베팅_png)
        self.콜 = ImageTk.PhotoImage(콜_png)
        레이즈 = ImageTk.PhotoImage(레이즈_png)
        체크 = ImageTk.PhotoImage(체크_png)
        폴드 = ImageTk.PhotoImage(폴드_png)

        #카드 뒷면 이미지
        뒷면_png = Image.open("./resources/cards/gray_back.png")
        뒷면 = ImageTk.PhotoImage(뒷면_png)

        #버튼
        #mainB1_png = PIL.Image.open("./resources/media/mainB1.png")
        #self.img_InstallerButton = PIL.ImageTk.PhotoImage(mainB1_png)
        #mainB1_Inactive_png = PIL.Image.open("./resources/media/mainB1_inactive.png")
        #self.img_InstallerButton_inactive = PIL.ImageTk.PhotoImage(mainB1_Inactive_png)

        #상대 정보: 상대 프로필 사진
        self.Player1Image = tkinter.Canvas(self.mainWindow)
        self.Player1Image.create_image(0, 0, anchor = "nw", image = 플레이어1프사)
        self.Player1Image.place(relx=0.025, rely=0.033, relheight=0.178, relwidth=0.1)
        self.Player1Image.configure(background=backgroundColor)
        self.Player1Image.configure(borderwidth="2")
        self.Player1Image.configure(insertbackground="black")
        self.Player1Image.configure(relief="ridge")
        self.Player1Image.configure(selectbackground="#c4c4c4")
        self.Player1Image.configure(selectforeground="black")

        #상대 정보: 상대 이름
        self.Player1Name = tkinter.Label(self.mainWindow)
        self.Player1Name.place(relx=0.145, rely=0.067, height=50, width=200)
        self.Player1Name.configure(anchor='w')
        self.Player1Name.configure(background=backgroundColor)
        self.Player1Name.configure(font=나눔스퀘어EB_24pt)
        self.Player1Name.configure(foreground="#FFFFFF")
        self.Player1Name.configure(justify='left')
        self.Player1Name.configure(text='''플레이어 1''')
        self.Player1Name.configure(wraplength="200")

        #상대 정보: 상대 소지금
        self.Player1Account = tkinter.Label(self.mainWindow)
        self.Player1Account.place(relx=0.145, rely=0.122, height=30, width=200)
        self.Player1Account.configure(anchor='w')
        self.Player1Account.configure(background=backgroundColor)
        self.Player1Account.configure(font=나눔스퀘어_16pt)
        self.Player1Account.configure(foreground="#FFFFFF")
        self.Player1Account.configure(justify='left')
        self.Player1Account.configure(text='''데이터 수신 대기중...''')
        self.Player1Account.configure(wraplength="200")

        #상대 패 (왼쪽)
        self.OpHand1 = tkinter.Button(self.mainWindow)
        self.OpHand1.place(relx=0.531, rely=-0.033, height=275, width=200)
        self.OpHand1.configure(image=뒷면)
        self.OpHand1.configure(activebackground=backgroundColor)
        self.OpHand1.configure(activeforeground="#000000")
        self.OpHand1.configure(background=backgroundColor)
        self.OpHand1.configure(disabledforeground="#a3a3a3")
        self.OpHand1.configure(foreground="#000000")
        self.OpHand1.configure(highlightbackground=backgroundColor)
        self.OpHand1.configure(highlightcolor="black")
        self.OpHand1.configure(relief=tkinter.FLAT)
        self.OpHand1.configure(pady="0")
        self.OpHand1.configure(text='''OpHand1''')
        
        #상대 패 (오른쪽)
        self.OpHand2 = tkinter.Button(self.mainWindow)
        self.OpHand2.place(relx=0.675, rely=-0.033, height=275, width=200)
        self.OpHand2.configure(image=뒷면)
        self.OpHand2.configure(activebackground=backgroundColor)
        self.OpHand2.configure(activeforeground="#000000")
        self.OpHand2.configure(background=backgroundColor)
        self.OpHand2.configure(disabledforeground="#a3a3a3")
        self.OpHand2.configure(foreground="#000000")
        self.OpHand2.configure(highlightbackground=backgroundColor)
        self.OpHand2.configure(highlightcolor="black")
        self.OpHand2.configure(relief=tkinter.FLAT)
        self.OpHand2.configure(pady="0")
        self.OpHand2.configure(text='''OpHand2''')

        #좌측 베팅 상황: 이미지
        self.BettingImage = tkinter.Canvas(self.mainWindow)
        self.BettingImage.place(relx=0.025, rely=0.311, relheight=0.333, relwidth=0.188)
        self.BettingImage.configure(background=backgroundColor)
        self.BettingImage.configure(borderwidth="2")
        self.BettingImage.configure(insertbackground="black")
        self.BettingImage.configure(relief="ridge")
        self.BettingImage.configure(selectbackground="#c4c4c4")
        self.BettingImage.configure(selectforeground="black")

        #좌측 베팅 상황: 텍스트
        self.BettingText= tkinter.Label(self.mainWindow)
        self.BettingText.place(relx=0.025, rely=0.656, height=30, width=300)
        self.BettingText.configure(background=backgroundColor)
        self.BettingText.configure(font=나눔스퀘어_16pt)
        self.BettingText.configure(foreground="#BBBBBB")
        self.BettingText.configure(justify='left')
        self.BettingText.configure(text='''0$ 베팅됨''')
        self.BettingText.configure(wraplength="200")

        #공유 카드 1
        self.OpenCard1 = tkinter.Button(self.mainWindow)
        self.OpenCard1.place(relx=0.254, rely=0.344, height=275, width=200)
        self.OpenCard1.configure(image=뒷면)
        self.OpenCard1.configure(activebackground=backgroundColor)
        self.OpenCard1.configure(activeforeground="#000000")
        self.OpenCard1.configure(background=backgroundColor)
        self.OpenCard1.configure(disabledforeground="#a3a3a3")
        self.OpenCard1.configure(foreground="#000000")
        self.OpenCard1.configure(highlightbackground=backgroundColor)
        self.OpenCard1.configure(highlightcolor="black")
        self.OpenCard1.configure(relief=tkinter.FLAT)
        self.OpenCard1.configure(pady="0")
        self.OpenCard1.configure(text='''OpenCard''')

        #공유 카드 2
        self.OpenCard2 = tkinter.Button(self.mainWindow)
        self.OpenCard2.place(relx=0.398, rely=0.344, height=275, width=200)
        self.OpenCard2.configure(image=뒷면)
        self.OpenCard2.configure(activebackground=backgroundColor)
        self.OpenCard2.configure(activeforeground="#000000")
        self.OpenCard2.configure(background=backgroundColor)
        self.OpenCard2.configure(foreground="#000000")
        self.OpenCard2.configure(highlightbackground=backgroundColor)
        self.OpenCard2.configure(highlightcolor="black")
        self.OpenCard2.configure(relief=tkinter.FLAT)
        self.OpenCard2.configure(pady="0")
        self.OpenCard2.configure(text='''OpenCard''')

        #공유 카드 3
        self.OpenCard3 = tkinter.Button(self.mainWindow)
        self.OpenCard3.place(relx=0.541, rely=0.344, height=275, width=200)
        self.OpenCard3.configure(image=뒷면)
        self.OpenCard3.configure(activebackground=backgroundColor)
        self.OpenCard3.configure(activeforeground="#000000")
        self.OpenCard3.configure(background=backgroundColor)
        self.OpenCard3.configure(foreground="#000000")
        self.OpenCard3.configure(highlightbackground=backgroundColor)
        self.OpenCard3.configure(highlightcolor="black")
        self.OpenCard3.configure(relief=tkinter.FLAT)
        self.OpenCard3.configure(pady="0")
        self.OpenCard3.configure(text='''OpenCard''')

        #공유 카드 4
        self.OpenCard4 = tkinter.Button(self.mainWindow)
        self.OpenCard4.place(relx=0.685, rely=0.344, height=275, width=200)
        self.OpenCard4.configure(image=뒷면)
        self.OpenCard4.configure(activebackground=backgroundColor)
        self.OpenCard4.configure(activeforeground="#000000")
        self.OpenCard4.configure(background=backgroundColor)
        self.OpenCard4.configure(disabledforeground="#a3a3a3")
        self.OpenCard4.configure(foreground="#000000")
        self.OpenCard4.configure(highlightbackground=backgroundColor)
        self.OpenCard4.configure(highlightcolor="black")
        self.OpenCard4.configure(relief=tkinter.FLAT)
        self.OpenCard4.configure(pady="0")
        self.OpenCard4.configure(text='''OpenCard''')

        #공유 카드 5
        self.OpenCard5 = tkinter.Button(self.mainWindow)
        self.OpenCard5.place(relx=0.829, rely=0.344, height=275, width=200)
        self.OpenCard5.configure(image=뒷면)
        self.OpenCard5.configure(activebackground=backgroundColor)
        self.OpenCard5.configure(activeforeground="#000000")
        self.OpenCard5.configure(background=backgroundColor)
        self.OpenCard5.configure(disabledforeground="#a3a3a3")
        self.OpenCard5.configure(foreground="#000000")
        self.OpenCard5.configure(highlightbackground=backgroundColor)
        self.OpenCard5.configure(highlightcolor="black")
        self.OpenCard5.configure(relief=tkinter.FLAT)
        self.OpenCard5.configure(pady="0")
        self.OpenCard5.configure(text='''OpenCard''')

        #내 정보: 내 프로필 사진
        self.Player2Image = tkinter.Canvas(self.mainWindow)
        self.Player2Image.place(relx=0.025, rely=0.8, relheight=0.167, relwidth=0.094)
        self.Player2Image.create_image(0, 0, anchor = "nw", image = 플레이어2프사)
        self.Player2Image.configure(background=backgroundColor)
        self.Player2Image.configure(borderwidth="2")
        self.Player2Image.configure(highlightbackground=backgroundColor)
        self.Player2Image.configure(highlightcolor="black")
        self.Player2Image.configure(insertbackground="black")
        self.Player2Image.configure(relief="ridge")
        self.Player2Image.configure(selectbackground="#c4c4c4")
        self.Player2Image.configure(selectforeground="black")
        
        #내 정보: 내 이름
        self.Player2Name = tkinter.Label(self.mainWindow)
        self.Player2Name.place(relx=0.145, rely=0.833, height=50, width=200)
        self.Player2Name.configure(anchor='w')
        self.Player2Name.configure(background=backgroundColor)
        self.Player2Name.configure(disabledforeground="#a3a3a3")
        self.Player2Name.configure(font=나눔스퀘어EB_24pt)
        self.Player2Name.configure(foreground="#FFFFFF")
        self.Player2Name.configure(justify='left')
        self.Player2Name.configure(text='''플레이어 2''')
        self.Player2Name.configure(wraplength="200")
        
        #내 정보: 내 소지금
        self.Player2Account = tkinter.Label(self.mainWindow)
        self.Player2Account.place(relx=0.145, rely=0.889, height=30, width=200)
        self.Player2Account.configure(anchor='w')
        self.Player2Account.configure(background=backgroundColor)
        self.Player2Account.configure(font=나눔스퀘어_16pt)
        self.Player2Account.configure(foreground="#FFFFFF")
        self.Player2Account.configure(justify='left')
        self.Player2Account.configure(text='''데이터 수신 대기중...''')
        self.Player2Account.configure(wraplength="200")

        #내 패 (왼쪽)
        self.MyHand1 = tkinter.Button(self.mainWindow)
        self.MyHand1.place(relx=0.331, rely=0.733, height=275, width=200)
        self.MyHand1.configure(image=뒷면)
        self.MyHand1.configure(activebackground=backgroundColor)
        self.MyHand1.configure(activeforeground="#000000")
        self.MyHand1.configure(background=backgroundColor)
        self.MyHand1.configure(disabledforeground="#a3a3a3")
        self.MyHand1.configure(foreground="#000000")
        self.MyHand1.configure(highlightbackground=backgroundColor)
        self.MyHand1.configure(highlightcolor="black")
        self.MyHand1.configure(pady="0")
        self.MyHand1.configure(text='''MyHand1''')

        #내 패 (오른쪽)
        self.MyHand2 = tkinter.Button(self.mainWindow)
        self.MyHand2.place(relx=0.475, rely=0.733, height=275, width=200)
        self.MyHand2.configure(image=뒷면)
        self.MyHand2.configure(activebackground=backgroundColor)
        self.MyHand2.configure(activeforeground="#000000")
        self.MyHand2.configure(background=backgroundColor)
        self.MyHand2.configure(disabledforeground="#a3a3a3")
        self.MyHand2.configure(foreground="#000000")
        self.MyHand2.configure(highlightbackground=backgroundColor)
        self.MyHand2.configure(highlightcolor="black")
        self.MyHand2.configure(pady="0")
        self.MyHand2.configure(text='''MyHand2''')

        #베팅 버튼: 콜
        self.Betting_CALL = tkinter.Button(self.mainWindow)
        self.Betting_CALL.place(relx=0.688, rely=0.744, height=75, width=200)
        self.Betting_CALL.configure(image=self.콜)
        self.Betting_CALL.configure(activebackground="#151820")
        self.Betting_CALL.configure(background=backgroundColor)
        self.Betting_CALL.configure(pady="0")
        self.Betting_CALL.configure(relief=tkinter.FLAT)
        self.Betting_CALL.configure(text='''CALL''')

        #베팅 버튼: 체크
        self.Betting_RAISE = tkinter.Button(self.mainWindow)
        self.Betting_RAISE.place(relx=0.844, rely=0.744, height=75, width=200)
        self.Betting_RAISE.configure(activebackground=backgroundColor)
        self.Betting_RAISE.configure(image=레이즈)
        self.Betting_RAISE.configure(activebackground="#151820")
        self.Betting_RAISE.configure(background=backgroundColor)
        self.Betting_RAISE.configure(pady="0")
        self.Betting_RAISE.configure(relief=tkinter.FLAT)
        self.Betting_RAISE.configure(text='''RAISE''')
        self.Betting_RAISE.configure(command=self.askRaiseValue)

        #베팅 버튼: 레이즈
        self.Betting_CHECK = tkinter.Button(self.mainWindow)
        self.Betting_CHECK.place(relx=0.688, rely=0.867, height=75, width=200)
        self.Betting_CHECK.configure(image=체크)
        self.Betting_CHECK.configure(activebackground="#151820")
        self.Betting_CHECK.configure(background=backgroundColor)
        self.Betting_CHECK.configure(pady="0")
        self.Betting_CHECK.configure(relief=tkinter.FLAT)
        self.Betting_CHECK.configure(text='''CHECK''')
        self.Betting_CHECK.configure(command=self.askCheck)

        #베팅 버튼: 폴드
        self.Betting_FOLD = tkinter.Button(self.mainWindow)
        self.Betting_FOLD.place(relx=0.844, rely=0.867, height=75, width=200)
        self.Betting_FOLD.configure(image=폴드)
        self.Betting_FOLD.configure(activebackground="#151820")
        self.Betting_FOLD.configure(background=backgroundColor)
        self.Betting_FOLD.configure(pady="0")
        self.Betting_FOLD.configure(relief=tkinter.FLAT)
        self.Betting_FOLD.configure(text='''FOLD''')
        self.Betting_CHECK.configure(command=self.askFold)

        #GUI 메인루프
        self.mainWindow.update()
        self.mainWindow.mainloop()
        
#Application Start.
mainWindow = Window()
mainWindowThread = threading.Thread(target = mainWindow.main)
mainWindowThread.start()




























