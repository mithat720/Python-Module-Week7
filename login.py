import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import Qt

admin_list = [{"user": "admin", "password": "admin"},
    {"user": "admin1", "password": "admin1"}]
user_list = [{"user": "user", "password": "user"},
    {"user": "user1", "password": "user11"}]
class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Login Page")

        self.login_pass_show.stateChanged.connect(self.toggle_password_visibility)
        self.login_buton_login.clicked.connect(self.control_login)
        self.login_buton_exit.clicked.connect(self.close)

    def toggle_password_visibility(self):
        from PyQt6.QtGui import QLineEdit
        self.login_line_password.setEchoMode(
            QLineEdit.EchoMode.Normal if self.login_pass_show.isChecked()
            else QLineEdit.EchoMode.Password
        )

    def control_login(self):
        from drive_utils import read_excel_from_drive

        FILE_ID = "1I0YBsw4ghlD1GPEhOb_DZyx5F0vd64wc1c8mk6LlMNg"  # Google Drive'daki Kullanicilar.xlsx ID
        try:
            df = read_excel_from_drive(FILE_ID)
        except Exception as e:
            self.show_message(f"Drive'dan dosya alınamadı: {e}")
            return

        username = self.login_lineedit_username.text().strip()
        password = self.login_lineedit_password.text().strip()

        match = df[(df["kullanici"] == username) & (df["parola"] == password)]

        if not match.empty:
            yetki = match.iloc[0]["yetki"].strip().lower()
            if yetki == "admin":
                self.show_message("Admin girişi başarılı")
                self.open_preferences_admin()
            else:
                self.show_message("Kullanıcı girişi başarılı")
                self.open_preference_menu()
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
        
        username = self.login_lineedit_username.text()
        password = self.login_lineedit_password.text()

        for admin in admin_list:
            if admin["user"] == username and admin["password"] == password:
                self.mesaj("Login Admin is Successful")
                self.open_preferences_admin()
                return
        for user in user_list:
            if user["user"] == username and user["password"] == password:
                self.mesaj("User Login is Successful")
                self.open_preference_menu()
                return
        self.mesaj("Login Failed, Please try again")

        
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
    window = LoginPage()
    window.show()
    sys.exit(app.exec())
