import sys
import gspread
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6 import uic
from oauth2client.service_account import ServiceAccountCredentials
from user_preference_menu import MainWindow as PreferenceMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interviews.ui", self)

        # Google Sheets dosya ID'si
        self.SHEET_ID = "1llV1MYFuIQRBbIvzVx09Rk0--_Lc00vRHltdzk7_3i0"

        try:
            self.df = get_data_from_google_sheet(self.SHEET_ID)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Google Sheets verisi alınamadı:\n{e}")
            return

        # Buton işlevleri
        self.interview_buton_search.clicked.connect(self.search_record)
        self.interview_buton_sub_poject.clicked.connect(self.filter_submitted_projects)
        self.interview_buton_arriv_project.clicked.connect(self.filter_arrived_projects)
        self.interview_buton_backmenu.clicked.connect(self.go_back_menu)
        self.interview_buton_exit.clicked.connect(self.close)

    def populate_table(self, df):
        table = self.interview_table_result
        table.setRowCount(0)
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)

        for row_idx, row in df.iterrows():
            table.insertRow(row_idx)
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                table.setItem(row_idx, col_idx, item)

    def search_record(self):
        text = self.interview_linedit_input.text().strip().lower()
        if not text:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir isim giriniz.")
            return

        if "Adınız Soyadınız" not in self.df.columns:
            QMessageBox.critical(self, "Hata", "'Adınız Soyadınız' sütunu bulunamadı.")
            return

        result = self.df[self.df["Adınız Soyadınız"].str.lower().str.contains(text, na=False)]
        if result.empty:
            QMessageBox.information(self, "Sonuç", "Eşleşen kayıt bulunamadı.")
        self.populate_table(result)

    def filter_submitted_projects(self):
        if "Proje gonderilis tarihi" not in self.df.columns:
            QMessageBox.critical(self, "Hata", "'Proje gonderilis tarihi' sütunu bulunamadı.")
            return

        result = self.df[self.df["Proje gonderilis tarihi"].notna()]
        self.populate_table(result)

    def filter_arrived_projects(self):
        if "Projenin gelis tarihi" not in self.df.columns:
            QMessageBox.critical(self, "Hata", "'Projenin gelis tarihi' sütunu bulunamadı.")
            return

        result = self.df[self.df["Projenin gelis tarihi"].notna()]
        self.populate_table(result)

    def go_back_menu(self):
        self.pref_window = PreferenceMenu()
        self.pref_window.show()
        self.close()

# Google Sheet verisini çeken yardımcı fonksiyon
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
