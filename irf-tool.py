from keyboard import wait
from time import sleep
from keyboard import is_pressed
from routes import api
from urllib3 import disable_warnings
from pyautogui import confirm
from os import system
from os import startfile
from os import chdir
from requests import status_codes
disable_warnings()

api = api.LeagueOfLegendsClientAPI()

def MultipleClients():
    system('cls')
    print('===================================================')
    print('[1] Default Path (C:/Riot Games/League of Legends/)')
    print('[2] Custom Path                                   ')
    print('[3] Return to menu')
    print('===================================================')
    print()
    path = int(input('[IRF TOOL]: '))

    if path == 1:
        system('cls')
        print('[IRF TOOL] Opening a new Client')
        chdir('C:/Riot Games/League of Legends/')
        system('start LeagueClient.exe --allow-multiple-clients')
        print()
        system('pause')
        MultipleClients()
    elif path == 2:
        system('cls')
        custompath = str(input('Insert custom League Folder Path (ex: D:/Riot Games/League of Legends): '))
        print('[IRF TOOL] Opening a new Client')
        chdir(custompath)
        system('start LeagueClient.exe --allow-multiple-clients')
        print()
        system('pause')
        MultipleClients()
    elif path == 3:
        Main()
    else:
        MultipleClients()
def ChampSelectSystem():
    pass
        
def CopyFriends():
    system('cls')
    data = api.get('/lol-chat/v1/friends').json()
    countfriends = len(data)
    # for i in range(countfriends):
    #     globals()[data[i]["name"]] = str(data[i]["id"])        
    # print()
    print()
    choice = input('[IRF TOOL] Insert the friend nickname: ')
    
    if choice == '':
        print('[IRF TOOL] Friend not found.')
        print()
        system('pause')
        Main()

    for i in range(countfriends):
        if data[i]["name"].lower() == choice.lower():
            choice = data[i]["id"]
            break

    friend = api.get('/lol-chat/v1/friends/{}'.format(choice))
    if friend.status_code == 200:
        friend = friend.json()
        api.put('/lol-chat/v1/me', {"icon": friend["icon"], "statusMessage": friend["statusMessage"]})
        print('[IRF TOOL] {} has been copied.'.format(friend["name"]))
        system('pause')
        Main()
    else:
        print('[IRF TOOL] Friend not found.')
        print()
        system('pause')
        Main()

def DeleteFriends():
    system('cls')
    data = api.get('/lol-chat/v1/friends').json()
    countfriends = len(data)
    confirmbox = confirm(text='Are you sure? this will delete ' + str(countfriends) + ' friends.', title='IRF Tool', buttons=['Yes', 'Cancel'])
    if confirmbox == 'Yes':
        if countfriends == 0:
            print("[IRF TOOL] You don't have any friend :'(")
            system('pause')
            Main()
        else:
            for i in range(countfriends):
                api.delete('/lol-chat/v1/friends/' + data[i]["puuid"])
            print('[IRF TOOL] All friends have been removed.')
            system('pause')
            Main()
    else:
        print('[IRF TOOL] Delete all friends cancelled.')
        system('pause')
        Main()


def Avaibility(): # Change avaibility 
    system('cls'    )
    print('=====================')
    print('[1] Online           ')
    print('[2] Away             ')
    print('[3] Mobile           ')
    print('[4] Offline          ')
    print('[5] Return to menu   ')
    print('=====================')
    choice = int(input('[IRF TOOL]: '))
    if choice == 1:
        req = api.put('/lol-chat/v1/me', {"availability": "online"})
        system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            system('pause')
            Main()
        else:
            print('[IRF TOOL] An error ocurred.')
            system('pause')
            system('exit')
    elif choice == 2:
        req = api.put('/lol-chat/v1/me', {"availability": "away"})
        system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            system('pause')
            Main()
        else:
            print('[IRF TOOL] An error ocurred.')
            system('pause')
            system('exit')
    elif choice == 3:
        req = api.put('/lol-chat/v1/me', {"availability": "mobile"})
        system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            system('pause')
            Main()
        else:
            print('[IRF TOOL] An error ocurred.')
            system('pause')
            system('exit')
    elif choice == 4:
        req = api.put('/lol-chat/v1/me', {"availability": "offline"})
        system('cls')
        if req.status_code == 201:
            print('[IRF TOOL] Avaibility Changed.')
            system('pause')
            Main()
        else:
            print('[IRF TOOL] An error ocurred.')
            system('pause')
            system('exit')
    elif choice == 5:
        Main()
    else:
        Avaibility()

def Status(): # Status Changer (bypass characters limit)
    system('cls')
    system('echo Paste status here, and save it (ctrl+s) > status.txt')
    f = open('status.txt', 'r')
    startfile('status.txt')
    print('[IRF TOOL] Press F8 to continue.')
    wait('f8')
    lines = f.readlines()
    text = '\t'.join([line.strip() for line in lines])
    msg = text.encode("windows-1252").decode("utf-8")
    if msg == 'Paste status here, and save it (ctrl+s)':
        msg = 'https://github.com/flowd1337/irf-tool/'
    data = api.put('/lol-chat/v1/me', {"statusMessage": msg})
    if data.status_code == 201:
        system('cls')
        print('[IRF TOOL] Status changed.')
        system('pause')
        Main()
    else:
        print('[IRF TOOL] An error ocurred.')
        system('pause')
        Main()

