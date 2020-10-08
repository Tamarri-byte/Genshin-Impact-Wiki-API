import charScraper as cs
import dictConverter as dc
import wepScraper as ws

#############################
# Get Playable Chars        #
#############################
#cs.getPlayableCharacters()

#############################
# Convert char dict to json #
#############################
#dc.buildPlayableCharDict()


#############################
#Get Weapon Categories
#############################
ws.getWeaponTypes()

#############################
# Convert wep dict to json #
#############################
dc.buildWeaponDict()