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
                #print(tl[x].name.strip())
        
                
        chIndex += 1