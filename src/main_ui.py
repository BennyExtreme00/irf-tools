from PySide2.QtCore import *
from PySide2 import QtCore
from PySide2.QtCore import Signal
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import api
import requests as req
import icons_rc

api = api.LCU()


class Ui_IRFTool(object):
    def setupUi(self, IRFTool):
        if not IRFTool.objectName():
            IRFTool.setObjectName(u"IRFTool")
        IRFTool.resize(980, 648)
        IRFTool.setMinimumSize(QSize(726, 598))
        IRFTool.setMaximumSize(QSize(980, 648))
        IRFTool.setCursor(QCursor(Qt.ArrowCursor))
        IRFTool.setStyleSheet(u"")
        self.centralwidget = QWidget(IRFTool)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(980, 648))
        self.centralwidget.setMaximumSize(QSize(980, 648))
        self.centralwidget.setStyleSheet(u"")
        self.leftBar = QFrame(self.centralwidget)
        self.leftBar.setObjectName(u"leftBar")
        self.leftBar.setGeometry(QRect(10, 10, 231, 631))
        self.leftBar.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.leftBar.setFrameShape(QFrame.StyledPanel)
        self.leftBar.setFrameShadow(QFrame.Raised)
        self.titleLabel = QLabel(self.leftBar)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 140, 221, 51))
        self.titleLabel.setStyleSheet(u"color: rgb(27, 139, 208);\n"
"font: 87 20pt \"Arial Black\";\n"
"")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.homeBtn = QPushButton(self.leftBar)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setGeometry(QRect(0, 190, 221, 51))
        self.homeBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"	border-radius: 0px;\n"
"	text-align: left;\n"
"	font: 87 15pt \"Segoe UI Black\";\n"
"	color: rgb(16, 104, 186);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(22, 33, 63, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(16, 24, 45);\n"
"}")
        self.instalockBtn = QPushButton(self.leftBar)
        self.instalockBtn.setObjectName(u"instalockBtn")
        self.instalockBtn.setGeometry(QRect(0, 290, 221, 51))
        self.instalockBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"	border-radius: 0px;\n"
"	text-align: left;\n"
"	font: 87 15pt \"Segoe UI Black\";\n"
"	color: rgb(16, 104, 186);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(22, 33, 63, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(16, 24, 45);\n"
"}")
        self.logo = QFrame(self.leftBar)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(0, 20, 221, 121))
        self.logo.setStyleSheet(u"image: url(:/icons/logo.jpg);\n"
"")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.exploitsBtn = QPushButton(self.leftBar)
        self.exploitsBtn.setObjectName(u"exploitsBtn")
        self.exploitsBtn.setGeometry(QRect(0, 240, 221, 51))
        self.exploitsBtn.setStyleSheet(u"QPushButton {\n"
"\n"
"	border-radius: 0px;\n"
"	text-align: left;\n"
"	font: 87 15pt \"Segoe UI Black\";\n"
"	color: rgb(16, 104, 186);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(22, 33, 63, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(16, 24, 45);\n"
"}")
        self.homeFrame = QFrame(self.leftBar)
        self.homeFrame.setObjectName(u"homeFrame")
        self.homeFrame.setGeometry(QRect(180, 200, 31, 31))
        self.homeFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.homeFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/icons/home5.png);")
        self.homeFrame.setFrameShape(QFrame.StyledPanel)
        self.homeFrame.setFrameShadow(QFrame.Raised)
        self.exploitsFrame = QFrame(self.leftBar)
        self.exploitsFrame.setObjectName(u"exploitsFrame")
        self.exploitsFrame.setGeometry(QRect(180, 250, 31, 31))
        self.exploitsFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/icons/infinity2.png);")
        self.exploitsFrame.setFrameShape(QFrame.StyledPanel)
        self.exploitsFrame.setFrameShadow(QFrame.Raised)
        self.miscBtn = QPushButton(self.leftBar)
        self.miscBtn.setObjectName(u"miscBtn")
        self.miscBtn.setGeometry(QRect(0, 390, 221, 51))
        self.miscBtn.setStyleSheet(u"QPushButton {\n"
"	border-radius: 0px;\n"
"	text-align: left;\n"
"	font: 87 15pt \"Segoe UI Black\";\n"
"	color: rgb(16, 104, 186);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(22, 33, 63, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(16, 24, 45);\n"
"}")
        self.miscFrame = QFrame(self.leftBar)
        self.miscFrame.setObjectName(u"miscFrame")
        self.miscFrame.setGeometry(QRect(180, 400, 31, 31))
        self.miscFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/icons/layers.png);")
        self.miscFrame.setFrameShape(QFrame.StyledPanel)
        self.miscFrame.setFrameShadow(QFrame.Raised)
        self.instalockFrame = QFrame(self.leftBar)
        self.instalockFrame.setObjectName(u"instalockFrame")
        self.instalockFrame.setGeometry(QRect(180, 300, 31, 31))
        self.instalockFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/icons/lock2.png);\n"
"")
        self.instalockFrame.setFrameShape(QFrame.StyledPanel)
        self.instalockFrame.setFrameShadow(QFrame.Raised)
        self.topbar2 = QFrame(self.leftBar)
        self.topbar2.setObjectName(u"topbar2")
        self.topbar2.setGeometry(QRect(0, 0, 221, 21))
        self.topbar2.setFrameShape(QFrame.StyledPanel)
        self.topbar2.setFrameShadow(QFrame.Raised)
        self.friendsPgBtn = QPushButton(self.leftBar)
        self.friendsPgBtn.setGeometry(QtCore.QRect(0, 340, 221, 51))
        self.friendsPgBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 0px;\n"
"    text-align: left;\n"
"    font: 87 15pt \"Segoe UI Black\";\n"
"    color: rgb(16, 104, 186);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(22, 33, 63, 180);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(16, 24, 45);\n"
"}")
        self.friendsPgBtn.setObjectName("friendsPgBtn")
        self.friendsIconFrame = QFrame(self.leftBar)
        self.friendsIconFrame.setGeometry(QtCore.QRect(180, 350, 31, 31))
        self.friendsIconFrame.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/icons/user3.png);\n"
"")
        self.friendsIconFrame.setFrameShape(QFrame.StyledPanel)
        self.friendsIconFrame.setFrameShadow(QFrame.Raised)
        self.friendsIconFrame.setObjectName("friendsIconFrame")
        self.contentBg = QFrame(self.centralwidget)
        self.contentBg.setObjectName(u"contentBg")
        self.contentBg.setGeometry(QRect(230, 10, 741, 631))
        self.contentBg.setStyleSheet(u"background-color: rgb(46, 51, 72);\n"
"border-radius: 10px;")
        self.contentBg.setFrameShape(QFrame.StyledPanel)
        self.contentBg.setFrameShadow(QFrame.Raised)
        self.topBar = QFrame(self.contentBg)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setGeometry(QRect(-220, 0, 961, 21))
        self.topBar.setStyleSheet(u"background-color: rgb(19, 28, 53);")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.invisibleFrame = QFrame(self.topBar)
        self.invisibleFrame.setObjectName(u"invisibleFrame")
        self.invisibleFrame.setGeometry(QRect(950, 10, 120, 80))
        self.invisibleFrame.setFrameShape(QFrame.StyledPanel)
        self.invisibleFrame.setFrameShadow(QFrame.Raised)
        self.closeBtn = QPushButton(self.topBar)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(935, 2, 16, 16))
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setStyleSheet(u"border: none;\n"
"image: url(:/icons/close-btn1.png);\n"
"color: rgb(27, 139, 208);")
        self.minimizeBtn = QPushButton(self.topBar)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setGeometry(QRect(915, 2, 16, 16))
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeBtn.setStyleSheet(u"border: none;\n"
"image: url(:/icons/minimize-btn.png);\n"
"color: rgb(27, 139, 208);")
        self.removeBotBorder = QFrame(self.contentBg)
        self.removeBotBorder.setObjectName(u"removeBotBorder")
        self.removeBotBorder.setGeometry(QRect(0, 619, 120, 71))
        self.removeBotBorder.setFrameShape(QFrame.StyledPanel)
        self.removeBotBorder.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.contentBg)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 30, 721, 591))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.stackedWidget.addWidget(self.homePage)
        self.homeBg = QFrame(self.homePage)
        self.homeBg.setObjectName(u"homeBg")
        self.homeBg.setGeometry(QRect(0, 0, 731, 591))
        self.homeBg.setStyleSheet(u"background-color: rgb(46, 51, 72);")
        self.homeBg.setFrameShape(QFrame.StyledPanel)
        self.homeBg.setFrameShadow(QFrame.Raised)
        self.summonerProfile = QFrame(self.homeBg)
        self.summonerProfile.setObjectName(u"summonerProfile")
        self.summonerProfile.setGeometry(QRect(20, 23, 231, 291))
        self.summonerProfile.setStyleSheet(u"\n"
"border-radius: 8px;\n"
"background-color: rgb(19, 28, 53);")
        self.summonerProfile.setFrameShape(QFrame.StyledPanel)
        self.summonerProfile.setFrameShadow(QFrame.Raised)
        self.usernameLabel = QLabel(self.summonerProfile)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(0, 0, 231, 41))
        self.usernameLabel.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(28, 146, 214);\n"
