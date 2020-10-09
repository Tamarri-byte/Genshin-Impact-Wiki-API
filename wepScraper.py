import requests
from bs4 import BeautifulSoup
import json


wepPageURL = "https://genshin-impact.fandom.com/wiki/Weapons"

wepReq = requests.get(wepPageURL)
wepReqSoup = BeautifulSoup(wepReq.text,'html.parser')
wepTable = wepReqSoup.find('table',class_ = 'article-table')
wepList = []


class weaponType:
    def __init__(self,typeName,typeInfo,fullWeapon):
        self.typeName = typeName
        self.typeInfo = typeInfo
        self.fullWeapon = fullWeapon

class fullWeapon:
    def __init__(self,wepName,wepImage,wepRarity,wepBaseAtk,wepSecStat,wepPass,wepRank1,wepRank5):
        self.wepName = wepName
        self.wepImage = wepImage
        self.wepRarity = wepRarity
        self.wepBaseAtk = wepBaseAtk
        self.wepSecStat = wepSecStat
        self.wepPass = wepPass
        self.wepRank1 = wepRank1
        self.wepRank5 = wepRank5

def getWeaponTypes():
    for TableObj in wepTable.find_all('tr'):
        newWepObj = TableObj.find_all('td')
        index = 0
        newWepType = weaponType('typeName','typeInfo',{})
        fullWepURL = "https://genshin-impact.fandom.com"
        for wepData in newWepObj:
            if(index == 0):
                newWepType.typeName = wepData.text
                link = wepData.find('a')
                if(link):
                    fullWepURL = fullWepURL + link['href']
                else:
                    fullWepURL = "no ref"

                getFullWeaponData(fullWepURL,newWepType)
                    

            if(index == 1):
                newWepType.typeInfo = wepData.text

            index += 1
            if(index >= 2):
                index = 0
            
        wepList.append(newWepType)


def getFullWeaponData(url,newWepType):
    #print(url)
    fullWepReq = requests.get(url)
    fullWepReqSoup = BeautifulSoup(fullWepReq.text,'html.parser')
    fullWepTable = fullWepReqSoup.findAll('table',class_ = 'wikitable sortable')[1]

    testList = []
    for obj in fullWepTable.find_all('tr'):
        newFullWepObj = obj.find_all('td')
        index = 0
        fullWepList = []
        wn = ''
        wi = ''
        wr = ''
        wba = ''
        wss = ''
        wp = ''
        wr1 = ''
        wr5 = ''
        for fullWepData in newFullWepObj:
            if(index == 0):
                wn = fullWepData.text
            elif(index == 1):
                img = fullWepData.find('a')
                if(img):
                    wi =  img['href']
                else:
                    wi =  "no img"
            elif(index == 2):
                wr = fullWepData.text
            elif(index == 3):
                wba = fullWepData.text
            elif(index == 4):
                wss = fullWepData.text
            elif(index == 5):
                wp = fullWepData.text
            elif(index == 6):
                wr1 = fullWepData.text
            elif(index == 7):
                wr5 = fullWepData.text
            
            index += 1
            if(index >= 8):
                index = 0
                newFullWep = fullWeapon(wn,wi,wr,wba,wss,wp,wr1,wr5)
                fullWepList.append(newFullWep)
    
        
        listOfDict = []
        for x in range(len(fullWepList)):
            fullWepToAdd = {"name": fullWepList[x].wepName.strip(),
            "img": fullWepList[x].wepImage.strip(),
            "rarity": fullWepList[x].wepRarity.strip(),
            "baseAtk": fullWepList[x].wepBaseAtk.strip(),
            "secStat": fullWepList[x].wepSecStat.strip(),
            "pass": fullWepList[x].wepPass.strip(),
            "rank1": fullWepList[x].wepRank1.strip(),
            "rank5": fullWepList[x].wepRank5.strip()}

            
            testList.append(fullWepToAdd)
            
 
        newWepType.fullWeapon = testList
    


