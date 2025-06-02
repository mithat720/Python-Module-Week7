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

    
if __name__ == "__main__":
    

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
