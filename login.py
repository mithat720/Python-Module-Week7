import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)  # Load the login UI
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint) #Frameless window
        self.setWindowTitle("Login Page")
        self.login_pass_show.stateChanged.connect(self.toggle_password_visibility)
        self.login_buton_login.clicked.connect(self.control_login)
        self.login_buton_exit.clicked.connect(self.close)


    def toggle_password_visibility(self):
        from PyQt6.QtGui import QLineEdit

        if self.login_pass_show.isChecked():
            self.login_line_password.setEchoMode(QLineEdit.EchoMode.Normal)  # Visible password
        else:
            self.login_line_password.setEchoMode(QLineEdit.EchoMode.Password)  # Hidden password

                
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def control_login(self):
        # Burada giriş kontrolü yapılabilir
        # Örneğin, kullanıcı adı ve şifre kontrolü
        username = self.login_lineedit_username.text()
        password = self.login_lineedit_password.text()
        
        if username == "admin" and password == "admin":
            self.mesaj("Login Admin is Successful")
            self.open_preferences_admin()
            
        elif username == "user" and password == "user":
            self.mesaj("User Login is Successful")
            self.open_preference_menu()
        else:
            self.mesaj("Login Failed, Please try again")
            return False
        
    def mesaj(self, mesaj):
        from PyQt6.QtWidgets import QMessageBox
        mesaj_box = QMessageBox()        
        mesaj_box.setText(mesaj)
        mesaj_box.exec()

    def open_preferences_admin(self):
        from preferences_admin_menu import MainWindow  # Prefereces_Admin_Menu is imported from preferences_admin_menu.py
        self.preferences_admin_menu = MainWindow()  # Preferences_Admin_Menu sınıfından bir örnek oluştur
        self.preferences_admin_menu.show()
        self.close()

    def open_preference_menu(self):
        from preference_menu import MainWindow
        self.preference_menu = MainWindow()
        self.preference_menu.show()
        self.close()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    pencere = LoginPage()
    pencere.show()
    sys.exit(app.exec())