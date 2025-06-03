import sys
from PyQt6.QtWidgets import QApplication
from login import LoginPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec())
