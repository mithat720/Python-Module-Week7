# Form implementation generated from reading ui file 'interviews.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 566)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Icons/png/rsz_rsz_logo_vit-7-3-2.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setMaximumSize(QtCore.QSize(225, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Search_tetx = QtWidgets.QLineEdit(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search_tetx.sizePolicy().hasHeightForWidth())
        self.Search_tetx.setSizePolicy(sizePolicy)
        self.Search_tetx.setMinimumSize(QtCore.QSize(205, 0))
        self.Search_tetx.setObjectName("Search_tetx")
        self.verticalLayout.addWidget(self.Search_tetx)
        self.btn_search = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        self.btn_search.setMinimumSize(QtCore.QSize(205, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/png/IMG-20250529-WA0013.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QtCore.QSize(16, 16))
        self.btn_search.setObjectName("btn_search")
        self.verticalLayout.addWidget(self.btn_search)
        self.btnFarkliKayit_2 = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFarkliKayit_2.sizePolicy().hasHeightForWidth())
        self.btnFarkliKayit_2.setSizePolicy(sizePolicy)
        self.btnFarkliKayit_2.setMinimumSize(QtCore.QSize(205, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnFarkliKayit_2.setFont(font)
        self.btnFarkliKayit_2.setStyleSheet("QPushButton {\n"
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
        icon1.addPixmap(QtGui.QPixmap("Icons/png/IMG-20250529-WA0006.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFarkliKayit_2.setIcon(icon1)
        self.btnFarkliKayit_2.setObjectName("btnFarkliKayit_2")
        self.verticalLayout.addWidget(self.btnFarkliKayit_2)
        self.btnFiltrelenmis_2 = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFiltrelenmis_2.sizePolicy().hasHeightForWidth())
        self.btnFiltrelenmis_2.setSizePolicy(sizePolicy)
        self.btnFiltrelenmis_2.setMinimumSize(QtCore.QSize(205, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnFiltrelenmis_2.setFont(font)
        self.btnFiltrelenmis_2.setStyleSheet("QPushButton {\n"
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
        icon2.addPixmap(QtGui.QPixmap("Icons/png/IMG-20250529-WA0007.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFiltrelenmis_2.setIcon(icon2)
        self.btnFiltrelenmis_2.setObjectName("btnFiltrelenmis_2")
        self.verticalLayout.addWidget(self.btnFiltrelenmis_2)
        self.btnMentorTanimlanan_8 = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMentorTanimlanan_8.sizePolicy().hasHeightForWidth())
        self.btnMentorTanimlanan_8.setSizePolicy(sizePolicy)
        self.btnMentorTanimlanan_8.setMinimumSize(QtCore.QSize(205, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/png/IMG-20250529-WA0023.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMentorTanimlanan_8.setIcon(icon3)
        self.btnMentorTanimlanan_8.setObjectName("btnMentorTanimlanan_8")
        self.verticalLayout.addWidget(self.btnMentorTanimlanan_8)
        self.btnMentorTanimlanan_9 = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnMentorTanimlanan_9.sizePolicy().hasHeightForWidth())
        self.btnMentorTanimlanan_9.setSizePolicy(sizePolicy)
        self.btnMentorTanimlanan_9.setMinimumSize(QtCore.QSize(205, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/png/exit-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMentorTanimlanan_9.setIcon(icon4)
        self.btnMentorTanimlanan_9.setObjectName("btnMentorTanimlanan_9")
        self.verticalLayout.addWidget(self.btnMentorTanimlanan_9)
        self.horizontalLayout_3.addWidget(self.frame)
        self.tblSonuclar_2 = QtWidgets.QTableWidget(parent=self.frame_3)
        self.tblSonuclar_2.setObjectName("tblSonuclar_2")
        self.tblSonuclar_2.setColumnCount(5)
        self.tblSonuclar_2.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblSonuclar_2.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_3.addWidget(self.tblSonuclar_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "C R M - Interviews"))
        self.btn_search.setText(_translate("MainWindow", "Search"))
        self.btnFarkliKayit_2.setText(_translate("MainWindow", "Submitted Project"))
        self.btnFiltrelenmis_2.setText(_translate("MainWindow", "Project Arrivals"))
        self.btnMentorTanimlanan_8.setText(_translate("MainWindow", "Back Menu "))
        self.btnMentorTanimlanan_9.setText(_translate("MainWindow", "Exit"))
        item = self.tblSonuclar_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tblSonuclar_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tblSonuclar_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tblSonuclar_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tblSonuclar_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "E-Mail"))
        item = self.tblSonuclar_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefon"))
        item = self.tblSonuclar_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Zip Code"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())