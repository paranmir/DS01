import random
import poker
from poker import Suit
from poker import Rank
from poker import Card
from poker.hand import Hand, Combo


def LeftIsBig(num1,num2):
    if num1>num2:
        return True
    elif num1<num2:
        return False
    else:
        return None

def defineSuit(card):
    if str(Suit.SPADES) in str(card):
        return 1
    elif str(Suit.HEARTS) in str(card):
        return 2
    elif str(Suit.CLUBS) in str(card):
        return 3
    elif str(Suit.DIAMONDS) in str(card):
        return 4

def defineRank(card):
    if str(2) in str(card):
        return 2
    if str(3) in str(card):
        return 3
    if str(4) in str(card):
        return 4
    if str(5) in str(card):
        return 5
    if str(6) in str(card):
        return 6
    if str(7) in str(card):
        return 7
    if str(8) in str(card):
        return 8
    if str(9) in str(card):
        return 9
    if 'T' in str(card):
        return 10
    if 'J' in str(card):
        return 11
    if 'Q' in str(card):
        return 12
    if 'K' in str(card):
        return 13
    if 'A' in str(card):
        return 14
    

def equals(num1,num2):
    if num1==num2:
        return 1
    else:
        return 0

def isFlush_wide(cards):
    result=equals(defineSuit(cards[0]),defineSuit(cards[1]))
    result*=equals(defineSuit(cards[0]),defineSuit(cards[2]))
    result*=equals(defineSuit(cards[0]),defineSuit(cards[3]))
    result*=equals(defineSuit(cards[0]),defineSuit(cards[4]))
    if result==1:
        return True
    else:
        return False

def isLinear(num1,num2,num3,num4,num5):
    result=equals((num1+1),num2)
    result*=equals((num2+1),num3)
    result*=equals((num3+1),num4)
    result*=equals((num4+1),num5)
    if result==1:
        return 1
    else:
        return 0

def isStraight_wide(cards):
    if isLinear(defineRank(cards[0]),defineRank(cards[1]),defineRank(cards[2]),defineRank(cards[3]),defineRank(cards[4]))==1:
        return True
    elif defineRank(cards[0])==2 and isLinear(defineRank(cards[0]),defineRank(cards[1]),defineRank(cards[2]),defineRank(cards[3]),(defineRank(cards[3])+1))==1 and defineRank(cards[4])==14:
        return True

    else:
        return False

def isHighCard(cards):
    for i in range(0,4):
        if equals(defineRank(cards[i]),defineRank(cards[i+1]))==1:
            return False
    return True

def isOnePair(cards):
    sum=0
    for i in range(0,4):
        if defineRank(cards[i])==defineRank(cards[i+1]):
            sum+=1
    if sum==1:
        return True
    else:
        return False

def isTwoPair(cards):
    sum=0
    for i in range(0,4):
        if defineRank(cards[i])==defineRank(cards[i+1]):
            sum+=1
    if sum==2 and isTriple(cards)==False:
        return True
    else:
        return False

def isTriple(cards):
    for i in range(0,3):
        if defineRank(cards[i])==defineRank(cards[i+1]) and defineRank(cards[i+1])==defineRank(cards[i+2]):
            if isPoker(cards)==False and isFullHouse(cards)==False:
                return True
    return False

def isFullHouse(cards):
    cards2=[]
    for i in range(0,3):
        if defineRank(cards[i])==defineRank(cards[i+1]) and defineRank(cards[i+1])==defineRank(cards[i+2]):
            if i==0:
                cards2.append(cards[3])
                cards2.append(cards[4])
            elif i==1:
                cards2.append(cards[0])
                cards2.append(cards[4])
            elif i==2:
                cards2.append(cards[0])
                cards2.append(cards[1])

            if defineRank(cards2[0])==defineRank(cards2[1]) and defineRank(cards2[0])!=defineRank(cards[i]) and defineRank(cards2[1])!=defineRank(cards[i]):
                return True
    return False

def isPoker(cards):
    for i in range(0,2):
        if defineRank(cards[i])==defineRank(cards[i+1]) and defineRank(cards[i+1])==defineRank(cards[i+2]) and defineRank(cards[i+2])==defineRank(cards[i+3]):
            return True
    return False

def isRoyalStraightFlush(cards):
    if isFlush_wide(cards)==True:
        if isStraight_wide(cards)==True:
            if defineRank(cards[0])==10:
                return True
    return False

def isStraightFlush(cards):
    if isFlush_wide(cards)==True:
        if isStraight_wide(cards)==True:
            if isRoyalStraightFlush(cards)==False:
                return True
    return False

def isStraight(cards):
    if isStraight_wide(cards)==True:
        if isStraightFlush(cards)==False:
            if isRoyalStraightFlush(cards)==False:
                return True
    return False

