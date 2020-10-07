import requests
from bs4 import BeautifulSoup
import json


#########################################
# *PLAYABLE CHARACTERS*                 #
#########################################

charPageURL = "https://genshin-impact.fandom.com/wiki/Characters"

charReq = requests.get(charPageURL)
charReqSoup = BeautifulSoup(charReq.text,'html.parser')
charTable = charReqSoup.find('table',class_ = 'article-table sortable')
charList = []

class charClass:
    def __init__(self,charRarity,charIcon,charName,charElem,charWep,charSex,charRegion,fullDataURL,charTalentInfo):
        self.charRarity = charRarity
        self.charIcon = charIcon
        self.charName = charName
        self.charElem = charElem
        self.charWep = charWep
        self.charSex = charSex
        self.charRegion = charRegion
        self.fullDataURL = fullDataURL
        self.charTalentInfo = charTalentInfo

class charTalentInfo:
    def __init__(self,type,name,icon,info):
        self.type = type
        self.name = name
        self.icon = icon
        self.info = info

def getPlayableCharacters():
    for TableObj in charTable.find_all('tr'):
        newCharObj = TableObj.find_all('td')
        index = 0
        newChar = charClass('charRarity','charIcon','charName','charElem','charWep','charSex','charRegion',"url",{})
        for charData in newCharObj: #Retreive simple data from table
            if(index == 0):
                newChar.charRarity = charData.text
            elif(index == 1):
                
                img = charData.find('a')
                if(img):
                    newChar.charIcon =  img['href']
                else:
                    newChar.charIcon =  "no img"
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
        bdt = specCharReqSoup.findAll('table',class_ = 'wikitable')
        check = bool
        if len(bdt) > 1:
            check = True
        else:
            check = False

        if not check:
            print("no table for this char")
        else:
            basicDataTable = specCharReqSoup.findAll('table',class_ = 'wikitable')[0]
            headerTitles = []
            listOfTalents = []
            newTalentData = charTalentInfo("t","n","i","in")
            for tableHeader in basicDataTable.find_all('th'):
                headerTitles.append(tableHeader.text.strip())

            tableContent = basicDataTable.find_all('td')
            talentIndex = 0
            n = 'n'
            t = 't'
            i = 'i'
            inf = 'inf'
            for talent in tableContent:
                if(headerTitles[talentIndex] == "Name"):
                    n = talent.text
                elif(headerTitles[talentIndex] == "Type"):
                    t = talent.text
                elif(headerTitles[talentIndex] == "Icon"):
                    img = talent.find('a')
                    if(img):
                        i = img['href']
                    else:
                        i = "no img"
                elif(headerTitles[talentIndex] == "Info"):
                    inf = talent.text

                talentIndex += 1
                if(talentIndex >= len(headerTitles)):
                    newTalentData = charTalentInfo(t,n,i,inf)
                    listOfTalents.append(newTalentData)
                    talentIndex = 0

            tl = listOfTalents

                
            for x in range(len(tl)):
                talentToAdd = {"name": tl[x].name.strip(),
                "type": tl[x].type.strip(),
                "icon": tl[x].icon.strip(),
                "info": tl[x].info.strip()}
                if tl[x].name in char.charTalentInfo:
                    char.charTalentInfo[tl[x].name].append(talentToAdd)
                else:
                    char.charTalentInfo[tl[x].name] = [talentToAdd]
        
                
        chIndex += 1        


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
    



