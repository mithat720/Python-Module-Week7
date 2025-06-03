import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("preferences_admin_menu.ui", self)  # Giriş ekranını yükle
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Preferences Admin Menu")
        self.preference_admin_menu_button_applications.clicked.connect(self.open_applications)
        self.preference_admin_menu_button_metor_meeting.clicked.connect(self.open_mentor_meeting)  
        self.preference_admin_menu_button_interviews.clicked.connect(self.open_interviews)
        self.preference_admin_menu_button_exit.clicked.connect(self.close)
        self.preference_admin_menu_button_admin_menu.clicked.connect(self.open_admin_menu)
        self.preference_admin_menu_button_main_menu.clicked.connect(self.open_main_menu)
       

    def open_applications(self):
        from Applications import MainWindow
        self.applications_menu = MainWindow()
        self.applications_menu.show()
        self.close()

    def open_mentor_meeting(self):
        from Mentor_Menu import MainWindow
        self.mentor_meeting_menu = MainWindow()
        self.mentor_meeting_menu.show()
        self.close()

    def open_interviews(self):
        from interviews import MainWindow
        self.interviews_menu = MainWindow()
        self.interviews_menu.show()
        self.close()

    def open_admin_menu(self):    
        from Admin_Menu import Admin_Menu
        self.admin_menu = Admin_Menu()
        self.admin_menu.show()
        self.close()

    def open_main_menu(self):    #### Main menumuz yokki.....
        from user_preference_menu import MainWindow
        self.main_menu = MainWindow()
        self.main_menu.show()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    pencere = MainWindow()
    pencere.show()
    sys.exit(app.exec())
