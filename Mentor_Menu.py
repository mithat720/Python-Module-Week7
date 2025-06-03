import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Mentor_Menu.ui", self)  # Giriş ekranını yükle
        # pushButton tıklanınca admin ekranını aç
        # self.pushButton.clicked.connect(self.MentorMenu)
        #µself.login_buton_login.clicked.connect(self.admin_ac)
        self.mentor_menu_buton_exit.clicked.connect(self.close)
        self.mentor_menu_buton_preferences.clicked.connect(self.open_user_preference_menu)

    def open_user_preference_menu(self):
        from user_preference_menu import MainWindow
        self.preference_menu = MainWindow()
        self.preference_menu.show()
        self.close()

if __name__ == "__main__":
    

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
