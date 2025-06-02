import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from login import LoginPage



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec())
