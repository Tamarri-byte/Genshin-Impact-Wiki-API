    for obj in fullWepTable.find_all('tr'):
        print(obj)
        newFullWepObj = obj.find_all('td')
        index = 0
        newFullWep = fullWeapon('wepName')
        for fullWepData in newFullWepObj:
            if(index == 0):
                newFullWep.wepName = fullWepData.text
            
            index += 1
            if(index >= 7):
                index = 0
        
        fullWepList.append(newFullWep)

        
    for x in fullWepList:
        print(x.wepName)
                
            