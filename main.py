import charScraper as cs
import dictConverter as dc
import wepScraper as ws
import artifactScraper as AS

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
#ws.getWeaponTypes()

#############################
# Convert wep dict to json #
#############################
#dc.buildWeaponDict()



#############################
#Get Artifact Categories
#############################
AS.get4PieceArtifacts()


#################################
# Convert artifact dict to json #
#################################
dc.build4pieceArtifactsDict()