def Practice(): # Add more bots to practice tool
    system("cls")
    data = api.post('/lol-lobby/v2/lobby', {"customGameLobby":{"configuration":{"gameMode":"PRACTICETOOL","gameMutator":"","gameServerRegion":"","mapId":11,"mutators":{"id":1},"spectatorPolicy":"NotAllowed","teamSize":5},"lobbyName":"PRACTICE TOOL (IRF TOOL)","lobbyPassword":""},"isCustom": True})
    if data.status_code == 200:
        print('[IRF TOOL] Lobby created.')
        system('pause')
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
    system('cls')
    print('[IRF TOOL] All icons: https://gonext.today/blog/explorer/icon')
    print()
    iconID = int(input('[IRF TOOL] ICON ID: '))
    data = api.put('/lol-summoner/v1/current-summoner/icon', {"profileIconId": iconID})
    if data.status_code == 201:
        print('[IRF TOOL] Icon altered to: {}.'.format(iconID))
        system('pause')
        Main()
    else:
        print('[IRF TOOL] An error ocurred.')
        Main()  
def IconClient(): # Icon Changer (client-only)
    system('cls')
    print('[IRF TOOL] All icons: https://gonext.today/blog/explorer/icon')
    print()
    iconID = int(input('[IRF TOOL] ICON ID: '))
    data = api.put('/lol-chat/v1/me', {"icon": iconID})
    if data.status_code == 201:
        print('[IRF TOOL] Icon altered to: {}.'.format(iconID))
        system('pause')
        Main()
    else:
        print('[IRF TOOL] An error ocurred.')
        Main()

def RankChanger():
    system('cls')
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
        system('cls')
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
                system('cls')
                print('[IRF TOOL] Rank changed to Challenger')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Grandmaster')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Master')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_SOLO_5X5","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    elif choiceQueue == 2:
        system('cls')
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
                system('cls')
                print('[IRF TOOL] Rank changed to Challenger')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Grandmaster')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Master')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_SR","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    elif choiceQueue == 3:
        system('cls')
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
                system('cls')
                print('[IRF TOOL] Rank changed to Challenger')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Grandmaster')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Master')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_FLEX_TT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    elif choiceQueue == 4:
        system('cls')
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
                system('cls')
                print('[IRF TOOL] Rank changed to Challenger')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 2:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GRANDMASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Grandmaster')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()            
        elif choiceElo == 3:
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "MASTER","rankedLeagueDivision": "I"}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Master')
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 4:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "DIAMOND","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Diamond {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 5:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "PLATINUM","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Platinum {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 6:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "GOLD","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Gold {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 7:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "SILVER","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Silver {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 8:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "BRONZE","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Bronze {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 9:
            division = str(input("[IRF TOOL] Division: "))
            data = api.put('/lol-chat/v1/me', {"lol":{"rankedLeagueQueue":"RANKED_TFT","regalia":"{\"bannerType\":1,\"crestType\":2}","rankedSplitRewardLevel":"3","rankedLeagueTier": "IRON","rankedLeagueDivision": division}})
            if data.status_code == 201:
                system('cls')
                print('[IRF TOOL] Rank changed to Iron {}'.format(division))
                system('pause')
                Main()
            else:
                print('[IRF TOOL] An error ocurred.')
                system('pause')
                Main()
        elif choiceElo == 10:
            RankChanger()
        else:
            Main()
    else:
        RankChanger()


def BackgroundChanger(): # Change Profile Background
    system('cls')
    print('[IRF TOOL] Background list: ')
    print()
    bgid = str(input('[IRF TOOL] Background ID: '))
    data = api.post('/lol-summoner/v1/current-summoner/summoner-profile/', {"key":"backgroundSkinId","value": bgid})
    if data.status_code == 200:
        print()
        print('[IRF TOOL] Background has been changed.')
        Main()
    else:
        print('[IRF TOOL] An error ocurred.')
        system('pause')
        Main()
    pass

def Main():
    try:
        #currentSummoner = api.get('/lol-summoner/v1/current-summoner').json()
        #nick = currentSummoner["displayName"]
        system('cls && title IRF TOOL && color b')
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
            system('cls')
            print('============IRF TOOL============')
            print('[1] Rank Changer                ')
            print('[2] Practice Tool (more bots)   ')
            print('[3] Remove all friends          ')
            print('[4] Copy Friend                 ')
            print('[5] Multiple Clients')
            print('[6] Previous Page               ')
            print('[7] Next Page                   ')
            print('[8] Exit')
            print('================================')
            choice2 = int(input('[IRF TOOL]: '))
            if choice2 == 1:
                RankChanger()
            elif choice2 == 2:
                Practice()
            elif choice2 == 3:
                DeleteFriends()
            elif choice2 == 4:
                CopyFriends()
            elif choice2 == 5:
                MultipleClients()
            elif choice2 == 6:
                Main()
            elif choice2 == 7:
                system('cls')
                print('[IRF TOOL] Coming soon...')
                system('pause')
                Main()
            elif choice2 == 8:
                system('exit')
            # elif choice2 == 2:
            #     Instalock()
        elif choice == 7:
            system('exit')
        else:
            Main()
    except KeyboardInterrupt:
        print()
        system('exit')
    except:
        print()
        print('[IRF TOOL] An error ocurred.')
        sleep(0.9)
        Main()

        
if __name__ in "__main__":
    Main()
