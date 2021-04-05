import os
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
    choice = int(input('[IRF-TOOL]: '))
    if choice == 1:
        req = api.put(routes.avaibilityroute, {"availability": "online"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF-TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF-TOOL] A error ocurred.')
            os.system('pause')
            exit()
    elif choice == 2:
        req = api.put(routes.avaibilityroute, {"availability": "away"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF-TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF-TOOL] A error ocurred.')
            os.system('pause')
            exit()
    elif choice == 3:
        req = api.put(routes.avaibilityroute, {"availability": "mobile"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF-TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF-TOOL] A error ocurred.')
            os.system('pause')
            exit()
    elif choice == 4:
        req = api.put(routes.avaibilityroute, {"availability": "offline"})
        os.system('cls')
        if req.status_code == 201:
            print('[IRF-TOOL] Avaibility Changed.')
            os.system('pause')
            Main()
        else:
            print('[IRF-TOOL] A error ocurred.')
            os.system('pause')
            exit()

def Status(): # Status Changer (bypass characters limit)
    pass
def IconChanger(): # Icon Changer (chinese icons)

    pass

def IconClient(): # Icon Changer (client-only)
    iconID = int(input('[IRF-TOOL] ICON ID: '))

    data = api.put(routes.statusroute, {"icon": iconID})
    print(data.json())
    pass

def BackgroundChanger(): # Change Profile Background
    pass

def Main():
    try:
        currentSummoner = api.get(routes.currentsummoner)
        nick = currentSummoner["displayName"]
        os.system('cls && title IRF-TOOL - ({})'.format(nick))
        print('[IRF-TOOL] Choose a feature.')
        print()
        print('============IRF-TOOL============')
        print('[1] Change Avaibility           ')
        print('[2] Status Changer              ')
        print('[3] Icon Changer (29 to 78)     ')
        print('[4] Icon Changer (client-only)  ')
        print('[5] Change Profile Background   ')
        print('[6] Next Page                   ')
        print('[7] Exit                        ')
        print('================================')

        choice = int(input('[IRF-TOOL]: '))
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

        else:
            Main()
    except KeyboardInterrupt:
        exit()
    except:
        print('[IRF-TOOL] An error ocurred.')
        Main()
        


if __name__ in "__main__":
    Main()