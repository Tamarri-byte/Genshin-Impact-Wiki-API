import requests
from bs4 import BeautifulSoup
import json


foodPageURL = "https://genshin-impact.fandom.com/wiki/Food"

foodReq = requests.get(foodPageURL)
foodReqSoup = BeautifulSoup(foodReq.text,'html.parser')
normFoodTable = foodReqSoup.find_all('table',class_ = 'wikitable')[0]


class normFoodClass:
    def __init__(self,name,icon,rarity,type,effect):
        self.name = name
        self.icon = icon
        self.rarity = rarity
        self.type = type
        self.effect = effect

listOfNormFood = []

def getNormalFood():
    for TableObj in normFoodTable.find_all('tr'):
        foodRow = TableObj.find_all('td')
        index = 0
        newFood = normFoodClass('name','icon','rarity','type','effect')
        
        for foodCol in foodRow:
            if(index == 0):
                newFood.name = foodCol.text
            elif(index == 1):
                imgParent = foodCol.find('a')
                #img = imgParent.find('img')
                if(imgParent):
                    newFood.icon = imgParent['href']
                else:
                    newFood.icon = "no image"
            elif(index == 2):
                newFood.rarity = foodCol.text
            elif(index == 3):
                newFood.type = foodCol.text
            elif(index == 4):
                newFood.effect = foodCol.text

            index += 1
            if(index >= 5):
                index = 0
                listOfNormFood.append(newFood)


specialFoodTable = foodReqSoup.find_all('table',class_ = 'wikitable')[1]

listOfSpecFood = []

class specFoodClass:
    def __init__(self,name,icon,rarity,type,effect,char):
        self.name = name
        self.icon = icon
        self.rarity = rarity
        self.type = type
        self.effect = effect
        self.char = char

def getSpecialFood():
    for TableObj in specialFoodTable.find_all('tr'):
        foodRow = TableObj.find_all('td')
        index = 0
        newFood = specFoodClass('name','icon','rarity','type','effect','char')
        
        for foodCol in foodRow:
            if(index == 0):
                newFood.name = foodCol.text
            elif(index == 1):
                imgParent = foodCol.find('a')
                if(imgParent):
                    newFood.icon = imgParent['href']
                else:
                    newFood.icon = "no image"
            elif(index == 2):
                newFood.rarity = foodCol.text
            elif(index == 3):
                newFood.type = foodCol.text
            elif(index == 4):
                newFood.effect = foodCol.text
            elif(index == 5):
                newFood.char = foodCol.text

            index += 1
            if(index >= 6):
                index = 0
                listOfSpecFood.append(newFood)
            
        