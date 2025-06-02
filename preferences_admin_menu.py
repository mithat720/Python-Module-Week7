import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("preferences_admin_menu.ui", self)  # Giriş ekranını yükle
        # pushButton tıklanınca admin ekranını aç
        # self.pushButton.clicked.connect(self.MentorMenu)
        #µself.login_buton_login.clicked.connect(self.admin_ac)
        #self.login_buton_exit.clicked.connect(self.close)

    
    def Preferences_Admin_Menu(self):
        self.window =MainWindow()
        self.window.show()
        self.close()  # Giriş ekranını kapatmak istersen


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
