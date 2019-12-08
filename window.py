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
programIcon = ""
resolution = "1600x900"
backgroundColor = "#252830"
나눔스퀘어_16pt = "-family 나눔스퀘어 -size 16 -weight normal -slant roman "
나눔스퀘어EB_24pt = "-family {나눔스퀘어 ExtraBold} -size 24 -weight bold "

class Window:
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
        self.gameProgress1=game_class2.GameProgress("고니","아귀",5000,1000)
        while True:
            deck = list(Card)
            random.shuffle(deck)

            #손패 카드 뽑기
            self.gameProgress1.update_notice("[Preflop round]")
            hands1=[deck.pop() for i in range(2)]
            self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer1 + "님이 2장의 카드를 뽑았습니다.")
            self.gameProgress1.append_handsOfPlayer1(hands1)
            hands2=[deck.pop() for i in range(2)]
            self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer2 + "님이 2장의 카드를 뽑았습니다.")
            self.gameProgress1.append_handsOfPlayer2(hands2)
            self.gameProgress1.betting_1()
            self.gameProgress1.afterBetting_1()

            #공유 카드 세 장 뽑기
            self.gameProgress1.update_notice("[Flop round]")
            self.gameProgress1.update_notice("3장의 공유 카드를 뽑습니다.")
            flop=[deck.pop() for i in range(3)]
            self.gameProgress1.append_communityCards(flop)
            self.gameProgress1.betting_2()
            self.gameProgress1.afterBetting_2()

            #공유 카드 한 장 뽑기
            self.gameProgress1.update_notice("[turn round]")
            self.gameProgress1.update_notice("1장의 공유 카드를 뽑습니다.")
            turn=[deck.pop() for i in range(1)]
            self.gameProgress1.append_communityCards(turn)
            self.gameProgress1.betting_2()
            self.gameProgress1.afterBetting_2()

            #공유 카드 한 장 뽑기
            self.gameProgress1.update_notice("[river round]")
            self.gameProgress1.update_notice("1장의 공유 카드를 뽑습니다.")
            river=[deck.pop() for i in range(1)]
            self.gameProgress1.append_communityCards(river)
            self.gameProgress1.betting_2()
            self.gameProgress1.afterBetting_2()

            # 승패 판정
            player1=self.gameProgress1.handsOfPlayer1+self.gameProgress1.communityCards
            player1.sort()
            player1=game_jokbo.evaluateMax(game_jokbo.combination(player1))

            player2=self.gameProgress1.handsOfPlayer2+self.gameProgress1.communityCards
            player2.sort()
            player2=game_jokbo.evaluateMax(game_jokbo.combination(player2))

            self.gameProgress1.update_notice("[결과]\n(" + self.gameProgress1.nameOfPlayer1 + ")의 최종 패:" +" <"+ game_jokbo.printEvaluate(player1) +"> "+ str(player1)+ "\n(" + self.gameProgress1.nameOfPlayer2 + ")의 최종 패: " + "<" + game_jokbo.printEvaluate(player2)+"> " + str(player2))
            self.gameProgress1.print1()		
                    
            if game_jokbo.compare(player1,player2) == True:
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer1+" 승리")
                self.gameProgress1.print1()
                self.gameProgress1.append_moneyOfPlayer1(self.gameProgress1.collectedBet)
                self.gameProgress1.reset()
                    
            elif game_jokbo.compare(player1,player2) == False:
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer2+" 승리")
                self.gameProgress1.print1()
                self.gameProgress1.append_moneyOfPlayer2(self.gameProgress1.collectedBet)
                self.gameProgress1.reset()

            else:
                self.gameProgress1.update_notice("무승부")
                self.gameProgress1.print1()
                self.gameProgress1.append_moneyOfPlayer1(self.gameProgress1.bet1)
                self.gameProgress1.append_moneyOfPlayer2(self.gameProgress1.bet2)
                self.gameProgress1.reset()

            self.gameProgress1.print1()
            deck.clear()		

            if(self.gameProgress1.moneyOfPlayer1==0):
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer1+"님께서 파산하셨습니다.")
                self.gameProgress1.print1()
                break
                
            if(self.gameProgress1.moneyOfPlayer2==0):
                self.gameProgress1.update_notice(self.gameProgress1.nameOfPlayer2+"님께서 파산하셨습니다.")
                self.gameProgress1.print1()
                break
    ########## [한 세트] 종료 ##########

    def main(self):
        self.gameThread()
        self.subT1 = threading.Thread()
        
        self.mainWindow = tkinter.Tk()
        #self.mainWindow.iconbitmap(programIcon)
        self.mainWindow.title("LANPoker: Client")
        self.mainWindow.resizable(False, False)
        self.mainWindow.geometry(resolution)
        self.mainWindow.configure(background = "#252830")

        #플레이어 프로필 사진
        아귀_png = Image.open("./resources/아귀.png")
        고니_png = Image.open("./resources/고니.png")
        플레이어1프사 = ImageTk.PhotoImage(아귀_png)
        플레이어2프사 = ImageTk.PhotoImage(고니_png)

        #베팅 버튼 이미지
        콜_png = Image.open("./resources/CALL.png")
        레이즈_png = Image.open("./resources/RAISE.png")
        체크_png = Image.open("./resources/CHECK.png")
        폴드_png = Image.open("./resources/FOLD.png")
        콜 = ImageTk.PhotoImage(콜_png)
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
        self.Player1Account.configure(text='''소지금: 3000$''')
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
        self.OpHand1.configure(relief="flat")
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
        self.OpHand2.configure(relief="flat")
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
        self.BettingText.configure(text='''3000$ 베팅됨''')
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
        self.OpenCard1.configure(relief="flat")
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
        self.OpenCard2.configure(relief="flat")
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
        self.OpenCard3.configure(relief="flat")
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
        self.OpenCard4.configure(relief="flat")
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
        self.OpenCard5.configure(relief="flat")
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
        self.Player2Account.configure(text='''소지금: 3000$''')
        self.Player2Account.configure(wraplength="200")

        #내 패 (왼쪽)
        self.MyHand1 = tkinter.Button(self.mainWindow)
        self.MyHand1.place(relx=0.331, rely=0.733, height=275, width=200)
        MyLeftHand_png = Image.open(cardImages.getImage(self.gameProgress1.handsOfPlayer2[0]))
        MyLeftHand = ImageTk.PhotoImage(MyLeftHand_png)
        self.MyHand1.configure(image=MyLeftHand)
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
        self.Betting_CALL.configure(image=콜)
        self.Betting_CALL.configure(activebackground="#151820")
        self.Betting_CALL.configure(background=backgroundColor)
        self.Betting_CALL.configure(pady="0")
        self.Betting_CALL.configure(relief="flat")
        self.Betting_CALL.configure(text='''CALL''')

        #베팅 버튼: 체크
        self.Betting_CHECK = tkinter.Button(self.mainWindow)
        self.Betting_CHECK.place(relx=0.844, rely=0.744, height=75, width=200)
        self.Betting_CHECK.configure(activebackground=backgroundColor)
        self.Betting_CHECK.configure(image=레이즈)
        self.Betting_CHECK.configure(activebackground="#151820")
        self.Betting_CHECK.configure(background=backgroundColor)
        self.Betting_CHECK.configure(pady="0")
        self.Betting_CHECK.configure(relief="flat")
        self.Betting_CHECK.configure(text='''RAISE''')

        #베팅 버튼: 레이즈
        self.Betting_RAISE = tkinter.Button(self.mainWindow)
        self.Betting_RAISE.place(relx=0.688, rely=0.867, height=75, width=200)
        self.Betting_RAISE.configure(image=체크)
        self.Betting_RAISE.configure(activebackground="#151820")
        self.Betting_RAISE.configure(background=backgroundColor)
        self.Betting_RAISE.configure(pady="0")
        self.Betting_RAISE.configure(relief="flat")
        self.Betting_RAISE.configure(text='''CHECK''')

        #베팅 버튼: 폴드
        self.Betting_FOLD = tkinter.Button(self.mainWindow)
        self.Betting_FOLD.place(relx=0.844, rely=0.867, height=75, width=200)
        self.Betting_FOLD.configure(image=폴드)
        self.Betting_FOLD.configure(activebackground="#151820")
        self.Betting_FOLD.configure(background=backgroundColor)
        self.Betting_FOLD.configure(pady="0")
        self.Betting_FOLD.configure(relief="flat")
        self.Betting_FOLD.configure(text='''FOLD''')

        self.mainWindow.update()
        self.mainWindow.mainloop()

#Application Start.
mainWindow = Window()
mainWindowThread = threading.Thread(target = mainWindow.main)
mainWindowThread.start()




