"background-color: rgba(19, 28, 53, 150);")
        self.usernameLabel.setAlignment(Qt.AlignCenter)
        self.refreshBtn = QPushButton(self.summonerProfile)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setGeometry(QRect(40, 240, 151, 41))
        self.refreshBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.summonerIcon = QLabel(self.summonerProfile)
        self.summonerIcon.setObjectName(u"summonerIcon")
        self.summonerIcon.setGeometry(QRect(30, 40, 171, 161))
        self.summonerIcon.setStyleSheet(u"background-color: rgba(19, 28, 53, 150);")
        self.summonerIcon.setAlignment(Qt.AlignCenter)
        self.activityLabel = QLabel(self.summonerProfile)
        self.activityLabel.setObjectName(u"activityLabel")
        self.activityLabel.setGeometry(QRect(50, 213, 131, 20))
        self.activityLabel.setAlignment(Qt.AlignCenter)
        self.availabilityImg = QLabel(self.summonerProfile)
        self.availabilityImg.setObjectName(u"availabilityImg")
        self.availabilityImg.setGeometry(QRect(0, 214, 231, 21))
        self.availabilityImg.setCursor(QCursor(Qt.ArrowCursor))
        self.availabilityImg.setAlignment(Qt.AlignCenter)
        self.summonerElo = QFrame(self.homeBg)
        self.summonerElo.setObjectName(u"summonerElo")
        self.summonerElo.setGeometry(QRect(29, 325, 211, 251))
        self.summonerElo.setStyleSheet(u"\n"
"border-radius: 8px;\n"
"background-color: rgb(19, 28, 53);")
        self.summonerElo.setFrameShape(QFrame.StyledPanel)
        self.summonerElo.setFrameShadow(QFrame.Raised)
        self.changeEloBtn = QPushButton(self.summonerElo)
        self.changeEloBtn.setObjectName(u"changeEloBtn")
        self.changeEloBtn.setGeometry(QRect(40, 213, 131, 31))
        self.changeEloBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 8pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.previousEloBtn = QPushButton(self.summonerElo)
        self.previousEloBtn.setObjectName(u"previousEloBtn")
        self.previousEloBtn.setGeometry(QRect(20, 90, 16, 16))
        self.previousEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.previousEloBtn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/leftarrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"}")
        self.nextEloBtn = QPushButton(self.summonerElo)
        self.nextEloBtn.setObjectName(u"nextEloBtn")
        self.nextEloBtn.setGeometry(QRect(173, 90, 16, 16))
        self.nextEloBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextEloBtn.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icons/right-arrow.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"}")
        self.divisionInput = QLineEdit(self.summonerElo)
        self.divisionInput.setObjectName(u"divisionInput")
        self.divisionInput.setGeometry(QRect(50, 189, 113, 21))
        self.divisionInput.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
"color: rgb(28, 146, 214);\n"
"padding-left: 6px;\n"
"")
        self.rankChangerLabel = QLabel(self.summonerElo)
        self.rankChangerLabel.setObjectName(u"rankChangerLabel")
        self.rankChangerLabel.setGeometry(QRect(0, 10, 211, 21))
        self.rankChangerLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.rankChangerLabel.setAlignment(Qt.AlignCenter)
        self.eloManager = QStackedWidget(self.summonerElo)
        self.eloManager.setObjectName(u"eloManager")
        self.eloManager.setGeometry(QRect(50, 39, 111, 101))
        self.unranked = QWidget()
        self.unranked.setObjectName(u"UNRANKED")
        self.unrankedImg = QLabel(self.unranked)
        self.unrankedImg.setObjectName(u"unrankedImg")
        self.unrankedImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.unranked)
        self.iron = QWidget()
        self.iron.setObjectName(u"IRON")
        self.ironImg = QLabel(self.iron)
        self.ironImg.setObjectName(u"ironImg")
        self.ironImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.iron)
        self.bronze = QWidget()
        self.bronze.setObjectName(u"BRONZE")
        self.bronzeImg = QLabel(self.bronze)
        self.bronzeImg.setObjectName(u"bronzeImg")
        self.bronzeImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.bronze)
        self.silver = QWidget()
        self.silver.setObjectName(u"SILVER")
        self.silverImg = QLabel(self.silver)
        self.silverImg.setObjectName(u"silverImg")
        self.silverImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.silver)
        self.gold = QWidget()
        self.gold.setObjectName(u"GOLD")
        self.goldImg = QLabel(self.gold)
        self.goldImg.setObjectName(u"goldImg")
        self.goldImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.gold)
        self.platinum = QWidget()
        self.platinum.setObjectName(u"PLATINUM")
        self.platinumImg = QLabel(self.platinum)
        self.platinumImg.setObjectName(u"platinumImg")
        self.platinumImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.platinum)
        self.diamond = QWidget()
        self.diamond.setObjectName(u"DIAMOND")
        self.diamondImg = QLabel(self.diamond)
        self.diamondImg.setObjectName(u"diamondImg")
        self.diamondImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.diamond)
        self.master = QWidget()
        self.master.setObjectName(u"MASTER")
        self.masterImg = QLabel(self.master)
        self.masterImg.setObjectName(u"masterImg")
        self.masterImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.master)
        self.grandmaster = QWidget()
        self.grandmaster.setObjectName(u"GRANDMASTER")
        self.grandmasterImg = QLabel(self.grandmaster)
        self.grandmasterImg.setObjectName(u"grandmasterImg")
        self.grandmasterImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.grandmaster)
        self.challenger = QWidget()
        self.challenger.setObjectName(u"CHALLENGER")
        self.challengerImg = QLabel(self.challenger)
        self.challengerImg.setObjectName(u"challengerImg")
        self.challengerImg.setGeometry(QRect(0, 0, 111, 101))
        self.eloManager.addWidget(self.challenger)
        self.queueManager = QStackedWidget(self.summonerElo)
        self.queueManager.setObjectName(u"queueManager")
        self.queueManager.setGeometry(QRect(60, 150, 101, 31))
        self.soloQ = QWidget()
        self.soloQ.setObjectName(u"RANKED_SOLO_5X5")
        self.soloqLabel = QLabel(self.soloQ)
        self.soloqLabel.setObjectName(u"soloqLabel")
        self.soloqLabel.setGeometry(QRect(-60, 0, 211, 41))
        self.soloqLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.soloqLabel.setAlignment(Qt.AlignCenter)
        self.queueManager.addWidget(self.soloQ)
        self.flexQ = QWidget()
        self.flexQ.setObjectName(u"RANKED_FLEX_SR")
        self.flexqLabel = QLabel(self.flexQ)
        self.flexqLabel.setObjectName(u"flexqLabel")
        self.flexqLabel.setGeometry(QRect(-60, -1, 211, 41))
        self.flexqLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.flexqLabel.setAlignment(Qt.AlignCenter)
        self.queueManager.addWidget(self.flexQ)
        self.flex3x3 = QWidget()
        self.flex3x3.setObjectName(u"RANKED_FLEX_TT")
        self.flex3x3Q = QLabel(self.flex3x3)
        self.flex3x3Q.setObjectName(u"flex3x3Q")
        self.flex3x3Q.setGeometry(QRect(-60, -1, 211, 41))
        self.flex3x3Q.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.flex3x3Q.setAlignment(Qt.AlignCenter)
        self.queueManager.addWidget(self.flex3x3)
        self.tft = QWidget()
        self.tft.setObjectName(u"RANKED_TFT")
        self.tftLabel = QLabel(self.tft)
        self.tftLabel.setObjectName(u"tftLabel")
        self.tftLabel.setGeometry(QRect(-60, -1, 211, 41))
        self.tftLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.tftLabel.setAlignment(Qt.AlignCenter)
        self.queueManager.addWidget(self.tft)
        self.previousQueueBtn = QPushButton(self.summonerElo)
        self.previousQueueBtn.setObjectName(u"previousQueueBtn")
        self.previousQueueBtn.setGeometry(QRect(50, 163, 16, 16))
        self.previousQueueBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.previousQueueBtn.setStyleSheet(u"image: url(:/icons/leftarrow.png);")
        self.nextQueueBtn = QPushButton(self.summonerElo)
        self.nextQueueBtn.setObjectName(u"nextQueueBtn")
        self.nextQueueBtn.setGeometry(QRect(145, 163, 16, 16))
        self.nextQueueBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextQueueBtn.setStyleSheet(u"image: url(:/icons/right-arrow.png);")
        self.statusFrame = QFrame(self.homeBg)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setGeometry(QRect(257, 30, 461, 271))
        self.statusFrame.setStyleSheet(u"\n"
"border-radius: 8px;\n"
"background-color: rgb(19, 28, 53);")
        self.statusFrame.setFrameShape(QFrame.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Raised)
        self.statusInput = QTextEdit(self.statusFrame)
        self.statusInput.setObjectName(u"statusInput")
        self.statusInput.setGeometry(QRect(13, 40, 431, 201))
        self.statusInput.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
"color: rgb(28, 146, 214);\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"")
        self.statusChangerLabel = QLabel(self.statusFrame)
        self.statusChangerLabel.setObjectName(u"statusChangerLabel")
        self.statusChangerLabel.setGeometry(QRect(0, 10, 461, 20))
        self.statusChangerLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.statusChangerLabel.setAlignment(Qt.AlignCenter)
        self.statusUpdateBtn = QPushButton(self.statusFrame)
        self.statusUpdateBtn.setObjectName(u"statusUpdateBtn")
        self.statusUpdateBtn.setGeometry(QRect(160, 243, 141, 21))
        self.statusUpdateBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 8pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.iconFrame = QFrame(self.homeBg)
        self.iconFrame.setObjectName(u"iconFrame")
        self.iconFrame.setGeometry(QRect(262, 309, 221, 131))
        self.iconFrame.setStyleSheet(u"\n"
"border-radius: 8px;\n"
"background-color: rgb(19, 28, 53);")
        self.iconFrame.setFrameShape(QFrame.StyledPanel)
        self.iconFrame.setFrameShadow(QFrame.Raised)
        self.iconLabel = QLabel(self.iconFrame)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setGeometry(QRect(0, 20, 221, 21))
        self.iconLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.updateIconBtn = QPushButton(self.iconFrame)
        self.updateIconBtn.setObjectName(u"updateIconBtn")
        self.updateIconBtn.setGeometry(QRect(70, 90, 81, 31))
        self.updateIconBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 8pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.iconInput = QLineEdit(self.iconFrame)
        self.iconInput.setObjectName(u"iconInput")
        self.iconInput.setGeometry(QRect(50, 50, 121, 31))
        self.iconInput.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
