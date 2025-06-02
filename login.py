import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import Qt

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
            self.show_message("Hatalı kullanıcı adı veya şifre")

    def show_message(self, mesaj):
        QMessageBox.information(self, "Bilgi", mesaj)

    def open_preferences_admin(self):
        from preferences_admin_menu import MainWindow
        self.admin_window = MainWindow()
        self.admin_window.show()
        self.close()

    def open_preference_menu(self):
        from preference_menu import MainWindow
        self.user_window = MainWindow()
        self.user_window.show()
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
    window = LoginPage()
    window.show()
    sys.exit(app.exec())
