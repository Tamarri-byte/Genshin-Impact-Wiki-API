from ast import dump
import json

dict_playableChar = {}

def buildPlayableCharDict():
    import charScraper as cs
    cl = cs.charList
    for x in range(len(cs.charList)):
        charToAdd = {"rarity": cl[x].charRarity.strip(),
        "icon": cl[x].charIcon.strip(),
        "name": cl[x].charName.strip(),
        "elem": cl[x].charElem.strip(),
        "wep": cl[x].charWep.strip(),
        "sex": cl[x].charSex.strip(),
        "region": cl[x].charRegion.strip()}

        dict_playableChar[cl[x].charName.strip()] = charToAdd

    with open("docs/characters/playableChar.json", 'w') as fp:
        json.dump(dict_playableChar,fp,indent=2,separators=(',', ':'))