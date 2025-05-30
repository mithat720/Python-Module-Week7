# Form implementation generated from reading ui file 'Mentor_Menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 562)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget {\n"
"    background-color: #f0f8ff;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    background-color: #ffffff;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Icons/png/rsz_rsz_logo_vit-7-3-2.png"))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnMentorTanimlanan_7 = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMentorTanimlanan_7.sizePolicy().hasHeightForWidth())
        self.btnMentorTanimlanan_7.setSizePolicy(sizePolicy)
        self.btnMentorTanimlanan_7.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnMentorTanimlanan_7.setFont(font)
        self.btnMentorTanimlanan_7.setStyleSheet("QPushButton {\n"
"    background-color: #55aaff;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8263c6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #594097;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/png/IMG-20250529-WA0007.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMentorTanimlanan_7.setIcon(icon)
        self.btnMentorTanimlanan_7.setIconSize(QtCore.QSize(24, 24))
        self.btnMentorTanimlanan_7.setObjectName("btnMentorTanimlanan_7")
        self.horizontalLayout_2.addWidget(self.btnMentorTanimlanan_7)
        self.btn_search = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("QPushButton {\n"
"    background-color: #55aaff;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8263c6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #594097;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/png/IMG-20250529-WA0013.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QtCore.QSize(24, 24))
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_2.addWidget(self.btn_search)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Search_tetx = QtWidgets.QLineEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_tetx.sizePolicy().hasHeightForWidth())
        self.Search_tetx.setSizePolicy(sizePolicy)
        self.Search_tetx.setMinimumSize(QtCore.QSize(250, 0))
        self.Search_tetx.setObjectName("Search_tetx")
        self.horizontalLayout_2.addWidget(self.Search_tetx)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setEnabled(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnMentorTanimlanan_8 = QtWidgets.QPushButton(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMentorTanimlanan_8.sizePolicy().hasHeightForWidth())
        self.btnMentorTanimlanan_8.setSizePolicy(sizePolicy)
        self.btnMentorTanimlanan_8.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnMentorTanimlanan_8.setFont(font)
        self.btnMentorTanimlanan_8.setStyleSheet("QPushButton {\n"
"    background-color: #55aaff;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8263c6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #594097;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/png/Prefenens.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMentorTanimlanan_8.setIcon(icon2)
        self.btnMentorTanimlanan_8.setIconSize(QtCore.QSize(24, 24))
        self.btnMentorTanimlanan_8.setObjectName("btnMentorTanimlanan_8")
        self.horizontalLayout.addWidget(self.btnMentorTanimlanan_8)
        self.btnMentorTanimlanan_9 = QtWidgets.QPushButton(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMentorTanimlanan_9.sizePolicy().hasHeightForWidth())
        self.btnMentorTanimlanan_9.setSizePolicy(sizePolicy)
        self.btnMentorTanimlanan_9.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnMentorTanimlanan_9.setFont(font)
        self.btnMentorTanimlanan_9.setStyleSheet("QPushButton {\n"
"    background-color: #55aaff;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #8263c6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #594097;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/png/exit-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMentorTanimlanan_9.setIcon(icon3)
        self.btnMentorTanimlanan_9.setIconSize(QtCore.QSize(24, 24))
        self.btnMentorTanimlanan_9.setObjectName("btnMentorTanimlanan_9")
        self.horizontalLayout.addWidget(self.btnMentorTanimlanan_9)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.tblSonuclar = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tblSonuclar.setObjectName("tblSonuclar")
        self.tblSonuclar.setColumnCount(5)
        self.tblSonuclar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tblSonuclar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "C R M - Mentor Menu"))
        self.btnMentorTanimlanan_7.setText(_translate("MainWindow", "    All Applications"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.Search_tetx.setText(_translate("MainWindow", "ARANACAK METNİ GİRİNİZ..."))
        self.btnMentorTanimlanan_8.setText(_translate("MainWindow", "Prefenens"))
        self.btnMentorTanimlanan_9.setText(_translate("MainWindow", "Exit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "VIT-1 Kursuna katılması uygun olur"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VIT-3 Kursuna katılması uygun olur"))
        item = self.tblSonuclar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Datum"))
        item = self.tblSonuclar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tblSonuclar.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mentor"))
        item = self.tblSonuclar.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IT-Informatie"))
        item = self.tblSonuclar.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "intensiteit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())