"color: rgb(28, 146, 214);\n"
"padding-left: 6px;\n"
"")
        self.backgroundFrame = QFrame(self.homeBg)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setGeometry(QRect(489, 309, 221, 131))
        self.backgroundFrame.setStyleSheet(u"\n"
"border-radius: 8px;\n"
"background-color: rgb(19, 28, 53);")
        self.backgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Raised)
        self.backgroundLabel = QLabel(self.backgroundFrame)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 20, 221, 20))
        self.backgroundLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.backgroundLabel.setAlignment(Qt.AlignCenter)
        self.updateBackgroundBtn = QPushButton(self.backgroundFrame)
        self.updateBackgroundBtn.setObjectName(u"updateBackgroundBtn")
        self.updateBackgroundBtn.setGeometry(QRect(70, 90, 81, 31))
        self.updateBackgroundBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 8pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.backgroundInput = QLineEdit(self.backgroundFrame)
        self.backgroundInput.setObjectName(u"backgroundInput")
        self.backgroundInput.setGeometry(QRect(50, 50, 121, 31))
        self.backgroundInput.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
"color: rgb(28, 146, 214);\n"
"padding-left: 6px;\n"
"")
        self.availabilityFrame = QFrame(self.homeBg)
        self.availabilityFrame.setObjectName(u"availabilityFrame")
        self.availabilityFrame.setGeometry(QRect(262, 445, 221, 131))
        self.availabilityFrame.setStyleSheet(u"\n"
"border-radius: 8px;\n"
"background-color: rgb(19, 28, 53);")
        self.availabilityFrame.setFrameShape(QFrame.StyledPanel)
        self.availabilityFrame.setFrameShadow(QFrame.Raised)
        self.availabilityLabel = QLabel(self.availabilityFrame)
        self.availabilityLabel.setObjectName(u"availabilityLabel")
        self.availabilityLabel.setGeometry(QRect(0, 20, 221, 21))
        self.availabilityLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.availabilityLabel.setAlignment(Qt.AlignCenter)
        self.availabilityManager = QStackedWidget(self.availabilityFrame)
        self.availabilityManager.setObjectName(u"availabilityManager")
        self.availabilityManager.setGeometry(QRect(70, 50, 81, 41))
        self.online = QWidget()
        self.online.setObjectName(u"online")
        self.onlineLabel = QLabel(self.online)
        self.onlineLabel.setObjectName(u"onlineLabel")
        self.onlineLabel.setGeometry(QRect(0, 0, 81, 41))
        self.onlineLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.onlineLabel.setAlignment(Qt.AlignCenter)
        self.availabilityManager.addWidget(self.online)
        self.away = QWidget()
        self.away.setObjectName(u"away")
        self.awayLabel = QLabel(self.away)
        self.awayLabel.setObjectName(u"awayLabel")
        self.awayLabel.setGeometry(QRect(0, 0, 81, 41))
        self.awayLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.awayLabel.setAlignment(Qt.AlignCenter)
        self.availabilityManager.addWidget(self.away)
        self.offline = QWidget()
        self.offline.setObjectName(u"offline")
        self.offlineLabel = QLabel(self.offline)
        self.offlineLabel.setObjectName(u"offlineLabel")
        self.offlineLabel.setGeometry(QRect(0, 0, 81, 41))
        self.offlineLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.offlineLabel.setAlignment(Qt.AlignCenter)
        self.availabilityManager.addWidget(self.offline)
        self.mobile = QWidget()
        self.mobile.setObjectName(u"mobile")
        self.mobileLabel = QLabel(self.mobile)
        self.mobileLabel.setObjectName(u"mobileLabel")
        self.mobileLabel.setGeometry(QRect(0, 0, 81, 41))
        self.mobileLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.mobileLabel.setAlignment(Qt.AlignCenter)
        self.availabilityManager.addWidget(self.mobile)
        self.previousAvailability = QPushButton(self.availabilityFrame)
        self.previousAvailability.setObjectName(u"previousAvailability")
        self.previousAvailability.setGeometry(QRect(60, 63, 20, 16))
        self.previousAvailability.setCursor(QCursor(Qt.PointingHandCursor))
        self.previousAvailability.setStyleSheet(u"image: url(:/icons/leftarrow.png);")
        self.nextAvailability = QPushButton(self.availabilityFrame)
        self.nextAvailability.setObjectName(u"nextAvailability")
        self.nextAvailability.setGeometry(QRect(140, 63, 16, 16))
        self.nextAvailability.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextAvailability.setStyleSheet(u"image: url(:/icons/right-arrow.png);")
        self.updateAvailabilityBtn = QPushButton(self.availabilityFrame)
        self.updateAvailabilityBtn.setObjectName(u"updateAvailabilityBtn")
        self.updateAvailabilityBtn.setGeometry(QRect(70, 90, 81, 31))
        self.updateAvailabilityBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 8pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.lobbyFrame = QFrame(self.homeBg)
        self.lobbyFrame.setObjectName(u"lobbyFrame")
        self.lobbyFrame.setGeometry(QRect(489, 445, 221, 131))
        self.lobbyFrame.setStyleSheet(u"\n"
"border-radius: 8px;\n"
"background-color: rgb(19, 28, 53);")
        self.lobbyFrame.setFrameShape(QFrame.StyledPanel)
        self.lobbyFrame.setFrameShadow(QFrame.Raised)
        self.lobbyLabel = QLabel(self.lobbyFrame)
        self.lobbyLabel.setObjectName(u"lobbyLabel")
        self.lobbyLabel.setGeometry(QRect(0, 20, 221, 21))
        self.lobbyLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.lobbyLabel.setAlignment(Qt.AlignCenter)
        self.queueInput = QLineEdit(self.lobbyFrame)
        self.queueInput.setObjectName(u"queueInput")
        self.queueInput.setGeometry(QRect(50, 50, 121, 31))
        self.queueInput.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
"color: rgb(28, 146, 214);\n"
"padding-left: 6px;\n"
"")
        self.createLobbyBtn = QPushButton(self.lobbyFrame)
        self.createLobbyBtn.setObjectName(u"createLobbyBtn")
        self.createLobbyBtn.setGeometry(QRect(70, 90, 81, 31))
        self.createLobbyBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 8pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"}\n"   
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.pushButton = QPushButton(self.lobbyFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(201, 20, 20, 16))
        self.updateBackgroundBtn.setText(QCoreApplication.translate("IRFTool", u"UPDATE", None))
        self.backgroundInput.setPlaceholderText(QCoreApplication.translate("IRFTool", u"4001", None))
        self.updateIconBtn.setText(QCoreApplication.translate("IRFTool", u"UPDATE", None))
        self.iconInput.setPlaceholderText(QCoreApplication.translate("IRFTool", u"29", None))
        self.retranslateUi(IRFTool)
        self.exploitsPage = QWidget()
        self.exploitsPage.setObjectName(u"exploitsPage")
        self.stackedWidget.addWidget(self.exploitsPage)
        self.backgroundExploits = QFrame(self.exploitsPage)
        self.backgroundExploits.setObjectName(u"backgroundExploits")
        self.backgroundExploits.setGeometry(QRect(-10, -10, 831, 641))
        self.backgroundExploits.setStyleSheet(u"background-color: rgb(46, 52, 72);")
        self.backgroundExploits.setFrameShape(QFrame.StyledPanel)
        self.backgroundExploits.setFrameShadow(QFrame.Raised)
        self.tristanaBg = QFrame(self.backgroundExploits)
        self.tristanaBg.setObjectName(u"tristanaBg")
        self.tristanaBg.setGeometry(QRect(40, 50, 211, 131))
        self.tristanaBg.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.tristanaBg.setFrameShape(QFrame.StyledPanel)
        self.tristanaBg.setFrameShadow(QFrame.Raised)
        self.tristanaLabel = QLabel(self.tristanaBg)
        self.tristanaLabel.setObjectName(u"tristanaLabel")
        self.tristanaLabel.setGeometry(QRect(0, 10, 211, 20))
        self.tristanaLabel.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(28, 146, 237);")
        self.tristanaLabel.setAlignment(Qt.AlignCenter)
        self.tristanaBtn = QPushButton(self.tristanaBg)
        self.tristanaBtn.setObjectName(u"tristanaBtn")
        self.tristanaBtn.setGeometry(QRect(50, 50, 111, 41))
        self.tristanaBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
