
from re import search
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QImage)
from PySide2.QtWidgets import *
from main_ui import Ui_IRFTool
from ui_functions import *

import webbrowser
import pymsgbox
from bs4 import BeautifulSoup
import pythread as thread
import sys
import threading
import platform
import requests as req
import json
import random
from os import system
from threadify import Threadify
from thread_task import Task
import keyboard
import ctypes
import multiprocessing
from pyautogui import confirm
from time import sleep
from pynotifier import Notification

from api import LCU
from features import friends
from features import instalocker
from features import exploits
from features import profile
from features import misc

api = LCU()

global instalockerBlind
global instalockerDraft
global autoAccept
global autoPlayAgain

instalockerBlind = 0
instalockerDraft = 0
autoAccept = 0
autoPlayAgain = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_IRFTool()
        self.ui.setupUi(self)
        self.hide_division()
        self.hide_availability()
        self.hide_lanes()
        self.hide_queue()
        

        # UI Functions
        UIFunctions.selectStandardMenu(self, "homeBtn")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.minimizeBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.closeBtn.clicked.connect(lambda: self.close())
        get_all_versions = req.get('https://ddragon.leagueoflegends.com/api/versions.json').json()
        self.latest_version = get_all_versions[0]
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        def keyPressEvent(self, event):
            if event.key() == Qt.Key_Tab:
               pass
        self.ui.topBar.mouseMoveEvent = moveWindow
        self.ui.topbar2.mouseMoveEvent = moveWindow

        ##

    
        # Pages
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.homeBtn.clicked.connect(lambda: UIFunctions.resetStyle(self, "homeBtn"))
        self.ui.homeBtn.clicked.connect(lambda: UIFunctions.selectStandardMenu(self, "homeBtn"))
        self.ui.homeBtn.clicked.connect(lambda: threading.Thread(target=self.refresh).start())

        self.ui.exploitsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.exploitsBtn.clicked.connect(lambda: UIFunctions.resetStyle(self, "exploitsBtn"))
        self.ui.exploitsBtn.clicked.connect(lambda: UIFunctions.selectStandardMenu(self, "exploitsBtn"))

        self.ui.instalockBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.instalockBtn.clicked.connect(lambda: UIFunctions.resetStyle(self, "instalockBtn"))
        self.ui.instalockBtn.clicked.connect(lambda: UIFunctions.selectStandardMenu(self, "instalockBtn"))

        self.ui.miscBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.miscBtn.clicked.connect(lambda: UIFunctions.resetStyle(self, "miscBtn"))
        self.ui.miscBtn.clicked.connect(lambda: UIFunctions.selectStandardMenu(self, "miscBtn"))

        self.ui.friendsPgBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.friendsPgBtn.clicked.connect(lambda: UIFunctions.resetStyle(self, "friendsPgBtn"))
        self.ui.friendsPgBtn.clicked.connect(lambda: UIFunctions.selectStandardMenu(self, "friendsPgBtn"))
        ##
    
        # Stacked Widgets
        self.ui.refreshBtn.clicked.connect(lambda: threading.Thread(target=self.refresh).start()) # Refresh
        self.ui.refreshFriendsBtn.clicked.connect(lambda: threading.Thread(target=self.refresh_friends).start()) # Refresh Friends
        self.ui.previousEloBtn.clicked.connect(lambda: self.ui.eloManager.setCurrentIndex(self.ui.eloManager.currentIndex() - 1)) #  Previous Elo
        self.ui.nextEloBtn.clicked.connect(lambda: self.ui.eloManager.setCurrentIndex(self.ui.eloManager.currentIndex() + 1)) # Next Elo
        self.ui.previousEloBtn.clicked.connect(lambda: self.hide_division()) 
        self.ui.nextEloBtn.clicked.connect(lambda: self.hide_division())
    
        self.ui.previousQueueBtn.clicked.connect(lambda: self.ui.queueManager.setCurrentIndex(self.ui.queueManager.currentIndex() - 1)) # Previous Queue
        self.ui.nextQueueBtn.clicked.connect(lambda: self.ui.queueManager.setCurrentIndex(self.ui.queueManager.currentIndex() + 1)) # Next Queue
        self.ui.previousQueueBtn.clicked.connect(lambda: self.hide_queue()) 
        self.ui.nextQueueBtn.clicked.connect(lambda: self.hide_queue())

        self.ui.previousAvailability.clicked.connect(lambda: self.ui.availabilityManager.setCurrentIndex(self.ui.availabilityManager.currentIndex() - 1)) # Previous Availability
        self.ui.nextAvailability.clicked.connect(lambda: self.ui.availabilityManager.setCurrentIndex(self.ui.availabilityManager.currentIndex() + 1))  # Next Availability
        self.ui.previousAvailability.clicked.connect(lambda: self.hide_availability()) 
        self.ui.nextAvailability.clicked.connect(lambda: self.hide_availability())

        self.ui.previousLaneBtn.clicked.connect(lambda: self.ui.laneSelector.setCurrentIndex(self.ui.laneSelector.currentIndex() - 1))
        self.ui.nextLaneBtn.clicked.connect(lambda: self.ui.laneSelector.setCurrentIndex(self.ui.laneSelector.currentIndex() + 1))
        self.ui.previousLaneBtn.clicked.connect(lambda: self.hide_lanes())
        self.ui.nextLaneBtn.clicked.connect(lambda: self.hide_lanes())
        ## 

        # Button Functions
        InstalockerBlindProcess = multiprocessing.Process(target=instalocker.Instalock)
        
        self.ui.removeAllFriendsBtn.clicked.connect(lambda: threading.Thread(target=self.remove_friends).start())
        self.ui.declineAllFriendsBtn.clicked.connect(lambda: threading.Thread(target=friends.decline_all_friend_requests).start())
        self.ui.acceptAllFriendsBtn.clicked.connect(lambda: threading.Thread(target=friends.accept_all_friend_requests).start())
        self.ui.copyStatusBtn.clicked.connect(lambda: threading.Thread(target=friends.CopyStatus, args=(self.ui.friendList.currentItem().text(),)).start())
        self.ui.copyIconBtn.clicked.connect(lambda: threading.Thread(target=friends.CopyIcon, args=(self.ui.friendList.currentItem().text(),)).start())
        self.ui.banMessageBtn.clicked.connect(lambda: threading.Thread(target=friends.fake_ban_message, args=(self.ui.friendList.currentItem().text(),)).start())
        self.ui.chatCrashBtn.clicked.connect(lambda: threading.Thread(target=exploits.CrashChat, args=(self.ui.friendList.currentItem().text(),)).start())
        self.ui.copyStatusBtn.clicked.connect(lambda: threading.Thread(target=self.refresh).start())
        self.ui.copyIconBtn.clicked.connect(lambda: threading.Thread(target=self.refresh).start())
        self.ui.changeEloBtn.clicked.connect(lambda: threading.Thread(target=profile.rankchanger, args=(self.ui.eloManager.currentWidget().objectName(), self.ui.divisionInput.text(), self.ui.queueManager.currentWidget().objectName(),)).start())
        self.ui.statusUpdateBtn.clicked.connect(lambda: threading.Thread(target=profile.StatusChanger, args=(self.ui.statusInput.toPlainText(),)).start())
        self.ui.updateAvailabilityBtn.clicked.connect(lambda: threading.Thread(target=profile.AvailabilityChanger, args=(self.ui.availabilityManager.currentWidget().objectName(),)).start())
        self.ui.updateAvailabilityBtn.clicked.connect(lambda: threading.Thread(target=self.refresh).start())
        self.ui.createLobbyBtn.clicked.connect(lambda: threading.Thread(target=profile.LobbyCreator, args=(self.ui.queueInput.text(),)).start())
        self.ui.updateIconBtn.clicked.connect(lambda: threading.Thread(target=profile.IconChanger, args=(self.ui.iconInput.text(),)).start())
        self.ui.updateBackgroundBtn.clicked.connect(lambda: threading.Thread(target=profile.BackgroundChanger, args=(self.ui.backgroundInput.text(),)).start())
        self.ui.tristanaBtn.clicked.connect(lambda: threading.Thread(target=exploits.Tristana).start())
        self.ui.enableMultiSearchBtn.clicked.connect(lambda: threading.Thread(target=self.multi_search).start())
        # self.ui.crashBtn.clicked.connect(lambda: threading.Thread(target=exploits.CrashChat, args=(self.ui.inputFriendCrash.text(),)).start())
        self.ui.startBtnB.clicked.connect(lambda: threading.Thread(target=self.instalocker_blind).start())
        # self.ui.startBtnD.clicked.connect(lambda: threading.Thread(target=self.instalocker_draft).start())
        self.ui.startAcceptBtn.clicked.connect(lambda: threading.Thread(target=self.auto_accept).start())
        self.ui.startPlayAgBtn.clicked.connect(lambda: threading.Thread(target=self.auto_play_again).start())
        self.ui.openClientBtn.clicked.connect(lambda: threading.Thread(target=misc.multiclients).start())
        self.ui.createPracticeToolBtn.clicked.connect(lambda: threading.Thread(target=misc.practice_tool).start())
        self.ui.enableInstaQuitBtn.clicked.connect(lambda: threading.Thread(target=self.insta_quit).start())
        self.ui.enableAutoRunesBtn.clicked.connect(lambda: threading.Thread(target=self.auto_runes).start())

        ##  

        # Enable Buttons
        self.ui.friendsPgBtn.clicked.connect(lambda: threading.Thread(target=self.refresh_friends).start())
        self.ui.friendList.itemClicked.connect(lambda: self.ui.friendSelected.show())
        self.ui.friendList.itemClicked.connect(lambda: self.ui.friendNameLabel.setText(self.ui.friendList.currentItem().text()))
        self.ui.startBtnB.clicked.connect(lambda: self.ui.instalockManagerB.setCurrentIndex(1))
        self.ui.stopBtnB.clicked.connect(lambda: self.ui.instalockManagerB.setCurrentIndex(0))
        # self.ui.startBtnD.clicked.connect(lambda: self.ui.instalockManagerD.setCurrentIndex(1))
        # self.ui.stopBtnD.clicked.connect(lambda: self.ui.instalockManagerD.setCurrentIndex(0))
        self.ui.startAcceptBtn.clicked.connect(lambda: self.ui.autoAcceptManager.setCurrentIndex(1))
        self.ui.stopAcceptBtn.clicked.connect(lambda: self.ui.autoAcceptManager.setCurrentIndex(0))
        self.ui.startPlayAgBtn.clicked.connect(lambda: self.ui.autoPlayAgainManager.setCurrentIndex(1))
        self.ui.stopPlayAgBtn.clicked.connect(lambda: self.ui.autoPlayAgainManager.setCurrentIndex(0))
        self.ui.enableInstaQuitBtn.clicked.connect(lambda: self.ui.instaQuitManager.setCurrentIndex(1))
        self.ui.disableInstaQuitBtn.clicked.connect(lambda: self.ui.instaQuitManager.setCurrentIndex(0))
        self.ui.enableAutoRunesBtn.clicked.connect(lambda: self.ui.runesManager.setCurrentIndex(1))
        self.ui.disableAutoRunesBtn.clicked.connect(lambda: self.ui.runesManager.setCurrentIndex(0))
        self.ui.enableMultiSearchBtn.clicked.connect(lambda: self.ui.multiSearchManager.setCurrentIndex(1))
        self.ui.disableMultiSearchBtn.clicked.connect(lambda: self.ui.multiSearchManager.setCurrentIndex(0))
        ##

        self.show()
        self.get_friend_requests()

    def multi_search(self):
        confirmbox = pymsgbox.alert(title='IRF Tools', text='Multi OP.GG enabled.', button='OK')
        searched = False
        while self.ui.multiSearchManager.currentIndex() == 1:
            sleep(1.5)
            region = api.get('/riotclient/get_region_locale').json()["region"].lower()
            champSelect = api.get('/lol-champ-select/v1/session')
            if champSelect.status_code == 404:
                searched = False
            else:
                data = api.get('/lol-lobby/v2/lobby').json()
                partyId = data["partyId"]
                champSelect = api.get('/lol-champ-select/v1/session').json()
                if champSelect["isCustomGame"] == True:
                    pass
                else:
                    if searched == False:
                        all_members = data["members"]
                        player_list = []
                        for i in range(len(all_members)):
                            print(all_members[i]["summonerInternalName"])
                            player_list.append(all_members[i]["summonerInternalName"])

                        opgg_url = "https://{}.op.gg/multi/query={}%2C{}%2C{}%2C{}%2C{}".format(region, player_list[0], player_list[1], player_list[2], player_list[3], player_list[4])
                        webbrowser.open(opgg_url)
                        searched = True        

    def auto_runes(self):
        confirmbox = pymsgbox.alert(title="IRF Tools", text='Coming Soon', button='OK')

    def insta_quit(self):
        confirmbox = pymsgbox.alert(title="IRF Tools", text='Coming Soon', button='OK')

    def champion_name_to_id(self, name):
        champion = name.lower().capitalize()
        champ_url = 'https://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion/{}.json'.format(self.latest_version, champion)
        championId = req.get(champ_url).json()["data"][champion]["key"]
        
        return championId
    
    def champion_id_to_name(self, championId):
        url = 'https://ddragon.leagueoflegends.com/cdn/{}/data/pt_BR/champion.json'.format(self.latest_version)
        data = req.get(url).json()
        for i in data:
            if championId == data[i]["key"]:
                championName = data[i]["name"]
                return championName
                break
            
    def get_champion_title(self, name):
        champion = name.lower().capitalize()
        champ_url = 'https://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion/{}.json'.format(self.latest_version, champion)
        championTitle = req.get(champ_url).json()["data"][champion]["title"]
        return championTitle

    def get_friend_requests(self):
        all_friend_requests = api.get('/lol-chat/v1/friend-requests')

    def instalocker_blind(self):
        self.lane = "None"

        if self.ui.laneSelector.currentIndex() == 1:
            self.lane = "Top"
        elif self.ui.laneSelector.currentIndex() == 2:
            self.lane = "Jungle"
        elif self.ui.laneSelector.currentIndex() == 3:
            self.lane = "Mid"
        elif self.ui.laneSelector.currentIndex() == 4:
            self.lane = "ADC"
        elif self.ui.laneSelector.currentIndex() == 5:
            self.lane = "Support"
        championName = self.ui.championLockB.text().lower().capitalize()
        data = req.get('https://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/champion/{}.json'.format(championName))
        if data.status_code == 200:
            confirmbox = pymsgbox.alert(title='IRF Tools', text='Instalocker enabled.', button='OK')
            champId = self.champion_name_to_id(championName)
            while self.ui.instalockManagerB.currentIndex() == 1: # stop btn
                sleep(1)
                champSelect = api.get('/lol-champ-select/v1/session')
                if champSelect.status_code == 404:
                    pass
                else:
                    champSelect = api.get('/lol-champ-select/v1/session').json()
                    current_summoner = api.get('/lol-summoner/v1/current-summoner').json()
                    summoner = current_summoner["displayName"]
                    platform_id = api.get('/lol-chat/v1/me').json()
                    chatId = champSelect["chatDetails"]["chatRoomName"]
                    platformId = platform_id["platformId"].lower()
                    fixedId = "@champ-select." + platformId + '.'
                    lobbyChatId = chatId.replace("@champ-select.", fixedId)
                    if "@sec" in chatId:
                        lobbyChatId = lobbyChatId.replace("@sec.", fixedId)
                    cellId = champSelect["localPlayerCellId"]
                    actions = champSelect["actions"][0]
                    for ac in actions:
                        actorCellId = ac["actorCellId"]
                        actionId = ac["id"]
                        if cellId == actorCellId:
                            break

                    if self.lane != "None":
                        api.post('/lol-chat/v1/conversations/' + lobbyChatId + '/messages', {
                            "body": self.lane,
                            "fromSummonerId" : current_summoner["summonerId"],
                            "isHistorical" : False,
                            "type" : "chat"
                        })
                        sleep(1)
                    else:
                        pass

                    if cellId == actorCellId:
                        instalock = api.patch('/lol-champ-select/v1/session/actions/{}'.format(actionId), json={"championId": champId, "completed": True})
                        if instalock.status_code == 204:
                            Notification(
                                title="IRF Tools",
                                description = "{} has been picked.".format(championName),
                                duration = 3,
                            ).send()
                    else:
                        pass
            else:
                pass
        else:
            Notification(
                title="IRF Tools",
                description = "Invalid Champion Name.".format(championName),
                duration = 3,
            ).send()
    # def instalocker_draft(self):
    #     self.banned = False
    #     self.picked = False
    #     banChampion = self.ui.championBan.text().lower().capitalize().replace("'", "")
    #     championName = self.ui.championLockDraft.text().lower().capitalize().replace("'", "")
    #     if championName == "Reksai":
    #         championName = "RekSai"
    #     if banChampion == "Reksai":
    #         banChampion == "RekSai"
        
    #     print(banChampion)
    #     print(championName)
    #     ban_champId = self.champion_name_to_id(banChampion)
    #     champId = self.champion_name_to_id(championName)
    #     data = req.get('https://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/champion/{}.json'.format(championName))
    #     if data.status_code == 200:
    #         Notification(
    #             title="IRF Tools",
    #             description = "Instalocking {}, and banning {}.".format(championName, banChampion),
    #             duration = 3,
    #         ).send()
    #         while self.ui.instalockManagerD.currentIndex() == 1:
    #             sleep(0.6)
    #             champSelect = api.get('/lol-champ-select/v1/session')
    #             if champSelect.status_code == 404:
    #                 pass
    #             else:
    #                 champSelect = api.get('/lol-champ-select/v1/session').json()
    #                 cellId = champSelect["localPlayerCellId"]
    #                 actions = champSelect["actions"][0]
    #                 for ac in actions:
    #                     actorCellId = ac["actorCellId"]
    #                     if cellId == actorCellId:
    #                         actorCellId = ac["actorCellId"]
    #                         action = ac["id"]
    #                         pick_or_ban = ac["type"]
    #                         break
    #                 print(actions)
    #                 if cellId == actorCellId and pick_or_ban == "ban":
    #                     ban_champion = api.patch('/lol-champ-select/v1/session/actions/{}'.format(action), json={"championId": ban_champId, "completed": True})
    #                     if ban_champion.status_code == 204:
    #                         Notification(
    #                             title="IRF Tools",
    #                             description = "{} has been banned.".format(banChampion),
    #                             duration = 3,
    #                         ).send()
    #                         self.banned = True
    #                         self.picked = False
    #                 elif cellId == actorCellId and self.banned == True:
    #                     pick_champion = api.patch('/lol-champ-select/v1/session/actions/{}'.format(action), json={"championId": champId, "completed": True})
    #                     if pick_champion.status_code == 204:
    #                         Notification(
    #                             title="IRF Tools",
    #                             description = "{} has been picked.".format(championName),
    #                             duration = 3,
    #                         ).send()
    #                         self.picked = True
    #                         self.banned = False
    #                     else:
    #                         pass
    #         else:
    #             pass
    #     elif data.status_code == 403:
    #         Notification(
    #             title="IRF Tools",
    #             description = "Invalid Champion Name.".format(championName, banChampion),
    #             duration = 3,
    #         ).send()
    #     else:
    #         Notification(
    #             title="IRF Tools",
    #             description = "Unexpected Error.".format(championName, banChampion),
    #             duration = 3,
    #         ).send()

    
    def auto_accept(self):
        confirmbox = pymsgbox.alert(title='IRF Tools', text='Auto Accept enabled.', button='OK')
        while self.ui.autoAcceptManager.currentIndex() == 1:
            sleep(1.2)
            api.post('/lol-matchmaking/v1/ready-check/accept')

    def auto_play_again(self):
        confirmbox = pymsgbox.alert(title='IRF Tools', text='Coming Soon', button='OK')
        Notification(
            title="IRF Tools",
            description = "Coming Soon...",
            duration = 3,
        ).send()

    def remove_friends(self):
        AllFriends = api.get('/lol-chat/v1/friends').json()
        countFriends = len(AllFriends)
        #confirmbox = confirm(text='Are you sure? this will delete ' + str(friends) + ' friends.', title='IRF Tool', buttons=['Yes', 'Cancel'])
        confirmbox = pymsgbox.confirm(text='Are you sure? this will delete ' +  str(countFriends) + ' friends.', title='IRF Tool', buttons=['Yes', 'No'])
        if confirmbox == "Yes":
            threading.Thread(target=friends.RemoveAllFriends).start()
            sleep(1)
            self.refresh_friends()
        else:
            pass
    def refresh_friends(self):
        friend_list = []
        all_friends = api.get('/lol-chat/v1/friends').json()
        countFriends = len(all_friends)
        for i in range(countFriends):
            if len(all_friends[i]["name"]) <= 16 and len(all_friends[i]["name"]) > 3:
                self.ui.friendList.clear()
                friend_list.append(all_friends[i]["name"])
        friend_list.sort()
            
        for i in range(len(friend_list)):
            self.ui.friendList.addItem(friend_list[i])
    
    def hide_lanes(self):
        if self.ui.laneSelector.currentIndex() == 0:
            self.ui.previousLaneBtn.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.nextLaneBtn.setCursor(QCursor(Qt.PointingHandCursor))
        elif self.ui.laneSelector.currentIndex() == 5:
            self.ui.nextLaneBtn.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.previousLaneBtn.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.ui.previousLaneBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.nextLaneBtn.setCursor(QCursor(Qt.PointingHandCursor))

    def hide_division(self):
        if self.ui.eloManager.currentIndex() == 9:
            self.ui.divisionInput.hide()
            self.ui.changeEloBtn.setGeometry(QRect(40, 190, 131, 31))
            self.ui.nextEloBtn.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.previousEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
        elif self.ui.eloManager.currentIndex() == 0:
            self.ui.divisionInput.hide()
            self.ui.changeEloBtn.setGeometry(QRect(40, 190, 131, 31))
            self.ui.previousEloBtn.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.nextEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
        elif self.ui.eloManager.currentIndex() == 8:
            self.ui.divisionInput.hide()
            self.ui.previousEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.nextEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.changeEloBtn.setGeometry(QRect(40, 190, 131, 31))
            
        elif self.ui.eloManager.currentIndex() == 7:
            self.ui.divisionInput.hide()
            self.ui.previousEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.nextEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.changeEloBtn.setGeometry(QRect(40, 190, 131, 31))
        else:
            self.ui.divisionInput.show()
            self.ui.previousEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.nextEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.changeEloBtn.setGeometry(QRect(40, 213, 131, 31))
        
    def hide_availability(self):
        if self.ui.availabilityManager.currentIndex() == 0:
            self.ui.previousAvailability.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.nextAvailability.setCursor(QCursor(Qt.PointingHandCursor))
        elif self.ui.availabilityManager.currentIndex() == 3:
            self.ui.nextAvailability.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.previousAvailability.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.ui.previousEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.nextEloBtn.setCursor(QCursor(Qt.PointingHandCursor))

    def hide_queue(self):
        if self.ui.queueManager.currentIndex() == 0:
            self.ui.previousQueueBtn.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.nextQueueBtn.setCursor(QCursor(Qt.PointingHandCursor))
        elif self.ui.queueManager.currentIndex() == 3:
            self.ui.nextQueueBtn.setCursor(QCursor(Qt.ArrowCursor))
            self.ui.previousQueueBtn.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.ui.nextQueueBtn.setCursor(QCursor(Qt.PointingHandCursor))
            self.ui.nextQueueBtn.setCursor(QCursor(Qt.PointingHandCursor))

    def refresh(self):
        data = api.get('/lol-chat/v1/me').json()
        self.nickname = data["name"]
        self.iconId = data["icon"]
        iconUrl = "https://cdn.communitydragon.org/latest/profile-icon/" + str(self.iconId)
        icon = QImage()
        icon.loadFromData(req.get(iconUrl).content)
        self.ui.usernameLabel.setText(self.nickname)
        pixmap = QPixmap(icon)
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.ui.summonerIcon.setPixmap(pixmap)
        self.ui.summonerIcon.setScaledContents(True)
        self.ui.summonerIcon.show()
        self.availability()
    
    def availability(self):
        availabilitys = ['online', 'offline', 'mobile']
        data = api.get('/lol-chat/v1/me').json()
        if data["availability"] == availabilitys[0]:
            onlineImg = QImage()
            onlineImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/online.png").content)
            onlinePixmap = QPixmap(onlineImg)
            onlinePixmap = onlinePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
            self.ui.availabilityImg.setPixmap(onlinePixmap)
            self.ui.availabilityImg.setScaledContents(True)
            self.ui.availabilityImg.show()
        elif data["availability"] == availabilitys[1]:
            offlineImg = QImage()
            offlineImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/offline.png").content)
            offlinePixmap = QPixmap(offlineImg)
            offlinePixmap = offlinePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
            self.ui.availabilityImg.setPixmap(offlinePixmap)
            self.ui.availabilityImg.setScaledContents(True)
            self.ui.availabilityImg.show()
        elif data["availability"] == availabilitys[2]:
            mobileImg = QImage()
            mobileImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/mobile.png").content)
            mobilePixmap = QPixmap(mobileImg)
            mobilePixmap = mobilePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
            self.ui.availabilityImg.setPixmap(mobilePixmap)
            self.ui.availabilityImg.setScaledContents(True)
            self.ui.availabilityImg.show()
        else:
            onlineImg = QImage()
            onlineImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/online.png").content)
            onlinePixmap = QPixmap(onlineImg)
            onlinePixmap = onlinePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
            self.ui.availabilityImg.setPixmap(onlinePixmap)
            self.ui.availabilityImg.setScaledContents(True)
            self.ui.availabilityImg.show()
            
    def closeEvent(self, event):
        self.ui.autoAcceptManager.setCurrentIndex(0)
        self.ui.instalockManagerB.setCurrentIndex(0)
        # self.ui.instalockManagerD.setCurrentIndex(0)
        self.ui.autoPlayAgainManager.setCurrentIndex(0)
        self.ui.instaQuitManager.setCurrentIndex(0)
        self.ui.runesManager.setCurrentIndex(0)
        self.ui.multiSearchManager.setCurrentIndex(0)
        event.accept()
    def mousePressEvent(self, event) -> None:
        self.dragPos = event.globalPos()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
