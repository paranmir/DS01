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
version = "0.0.0.dev191021A.alpha"
programIcon = ""

resX = 1280
resY = 720
targetRes = 0
resolution = "1280x720"

def refreshResolution():
    resolution = (str(resX) + "x" + str(resY))
    print(targetRes)
    print(resolution)

import tkinter
import tkinter.messagebox as msgPop
import threading
from time import sleep

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

    def main(self):
        self.subT1 = threading.Thread()
        
        self.mainWindow = tkinter.Tk()
        #self.mainWindow.iconbitmap(programIcon)
        self.mainWindow.title("LANPoker: Client")
        self.mainWindow.resizable(False, False)
        self.mainWindow.geometry(resolution)
        self.mainWindow.configure(background = "#252830")

        #버튼
        #mainB1_png = PIL.Image.open("./resources/media/mainB1.png")
        #self.img_InstallerButton = PIL.ImageTk.PhotoImage(mainB1_png)
        #mainB1_Inactive_png = PIL.Image.open("./resources/media/mainB1_inactive.png")
        #self.img_InstallerButton_inactive = PIL.ImageTk.PhotoImage(mainB1_Inactive_png)

        #상대 정보
        self.opponentInfo = tkinter.Button(self.mainWindow)
        self.opponentInfo.place(x = 0, y = 0, width = 300, height = 185)

        #상대 패
        self.myCard1 = tkinter.Button(self.mainWindow)
        self.myCard1.place(x = 740, y = -90, width = 200, height = 275)
        self.myCard2 = tkinter.Button(self.mainWindow)
        self.myCard2.place(x = 986, y = -90, width = 200, height = 275)


        #좌측 족보
        self.jokbo = tkinter.Button(self.mainWindow)
        self.jokbo.place(x = 0, y = 185, width = 300, height = 350)

        #공유 카드
        self.myCard1 = tkinter.Button(self.mainWindow)
        self.myCard1.place(x = 740, y = -90, width = 200, height = 275)
        self.myCard2 = tkinter.Button(self.mainWindow)
        self.myCard2.place(x = 986, y = -90, width = 200, height = 275)


        #내 정보
        self.myInfo = tkinter.Button(self.mainWindow)
        self.myInfo.place(x = 0, y = 535, width = 300, height = 185)

        #내 패
        self.myCard1 = tkinter.Button(self.mainWindow)
        self.myCard1.place(x = 417, y = 535, width = 200, height = 275)
        self.myCard2 = tkinter.Button(self.mainWindow)
        self.myCard2.place(x = 663, y = 535, width = 200, height = 275)

        #베팅
        self.betting = tkinter.Button(self.mainWindow)
        self.betting.place(x = 980, y = 535, width = 300, height = 185)

        self.mainWindow.update()
        self.mainWindow.mainloop()

#Application Start.
mainWindow = Window()
mainWindowThread = threading.Thread(target = mainWindow.main)
mainWindowThread.start()




