#         self.crashChatFrame = QFrame(self.backgroundExploits)
#         self.crashChatFrame.setObjectName(u"crashChatFrame")
#         self.crashChatFrame.setGeometry(QRect(40, 50, 211, 131))
#         self.crashChatFrame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
# "border-radius: 10px;")
#         self.crashChatFrame.setFrameShape(QFrame.StyledPanel)
#         self.crashChatFrame.setFrameShadow(QFrame.Raised)
#         self.chatCrasherLabel = QLabel(self.crashChatFrame)
#         self.chatCrasherLabel.setObjectName(u"chatCrasherLabel")
#         self.chatCrasherLabel.setGeometry(QRect(0, 10, 211, 20))
#         self.chatCrasherLabel.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
# "color: rgb(28, 146, 237);")
#         self.chatCrasherLabel.setAlignment(Qt.AlignCenter)
#         self.crashBtn = QPushButton(self.crashChatFrame)
#         self.crashBtn.setObjectName(u"crashBtn")
#         self.crashBtn.setGeometry(QRect(50, 80, 111, 41))
#         self.crashBtn.setStyleSheet(u"QPushButton {\n"
# "	font: 87 9pt \"Arial Black\";\n"
# "	color: rgb(28, 146, 214);\n"
# "	background-color: rgb(16, 24, 45);\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "	\n"
# "	background-color: rgba(17, 25, 47, 190);\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "	background-color: rgb(16, 24, 45);\n"
# "\n"
# "\n"
# "}")
#         self.inputFriendCrash = QLineEdit(self.crashChatFrame)
#         self.inputFriendCrash.setObjectName(u"inputFriendCrash")
#         self.inputFriendCrash.setGeometry(QRect(40, 40, 131, 31))
#         self.inputFriendCrash.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
# "color: rgb(28, 146, 214);\n"
# "")
#         self.inputFriendCrash.setAlignment(Qt.AlignCenter)
        self.tristanaLabel.setText(QCoreApplication.translate("IRFTool", u"Tristana Riot Girl", None))
        self.tristanaBtn.setText(QCoreApplication.translate("IRFTool", u"GET SKIN", None))
        # self.chatCrasherLabel.setText(QCoreApplication.translate("IRFTool", u"Chat Crasher", None))
        # self.crashBtn.setText(QCoreApplication.translate("IRFTool", u"CRASH", None))
        # self.inputFriendCrash.setPlaceholderText(QCoreApplication.translate("IRFTool", u"Friend Name", None))
        self.instalockPage = QWidget()
        self.instalockPage.setObjectName(u"instalockPage")
        self.stackedWidget.addWidget(self.instalockPage)
        self.instalockBg = QFrame(self.instalockPage)
        self.instalockBg.setObjectName(u"instalockBg")
        self.instalockBg.setGeometry(QRect(-11, -1, 821, 601))
        self.instalockBg.setStyleSheet(u"background-color: rgb(46, 51, 72);")
        self.instalockBg.setFrameShape(QFrame.StyledPanel)
        self.instalockBg.setFrameShadow(QFrame.Raised)
        self.instalockBlindFrame = QFrame(self.instalockBg)
        self.instalockBlindFrame.setObjectName(u"instalockBlindFrame")
        self.instalockBlindFrame.setGeometry(QRect(30, 30, 221, 201))
        self.instalockBlindFrame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.instalockBlindFrame.setFrameShape(QFrame.StyledPanel)
        self.instalockBlindFrame.setFrameShadow(QFrame.Raised)
        self.instaBlindPickLabel = QLabel(self.instalockBlindFrame)
        self.instaBlindPickLabel.setObjectName(u"instaBlindPickLabel")
        self.instaBlindPickLabel.setGeometry(QRect(0, 9, 221, 21))
        self.instaBlindPickLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.instaBlindPickLabel.setAlignment(Qt.AlignCenter)
        self.championLockB = QLineEdit(self.instalockBlindFrame)
        self.championLockB.setObjectName(u"championLockB")
        self.championLockB.setGeometry(QRect(50, 60, 121, 31))
        self.championLockB.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
