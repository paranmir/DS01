import random
import poker
from poker import Suit
from poker import Rank
from poker import Card
from poker.hand import Hand, Combo

import game_jokbo
import game_class

class Print(game_class.GameInfo):     # 그냥 gui만들기 전에 값 전달 잘 되는지 확인해보려고 만들어본 클래스
    def print1(self):
        print(self.notice)
        print("============================================")
        print("player1: ",self.nameOfPlayer1)
        print("         남은 돈: ",self.moneyOfPlayer1)
        print("         패: ",self.handsOfPlayer1)
        print("============================================")
        print("player2: ",self.nameOfPlayer2)
        print("         남은 돈: ",self.moneyOfPlayer2)
        print("         패: ",self.handsOfPlayer2)
        print("============================================")
        print("전체: ")
        print("         모인 돈: ",self.collectedBet)
        print("         공통 카드: ",self.communityCards)
        print("============================================")




class GameProgress(Print):	# 선택을 입력받고 결과 출력하는 클래스.(게임은 한 사람이 선택을 할 때마다 진행된다.)
    def __init(self):
        self.choice=0     # 선택한 번호를 저장하는 변수.(이 부분은 수정해야 할 듯.)
        self.bet1=0
        self.bet1_1=0
        self.bet2=0
        self.bet2_2=0



    def reset(self):
        self.handsOfPlayer1.clear()
        self.handsOfPlayer2.clear()
        self.collectedBet=0
        self.communityCards.clear()
        self.bet1=0
        self.bet2=0
        self.bet1_1=0
        self.bet2_1=0


               
    def betting_1(self): # big blind가 먼저 베팅을 하는 메소드.(일단 player1이 big blind라고 했음.)

        self.print1()    # 출력

        
        self.update_notice("big bind ("+self.nameOfPlayer1+") 님이 베팅을 선택하십시오: \n1: 베팅 \n2: 체크 (베팅을 하지 않음.)")

        self.print1()    # 출력

        self.choice=int(input()) # 선택을 입력받음.(이 부분은 수정해야 할 듯.)

        if int(self.choice)==1:
            self.update_notice("베팅 \nbig bind ("+self.nameOfPlayer1+") 님께서 베팅하실 금액을 정해주십시오: ")
            self.print1()    # 출력
            self.bet1_1=int(input())
            self.append_moneyOfPlayer1(-int(self.bet1_1))
            self.append_collectedBet(int(self.bet1_1))
            self.append_bet1(int(self.bet1_1))

        else:
            self.update_notice("체크")
    
        self.print1()    # 출력

    def afterBetting_1(self):			# 처음 한 사람이 베팅을 한 뒤, 그 다음 사람이 선택을 할 수 있는 함수 afterBetting의 선언
                                                        # big bind가 먼저 선택을 한 뒤, small blind의 선택.

        self.print1()    # 출력


        self.update_notice(self.nameOfPlayer2+"(small blind) 님께선 선택을 하십시오: \n1: 콜 (big blind와 같은 금액 베팅) \n2: 레이즈 (big blind보다 많은 금액 베팅) \n3: 폴드 (베팅을 포기)")
        self.print1()    # 출력

        self.choice=int(input())
        if int(self.choice)==1:
            self.update_notice("콜")
            self.bet2_1=int(self.bet1_1)
            self.append_moneyOfPlayer2(-int(self.bet2_1))
            self.append_collectedBet(int(self.bet2_1))
            self.append_bet2(self.bet2_1)

        elif int(self.choice)==2:
            self.update_notice("레이즈 \n 베팅할 금액을 입력하세요.(원래 베팅 금액보다 커야 합니다.)")            
            self.bet2_1=int(input())
            self.append_moneyOfPlayer2(-int(self.bet2_1))
            self.append_collectedBet(int(self.bet2_1))
            self.append_bet2(self.bet2_1)

        elif int(self.choice)==3:
            self.update_notice("폴드")
        
        self.print1()    # 출력



    def betting_2(self): # small blind가 먼저 베팅을 하는 메소드.(일단 player2가 small blind라고 했음.)

        self.print1()    # 출력

        self.update_notice("small bind ("+self.nameOfPlayer2+") 님이 베팅을 선택하십시오: \n1: 베팅 \n2: 체크 (베팅을 하지 않음.)")

        self.print1()    # 출력

        self.choice=int(input()) # 선택을 입력받음.(이 부분은 수정해야 할 듯.)

        if int(self.choice)==1:
            self.update_notice("베팅 \nsmall bind ("+self.nameOfPlayer2+") 님께서 베팅하실 금액을 정해주십시오: ")

            self.print1()    # 출력

            self.bet2_1=int(input())
            self.append_moneyOfPlayer2(-int(self.bet2_1))
            self.append_collectedBet(int(self.bet2_1))
            self.append_bet2(self.bet2_1)

        else:
            self.update_notice("체크")

    
        self.print1()    # 출력

    def afterBetting_2(self):			# 처음 한 사람이 베팅을 한 뒤, 그 다음 사람이 선택을 할 수 있는 함수 afterBetting의 선언
                                                        # small bind가 먼저 선택을 한 뒤, big blind의 선택.

        self.print1()    # 출력


        self.update_notice(self.nameOfPlayer1+"(big blind) 님께선 선택을 하십시오: \n1: 콜 (big blind와 같은 금액 베팅) \n2: 레이즈 (big blind보다 많은 금액 베팅) \n3: 폴드 (베팅을 포기)")
        self.print1()    # 출력

        self.choice=int(input())
        if int(self.choice)==1:
            self.update_notice("콜")

            self.print1()    # 출력

            self.bet1_1=self.bet2_1
            self.append_moneyOfPlayer1(-int(self.bet1_1))
            self.append_collectedBet(self.bet1_1)
            self.append_bet1(self.bet1_1)

        elif int(self.choice)==2:
            self.update_notice("레이즈 \n 베팅할 금액을 입력하세요.(원래 베팅 금액보다 커야 합니다.)")   

            self.print1()    # 출력
         
            self.bet1_1=input()
            self.append_moneyOfPlayer1(-int(self.bet1_1))
            self.append_collectedBet(int(self.bet1_1))
            self.append_bet1(self.bet1_1)


        elif int(self.choice)==3:
            self.update_notice("폴드")
            self.print1()    # 출력

        
        self.print1()    # 출력


