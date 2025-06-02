import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt

class Admin_Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Admin_Menu.ui", self)  # Giriş ekranını yükle
        self.setWindowTitle("Admin Menu")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # Frameless window
        self.admin_menu_buton_prefencemenu.clicked.connect(self.open_preferences_admin_menu)
        self.admin_menu_buton_exit.clicked.connect(self.close)

    # def open_preferences_admin_menu(self):
    #     from preferences_admin_menu import Preferences_Admin_Menu
    #     self.preferences_admin_menu = Preferences_Admin_Menu()
    #     self.preferences_admin_menu.show()
    #     self.close()

    def open_preferences_admin_menu(self):
        from preferences_admin_menu import MainWindow  # Prefereces_Admin_Menu is imported from preferences_admin_menu.py
        self.preferences_admin_menu = MainWindow()  # Preferences_Admin_Menu sınıfından bir örnek oluştur
        self.preferences_admin_menu.show()
        self.close()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    pencere = Admin_Menu()
    pencere.show()
    sys.exit(app.exec())