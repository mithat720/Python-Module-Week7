import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class Admin_Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Admin_Menu.ui", self)  # Giriş ekranını yükle
        # pushButton tıklanınca admin ekranını aç
        # self.pushButton.clicked.connect(self.MentorMenu)
        #µself.login_buton_login.clicked.connect(self.admin_ac)
        #self.login_buton_exit.clicked.connect(self.close)

    
    def Admin_Menu(self):
        self.Admin_Menu = Admin_Menu()
        self.Admin_Menu.show()
        self.close()  # Giriş ekranını kapatmak istersen


app = QApplication(sys.argv)
pencere = Admin_Menu()
pencere.show()
sys.exit(app.exec())
