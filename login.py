import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from preferences_admin_menu import Preferences_Admin_Menu  

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)  # Giriş ekranını yükle
        self.login_buton_login.clicked.connect(self.open_preferences_admin)
        self.login_buton_exit.clicked.connect(self.close)

    # def open_preferences_admin_menu(self):
    #     self.admin_menu = Preferences_Admin_Menu()  
    #     self.admin_menu.show()
    #     self.close()  

app = QApplication(sys.argv)
login_page = LoginPage()
login_page.show()
sys.exit(app.exec())