"color: rgb(28, 146, 214);\n"
"")
        self.championLockB.setAlignment(Qt.AlignCenter)
        self.instalockBlindLabel = QLabel(self.instalockBlindFrame)
        self.instalockBlindLabel.setObjectName(u"instalockBlindLabel")
        self.instalockBlindLabel.setGeometry(QRect(0, 40, 221, 16))
        self.instalockBlindLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.instalockBlindLabel.setAlignment(Qt.AlignCenter)
        self.instalockLaneLabel = QLabel(self.instalockBlindFrame)
        self.instalockLaneLabel.setObjectName(u"instalockLaneLabel")
        self.instalockLaneLabel.setGeometry(QRect(0, 100, 221, 16))
        self.instalockLaneLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.instalockLaneLabel.setAlignment(Qt.AlignCenter)
        self.instalockManagerB = QStackedWidget(self.instalockBlindFrame)
        self.instalockManagerB.setObjectName(u"instalockManagerB")
        self.instalockManagerB.setGeometry(QRect(20, 160, 191, 31))
        self.startBlind = QWidget()
        self.startBlind.setObjectName(u"startBlind")
        self.startBtnB = QPushButton(self.startBlind)
        self.startBtnB.setObjectName(u"startBtnB")
        self.startBtnB.setGeometry(QRect(40, 0, 101, 31))
        self.startBtnB.setStyleSheet(u"QPushButton {\n"
"       font: 87 8pt \"Arial Black\";\n"
"       color: rgb(28, 146, 214);\n"
"       background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"       \n"
"       background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"       background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.instalockManagerB.addWidget(self.startBlind)
        self.stopBLind = QWidget()
        self.stopBLind.setObjectName(u"stopBLind")
        self.stopBtnB = QPushButton(self.stopBLind)
        self.stopBtnB.setObjectName(u"stopBtnB")
        self.stopBtnB.setGeometry(QRect(40, 0, 101, 31))
        self.stopBtnB.setStyleSheet(u"QPushButton {\n"
"       font: 87 8pt \"Arial Black\";\n"
"       color: rgb(28, 146, 214);\n"
"       background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"       \n"
"       background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"       background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.instalockManagerB.addWidget(self.stopBLind)
        self.laneSelector = QStackedWidget(self.instalockBlindFrame)
        self.laneSelector.setObjectName(u"laneSelector")
        self.laneSelector.setGeometry(QRect(69, 120, 141, 31))
        self.none_lane = QWidget()
        self.none_lane.setObjectName(u"none_lane")
        self.noneLabel = QLabel(self.none_lane)
        self.noneLabel.setObjectName(u"noneLabel")
        self.noneLabel.setGeometry(QRect(10, 0, 71, 31))
        self.noneLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.noneLabel.setAlignment(Qt.AlignCenter)
        self.laneSelector.addWidget(self.none_lane)
        self.toplane = QWidget()
        self.toplane.setObjectName(u"toplane")
        self.topLabel = QLabel(self.toplane)
        self.topLabel.setObjectName(u"topLabel")
        self.topLabel.setGeometry(QRect(10, -5, 71, 41))
        self.topLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.topLabel.setAlignment(Qt.AlignCenter)
        self.laneSelector.addWidget(self.toplane)
        self.jungle = QWidget()
        self.jungle.setObjectName(u"jungle")
        self.jungleLabel = QLabel(self.jungle)
        self.jungleLabel.setObjectName(u"jungleLabel")
        self.jungleLabel.setGeometry(QRect(10, -5, 71, 41))
        self.jungleLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.jungleLabel.setAlignment(Qt.AlignCenter)
        self.laneSelector.addWidget(self.jungle)
        self.mid = QWidget()
        self.mid.setObjectName(u"mid")
        self.midLabel = QLabel(self.mid)
        self.midLabel.setObjectName(u"midLabel")
        self.midLabel.setGeometry(QRect(10, -5, 71, 41))
        self.midLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.midLabel.setAlignment(Qt.AlignCenter)
        self.laneSelector.addWidget(self.mid)
        self.adc = QWidget()
        self.adc.setObjectName(u"adc")
        self.adcLabel = QLabel(self.adc)
        self.adcLabel.setObjectName(u"adcLabel")
        self.adcLabel.setGeometry(QRect(10, -5, 71, 41))
        self.adcLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.adcLabel.setAlignment(Qt.AlignCenter)
        self.laneSelector.addWidget(self.adc)
        self.support = QWidget()
        self.support.setObjectName(u"support")
        self.supportLabel = QLabel(self.support)
        self.supportLabel.setObjectName(u"supportLabel")
        self.supportLabel.setGeometry(QRect(10, -5, 71, 41))
        self.supportLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 11pt \"Segoe UI Black\";")
        self.supportLabel.setAlignment(Qt.AlignCenter)
        self.laneSelector.addWidget(self.support)
        self.pushButton = QPushButton(self.instalockBlindFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 130, 21, 23))
        self.previousLaneBtn = QPushButton(self.instalockBlindFrame)
        self.previousLaneBtn.setObjectName(u"previousLaneBtn")
        self.previousLaneBtn.setGeometry(QRect(60, 130, 16, 16))
        self.previousLaneBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.previousLaneBtn.setStyleSheet(u"image: url(:/icons/leftarrow.png);")
        self.nextLaneBtn = QPushButton(self.instalockBlindFrame)
        self.nextLaneBtn.setObjectName(u"nextLaneBtn")
        self.nextLaneBtn.setGeometry(QRect(150, 130, 16, 16))
        self.nextLaneBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.nextLaneBtn.setStyleSheet(u"image: url(:/icons/right-arrow.png);")
        self.autoAcceptFrame = QFrame(self.instalockBg)
        self.autoAcceptFrame.setObjectName(u"autoAcceptFrame")
        self.autoAcceptFrame.setGeometry(QRect(280, 30, 221, 91))
        self.autoAcceptFrame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.autoAcceptFrame.setFrameShape(QFrame.StyledPanel)
        self.autoAcceptFrame.setFrameShadow(QFrame.Raised)
        self.autoAcceptLabel = QLabel(self.autoAcceptFrame)
        self.autoAcceptLabel.setObjectName(u"autoAcceptLabel")
        self.autoAcceptLabel.setGeometry(QRect(0, 9, 221, 21))
        self.autoAcceptLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.autoAcceptLabel.setAlignment(Qt.AlignCenter)
        self.autoAcceptManager = QStackedWidget(self.autoAcceptFrame)
        self.autoAcceptManager.setObjectName(u"autoAcceptManager")
        self.autoAcceptManager.setGeometry(QRect(20, 40, 191, 31))
        self.startAccept = QWidget()
        self.startAccept.setObjectName(u"startAccept")
        self.startAcceptBtn = QPushButton(self.startAccept)
        self.startAcceptBtn.setObjectName(u"startAcceptBtn")
        self.startAcceptBtn.setGeometry(QRect(40, 0, 101, 31))
        self.startAcceptBtn.setStyleSheet(u"QPushButton {\n"
"       font: 87 8pt \"Arial Black\";\n"
"       color: rgb(28, 146, 214);\n"
"       background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"       \n"
"       background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"       background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.autoAcceptManager.addWidget(self.startAccept)
        self.stopAccept = QWidget()
        self.stopAccept.setObjectName(u"stopAccept")
        self.stopAcceptBtn = QPushButton(self.stopAccept)
        self.stopAcceptBtn.setObjectName(u"stopAcceptBtn")
        self.stopAcceptBtn.setGeometry(QRect(40, 0, 101, 31))
        self.stopAcceptBtn.setStyleSheet(u"QPushButton {\n"
"       font: 87 8pt \"Arial Black\";\n"
"       color: rgb(28, 146, 214);\n"
"       background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"       \n"
"       background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"       background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.autoAcceptManager.addWidget(self.stopAccept)
        self.autoPlayAgainFrame = QFrame(self.instalockBg)
        self.autoPlayAgainFrame.setObjectName(u"autoPlayAgainFrame")
        self.autoPlayAgainFrame.setGeometry(QRect(280, 130, 221, 101))
        self.autoPlayAgainFrame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.autoPlayAgainFrame.setFrameShape(QFrame.StyledPanel)
        self.autoPlayAgainFrame.setFrameShadow(QFrame.Raised)
        self.autoPlayAgainLabel = QLabel(self.autoPlayAgainFrame)
        self.autoPlayAgainLabel.setObjectName(u"autoPlayAgainLabel")
        self.autoPlayAgainLabel.setGeometry(QRect(0, 9, 221, 21))
        self.autoPlayAgainLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.autoPlayAgainLabel.setAlignment(Qt.AlignCenter)
        self.autoPlayAgainManager = QStackedWidget(self.autoPlayAgainFrame)
        self.autoPlayAgainManager.setObjectName(u"autoPlayAgainManager")
        self.autoPlayAgainManager.setGeometry(QRect(20, 50, 191, 31))
        self.startPlayAg = QWidget()
        self.startPlayAg.setObjectName(u"startPlayAg")
        self.startPlayAgBtn = QPushButton(self.startPlayAg)
        self.startPlayAgBtn.setObjectName(u"startPlayAgBtn")
        self.startPlayAgBtn.setGeometry(QRect(40, 0, 101, 31))
        self.startPlayAgBtn.setStyleSheet(u"QPushButton {\n"
"       font: 87 8pt \"Arial Black\";\n"
"       color: rgb(28, 146, 214);\n"
"       background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"       \n"
"       background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"       background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.autoPlayAgainManager.addWidget(self.startPlayAg)
        self.stopPlayAg = QWidget()
        self.stopPlayAg.setObjectName(u"stopPlayAg")
        self.stopPlayAgBtn = QPushButton(self.stopPlayAg)
        self.stopPlayAgBtn.setObjectName(u"stopPlayAgBtn")
        self.stopPlayAgBtn.setGeometry(QRect(40, 0, 101, 31))
        self.stopPlayAgBtn.setStyleSheet(u"QPushButton {\n"
"       font: 87 8pt \"Arial Black\";\n"
"       color: rgb(28, 146, 214);\n"
"       background-color: rgb(16, 24, 45);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"       \n"
"       background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"       background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.autoPlayAgainManager.addWidget(self.stopPlayAg)
        IRFTool.setCentralWidget(self.centralwidget)

        self.retranslateUi(IRFTool)

        self.instalockManagerB.setCurrentIndex(0)
        self.laneSelector.setCurrentIndex(0)
        self.autoAcceptManager.setCurrentIndex(0)
        self.autoPlayAgainManager.setCurrentIndex(0)

        self.instaBlindPickLabel.setText(QCoreApplication.translate("IRFTool", u"Instalock (Blind Pick)", None))
        self.championLockB.setText("")
        self.championLockB.setPlaceholderText(QCoreApplication.translate("IRFTool", u"Champion to lock", None))
        self.instalockBlindLabel.setText(QCoreApplication.translate("IRFTool", u"Champion", None))
        self.instalockLaneLabel.setText(QCoreApplication.translate("IRFTool", u"Lane", None))
        self.startBtnB.setText(QCoreApplication.translate("IRFTool", u"START", None))
        self.stopBtnB.setText(QCoreApplication.translate("IRFTool", u"STOP", None))
        self.noneLabel.setText(QCoreApplication.translate("IRFTool", u"NONE", None))
        self.topLabel.setText(QCoreApplication.translate("IRFTool", u"TOP", None))
        self.jungleLabel.setText(QCoreApplication.translate("IRFTool", u"JUNGLE", None))
        self.midLabel.setText(QCoreApplication.translate("IRFTool", u"MID", None))
        self.adcLabel.setText(QCoreApplication.translate("IRFTool", u"ADC", None))
        self.supportLabel.setText(QCoreApplication.translate("IRFTool", u"SUP", None))
        self.pushButton.setText("")
        self.previousLaneBtn.setText("")
        self.nextLaneBtn.setText("")
        self.autoAcceptLabel.setText(QCoreApplication.translate("IRFTool", u"Auto Accept", None))
        self.startAcceptBtn.setText(QCoreApplication.translate("IRFTool", u"START", None))
        self.stopAcceptBtn.setText(QCoreApplication.translate("IRFTool", u"STOP", None))
        self.autoPlayAgainLabel.setText(QCoreApplication.translate("IRFTool", u"Auto Play Again", None))
        self.startPlayAgBtn.setText(QCoreApplication.translate("IRFTool", u"START", None))
        self.stopPlayAgBtn.setText(QCoreApplication.translate("IRFTool", u"STOP", None))
        self.miscPage = QWidget()
        self.miscPage.setObjectName(u"miscPage")
        self.stackedWidget.addWidget(self.miscPage)
        self.instaquit_frame = QFrame(self.miscPage)
        self.instaquit_frame.setObjectName(u"instaquit_frame")
        self.instaquit_frame.setGeometry(QRect(20, 40, 221, 121))
        self.instaquit_frame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.instaquit_frame.setFrameShape(QFrame.StyledPanel)
        self.instaquit_frame.setFrameShadow(QFrame.Raised)
        self.instaQuitLabel = QLabel(self.instaquit_frame)
        self.instaQuitLabel.setObjectName(u"instaQuitLabel")
        self.instaQuitLabel.setGeometry(QRect(0, 20, 221, 20))
        self.instaQuitLabel.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(28, 146, 237);")
        self.instaQuitLabel.setAlignment(Qt.AlignCenter)
        self.instaQuitManager = QStackedWidget(self.instaquit_frame)
        self.instaQuitManager.setObjectName(u"instaQuitManager")
        self.instaQuitManager.setGeometry(QRect(10, 50, 201, 61))
        self.instaquit_enable = QWidget()
        self.instaquit_enable.setObjectName(u"instaquit_enable")
        self.enableInstaQuitBtn = QPushButton(self.instaquit_enable)
        self.enableInstaQuitBtn.setObjectName(u"enableInstaQuitBtn")
        self.enableInstaQuitBtn.setGeometry(QRect(40, 10, 121, 41))
        self.enableInstaQuitBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.instaQuitManager.addWidget(self.instaquit_enable)
        self.instaquit_disable = QWidget()
        self.instaquit_disable.setObjectName(u"instaquit_disable")
        self.disableInstaQuitBtn = QPushButton(self.instaquit_disable)
        self.disableInstaQuitBtn.setObjectName(u"disableInstaQuitBtn")
        self.disableInstaQuitBtn.setGeometry(QRect(40, 10, 121, 41))
        self.disableInstaQuitBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.instaQuitManager.addWidget(self.instaquit_disable)
        self.auto_runes_frame = QFrame(self.miscPage)
        self.auto_runes_frame.setObjectName(u"auto_runes_frame")
        self.auto_runes_frame.setGeometry(QRect(260, 40, 221, 121))
        self.auto_runes_frame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.auto_runes_frame.setFrameShape(QFrame.StyledPanel)
        self.auto_runes_frame.setFrameShadow(QFrame.Raised)
        self.auto_runes_label = QLabel(self.auto_runes_frame)
        self.auto_runes_label.setObjectName(u"auto_runes_label")
        self.auto_runes_label.setGeometry(QRect(0, 20, 221, 20))
        self.auto_runes_label.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(28, 146, 237);")
        self.auto_runes_label.setAlignment(Qt.AlignCenter)
        self.runesManager = QStackedWidget(self.auto_runes_frame)
        self.runesManager.setObjectName(u"runesManager")
        self.runesManager.setGeometry(QRect(10, 50, 201, 61))
        self.runes_import_enable = QWidget()
        self.runes_import_enable.setObjectName(u"runes_import_enable")
        self.enableAutoRunesBtn = QPushButton(self.runes_import_enable)
        self.enableAutoRunesBtn.setObjectName(u"enableAutoRunesBtn")
        self.enableAutoRunesBtn.setGeometry(QRect(40, 10, 121, 41))
        self.enableAutoRunesBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.runesManager.addWidget(self.runes_import_enable)
        self.runes_import_disable = QWidget()
        self.runes_import_disable.setObjectName(u"runes_import_disable")
        self.disableAutoRunesBtn = QPushButton(self.runes_import_disable)
        self.disableAutoRunesBtn.setObjectName(u"disableAutoRunesBtn")
        self.disableAutoRunesBtn.setGeometry(QRect(40, 10, 121, 41))
        self.disableAutoRunesBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.runesManager.addWidget(self.runes_import_disable)
        self.multi_search_frame = QFrame(self.miscPage)
        self.multi_search_frame.setObjectName(u"multi_search_frame")
        self.multi_search_frame.setGeometry(QRect(490, 40, 221, 121))
        self.multi_search_frame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.multi_search_frame.setFrameShape(QFrame.StyledPanel)
        self.multi_search_frame.setFrameShadow(QFrame.Raised)
        self.multi_search_label = QLabel(self.multi_search_frame)
        self.multi_search_label.setObjectName(u"multi_search_label")
        self.multi_search_label.setGeometry(QRect(0, 20, 221, 20))
        self.multi_search_label.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(28, 146, 237);")
        self.multi_search_label.setAlignment(Qt.AlignCenter)
        self.multiSearchManager = QStackedWidget(self.multi_search_frame)
        self.multiSearchManager.setObjectName(u"multiSearchManager")
        self.multiSearchManager.setGeometry(QRect(10, 50, 201, 61))
        self.multi_search_enable = QWidget()
        self.multi_search_enable.setObjectName(u"multi_search_enable")
        self.enableMultiSearchBtn = QPushButton(self.multi_search_enable)
        self.enableMultiSearchBtn.setObjectName(u"enableMultiSearchBtn")
        self.enableMultiSearchBtn.setGeometry(QRect(40, 10, 121, 41))
        self.enableMultiSearchBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.multiSearchManager.addWidget(self.multi_search_enable)
        self.multi_search_disable = QWidget()
        self.multi_search_disable.setObjectName(u"multi_search_disable")
        self.disableMultiSearchBtn = QPushButton(self.multi_search_disable)
        self.disableMultiSearchBtn.setObjectName(u"disableMultiSearchBtn")
        self.disableMultiSearchBtn.setGeometry(QRect(40, 10, 121, 41))
        self.disableMultiSearchBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.multiSearchManager.addWidget(self.multi_search_disable)
        self.mutli_client_frame = QFrame(self.miscPage)
        self.mutli_client_frame.setObjectName(u"mutli_client_frame")
        self.mutli_client_frame.setGeometry(QRect(20, 180, 221, 121))
        self.mutli_client_frame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.mutli_client_frame.setFrameShape(QFrame.StyledPanel)
        self.mutli_client_frame.setFrameShadow(QFrame.Raised)
        self.multiClientLabel = QLabel(self.mutli_client_frame)
        self.multiClientLabel.setObjectName(u"multiClientLabel")
        self.multiClientLabel.setGeometry(QRect(0, 20, 221, 20))
        self.multiClientLabel.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(28, 146, 237);")
        self.multiClientLabel.setAlignment(Qt.AlignCenter)
        self.openClientBtn = QPushButton(self.mutli_client_frame)
        self.openClientBtn.setObjectName(u"openClientBtn")
        self.openClientBtn.setGeometry(QRect(50, 60, 121, 41))
        self.openClientBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.practice_tool_frame = QFrame(self.miscPage)
        self.practice_tool_frame.setObjectName(u"practice_tool_frame")
        self.practice_tool_frame.setGeometry(QRect(260, 180, 221, 121))
        self.practice_tool_frame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;")
        self.practice_tool_frame.setFrameShape(QFrame.StyledPanel)
        self.practice_tool_frame.setFrameShadow(QFrame.Raised)
        self.practiceToolLabel = QLabel(self.practice_tool_frame)
        self.practiceToolLabel.setObjectName(u"practiceToolLabel")
        self.practiceToolLabel.setGeometry(QRect(0, 20, 221, 20))
        self.practiceToolLabel.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(28, 146, 237);")
        self.practiceToolLabel.setAlignment(Qt.AlignCenter)
        self.createPracticeToolBtn = QPushButton(self.practice_tool_frame)
        self.createPracticeToolBtn.setObjectName(u"createPracticeToolBtn")
        self.createPracticeToolBtn.setGeometry(QRect(50, 60, 121, 41))
        self.createPracticeToolBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")

        self.instaQuitManager.setCurrentIndex(0)
        self.runesManager.setCurrentIndex(0)
        self.multiSearchManager.setCurrentIndex(0)
        
        self.instaQuitLabel.setText(QCoreApplication.translate("IRFTool", u"Insta Quit", None))
        self.enableInstaQuitBtn.setText(QCoreApplication.translate("IRFTool", u"ENABLE", None))
        self.disableInstaQuitBtn.setText(QCoreApplication.translate("IRFTool", u"DISABLE", None))
        self.auto_runes_label.setText(QCoreApplication.translate("IRFTool", u"Auto Runes", None))
        self.enableAutoRunesBtn.setText(QCoreApplication.translate("IRFTool", u"ENABLE", None))
        self.disableAutoRunesBtn.setText(QCoreApplication.translate("IRFTool", u"DISABLE", None))
        self.multi_search_label.setText(QCoreApplication.translate("IRFTool", u"OP.GG Multi Search", None))
        self.enableMultiSearchBtn.setText(QCoreApplication.translate("IRFTool", u"ENABLE", None))
        self.disableMultiSearchBtn.setText(QCoreApplication.translate("IRFTool", u"DISABLE", None))
        self.multiClientLabel.setText(QCoreApplication.translate("IRFTool", u"Multi Clients", None))
        self.openClientBtn.setText(QCoreApplication.translate("IRFTool", u"OPEN", None))
        self.practiceToolLabel.setText(QCoreApplication.translate("IRFTool", u"Practice Tool+", None))
        self.createPracticeToolBtn.setText(QCoreApplication.translate("IRFTool", u"CREATE ", None))
        self.friendsPage = QWidget()
        self.friendsPage.setObjectName("friendsPage")
        self.stackedWidget.addWidget(self.friendsPage)
        self.friendsBg = QFrame(self.friendsPage)
        self.friendsBg.setGeometry(QtCore.QRect(0, 0, 721, 591))
        self.friendsBg.setStyleSheet("background-color: rgb(46, 51, 72);")
        self.friendsBg.setFrameShape(QFrame.StyledPanel)
        self.friendsBg.setFrameShadow(QFrame.Raised)
        self.friendsBg.setObjectName("friendsBg")
        self.friendsManagerFrame = QFrame(self.friendsBg)
        self.friendsManagerFrame.setGeometry(QtCore.QRect(15, 40, 291, 501))
        self.friendsManagerFrame.setStyleSheet("\n"
"border-radius: 8px;\n"
"background-color: rgba(19, 28, 53, 200);")
        self.friendsManagerFrame.setFrameShape(QFrame.StyledPanel)
        self.friendsManagerFrame.setFrameShadow(QFrame.Raised)
        self.friendsManagerFrame.setObjectName("friendsManagerFrame")
        self.refreshFriendsBtn = QPushButton(self.friendsManagerFrame)
        self.refreshFriendsBtn.setGeometry(QtCore.QRect(80, 445, 131, 41))
        self.refreshFriendsBtn.setStyleSheet("QPushButton {\n"
"    font: 87 9pt \"Arial Black\";\n"
"    color: rgb(28, 146, 214);\n"
"    background-color: rgb(16, 24, 45);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.refreshFriendsBtn.setObjectName("refreshFriendsBtn")
        self.topBarFriends = QFrame(self.friendsManagerFrame)
        self.topBarFriends.setGeometry(QtCore.QRect(0, 0, 291, 21))
        self.topBarFriends.setStyleSheet("background-color: rgb(31, 34, 49);\n"
"background-color: rgb(18, 26, 45);\n"
"border-radius: 10px;")
        self.topBarFriends.setFrameShape(QFrame.StyledPanel)
        self.topBarFriends.setFrameShadow(QFrame.Raised)
        self.topBarFriends.setObjectName("topBarFriends")
        self.inviFrameFriends = QFrame(self.topBarFriends)
        self.inviFrameFriends.setGeometry(QtCore.QRect(0, 9, 21, 71))
        self.inviFrameFriends.setFrameShape(QFrame.StyledPanel)
        self.inviFrameFriends.setFrameShadow(QFrame.Raised)
        self.inviFrameFriends.setObjectName("inviFrameFriends")
        self.inviFrameFriends2 = QFrame(self.topBarFriends)
        self.inviFrameFriends2.setGeometry(QtCore.QRect(275, 10, 31, 80))
        self.inviFrameFriends2.setFrameShape(QFrame.StyledPanel)
        self.inviFrameFriends2.setFrameShadow(QFrame.Raised)
        self.inviFrameFriends2.setObjectName("inviFrameFriends2")
        self.friendManagerLabel = QLabel(self.topBarFriends)
        self.friendManagerLabel.setGeometry(QtCore.QRect(20, 0, 251, 21))
        self.friendManagerLabel.setStyleSheet("font: 87 9pt \"Segoe UI Black\";\n"
"\n"
"color: rgb(28, 146, 214);")
        self.friendManagerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.friendManagerLabel.setObjectName("friendManagerLabel")
        self.friendList = QListWidget(self.friendsManagerFrame)
        self.friendList.setGeometry(QtCore.QRect(15, 30, 261, 401))
        self.friendList.setStyleSheet("QListWidget {\n"
"    background-color: rgba(18, 26, 45, 190);\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    font: 87 9pt \"Segoe UI Black\";\n"
"    color: rgb(28, 146, 214);\n"
"\n"
"}")
        self.friendList.setObjectName("friendList")
        self.frame = QFrame(self.friendsBg)
        self.frame.setGeometry(QtCore.QRect(320, 140, 191, 261))
        self.frame.setStyleSheet("background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"\n"
"color: rgb(28, 146, 214);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.acceptAllFriendsBtn = QPushButton(self.frame)
        self.acceptAllFriendsBtn.setGeometry(QtCore.QRect(50, 80, 101, 31))
        self.acceptAllFriendsBtn.setStyleSheet("QPushButton {\n"
"    font: 87 9pt \"Arial Black\";\n"
"    color: rgb(28, 146, 214);\n"
"    background-color: rgb(16, 24, 45);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.acceptAllFriendsBtn.setObjectName("acceptAllFriendsBtn")
        self.declineAllFriendsBtn = QPushButton(self.frame)
        self.declineAllFriendsBtn.setGeometry(QtCore.QRect(50, 150, 101, 31))
        self.declineAllFriendsBtn.setStyleSheet("QPushButton {\n"
"    font: 87 9pt \"Arial Black\";\n"
"    color: rgb(28, 146, 214);\n"
"    background-color: rgb(16, 24, 45);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.declineAllFriendsBtn.setObjectName("declineAllFriendsBtn")
        self.removeAllFriendsBtn = QPushButton(self.frame)
        self.removeAllFriendsBtn.setGeometry(QtCore.QRect(49, 215, 101, 31))
        self.removeAllFriendsBtn.setStyleSheet("QPushButton {\n"
"    font: 87 9pt \"Arial Black\";\n"
"    color: rgb(28, 146, 214);\n"
"    background-color: rgb(16, 24, 45);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.removeAllFriendsBtn.setObjectName("removeAllFriendsBtn")
        self.acceptAllFriendsLabel = QLabel(self.frame)
        self.acceptAllFriendsLabel.setGeometry(QtCore.QRect(0, 50, 191, 20))
        self.acceptAllFriendsLabel.setStyleSheet("font: 87 9pt \"Segoe UI Black\";\n"
"\n"
"color: rgb(28, 146, 214);")
        self.acceptAllFriendsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.acceptAllFriendsLabel.setObjectName("acceptAllFriendsLabel")
        self.declineAllFriendsLabel = QLabel(self.frame)
        self.declineAllFriendsLabel.setGeometry(QtCore.QRect(0, 120, 191, 20))
        self.declineAllFriendsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.declineAllFriendsLabel.setObjectName("declineAllFriendsLabel")
        self.removeAllFriendsLabel = QLabel(self.frame)
        self.removeAllFriendsLabel.setGeometry(QtCore.QRect(0, 191, 191, 20))
        self.removeAllFriendsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.removeAllFriendsLabel.setObjectName("removeAllFriendsLabel")
        self.featuresLabel = QLabel(self.frame)
        self.featuresLabel.setGeometry(QtCore.QRect(0, -1, 191, 51))
        self.featuresLabel.setStyleSheet("font: 87 10pt \"Segoe UI Black\";")
        self.featuresLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.featuresLabel.setObjectName("featuresLabel")
        self.friendSelected = QFrame(self.friendsBg)
        self.friendSelected.setObjectName(u"friendSelected")
        self.friendSelected.setGeometry(QRect(520, 100, 181, 351))
        self.friendSelected.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
"border-radius: 10px;\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"\n"
"color: rgb(28, 146, 214);")
        self.friendSelected.setFrameShape(QFrame.StyledPanel)
        self.friendSelected.setFrameShadow(QFrame.Raised)
        self.friendNameLabel = QLabel(self.friendSelected)
        self.friendNameLabel.setObjectName(u"friendNameLabel")
        self.friendNameLabel.setGeometry(QRect(0, -1, 181, 51))
        self.friendNameLabel.setStyleSheet(u"font: 87 10pt \"Segoe UI Black\";")
        self.friendNameLabel.setAlignment(Qt.AlignCenter)
        self.copyIconBtn = QPushButton(self.friendSelected)
        self.copyIconBtn.setObjectName(u"copyIconBtn")
        self.copyIconBtn.setGeometry(QRect(40, 80, 101, 31))
        self.copyIconBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.copyStatusBtn = QPushButton(self.friendSelected)
        self.copyStatusBtn.setObjectName(u"copyStatusBtn")
        self.copyStatusBtn.setGeometry(QRect(39, 150, 101, 31))
        self.copyStatusBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.banMessageBtn = QPushButton(self.friendSelected)
        self.banMessageBtn.setObjectName(u"banMessageBtn")
        self.banMessageBtn.setGeometry(QRect(40, 290, 101, 31))
        self.banMessageBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.copyIconLabel = QLabel(self.friendSelected)
        self.copyIconLabel.setObjectName(u"copyIconLabel")
        self.copyIconLabel.setGeometry(QRect(0, 50, 181, 16))
        self.copyIconLabel.setAlignment(Qt.AlignCenter)
        self.copyStatusLabel = QLabel(self.friendSelected)
        self.copyStatusLabel.setObjectName(u"copyStatusLabel")
        self.copyStatusLabel.setGeometry(QRect(0, 120, 181, 16))
        self.copyStatusLabel.setAlignment(Qt.AlignCenter)
        self.fakeBanLabel = QLabel(self.friendSelected)
        self.fakeBanLabel.setObjectName(u"fakeBanLabel")
        self.fakeBanLabel.setGeometry(QRect(1, 260, 181, 16))
        self.fakeBanLabel.setAlignment(Qt.AlignCenter)
        self.crashChatLabel = QLabel(self.friendSelected)
        self.crashChatLabel.setObjectName(u"crashChatLabel")
        self.crashChatLabel.setGeometry(QRect(1, 190, 181, 16))
        self.crashChatLabel.setAlignment(Qt.AlignCenter)
        self.chatCrashBtn = QPushButton(self.friendSelected)
        self.chatCrashBtn.setObjectName(u"chatCrashBtn")
        self.chatCrashBtn.setGeometry(QRect(40, 220, 101, 31))
        self.chatCrashBtn.setStyleSheet(u"QPushButton {\n"
"	font: 87 9pt \"Arial Black\";\n"
"	color: rgb(28, 146, 214);\n"
"	background-color: rgb(16, 24, 45);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(17, 25, 47, 190);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(16, 24, 45);\n"
"\n"
"\n"
"}")
        self.crashChatLabel.setText(QCoreApplication.translate("IRFTool", u"Chat Crasher", None))
        self.chatCrashBtn.setText(QCoreApplication.translate("IRFTool", u"CRASH", None))
        self.refreshFriendsBtn.setText(QCoreApplication.translate("IRFTool", "REFRESH"))
        self.friendManagerLabel.setText(QCoreApplication.translate("IRFTool", "Friends Manager"))
        self.acceptAllFriendsBtn.setText(QCoreApplication.translate("IRFTool", "ACCEPT"))
        self.declineAllFriendsBtn.setText(QCoreApplication.translate("IRFTool", "DECLINE"))
        self.removeAllFriendsBtn.setText(QCoreApplication.translate("IRFTool", "REMOVE"))
        self.acceptAllFriendsLabel.setText(QCoreApplication.translate("IRFTool", "Accept All Friend Requests"))
        self.declineAllFriendsLabel.setText(QCoreApplication.translate("IRFTool", "Decline All Friend Requests"))
        self.removeAllFriendsLabel.setText(QCoreApplication.translate("IRFTool", "Remove All Friends"))
        self.featuresLabel.setText(QCoreApplication.translate("IRFTool", "Features"))
        self.copyIconBtn.setText(QCoreApplication.translate("IRFTool", "COPY"))
        self.copyStatusBtn.setText(QCoreApplication.translate("IRFTool", "COPY"))
        self.banMessageBtn.setText(QCoreApplication.translate("IRFTool", "SEND"))
        self.copyIconLabel.setText(QCoreApplication.translate("IRFTool", "Copy Icon"))
        self.copyStatusLabel.setText(QCoreApplication.translate("IRFTool", "Copy Status"))
        self.fakeBanLabel.setText(QCoreApplication.translate("IRFTool", "Fake Ban Message"))
        self.friendSelected.hide()
        IRFTool.setCentralWidget(self.centralwidget)
        self.retranslateUi(IRFTool)
        self.eloManager.setCurrentIndex(9)
        self.queueManager.setCurrentIndex(0)
        self.availabilityManager.setCurrentIndex(0)
        

        data = api.get('/lol-chat/v1/me').json()
        self.nickname = data["name"]
        self.iconId = data["icon"]
        iconUrl = "https://cdn.communitydragon.org/latest/profile-icon/" + str(self.iconId)
        icon = QImage()
        icon.loadFromData(req.get(iconUrl).content)
        self.usernameLabel.setText(self.nickname)
        pixmap = QPixmap(icon)
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.summonerIcon.setPixmap(pixmap)
        self.summonerIcon.setScaledContents(True)
        self.summonerIcon.show()
        eloUrl = [
                "https://lolslaves.com/wp-content/uploads/2019/07/UNRANKED-LEAGUE-OF-LEGENDS-ACCOUNTS.png",
                "https://opgg-static.akamaized.net/images/medals/iron_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/bronze_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/silver_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/gold_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/platinum_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/diamond_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/master_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/grandmaster_1.png?image=q_auto:best&v=1",
                "https://opgg-static.akamaized.net/images/medals/challenger_1.png?image=q_auto:best&v=1",
        ]
        unrankedUrl = eloUrl[0]
        ironUrl = eloUrl[1]
        bronzeUrl = eloUrl[2]
        silverUrl = eloUrl[3]
        goldUrl = eloUrl[4]
        platinumUrl = eloUrl[5]
        diamondUrl = eloUrl[6]
        masterUrl = eloUrl[7]
        grandmasterUrl = eloUrl[8]
        challengerUrl = eloUrl[9]

        unrankedImage = QImage()
        unrankedImage.loadFromData(req.get(unrankedUrl).content)
        unrankedPixmap = QPixmap(unrankedImage)
        unrankedPixmap = unrankedPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.unrankedImg.setPixmap(unrankedPixmap)
        self.unrankedImg.setScaledContents(True)
        self.unrankedImg.show()

        ironImage = QImage()
        ironImage.loadFromData(req.get(ironUrl).content)
        ironPixmap = QPixmap(ironImage)
        ironPixmap = ironPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.ironImg.setPixmap(ironPixmap)
        self.ironImg.setScaledContents(True)
        self.ironImg.show()

        bronzeImage = QImage()
        bronzeImage.loadFromData(req.get(bronzeUrl).content)
        bronzePixmap = QPixmap(bronzeImage)
        bronzePixmap = bronzePixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.bronzeImg.setPixmap(bronzePixmap)
        self.bronzeImg.setScaledContents(True)
        self.bronzeImg.show()

        silverImage = QImage()
        silverImage.loadFromData(req.get(silverUrl).content)
        silverPixmap = QPixmap(silverImage)
        silverPixmap = silverPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.silverImg.setPixmap(silverPixmap)
        self.silverImg.setScaledContents(True)
        self.silverImg.show()

        goldImage = QImage()
        goldImage.loadFromData(req.get(goldUrl).content)
        goldPixmap = QPixmap(goldImage)
        goldPixmap = goldPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.goldImg.setPixmap(goldPixmap)
        self.goldImg.setScaledContents(True)
        self.goldImg.show()

        platinumImage = QImage()
        platinumImage.loadFromData(req.get(platinumUrl).content)
        platinumPixmap = QPixmap(platinumImage)
        platinumPixmap = platinumPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.platinumImg.setPixmap(platinumPixmap)
        self.platinumImg.setScaledContents(True)
        self.platinumImg.show()

        diamondImage = QImage()
        diamondImage.loadFromData(req.get(diamondUrl).content)
        diamondPixmap = QPixmap(diamondImage)
        diamondPixmap = diamondPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.diamondImg.setPixmap(diamondPixmap)
        self.diamondImg.setScaledContents(True)
        self.diamondImg.show()

        masterImage = QImage()
        masterImage.loadFromData(req.get(masterUrl).content)
        masterPixmap = QPixmap(masterImage)
        masterPixmap = masterPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.masterImg.setPixmap(masterPixmap)
        self.masterImg.setScaledContents(True)
        self.masterImg.show()

        grandmasterImage = QImage()
        grandmasterImage.loadFromData(req.get(grandmasterUrl).content)
        grandmasterPixmap = QPixmap(grandmasterImage)
        grandmasterPixmap = grandmasterPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.grandmasterImg.setPixmap(grandmasterPixmap)
        self.grandmasterImg.setScaledContents(True)
        self.grandmasterImg.show()

        challengerImage = QImage()
        challengerImage.loadFromData(req.get(challengerUrl).content)
        challengerPixmap = QPixmap(challengerImage)
        challengerPixmap = challengerPixmap.scaled(150, 150, QtCore.Qt.KeepAspectRatio)
        self.challengerImg.setPixmap(challengerPixmap)
        self.challengerImg.setScaledContents(True)
        self.challengerImg.show()

        availabilitys = ['online', 'offline', 'mobile']
        if data["availability"] == availabilitys[0]:
                onlineImg = QImage()
                onlineImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/online.png").content)
                onlinePixmap = QPixmap(onlineImg)
                onlinePixmap = onlinePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
                self.availabilityImg.setPixmap(onlinePixmap)
                self.availabilityImg.setScaledContents(True)
                self.availabilityImg.show()
        elif data["availability"] == availabilitys[1]:
                offlineImg = QImage()
                offlineImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/offline.png").content)
                offlinePixmap = QPixmap(offlineImg)
                offlinePixmap = offlinePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
                self.availabilityImg.setPixmap(offlinePixmap)
                self.availabilityImg.setScaledContents(True)
                self.availabilityImg.show()
        elif data["availability"] == availabilitys[2]:
                mobileImg = QImage()
                mobileImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/mobile.png").content)
                mobilePixmap = QPixmap(mobileImg)
                mobilePixmap = mobilePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
                self.availabilityImg.setPixmap(mobilePixmap)
                self.availabilityImg.setScaledContents(True)
                self.availabilityImg.show()
        else:
                onlineImg = QImage()
                onlineImg.loadFromData(req.get("https://cdn.flowd1337.repl.co/images/online.png").content)
                onlinePixmap = QPixmap(onlineImg)
                onlinePixmap = onlinePixmap.scaled(190, 24, QtCore.Qt.KeepAspectRatio)
                self.availabilityImg.setPixmap(onlinePixmap)
                self.availabilityImg.setScaledContents(True)
                self.availabilityImg.show()

        QMetaObject.connectSlotsByName(IRFTool)
        IRFTool.setCentralWidget(self.centralwidget)
        def SortFriends():
                friend_list = []
                all_friends = api.get('/lol-chat/v1/friends').json()
                countFriends = len(all_friends)
                for i in range(countFriends):
                        if len(all_friends[i]["name"]) <= 16 and len(all_friends[i]["name"]) > 3:
                                friend_list.append(all_friends[i]["name"])
                friend_list.sort()
                for i in range(len(friend_list)):
                        self.friendList.addItem(friend_list[i])


        SortFriends()
    # setupUi

    def retranslateUi(self, IRFTool):
        QCoreApplication.translate = QCoreApplication.translate
        IRFTool.setWindowTitle(QCoreApplication.translate("IRFTool", u"IRF Tools", None))
        self.titleLabel.setText(QCoreApplication.translate("IRFTool", u"IRF Tools", None))
        self.homeBtn.setText(QCoreApplication.translate("IRFTool", u"     Home", None))
        self.instalockBtn.setText(QCoreApplication.translate("IRFTool", u"     Instalocker", None))
        self.exploitsBtn.setText(QCoreApplication.translate("IRFTool", u"     Exploits", None))
        self.miscBtn.setText(QCoreApplication.translate("IRFTool", u"     Misc", None))
        self.usernameLabel.setText("")
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.summonerIcon.setText("")
        self.closeBtn.setText("")
        self.minimizeBtn.setText("")
        self.summonerIcon.setText("")
        self.activityLabel.setText("")
        self.changeEloBtn.setText(QCoreApplication.translate("IRFTool", u"CHANGE ELO", None))
        self.previousEloBtn.setText(QCoreApplication.translate("IRFTool", u"", None))
        self.nextEloBtn.setText("")
        self.divisionInput.setPlaceholderText(QCoreApplication.translate("IRFTool", u"Division", None))
        self.rankChangerLabel.setText(QCoreApplication.translate("IRFTool", u"Rank Changer", None))
        self.unrankedImg.setText("")
        self.ironImg.setText("")
        self.bronzeImg.setText("")
        self.silverImg.setText("")
        self.goldImg.setText("")
        self.platinumImg.setText("")
        self.diamondImg.setText("")
        self.masterImg.setText("")
        self.grandmasterImg.setText("")
        self.challengerImg.setText("")
        self.soloqLabel.setText(QCoreApplication.translate("IRFTool", u"SOLO QUEUE", None))
        self.flexqLabel.setText(QCoreApplication.translate("IRFTool", u"FLEX 5X5", None))
        self.flex3x3Q.setText(QCoreApplication.translate("IRFTool", u"FLEX 3X3", None))
        self.tftLabel.setText(QCoreApplication.translate("IRFTool", u"TFT", None))
        self.previousQueueBtn.setText("")
        self.nextQueueBtn.setText("")
        self.statusInput.setPlaceholderText(QCoreApplication.translate("IRFTool", u"Custom status here", None))
        self.statusChangerLabel.setText(QCoreApplication.translate("IRFTool", u"Status Changer", None))
        self.statusUpdateBtn.setText(QCoreApplication.translate("IRFTool", u"UPDATE", None))
        self.iconLabel.setText(QCoreApplication.translate("IRFTool", u"Icon Changer", None))
        self.backgroundLabel.setText(QCoreApplication.translate("IRFTool", u"Background Changer", None))
        self.availabilityLabel.setText(QCoreApplication.translate("IRFTool", u"Change Availability", None))
        self.onlineLabel.setText(QCoreApplication.translate("IRFTool", u"Online", None))
        self.awayLabel.setText(QCoreApplication.translate("IRFTool", u"Away", None))
        self.offlineLabel.setText(QCoreApplication.translate("IRFTool", u"Offline", None))
        self.mobileLabel.setText(QCoreApplication.translate("IRFTool", u"Mobile", None))
        self.previousAvailability.setText("")
        self.nextAvailability.setText("")
        self.lobbyLabel.setText(QCoreApplication.translate("IRFTool", u"Lobby Creator", None))
        self.updateAvailabilityBtn.setText(QCoreApplication.translate("IRFTool", u"UPDATE", None))
        self.queueInput.setPlaceholderText(QCoreApplication.translate("IRFTool", u"Queue ID", None))
        self.createLobbyBtn.setText(QCoreApplication.translate("IRFTool", u"CREATE", None))
        self.friendsPgBtn.setText(QCoreApplication.translate("IRFTool", u"     Friends", None))


    # retranslateUi

