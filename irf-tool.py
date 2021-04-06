import os
import keyboard
from routes import api
from routes import routes
from urllib3 import disable_warnings


disable_warnings()

print('Waiting league client...')

api = api.LeagueOfLegendsClientAPI()

def Avaibility():
    os.system('cls')
    print('===================')
    print('[1] Online          ')
    print('[2] Away            ')
    print('[3] Mobile          ')
    print('[4] Offline         ')
    print('===================')
    choice = int(input('[IRF TOOL]: '))
    if choice == 1:
        req = api.put('/lol-chat/v1/me', {"availability": "online"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF TOOL] A error ocurred.')
            os.system('pause')
            os.system('exit')
    elif choice == 2:
        req = api.put('/lol-chat/v1/me', {"availability": "away"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF TOOL] A error ocurred.')
            os.system('pause')
            os.system('exit')
    elif choice == 3:
        req = api.put('/lol-chat/v1/me', {"availability": "mobile"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF TOOL] A error ocurred.')
            os.system('pause')
            os.system('exit')
    elif choice == 4:
        req = api.put('/lol-chat/v1/me', {"availability": "offline"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF TOOL] A error ocurred.')
            os.system('pause')
            os.system('exit')
    else:
        Avaibility()

def Status(): # Status Changer (bypass characters limit)
    os.system('echo Paste status here, and save it (ctrl+s) > status.txt')
    f = open('status.txt', 'r')
    os.startfile('status.txt')
    print('[IRF TOOL] Press F8 to continue.')
    keyboard.wait('f8')
    lines = f.readlines()
    text = '\t'.join([line.strip() for line in lines])
    msg = text.encode("windows-1252").decode("utf-8")
    data = api.put('/lol-chat/v1/me', {"statusMessage": msg})
    if data.status_code == 201:
        print('[IRF TOOL] Status changed.')
    else:
        print('[IRF TOOL] An error ocurred.')
        os.system('pause')
        Main()

def Practice():
    os.system("cls")
    data = api.post('/lol-lobby/v2/lobby', {"customGameLobby":{"configuration":{"gameMode":"PRACTICETOOL","gameMutator":"","gameServerRegion":"","mapId":11,"mutators":{"id":1},"spectatorPolicy":"NotAllowed","teamSize":5},"lobbyName":"PRACTICE TOOL (IRF TOOL)","lobbyPassword":""},"isCustom": True})
    if data.status_code == 200:
        print('[IRF TOOL] Lobby created.')
        os.system('pause')
        Main()
    else:
        print('[IRF TOOL] An error ocurred.')
        Main()
# def Instalock():
#     data = api.patch('/lol-champ-select/v1/session/actions/1', {"championId": "1","completed": True})
#     if data.status_code == 204:
#         Main()
#     else:
#         Main()
def IconChanger(): # Icon Changer (chinese icons)
    os.system('cls')
    print('[IRF TOOL] All icons: https://gonext.today/blog/explorer/icon')
    print()
    iconID = int(input('[IRF TOOL] ICON ID: '))
    data = api.put('/lol-summoner/v1/current-summoner/icon', {"profileIconId": iconID})
    if data.status_code == 201:
        print('[IRF TOOL] Icon altered to: {}.'.format(iconID))
        os.system('pause')
        Main()
    else:
        print('[IRF TOOL] An error ocurred.')
        Main()
def IconClient(): # Icon Changer (client-only)
    os.system('cls')
    print('[IRF TOOL] All icons: https://gonext.today/blog/explorer/icon')
    print()
    iconID = int(input('[IRF TOOL] ICON ID: '))
    data = api.put('/lol-chat/v1/me', {"icon": iconID})
    if data.status_code == 201:
        print('[IRF TOOL] Icon altered to: {}.'.format(iconID))
        os.system('pause')
        Main()
    else:
        print('[IRF TOOL] An error ocurred.')
        Main()

def RankChanger():
    os.system('cls')
    print('[IRF TOOL] CHOOSE THE QUEUE  ')
    print()
    print('=============================')
    print('[1] SOLO/DUO (5X5)           ')
    print('[2] FLEX (5X5)               ')
    print('[3] TWISTED TREE LINE (3X3)  ')
    print('[4] TFT                      ')
    print('[5] Back to menu             ')
    print('=============================')
    print()
    choiceQueue = int(input('[IRF TOOL]: '))
    if choiceQueue == 1:
        os.system('cls')
        print('[IRF TOOL] SOLO/DUO')
        print()
        print('=============================')
        print('[1] Challenger               ')
        print('[2] Grandmaster              ')
        print('[3] Master                   ')
        print('[4] Diamond                  ')
        print('[5] Platinum                 ')
        print('[6] Gold                     ')
        print('[7] Silver                   ')
        print('[8] Bronze                   ')
        print('[9] Iron                     ')
        print('[10] Back to queue selector  ')
        print('=============================')
        print()
        choiceElo = int(input('[IRF TOOL]: '))
        if choiceElo == 1:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5", "regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "CHALLENGER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Challenger')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Grandmaster')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Master')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    elif choiceQueue == 2:
        os.system('cls')
        print('[IRF TOOL] FLEX')
        print()
        print('=============================')
        print('[1] Challenger               ')
        print('[2] Grandmaster              ')
        print('[3] Master                   ')
        print('[4] Diamond                  ')
        print('[5] Platinum                 ')
        print('[6] Gold                     ')
        print('[7] Silver                   ')
        print('[8] Bronze                   ')
        print('[9] Iron                     ')
        print('[10] Back to queue selector  ')
        print('=============================')
        print()
        choiceElo = int(input('[IRF TOOL]: '))
        if choiceElo == 1:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "CHALLENGER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Challenger')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Grandmaster')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Master')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    elif choiceQueue == 3:
        os.system('cls')
        print('[IRF TOOL] TWISTED TREE LINE ')
        print()
        print('=============================')
        print('[1] Challenger               ')
        print('[2] Grandmaster              ')
        print('[3] Master                   ')
        print('[4] Diamond                  ')
        print('[5] Platinum                 ')
        print('[6] Gold                     ')
        print('[7] Silver                   ')
        print('[8] Bronze                   ')
        print('[9] Iron                     ')
        print('[10] Back to queue selector  ')
        print('=============================')
        print()
        choiceElo = int(input('[IRF TOOL]: '))
        if choiceElo == 1:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "CHALLENGER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Challenger')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Grandmaster')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Master')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    elif choiceQueue == 4:
        os.system('cls')
        print('[IRF TOOL] TFT')
        print()
        print('=============================')
        print('[1] Challenger               ')
        print('[2] Grandmaster              ')
        print('[3] Master                   ')
        print('[4] Diamond                  ')
        print('[5] Platinum                 ')
        print('[6] Gold                     ')
        print('[7] Silver                   ')
        print('[8] Bronze                   ')
        print('[9] Iron                     ')
        print('[10] Back to queue selector  ')
        print('=============================')
        print()
        choiceElo = int(input('[IRF TOOL]: '))
        if choiceElo == 1:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "CHALLENGER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Challenger')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Grandmaster')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Master')
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                os.system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                os.system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    else:
        RankChanger()


def BackgroundChanger(): # Change Profile Background
    pass

def Main():
    try:
        currentSummoner = api.get('/lol-summoner/v1/current-summoner').json()
        nick = currentSummoner["displayName"]
        os.system('cls && title IRF TOOL - ({}) && color b'.format(nick))
        print('[IRF TOOL] Choose a feature.')
        print()
        print('============IRF TOOL============')
        print('[1] Change Avaibility           ')
        print('[2] Status Changer              ')
        print('[3] Icon Changer (29 to 78)     ')
        print('[4] Icon Changer (client-only)  ')
        print('[5] Change Profile Background   ')
        print('[6] Next Page                   ')
        print('[7] Exit                        ')
        print('================================')

        choice = int(input('[IRF TOOL]: '))
        if choice == 1:
            Avaibility()
        elif choice == 2:
            Status()
        elif choice == 3:
            IconChanger()
        elif choice == 4:
            IconClient()
        elif choice == 5:
            BackgroundChanger()
        elif choice == 6:
            os.system('cls')
            print('============IRF TOOL============')
            print('[1] Rank Changer                ')
            print('[2] Practice Tool (more bots)   ')
            # print('[2] Instalock                   ')
            print('================================')
            choice2 = int(input('[IRF TOOL]: '))
            if choice2 == 1:
                RankChanger()
            elif choice2 == 2:
                Practice()
            # elif choice2 == 2:
            #     Instalock()
        elif choice == 7:
            os.system('exit')
        else:
            Main()
    except KeyboardInterrupt:
        os.system('exit')
    except:
        print('[IRF TOOL] An error ocurred.')
        Main()
        
if __name__ in "__main__":
    Main()
