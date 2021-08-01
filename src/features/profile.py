import api
from pynotifier import Notification
import pymsgbox

api = api.LCU()



def rankchanger(elo, division, queue):
    api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue": queue, "regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": elo,"rankedLeagueDivision": division.upper()}})
    pymsgbox.alert(title='IRF Tools', text="Rank changed to {} {}".format(elo, division), button='OK')

def StatusChanger(status):
    api.put('/lol-chat/v1/me', {"statusMessage": status})
    pymsgbox.alert(title='IRF Tools', text="Status changed.", button='OK')

def IconChanger(iconId):
    if iconId.isnumeric() == True:
        if iconId == 29:
            api.put('/lol-chat/v1/me', {"icon": iconId})
            pymsgbox.alert(title='IRF Tools', text="Icon changed to {}".format(iconId), button='OK')
        else:
            api.put('/lol-chat/v1/me', {"icon": iconId})
            api.put('/lol-summoner/v1/current-summoner/icon', {"profileIconId": iconId})
            pymsgbox.alert(title='IRF Tools', text="Icon changed to {}".format(iconId), button='OK')
    elif iconId.isnumeric() == False:
        pass

def AvailabilityChanger(stts):
    api.put('/lol-chat/v1/me', {"availability": str(stts)})
    pymsgbox.alert(title='IRF Tools', text="Availability changed to {}".format(str(stts)), button='OK')

def BackgroundChanger(skinId):
    api.post('/lol-summoner/v1/current-summoner/summoner-profile/', {"key": "backgroundSkinId", "value": skinId})
    pymsgbox.alert(title='IRF Tools', text="Background Skin changed to {}".format(skinId), button='OK')

def LobbyCreator(queueId):
    data = api.post('/lol-lobby/v2/lobby', {"queueId": queueId})
    if data.status_code == 200:
        pymsgbox.alert(title='IRF Tools', text="Lobby Created ({})".format(queueId), button='OK')
    else:
        pymsgbox.alert(title='IRF Tools', text="Unable to create Lobby.".format(queueId), button='OK')



