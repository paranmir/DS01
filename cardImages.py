# -*- Coding: UTF-8 -*-
'''
Project name: LANPoker
FIle name: cardImages.py
File info: Returns card images to GUI window.
Written by: pinkrabbit412 
Written at: 2019.10.21.
Version: v0.0.0.dev191021A.alpha

Copyright 2019. 악동분홍토끼(pinkrabbit412@daum.net). All rights reserved.
'''

#cardValue = {'2', '3', '4',  '5',  '6',  '7',  '8',  '9',  'T',  'J', 'Q', 'K', 'A'}
cardType = {"♠", "♥", "♣", "♦"}

def getImage(cardInfo):
    toReturn = "./resources/cards/" + cardInfo[0]
    
    if (cardInfo[1] == cardType[0]):
        toReturn += "S"
    elif (cardInfo[1] == cardType[1]):
        toReturn += "H"
    elif (cardInfo[1] == cardType[2]):
        toReturn += "C"
    elif (cardInfo[1] == cardType[3]):
        toReturn += "D"
    toReturn += ".png"

    return toReturn;
