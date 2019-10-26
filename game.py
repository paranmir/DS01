import random
import poker
from poker import Suit
from poker import Rank
from poker import Card
from poker.hand import Hand, Combo



class PlayerInfo: 
 
    def __init__(self,name,money,hands): # 클래스에 정보를 전달해주는 setInfo
        self.name=name
        self.money=money
        self.hands=hands

    def printInfo(self):                # 플레이어의 정보를 출력해주는 printInfo
        print("----------")
        print("이름: ", self.name)
        print("남은 돈: ",self.money,"  가지고 있는 패: ",self.hands)
        print("----------")

    def earnMoney(self,amount):         # 돈을 얻었을 때 더해주는 인스턴스 earnMoney
        self.money=self.money+amount

    def loseMoney(self,amount):         # 돈을 잃었을 때 빼주는 인스턴스 loseMoney
        self.money=self.money-amount

    def appendHands(self,flop):         # 뽑은 카드를 패에 추가해주는 인스턴스 appendHands
        for i in flop:
            self.hands.append(i)


class GameProgress:		# 게임의 진행에 필요한 모든 선택을 할 수 있는 클래스 GameProgress의 선언 

    def __init__(self,players,gameInfo):

        self.players=players
        self.bigBlind=players[0]
        self.smallBlind=players[1]
 
        self.gameInfo=gameInfo
       
        self.bettingMoney=0
        
    def betting(self,bigBlindBetting):
        print("-----------------")
        if bigBlindBetting==True:
            print("big bind ("+self.bigBlind.name+") 님이 베팅을 선택하십시오: ")
            print("1: 베팅")
            print("2: 체크 (베팅을 하지 않음.)")
            choice=input()
            if int(choice)==1:
                print("베팅")
                self.bettingMoney=int(input("big blind ("+ self.bigBlind.name +")님께서 베팅하실 금액을 정해주십시오."))
                self.bigBlind.loseMoney(self.bettingMoney)
                self.gameInfo.appendMoney(self.bettingMoney)
            else:
                print("체크")

        else:
            print("small bind (",self.smallBlind.name,") 님이 베팅을 선택하십시오: ")
            print("1: 베팅")
            print("2: 체크 (베팅을 하지 않음.)")
            choice=input()
            if int(choice)==1:
                print("베팅")
                self.bettingMoney=int(input("small blind ("+ self.smallBlind.name +")님께서 베팅하실 금액을 정해주십시오."))
                self.smallBlind.loseMoney(self.bettingMoney)
                self.gameInfo.appendMoney(self.bettingMoney)
            else:
                print("체크")

        print("-----------------")
        

    def afterBetting(self,bigBlindBetting):			# 처음 한 사람이 베팅을 한 뒤, 그 다음 사람이 선택을 할 수 있는 함수 afterBetting의 선언
      
        print("-----------------")  
        if  bigBlindBetting==True:
            print(self.smallBlind.name,"(small blind) 님께선 선택을 하십시오:")
            print("1: 콜 (big blind와 같은 금액 베팅)")
            print("2: 레이즈 (big blind보다 많은 금액 베팅)")
            print("3: 폴드 (베팅을 포기)")
            choice=input()
            if int(choice)==1:
                print("콜")
                self.smallBlind.loseMoney(self.bettingMoney)
                self.gameInfo.appendMoney(self.bettingMoney)

            elif int(choice)==2:
                print("레이즈")
                raisedMoney=input("베팅할 금액을 입력하세요.")
                self.smallBlind.loseMoney(raisedMoney)
                self.gameInfo.appendMoney(raisedMoney)

            elif int(choice)==3:
                print("폴드")

        else:
            print(self.bigBlind.name,"(big blind) 님께선 선택을 하십시오:")
            print("1: 콜 (small blind와 같은 금액 베팅)")
            print("2: 레이즈 (small blind보다 많은 금액 베팅)")
            print("3: 폴드 (베팅을 포기)")
            choice=input()
            if int(choice)==1:
                print("콜")
                self.bigBlind.loseMoney(self.bettingMoney)
                self.gameInfo.appendMoney(self.bettingMoney)

            elif int(choice)==2:
                print("레이즈")
                raisedMoney=input("베팅할 금액을 입력하세요.")
                self.bigBlind.loseMoney(raisedMoney)
                self.gameInfo.appendMoney(raisedMoney)
            elif int(choice)==3:
                print("폴드")

            print("-----------------")
        
        



class GameInfo():                              # 모인 돈, 공통 카드 등 전체적인 게임의 정보를 담는 클래스 GameInfo의 정의
     def __init__(self,cards,money=0):        
         self.cards=cards
         self.money=money

     def printInfo(self):                    # 게임의 상황을 알려주는 인스턴스 printInfo의 정의
         print("-----------------")
         print("공통 카드: ",self.cards)
         print("모인 돈: ",self.money)
         print("-----------------")
    
     def appendMoney(self,amount):              # 모은 돈을 추가해주는 인스턴스 appendMoney의 정의           
         self.money+=amount

     def appendFlop(self,newcards):              # 공통 카드를 추가해주는 인스턴스 appendFlop의 정의
         self.cards+=newcards


   

player1=PlayerInfo("고니",500,[])      # player1 생성
player2=PlayerInfo("아귀",1000,[])     # player2 생성

gameInfo1=GameInfo([],0)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

gameProgress1=GameProgress([player1,player2],gameInfo1)

gameProgress1.betting(True)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()


# Preflop round #
print("[Preflop round]")

deck = list(Card)
random.shuffle(deck)	# 카드 셔플


hands1=[deck.pop() for i in range(2)]		# player1이 카드를 2장 뽑음.
print(player1.name + "님이 2장의 카드를 뽑았습니다.")
print(hands1)
player1.appendHands(hands1)


hands2=[deck.pop() for i in range(2)]		# player가 카드를 2장 뽑음.
print(player2.name + "님이 2장의 카드를 뽑았습니다.")
print(hands2)
player2.appendHands(hands2)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

gameProgress1.afterBetting(True)


# Flop round #
print("[Flop round]")
print("3장의 공유 카드를 뽑습니다.")
flop=[deck.pop() for i in range(3)]
print(flop)
gameInfo1.appendFlop(flop)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()


gameProgress1.betting(False)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

gameProgress1.afterBetting(False)


# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

# Turn round #
print("[Turn round]")
print("공유 카드 1장을 뽑습니다.")
turn=[deck.pop()]
print(turn)
gameInfo1.appendFlop(turn)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()


gameProgress1.betting(False)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

gameProgress1.afterBetting(False)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

# River round #

print("[River round]")
print("공유 카드 1장을 뽑습니다.")
river=[deck.pop()]
print(river)
gameInfo1.appendFlop(river)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()


gameProgress1.betting(False)

# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

gameProgress1.afterBetting(False)


# 게임 정보 출력
gameInfo1.printInfo()
player1.printInfo()
player2.printInfo()

player1.finalCards=player1.hands+gameInfo1.cards
player2.fanalCards=player2.hands+gameInfo1.cards



