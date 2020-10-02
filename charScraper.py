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
    fullDataDict = {}
    fullDataURL = ""
    def __init__(self,charRarity,charIcon,charName,charElem,charWep,charSex,charRegion):
        self.charRarity = charRarity
        self.charIcon = charIcon
        self.charName = charName
        self.charElem = charElem
        self.charWep = charWep
        self.charSex = charSex
        self.charRegion = charRegion

def getPlayableCharacters():
    for TableObj in charTable.find_all('tr'):
        newCharObj = TableObj.find_all('td')
        index = 0
        newChar = charClass('charRarity','charIcon','charName','charElem','charWep','charSex','charRegion')

        for charData in newCharObj: #Retreive simple data from table
            if(index == 0):
                newChar.charRarity = charData.text
            elif(index == 1):
                newChar.charIcon = charData.text
            elif(index == 2):
                newChar.charName = charData.text
                focusedCharData = charData.find('a')
                newChar.fullDataURL = "https://genshin-impact.fandom.com" + focusedCharData['href']
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
        
    charList.remove(charList[0])
    #Get Data from focused char page
    chIndex = 0
    for char in charList:
        url = char.fullDataURL
        specCharReq = requests.get(url)
        specCharReqSoup = BeautifulSoup(specCharReq.text,'html.parser')
        basicDataTable = specCharReqSoup.find('div',class_ = 'pi-section-contents')

        if(chIndex == 1):
            print(basicDataTable)

        chIndex += 1

        
        

    #import dictConverter as DC
    #DC.buildPlayableCharDict()

getPlayableCharacters()
#########################################
# *UPCOMING CHARACTERS*                 #
#########################################

upcomingCharTable = charReqSoup.findAll('table',class_ = 'article-table sortable')[1]
upcomingCharList = []

class upcomingCharClass:
    def __init__(self,charName,charElement,charWep,charSex,charRegion):
        self.charName = charName
        self.charElement = charElement
        self.charWep = charWep
        self.charSex = charSex
        self.charRegion = charRegion

def getUpcomingCharacters():
    for TableObj in upcomingCharTable.find_all('tr'):
            newCharObj = TableObj.find_all('td')
            index = 0
            upcomChar = upcomingCharClass('charName','charElement','charWep','charSex','charRegion')

            for charData in newCharObj:
                if(index == 0):
                    upcomChar.charName = charData.text
                elif(index == 1):
                    upcomChar.charElement = charData.text
                elif(index == 2):
                    upcomChar.charWep = charData.text
                elif(index == 3):
                    upcomChar.charSex = charData.text
                elif(index == 4):
                    upcomChar.charRegion = charData.text
                    index = 0

                index +=1
                
            upcomingCharList.append(upcomChar)

    import dictConverter as DC
    DC.buildUpcomingCharDict()

#########################################
# *NON-PLAYABLE CHARACTERS*             #
#########################################


nonPlayableCharTable = charReqSoup.findAll('table',class_ = 'article-table sortable')[2]
nonPlayableCharList = []

class nonPlayableCharClass:
    def __init__(self,charName,charElem,charRole,charRegion):
        self.charName = charName
        self.charElem = charElem
        self.charRole = charRole
        self.charRegion = charRegion


def getNonPlayableCharacters():
    for TableObj in nonPlayableCharTable.find_all('tr'):
        newCharObj = TableObj.find_all('td')
        index = 0
        NPChar = nonPlayableCharClass('charName','charElem','charRole','charRegion')

        for charData in newCharObj:
            if(index == 0):
                NPChar.charName = charData.text
            elif(index == 1):
                NPChar.charElem = charData.text
            elif(index == 2):
                NPChar.charRole = charData.text
            elif(index == 3):
                NPChar.charRegion = charData.text
                index = 0

            index +=1
            nonPlayableCharList.append(NPChar)

    import dictConverter as DC
    DC.buildNonPlayableCharDict()
    