def isFlush(cards):
    if isFlush_wide(cards)==True:
        if isStraightFlush(cards)==False:
            if isRoyalStraightFlush(cards)==False:
                return True
    return False


def compareHighCard(cards1,cards2):
    cardsRank1=[]
    cardsRank2=[]
    cards3=[]
    cards4=[]
    for i in cards1:
        cardsRank1.append(defineRank(i))
    for i in cards2:
        cardsRank2.append(defineRank(i))
    if listMax(cardsRank1) >listMax(cardsRank2):
        return True
    elif listMax(cardsRank1)<listMax(cardsRank2):
        return False
    else:
        for j in range(0,listMaxIndex(cards1)):
            cards3.append(cards1[j])
        for j in range((listMaxIndex(cards1)+1),len(cards1)):
            cards3.append(cards1[j])

        for j in range(0,listMaxIndex(cards2)):
            cards4.append(cards2[j])
        for j in range((listMaxIndex(cards2)+1),len(cards2)):
            cards4.append(cards2[j])

        if len(cards3)==0:
            return None

        return compareHighCard(cards3,cards4)

def compareOnePair(cards1,cards2):
    cardsPair1=[]
    cardsPair2=[]
    cardsNotPair1=[]
    cardsNotPair2=[]

    for i in range(0,4):
        if defineRank(cards1[i])==defineRank(cards1[i+1]):
            cardsPair1.append(cards1[i])
            cardsPair1.append(cards1[i+1])
            for j in range(0,i):
                cardsNotPair1.append(cards1[j])
            for j in range(i+2,5):
                cardsNotPair1.append(cards1[j])

    for i in range(0,4):
        if defineRank(cards2[i])==defineRank(cards2[i+1]):
            cardsPair2.append(cards2[i])
            cardsPair2.append(cards2[i+1])
            for j in range(0,i):
                cardsNotPair2.append(cards2[j])
            for j in range(i+2,5):
                cardsNotPair2.append(cards2[j])

    if defineRank(cardsPair1[0])==defineRank(cardsPair2[0]):
        return compareHighCard(cardsNotPair1,cardsNotPair2)
    else:
        return compareHighCard(cardsPair1,cardsPair2)


def compareTwoPair(cards1,cards2):
    cardsPair1=[]
    cardsPair1_1=[]
    cardsPair2=[]
    cardsPair2_1=[]
    cardsNotPair1=[]
    cardsNotPair2=[]

    for i in range(0,4):
        if defineRank(cards1[i])==defineRank(cards1[i+1]):
            cardsPair1.append(cards1[i])
            cardsPair1.append(cards1[i+1])
            for j in range(i+2,4):
                if defineRank(cards1[j])==defineRank(cards1[j+1]):
                    cardsPair1_1.append(cards1[j])
                    cardsPair1_1.append(cards1[j+1])
                    for k in range(0,i):
                        cardsNotPair1.append(cards1[k])
                    for k in range(i+2,j):
                        cardsNotPair1.append(cards1[k])
                    for k in range(j+2,5):
                        cardsNotPair1.append(cards1[k])
            break

    for i in range(0,4):
        if defineRank(cards2[i])==defineRank(cards2[i+1]):
            cardsPair2.append(cards2[i])
            cardsPair2.append(cards2[i+1])
            for j in range(i+2,4):
                if defineRank(cards2[j])==defineRank(cards2[j+1]):
                    cardsPair2_1.append(cards2[j])
                    cardsPair2_1.append(cards2[j+1])
                    for k in range(0,i):
                        cardsNotPair2.append(cards2[k])
                    for k in range(i+2,j):
                        cardsNotPair2.append(cards2[k])
                    for k in range(j+2,5):
                        cardsNotPair2.append(cards2[k])
            break


    if defineRank(cardsPair1_1[0])>defineRank(cardsPair2_1[0]):
        return True
    elif defineRank(cardsPair1_1[0])<defineRank(cardsPair2_1[0]):
        return False
    else:
        if defineRank(cardsPair1[0])>defineRank(cardsPair2[0]):
            return True
        elif defineRank(cardsPair1[0])<defineRank(cardsPair2[0]):
            return False
        else:
            if defineRank(cardsNotPair1[0])>defineRank(cardsNotPair2[0]):
                return True
            elif defineRank(cardsNotPair1[0])<defineRank(cardsNotPair2[0]):
                return False
            else:
                return None

