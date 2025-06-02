import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from login import LoginPage



app = QApplication(sys.argv)
window = LoginPage()
window.show()
sys.exit(app.exec())
