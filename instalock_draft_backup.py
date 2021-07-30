#         self.instalockDraftFrame = QFrame(self.instalockBg)
#         self.instalockDraftFrame.setObjectName(u"instalockDraftFrame")
#         self.instalockDraftFrame.setGeometry(QRect(265, 30, 221, 201))
#         self.instalockDraftFrame.setStyleSheet(u"background-color: rgb(19, 28, 53);\n"
# "border-radius: 10px;")
#         self.instalockDraftFrame.setFrameShape(QFrame.StyledPanel)
#         self.instalockDraftFrame.setFrameShadow(QFrame.Raised)
#         self.instalockDraftLabel = QLabel(self.instalockDraftFrame)
#         self.instalockDraftLabel.setObjectName(u"instalockDraftLabel")
#         self.instalockDraftLabel.setGeometry(QRect(0, 9, 221, 21))
#         self.instalockDraftLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
# "font: 87 12pt \"Segoe UI Black\";")
#         self.instalockDraftLabel.setAlignment(Qt.AlignCenter)
#         self.championLockDraft = QLineEdit(self.instalockDraftFrame)
#         self.championLockDraft.setObjectName(u"championLockDraft")
#         self.championLockDraft.setGeometry(QRect(50, 60, 121, 31))
#         self.championLockDraft.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
# "color: rgb(28, 146, 214);\n"
# "")
#         self.championLockDraft.setAlignment(Qt.AlignCenter)
#         self.championLabelD = QLabel(self.instalockDraftFrame)
#         self.championLabelD.setObjectName(u"championLabelD")
#         self.championLabelD.setGeometry(QRect(0, 40, 221, 16))
#         self.championLabelD.setStyleSheet(u"color: rgb(28, 146, 214);\n"
# "font: 87 9pt \"Segoe UI Black\";")
#         self.championLabelD.setAlignment(Qt.AlignCenter)
#         self.championBanLabel = QLabel(self.instalockDraftFrame)
#         self.championBanLabel.setObjectName(u"championBanLabel")
#         self.championBanLabel.setGeometry(QRect(0, 100, 221, 16))
#         self.championBanLabel.setStyleSheet(u"color: rgb(28, 146, 214);\n"
# "font: 87 9pt \"Segoe UI Black\";")
#         self.championBanLabel.setAlignment(Qt.AlignCenter)
#         self.championBan = QLineEdit(self.instalockDraftFrame)
#         self.championBan.setObjectName(u"championBan")
#         self.championBan.setGeometry(QRect(50, 120, 121, 31))
#         self.championBan.setStyleSheet(u"background-color: rgb(12, 19, 35);\n"
# "color: rgb(28, 146, 214);\n"
# "")
#         self.championBan.setAlignment(Qt.AlignCenter)
#         self.instalockManagerD = QStackedWidget(self.instalockDraftFrame)
#         self.instalockManagerD.setObjectName(u"instalockManagerD")
#         self.instalockManagerD.setGeometry(QRect(20, 160, 191, 31))
#         self.startDraft = QWidget()
#         self.startDraft.setObjectName(u"startDraft")
#         self.startBtnD = QPushButton(self.startDraft)
#         self.startBtnD.setObjectName(u"startBtnD")
#         self.startBtnD.setGeometry(QRect(40, 0, 101, 31))
#         self.startBtnD.setStyleSheet(u"QPushButton {\n"
# "	font: 87 8pt \"Arial Black\";\n"
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
#         self.instalockManagerD.addWidget(self.startDraft)
#         self.stopDraft = QWidget()
#         self.stopDraft.setObjectName(u"stopDraft")
#         self.stopBtnD = QPushButton(self.stopDraft)
#         self.stopBtnD.setObjectName(u"stopBtnD")
#         self.stopBtnD.setGeometry(QRect(40, 0, 101, 31))
#         self.stopBtnD.setStyleSheet(u"QPushButton {\n"
# "	font: 87 8pt \"Arial Black\";\n"
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
#         self.instalockManagerD.addWidget(self.stopDraft)