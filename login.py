import sys
import gspread
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt6 import uic
from PyQt6.QtCore import Qt
from oauth2client.service_account import ServiceAccountCredentials


def get_users_from_sheet(sheet_id):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    worksheet = client.open_by_key(sheet_id).sheet1
    data = worksheet.get_all_values()
    return pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame()


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle("Login Page")

        self.login_password_show.stateChanged.connect(self.toggle_password_visibility)
        self.login_buton_login.clicked.connect(self.control_login)
        self.login_buton_exit.clicked.connect(self.close)
        self.login_line_edit_username.returnPressed.connect(lambda: self.login_line_edit_password.setFocus()) # Enter tuşuna basıldığında parola alanına geç
        self.login_line_edit_password.returnPressed.connect(self.control_login) # Enter tuşuna basıldığında giriş yap

    def toggle_password_visibility(self):
        if self.login_password_show.isChecked():
            self.login_line_edit_password.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.login_line_edit_password.setEchoMode(QLineEdit.EchoMode.Password)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def control_login(self):
        username = self.login_line_edit_username.text()
        password = self.login_line_edit_password.text()

        sheet_id = "1I0YBsw4ghlD1GPEhOb_DZyx5F0vd64wc1c8mk6LlMNg"
        df = get_users_from_sheet(sheet_id)

        # Beklenen başlıklar: kullanici, parola, yetki
        if not {"kullanici", "parola", "yetki"}.issubset(df.columns):
            self.mesaj("Sheet başlıkları hatalı. 'kullanici', 'parola', 'yetki' olmalı.")
            return

        match = df[(df["kullanici"] == username) & (df["parola"] == password)]

        if not match.empty:
            yetki = match.iloc[0]["yetki"].strip().lower()
            if yetki == "admin":
                self.mesaj("Login Admin is Successful")
                self.open_preferences_admin()
            elif yetki == "user":
                self.mesaj("User Login is Successful")
                self.open_preference_menu()
            else:
                self.mesaj(f"Bilinmeyen yetki türü: {yetki}")
            return

        self.mesaj("Login Failed, Please try again.")

    def mesaj(self, mesaj):
        mesaj_box = QMessageBox()
        mesaj_box.setText(mesaj)
        mesaj_box.exec()

    def open_preferences_admin(self):
        from preferences_admin_menu import MainWindow
        self.preferences_admin_menu = MainWindow()
        self.preferences_admin_menu.show()
        self.close()

    def open_preference_menu(self):
        from user_preference_menu import MainWindow
        self.preference_menu = MainWindow()
        self.preference_menu.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec())
