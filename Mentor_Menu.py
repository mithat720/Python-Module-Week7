import sys
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic
#from PyQt6.QtCore import Qt

from user_preference_menu import MainWindow as PreferenceMenuWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Mentor_Menu.ui", self)

        self.mentor_menu_buton_exit.clicked.connect(self.close)
        self.mentor_menu_buton_all_applications.clicked.connect(self.load_google_sheet_into_table)
        self.mentor_menu_buton_preferences.clicked.connect(self.open_preference_menu)
    #    self.setWindowFlag(Qt.WindowType.FramelessWindowHint) #Frameless window

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.MouseButton.LeftButton:
    #         self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
    #         event.accept()

    # def mouseMoveEvent(self, event):
    #     if event.buttons() == Qt.MouseButton.LeftButton:
    #         self.move(event.globalPosition().toPoint() - self.drag_position)
    #         event.accept()

        # Arama tetikleyicileri
        self.mentor_menu_buton_search.clicked.connect(self.filter_table)
        self.mentor_menu_lineedit_input.returnPressed.connect(self.filter_table)

        # ComboBox filtreleme tetikleyicisi
        self.mentor_menu_combobox.currentIndexChanged.connect(self.filter_table)

    def load_google_sheet_into_table(self):
        sheet_id = "1z0ZIEzs1VqdB-3JlMmg-G3ud3T6FFOvtmhI45rBqvTI"
        df = get_data_from_google_sheet(sheet_id)
        self.df = df  # Tüm veri bellekte tutulur
        self.populate_combobox(df)
        self.update_table(df)

    def populate_combobox(self, df):
        self.mentor_menu_combobox.blockSignals(True)  # Geçici olarak sinyalleri kapat
        self.mentor_menu_combobox.clear()
        column_name = "VIT projesinin tamamına katılması uygun olur"

        if column_name in df.columns:
            options = sorted(set(df[column_name].dropna()))
            self.mentor_menu_combobox.addItem("Tümünü Göster")
            for option in options:
                self.mentor_menu_combobox.addItem(option)
        self.mentor_menu_combobox.blockSignals(False)

    def update_table(self, df):
        table = self.mentor_menu_table_result
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                table.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

    def filter_table(self):
        if not hasattr(self, 'df'):
            return  # Veri yüklenmeden filtre yapılmasın

        filtered_df = self.df

        # 1. Arama kutusuna göre filtrele
        input_text = self.mentor_menu_lineedit_input.text().strip().lower()
        if input_text and "Mentinin adi soyadi" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Mentinin adi soyadi"].str.lower().str.startswith(input_text)]

        # 2. ComboBox'a göre filtrele
        selected_value = self.mentor_menu_combobox.currentText()
        column_name = "VIT projesinin tamamına katılması uygun olur"
        if selected_value != "Tümünü Göster" and column_name in filtered_df.columns:
            filtered_df = filtered_df[filtered_df[column_name] == selected_value]

        self.update_table(filtered_df)

    def open_preference_menu(self):
        self.preference_menu = PreferenceMenuWindow()
        self.preference_menu.show()
        self.close()

def get_data_from_google_sheet(sheet_id):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    worksheet = client.open_by_key(sheet_id).sheet1

    data = worksheet.get_all_values()
    return pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
