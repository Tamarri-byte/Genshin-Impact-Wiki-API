import requests
from bs4 import BeautifulSoup

#########################################
# *PLAYABLE CHARACTERS*                 #
#########################################

charPageURL = "https://genshin-impact.fandom.com/wiki/Characters"

charReq = requests.get(charPageURL)
charReqSoup = BeautifulSoup(charReq.text,'html.parser')
charTable = charReqSoup.find('table',class_ = 'article-table sortable')
charList = []

class charClass:
    def __init__(self,charRarity,charIcon,charName,charElem,charWep,charSex,charRegion):
        self.charRarity = charRarity
        self.charIcon = charIcon
        self.charName = charName
        self.charElem = charElem
        self.charWep = charWep
        self.charSex = charSex
        self.charRegion = charRegion


for TableObj in charTable.find_all('tr'):
    newCharObj = TableObj.find_all('td')
    index = 0
    newChar = charClass('charRarity','charIcon','charName','charElem','charWep','charSex','charRegion')

    for charData in newCharObj:
        if(index == 0):
            newChar.charRarity = charData.text
        elif(index == 1):
            newChar.charIcon = charData.text
        elif(index == 2):
            newChar.charName = charData.text
        elif(index == 3):
            newChar.charElem = charData.text
        elif(index == 4):
            newChar.charWep = charData.text
        elif(index == 5):
            newChar.charSex = charData.text
        elif(index == 6):
            newChar.charRegion = charData.text
            index = 0

        index +=1
        
    charList.append(newChar)
        
import dictConverter as DC
DC.buildPlayableCharDict()
            