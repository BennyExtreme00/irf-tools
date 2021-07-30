from main_ui import Ui_IRFTool
import api
import main_ui
import requests as req
from pymongo import MongoClient
import shutil
import win32gui, win32con
import subprocess
from os import access, system
from time import sleep
import sys
from pynotifier import Notification

api = api.LCU()
local_hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
shutil.rmtree('./__pycache__', ignore_errors=True)
banned_proc_name = ["ProcessHacker.exe", "HTTPDebuggerUI.exe", "HTTPDebuggerSvc.exe"] 
banned_titles = ["Process Hacker", "HxD", "Charles", "HTTP Debugger", "WinHex"]
cluster = MongoClient("mongodb+srv://mangobot:BuK19VGK03aB9QqF@cluster0.8nu7c.mongodb.net/hwids?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = cluster["hwids"]
collection = db["users_hwid"]

img = req.get('https://s3.cointelegraph.com/storage/uploads/view/a7872fcc56858227ffa183256a5d55e1.png').content




def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        all_windows = win32gui.GetWindowText(hwnd)
        for i in range(len(banned_titles)):
                if banned_titles[i] in all_windows:
                        handle = win32gui.FindWindow(None, banned_titles[i])
                        block_info = {"tries": 0, "hwid": local_hwid}
                        data = req.get('http://ip.jsontest.com/', verify=True).json()
                        ip = data["ip"]
                        search = collection.find_one({"hwid": local_hwid})
                        user = search["name"]
                        win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)
                        req.post('https://discord.com/api/webhooks/841715585649344554/wygDqRX9Tq82JMT3d4CJafrFPw_WG6qgNCH7Vh2U-LIoixBPnBOtAaMZXTctqwrXGRWT', json={
                                "username": "Moritz Zimmerman",
                                
                                "content": "```O usuário " + user + " tentou usar " + banned_titles[i] + "\nIP: " + ip + "\nHWID: " + local_hwid + "\n"+"```" + "\n@everyone"
                        })
                        collection.find_one_and_delete({"hwid": local_hwid})
                        exit()
def ClientMode(self, nickname, coin):
    self.ui = Ui_IRFTool()
    win32gui.EnumWindows(winEnumHandler, None)
    tentativas = 0
    access_token = api.get('/lol-rso-auth/v1/authorization/id-token').json()
    access_token = access_token["token"]
    headers = {
        "Authorization": "Bearer " + access_token
    }
    win32gui.EnumWindows(winEnumHandler, None)
    data = req.get('https://br.store.leagueoflegends.com/storefront/v3/history/purchase?language=pt_BR', headers=headers).json()
    accountId = data["player"]["accountId"]
    ea = data["player"]["ip"]
    rp = data["player"]["rp"]

    if coin == "EA" and ea >= 13900:
        print('[IRF Tools] Client Mode Started')
        while True:
            win32gui.EnumWindows(winEnumHandler, None)
            tentativas = tentativas + 1
            checker = api.get('/lol-summoner/v1/check-name-availability/{}'.format(nickname))
            if checker.json() == False:
                pass
            if checker.json() == True:
                purchase = req.post('https://br.store.leagueoflegends.com/storefront/v3/summonerNameChange/purchase?language=pt_BR', headers=headers, json={"summonerName": nickname,"accountId": accountId,"items":[{"inventoryType":"SUMMONER_CUSTOMIZATION","itemId":1,"ipCost": 13900, "quantity":1}]})
                if purchase.status_code == 200:
                    Notification(
                        title="IRF Sniper",
                        description = "You got the nick " + nickname + " in " + tentativas + " tries",
                        duration = 10,
                        urgency = 'normal',
                    ).send()
                    break
                else:
                    pass
    elif coin == "RP" and rp >= 13900:
        print('[IRF Tools] Client Mode Started')
        while True:
            win32gui.EnumWindows(winEnumHandler, None)
            tentativas = tentativas + 1
            checker = api.get('/lol-summoner/v1/check-name-availability/{}'.format(nickname))
            if checker.json() == False:
                pass
            if checker.json() == True:
                purchase = req.post('https://br.store.leagueoflegends.com/storefront/v3/summonerNameChange/purchase?language=pt_BR', headers=headers, json={"summonerName": nickname,"accountId": accountId,"items":[{"inventoryType":"SUMMONER_CUSTOMIZATION","itemId":1,"ipCost": 13900, "quantity":1}]})
                if purchase.status_code == 200:
                    Notification(
                        title="IRF Sniper",
                        description = "You got the nick " + nickname + " in " + tentativas + " tries",
                        duration = 10,
                        urgency = 'normal',
                    ).send()
                    break
                else:
                    pass
    else:
        print("You don't have enough {} ".format(coin.upper()))




def NickSwapper(self, login1, passw1):
    pass