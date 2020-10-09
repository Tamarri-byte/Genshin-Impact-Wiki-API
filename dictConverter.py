from ast import dump
import json

dict_playableChar = {}
allplayabledicts = []

def buildPlayableCharDict():   #Playable Chars
    import charScraper as cs
    cl = cs.charList
    for x in range(len(cs.charList)):
        charToAdd = {"rarity": cl[x].charRarity.strip(),
        "icon": cl[x].charIcon.strip(),
        "name": cl[x].charName.strip(),
        "elem": cl[x].charElem.strip(),
        "wep": cl[x].charWep.strip(),
        "sex": cl[x].charSex.strip(),
        "region": cl[x].charRegion.strip(),
        "talents" : cl[x].charTalentInfo}

        #dict_playableChar = dict_playableChar + charToAdd
        allplayabledicts.append(charToAdd)

    dict_playableChar = allplayabledicts

    with open("docs/characters/playableChar.json", 'w') as fp:
        json.dump(dict_playableChar,fp,indent=2,separators=(',', ':'))


#---------------------------------------------------------------
dict_upcomingChar = {}

def buildUpcomingCharDict():
    import charScraper as cs
    ucl = cs.upcomingCharList
    for x in range(len(ucl)):
        charToAdd = {"name": ucl[x].charName.strip(),
        "element": ucl[x].charElement.strip(),
        "weapon": ucl[x].charWep.strip(),
        "sex": ucl[x].charSex.strip(),
        "region": ucl[x].charRegion.strip()}

        dict_upcomingChar[ucl[x].charName.strip()] = charToAdd
        

    with open("docs/characters/upcomingChar.json", 'w') as fp:
        json.dump(dict_upcomingChar,fp,indent=2,separators=(',', ':'))

#-----------------------------------------------------------------------
dict_nonPlayableChar = {}

def buildNonPlayableCharDict():
    import charScraper as cs
    npcl = cs.nonPlayableCharList

    for x in range(len(npcl)):
        charToAdd = {"name": npcl[x].charName.strip(),
        "element": npcl[x].charElem.strip(),
        "role": npcl[x].charRole.strip(),
        "region": npcl[x].charRegion.strip(),}

        dict_nonPlayableChar[npcl[x].charName.strip()] = charToAdd


    with open("docs/characters/nonplayableChar.json", 'w') as fp:
        json.dump(dict_nonPlayableChar,fp,indent=2,separators=(',', ':'))


#-----------------------------------------------------------------------

dict_weaponTypes = {}
allweaponTypeDicts = []
def buildWeaponDict():
    import wepScraper as ws
    WL = ws.wepList
    WL.remove(WL[0])
    for x in range(len(WL)):
        wepTypeToAdd = {"name": WL[x].typeName.strip(),
        "info": WL[x].typeInfo.strip(),
        "weapons": WL[x].fullWeapon}

        allweaponTypeDicts.append(wepTypeToAdd)
    

    dict_weaponTypes = allweaponTypeDicts

    #print(WL[0].fullWeapon)
    
    
    with open("docs/weapons/weaponTypes.json", 'w') as fp:
        json.dump(dict_weaponTypes,fp,indent=2,separators=(',', ':'))
    
    