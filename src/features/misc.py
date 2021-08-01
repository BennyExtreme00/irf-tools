from os import system, chdir
import pyautogui
import webbrowser
import keyboard
import time
import clipboard
from bs4 import BeautifulSoup
from pynotifier import Notification
import api
import requests as req
import pymsgbox

api = api.LCU()

def insta_quit():
    system('taskkill /f /im LeagueCrashHandler.exe /t')
    system('taskkill /f /im  "League of Legends.exe" /t')

def multiclients():
    get_path = api.get('/data-store/v1/install-dir').json()
    chdir(get_path)
    system('start LeagueClient.exe --allow-multiple-clients')
    pymsgbox.alert(title='IRF Tools', text="A new League Client has been opened.", button='OK')


def practice_tool():
    data = api.post('/lol-lobby/v2/lobby', {
        "customGameLobby": {
            "configuration": {
            "gameMode":"PRACTICETOOL",
            "gameMutator":"",
            "gameServerRegion":"",
            "mapId":11,
            "mutators":{
                "id":1
                },
            "spectatorPolicy":"NotAllowed",
            "teamSize":5
            },
            "lobbyName":
            "Practice Tool+ (IRF TOOLS)",
            "lobbyPassword":""
            },
            "isCustom": True
        }
    )
    if data.status_code == 200:
        pymsgbox.alert(title='IRF Tools', text="Practice Tool Lobby has been created.", button='OK')
    else:
        pymsgbox.alert(title='IRF Tools', text="Unexpected Error.", button='OK')

def autorunes():
    url = 'https://na.op.gg/champion/leesin/statistics/build'
    html = req.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    rune_first_row = soup.find_all("div", class_="perk-page")[0].find_all_next("div", class_="perk-page__row")[1].find_next("div", class_="perk-page__item perk-page__item--keystone perk-page__item--active").find_all("img")
    for img in rune_first_row:
        rune_first_row = img["src"]
    rune_second_row = soup.find_all("div", class_="perk-page")[0].find_all_next("div", class_="perk-page__row")
    rune_third_row = soup.find_all("div", class_="perk-page")[0].find_all_next("div", class_="perk-page__row")
    rune_fourth_row = soup.find_all("div", class_="perk-page")[0].find_all_next("div", class_="perk-page__row")
    print(rune_first_row)
    print(rune_second_row)
    # champSelect = api.get('/lol-champ-select/v1/session')
    # if champSelect.status_code == 404:
    #     searched = False
    # else:
        # data = api.get('/lol-lobby/v2/lobby').json()
        # partyId = data["partyId"]
        # champSelect = api.get('/lol-champ-select/v1/session').json()
        # if champSelect["isCustomGame"] == True:
    # champion_id = api.get('/lol-champ-select/v1/current-champion').json()
    # champion_name = self.champion_id_to_name(champion_id)
        # else:
        #     pass
         

def change_language(language):
    change_language = api.put('/riotclient/region-locale', json={
        "locale": language
    })
    if change_language.status_code == 204:
        pymsgbox.alert(title='IRF Tools', text="Language changed to {}".format(language), button='OK')
