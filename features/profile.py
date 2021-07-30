import api
from pynotifier import Notification

api = api.LCU()



def rankchanger(elo, division, queue):
    api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue": queue, "regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": elo,"rankedLeagueDivision": division.upper()}})
    Notification(
        title="IRF Tools",
        description = "Rank changed to {}.".format(elo),
        duration = 3,
    ).send()
def StatusChanger(status):
    api.put('/lol-chat/v1/me', {"statusMessage": status})
    Notification(
        title="IRF Tools",
        description = "Status changed.",
        duration = 3,
    ).send()
def IconChanger(iconId):
    if iconId.isnumeric() == True:
        if iconId == 29:
            api.put('/lol-chat/v1/me', {"icon": iconId})
            Notification(
                title="IRF Tools",
                description = "Icon changed to {}".format(iconId),
                duration = 3,
            ).send()
        else:
            api.put('/lol-chat/v1/me', {"icon": iconId})
            api.put('/lol-summoner/v1/current-summoner/icon', {"profileIconId": iconId})
            Notification(
                title="IRF Tools",
                description = "Icon changed to {}".format(iconId),
                duration = 3,
            ).send()
    elif iconId.isnumeric() == False:
        pass

def AvailabilityChanger(stts):
    api.put('/lol-chat/v1/me', {"availability": str(stts)})
    Notification(
        title="IRF Tools",
        description = "Availability changed to {}".format(str(stts.capitalize())),
        duration = 3,
    ).send()
def BackgroundChanger(skinId):
    api.post('/lol-summoner/v1/current-summoner/summoner-profile/', {"key": "backgroundSkinId", "value": skinId})
    Notification(
        title="IRF Tools",
        description = "Background Skin changed to {}".format(str(skinId)),
        duration = 3,
    ).send()

def LobbyCreator(queueId):
    api.post('/lol-lobby/v2/lobby', {"queueId": queueId})
    Notification(
        title="IRF Tools",
        description = "Lobby created ({}).".format(str(queueId)),
        duration = 3,
    ).send()



