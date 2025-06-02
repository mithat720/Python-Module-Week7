import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from preferences_admin_menu import Preferences_Admin_Menu  # Admin menüsünü içe aktar


class Admin_Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Admin_Menu.ui", self)  # Giriş ekranını yükle
        # pushButton tıklanınca admin ekranını aç
        # self.pushButton.clicked.connect(self.MentorMenu)
        self.admin_menu_buton_prefencemenu.clicked.connect(self.preferences_admin_menu)
        self.admin_menu_buton_exit.clicked.connect(self.close)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    pencere = Admin_Menu()
    pencere.show()
    sys.exit(app.exec())