def compareTriple(cards1,cards2):
    cardsTriple1=[]
    cardsTriple2=[]
    cardsNotTriple1=[]
    cardsNotTriple2=[]

    for i in range(0,3):
        if defineRank(cards1[i])==defineRank(cards1[i+1]) and defineRank(cards1[i+1])==defineRank(cards1[i+2]):
            cardsTriple1.append(cards1[i])
            cardsTriple1.append(cards1[i+1])
            cardsTriple1.append(cards1[i+2])
            for j in range(0,i):
                cardsNotTriple1.append(cards1[j])
            for j in range(i+3,5):
                cardsNotTriple1.append(cards1[j])

    for i in range(0,3):
        if defineRank(cards2[i])==defineRank(cards2[i+1]) and defineRank(cards2[i+1])==defineRank(cards2[i+2]):
            cardsTriple2.append(cards2[i])
            cardsTriple2.append(cards2[i+1])
            cardsTriple2.append(cards2[i+2])
            for j in range(0,i):
                cardsNotTriple2.append(cards2[j])
            for j in range(i+3,5):
                cardsNotTriple2.append(cards2[j])

    # print(cardsTriple1)
    # print(cardsNotTriple1)
    # print(cardsTriple2)
    # print(cardsNotTriple2)  


    if defineRank(cardsTriple1[0])>defineRank(cardsTriple2[0]):
        return True
    elif defineRank(cardsTriple1[0])<defineRank(cardsTriple2[0]):
        return False
    else:
        if defineRank(cardsNotTriple1[1])>defineRank(cardsNotTriple2[1]):
            return True
        elif defineRank(cardsNotTriple1[1])<defineRank(cardsNotTriple2[1]):
            return False
        else:
            if defineRank(cardsNotTriple1[0])>defineRank(cardsNotTriple2[0]):
                return True
            elif defineRank(cardsNotTriple1[0])<defineRank(cardsNotTriple2[0]):
                return False
            else:
                return None

def compareStraight(cards1,cards2):
    if defineRank(cards1[0])>defineRank(cards2[0]):
        return True
    elif defineRank(cards1[0])<defineRank(cards2[0]):
        return False
    else:
        if defineRank(cards1[0])==2:
            if defineRank(cards1[4])==14:
                if defineRank(cards2[4])==14:
                    return None
                else:
                    return True
            else:
                if defineRank(cards2[4])==14:
                    return False
                else:
                    return None
                    
        else:
            return None


def compareFlush(cards1,cards2):
    return compareHighCard(cards1,cards2)

def compareFullHouse(cards1,cards2):
    cardsTriple1=[]
    cardsTriple2=[]
    cardsNotTriple1=[]
    cardsNotTriple2=[]

    for i in range(0,3):
        if defineRank(cards1[i])==defineRank(cards1[i+1]) and defineRank(cards1[i+1])==defineRank(cards1[i+2]):
            cardsTriple1.append(cards1[i])
            cardsTriple1.append(cards1[i+1])
            cardsTriple1.append(cards1[i+2])
            for j in range(0,i):
                cardsNotTriple1.append(cards1[j])
            for j in range(i+3,5):
                cardsNotTriple1.append(cards1[j])

    for i in range(0,3):
        if defineRank(cards2[i])==defineRank(cards2[i+1]) and defineRank(cards2[i+1])==defineRank(cards2[i+2]):
            cardsTriple2.append(cards2[i])
            cardsTriple2.append(cards2[i+1])
            cardsTriple2.append(cards2[i+2])
            for j in range(0,i):
                cardsNotTriple2.append(cards2[j])
            for j in range(i+3,5):
                cardsNotTriple2.append(cards2[j])

    # print(cardsTriple1)
    # print(cardsNotTriple1)
    # print(cardsTriple2)
    # print(cardsNotTriple2)  

    if defineRank(cardsTriple1[0])>defineRank(cardsTriple2[0]):
        return True
    elif defineRank(cardsTriple1[0])<defineRank(cardsTriple2[0]): 
        return False
    else:
        if defineRank(cardsNotTriple1[0])>defineRank(cardsNotTriple2[0]):
            return True
        elif defineRank(cardsNotTriple1[0])<defineRank(cardsNotTriple2[0]):
            return False
        else:
            return None

