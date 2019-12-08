import random
import poker
from poker import Suit
from poker import Rank
from poker import Card
from poker.hand import Hand, Combo

import game_jokbo
import game_class1
import game_class2


gameProgress1=game_class2.GameProgress("고니","아귀",5000,1000)


while True:
    deck = list(Card)
    random.shuffle(deck)	# 카드 셔플


    #preflop round
    gameProgress1.update_notice("[Preflop round]")

    hands1=[deck.pop() for i in range(2)]		# player1이 카드를 2장 뽑음.
    gameProgress1.update_notice(gameProgress1.nameOfPlayer1 + "님이 2장의 카드를 뽑았습니다.")
    gameProgress1.append_handsOfPlayer1(hands1)

    hands2=[deck.pop() for i in range(2)]		# player2이 카드를 2장 뽑음.
    gameProgress1.update_notice(gameProgress1.nameOfPlayer2 + "님이 2장의 카드를 뽑았습니다.")
    gameProgress1.append_handsOfPlayer2(hands2)

    gameProgress1.betting_1()
    gameProgress1.afterBetting_1()


    #flop round
    gameProgress1.update_notice("[Flop round]")
    gameProgress1.update_notice("3장의 공유 카드를 뽑습니다.")
    flop=[deck.pop() for i in range(3)]
    gameProgress1.append_communityCards(flop)
    gameProgress1.betting_2()
    gameProgress1.afterBetting_2()

    #turn round
    gameProgress1.update_notice("[turn round]")
    gameProgress1.update_notice("1장의 공유 카드를 뽑습니다.")
    turn=[deck.pop() for i in range(1)]
    gameProgress1.append_communityCards(turn)
    gameProgress1.betting_2()
    gameProgress1.afterBetting_2()

    #river round

    gameProgress1.update_notice("[river round]")
    gameProgress1.update_notice("1장의 공유 카드를 뽑습니다.")
    river=[deck.pop() for i in range(1)]
    gameProgress1.append_communityCards(river)
    gameProgress1.betting_2()
    gameProgress1.afterBetting_2()


    # 승패 판정
    player1=gameProgress1.handsOfPlayer1+gameProgress1.communityCards
    player1.sort()
    player1=game_jokbo.evaluateMax(game_jokbo.combination(player1))


    player2=gameProgress1.handsOfPlayer2+gameProgress1.communityCards
    player2.sort()
    player2=game_jokbo.evaluateMax(game_jokbo.combination(player2))


    gameProgress1.update_notice("[결과]\n(" + gameProgress1.nameOfPlayer1 + ")의 최종 패:" +" <"+ game_jokbo.printEvaluate(player1) +"> "+ str(player1)+ "\n(" + gameProgress1.nameOfPlayer2 + ")의 최종 패: " + "<" + game_jokbo.printEvaluate(player2)+"> " + str(player2))
    gameProgress1.print1()		

            
    if game_jokbo.compare(player1,player2) == True:
        gameProgress1.update_notice(gameProgress1.nameOfPlayer1+" 승리")
        gameProgress1.print1()
        gameProgress1.append_moneyOfPlayer1(gameProgress1.collectedBet)
        gameProgress1.reset()
            
    elif game_jokbo.compare(player1,player2) == False:
        gameProgress1.update_notice(gameProgress1.nameOfPlayer2+" 승리")
        gameProgress1.print1()
        gameProgress1.append_moneyOfPlayer2(gameProgress1.collectedBet)
        gameProgress1.reset()

    else:
        gameProgress1.update_notice("무승부")
        gameProgress1.print1()
        gameProgress1.append_moneyOfPlayer1(gameProgress1.bet1)
        gameProgress1.append_moneyOfPlayer2(gameProgress1.bet2)
        gameProgress1.reset()

    gameProgress1.print1()
    deck.clear()		

    if(gameProgress1.moneyOfPlayer1==0):
        gameProgress1.update_notice(gameProgress1.nameOfPlayer1+"님께서 파산하셨습니다.")
        gameProgress1.print1()
        break
        
    if(gameProgress1.moneyOfPlayer2==0):
        gameProgress1.update_notice(gameProgress1.nameOfPlayer2+"님께서 파산하셨습니다.")
        gameProgress1.print1()
        break
