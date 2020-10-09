import requests
from bs4 import BeautifulSoup
import json


artPageURL = "https://genshin-impact.fandom.com/wiki/Artifacts"

artReq = requests.get(artPageURL)
artReqSoup = BeautifulSoup(artReq.text,'html.parser')
artTable = artReqSoup.find_all('table',class_ = 'wikitable')[6]


class artifactClass:
    def __init__(self,name,icon,bonus2,bonus4):
        self.name = name
        self. icon = icon
        self.bonus2 = bonus2
        self.bonus4 = bonus4

listOfArtifacts = []

for TableObj in artTable.find_all('tr'):
    artRow = TableObj.find_all('td')
    index = 0
    newArtifact = artifactClass('name','icon','bonus2','bonus4')

    for artColumn in artRow:
        if(index == 0):
            newArtifact.name = artColumn.text
        elif(index == 1):
            #newArtifact.icon = artColumn.text
            imgParent = artColumn.find('a')
            img = imgParent.find('img')
            if(img):
                print(img['data-src'])
            else:
                print("no image")
        elif(index == 2):
            newArtifact.bonus2 = artColumn.text
        elif(index == 3):
            newArtifact.bonus4 = artColumn.text
        
        index += 1
        if(index >= 4):
            index = 0
            listOfArtifacts.append(newArtifact)
        

        