def comparePoker(cards1,cards2):
    cardsPoker1=[]
    cardsPoker2=[]
    cardsNotPoker1=[]
    cardsNotPoker2=[]
    for i in range(0,2):
        if defineRank(cards1[i])==defineRank(cards1[i+1]) and defineRank(cards1[i+1])==defineRank(cards1[i+2]) and defineRank(cards1[i+2])==defineRank(cards1[i+3]):
            cardsPoker1.append(cards1[i])
            cardsPoker1.append(cards1[i+1])
            cardsPoker1.append(cards1[i+2])
            cardsPoker1.append(cards1[i+3])
            if i==0:
                cardsNotPoker1.append(cards1[4])
            else:
                cardsNotPoker1.append(cards1[0])

    for i in range(0,2):
        if defineRank(cards2[i])==defineRank(cards2[i+1]) and defineRank(cards2[i+1])==defineRank(cards2[i+2]) and defineRank(cards2[i+2])==defineRank(cards2[i+3]):
            cardsPoker2.append(cards2[i])
            cardsPoker2.append(cards2[i+1])
            cardsPoker2.append(cards2[i+2])
            cardsPoker2.append(cards2[i+3])
            if i==0:
                cardsNotPoker2.append(cards2[4])
            else:
                cardsNotPoker2.append(cards2[0])

    # print(cardsPoker1)
    # print(cardsNotPoker1)

    # print(cardsPoker2)
    # print(cardsNotPoker2)

    if defineRank(cardsPoker1[0])>defineRank(cardsPoker2[0]):
        return True
    elif defineRank(cardsPoker1[0])<defineRank(cardsPoker2[0]):
        return False
    else:
        if defineRank(cardsNotPoker1[0])>defineRank(cardsNotPoker2[0]):
            return True
        elif defineRank(cardsNotPoker1[0])<defineRank(cardsNotPoker2[0]):
            return False
        else:
            return None


def compareStraightFlush(cards1,cards2):
    return compareStraight(cards1,cards2)

def compareRoyalStraightFlush(cards1,cards2):
    return None

def listMax(list):
    max=list[0]
    for i in range(0,len(list)):
        if list[i]>max:
            max=list[i]
    return max

def listMaxIndex(list):
    max=list[0]
    for i in range(0,len(list)):
        if list[i]>max:
            max=list[i]
    return i


def combination(cards):
    cards2=[]
    for i in cards:
        cards2.append(i)
    cards3=[]
    newCards=[]

    for i in range(0,7):
        del cards2[i]
        for k in range(0,6):
            #
            cards3=[]
            for w in cards2:
                cards3.append(w)
            #
            del cards3[k]
            newCards.append(cards3)
            #
            cards3=[]
            for q in cards2:
                cards3.append(q)
            #
        #
        cards2=[]
        for j in cards:
            cards2.append(j)
        #
    return newCards


def evaluate(cards):
    if isRoyalStraightFlush(cards)==True:
        return 10
    elif isStraightFlush(cards)==True:
        return 9
    elif isPoker(cards)==True:
        return 8
    elif isFullHouse(cards)==True:
        return 7
    elif isFlush(cards)==True:
        return 6
    elif isStraight(cards)==True:
        return 5
    elif isTriple(cards)==True:
        return 4
    elif isTwoPair(cards)==True:
        return 3
    elif isOnePair(cards)==True:
        return 2
    elif isHighCard(cards)==True:
        return 1

def compare(cards1,cards2):
    if evaluate(cards1) > evaluate(cards2):
        return True
    elif evaluate(cards1) < evaluate(cards2):
        return False
    else:
        if evaluate(cards1)==10:
            return compareRoyalStraightFlush(cards1,cards2)
        elif evaluate(cards1)==9:
            return compareStraightFlush(cards1,cards2)
        elif evaluate(cards1)==8:
            return comparePoker(cards1,cards2)
        elif evaluate(cards1)==7:
            return compareFullHouse(cards1,cards2)
        elif evaluate(cards1)==6:
            return compareFlush(cards1,cards2)
        elif evaluate(cards1)==5:
            return compareStraight(cards1,cards2)
        elif evaluate(cards1)==4:
            return compareTriple(cards1,cards2)
        elif evaluate(cards1)==3:
            return compareTwoPair(cards1,cards2)
        elif evaluate(cards1)==2:
            return compareOnePair(cards1,cards2)
        elif evaluate(cards1)==1:
            return compareHighCard(cards1,cards2)

def printEvaluate(cards1):
        if evaluate(cards1)==10:
            return "로얄 스트레이트 플러시"
        elif evaluate(cards1)==9:
            return "스트레이트 플러시"
        elif evaluate(cards1)==8:
            return "포커"
        elif evaluate(cards1)==7:
            return "풀하우스"
        elif evaluate(cards1)==6:
            return "플러시"
        elif evaluate(cards1)==5:
            return "스트레이트"
        elif evaluate(cards1)==4:
            return "트리플"
        elif evaluate(cards1)==3:
            return "투페어"
        elif evaluate(cards1)==2:
            return "원페어"
        elif evaluate(cards1)==1:
            return "하이카드"


def evaluateMax(cards):
    cardsMax=cards[0]
    for i in range(0,len(cards)):
        if compare(cards[i],cardsMax)==True:
            cardsMax=cards[i]

    return cardsMax




