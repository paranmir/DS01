import random
import poker
from poker import Suit
from poker import Rank
from poker import Card
from poker.hand import Hand, Combo

import game_jokbo



class GameInfo:    # 게임의 정보를 저장하는 클래스 GameInfo(전달 위한 클래스.)
    def __init__(self,name1,name2,money1,money2):   # 생성자: 플레이어 2명의 이름(string형)과 가진 돈(int형)을 입력해서 생성.
        self.nameOfPlayer1=name1    # 플레이어 1의 이름(string형)
        self.nameOfPlayer2=name2    # 플레이어 2의 이름(string형)

        self.handsOfPlayer1=[]  # 플레이어1의 카드패(Card 자료형)
        self.handsOfPlayer2=[]  # 플레이어2의 카드패(Card 자료형)

        self.moneyOfPlayer1=money1  # 플레이어1의 돈(int형)
        self.moneyOfPlayer2=money2  # 플레이어2의 돈(int형)

        self.communityCards=[]  # 공통 카드(Card 자료형)

        self.bet1=0  # 첫번째 사람이 베팅한 돈(int형)
        self.bet2=0  # 두번째 사람이 베팅한 돈(두번째 사람이 콜하면 첫번째랑 같고, 
                     # 레이즈하면 더 큰 값을 입력받고, 폴드하면 0이 되는 식으로.)(int형)

        self.collectedBet=0 # 베팅한 돈을 모은 것(int형)
        self.notice=""    # 안내문구(string형)


    def append_handsOfPlayer1(self,newCard1):   # 플레이어1의 카드패에 입력받은걸 추가해주는 메소드. append가 앞에 붙은거 다 마찬가지로 추가한 것.
        self.handsOfPlayer1.extend(newCard1)    # 매개변수: Card 자료형

    def append_handsOfPlayer2(self,newCard2):   # 매개변수: Card 자료형
        self.handsOfPlayer2.extend(newCard2)

    def append_communityCards(self,newCard3):   # 매개변수: Card형
        self.communityCards.extend(newCard3)


    def append_moneyOfPlayer1(self,newMoney1):   # 매개변수: int형
        self.moneyOfPlayer1+=int(newMoney1)

    def append_moneyOfPlayer2(self,newMoney2):   # 매개변수: int형
        self.moneyOfPlayer2+=int(newMoney2)

    def append_collectedBet(self,newMoney3):  # 매개변수: int형
        self.collectedBet+=int(newMoney3)

    def append_bet1(self,newBet1):   # bet1의 값을 newBet1으로 바꾸는 메소드. update가 앞에 붙은거 다 마찬가지임.  
        self.bet1+=int(newBet1)       # 매개변수: int형

    def append_bet2(self,newBet2):   # 매개변수: int형
        self.bet2+=int(newBet2)
    
    def update_notice(self,newNotice):  # string형을 매개변수로 넣으면 notice의 값을 그걸로 갱신해주는 메소드.
        self.notice=newNotice       # 매개변수: string형.





