import sys
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic
from user_preference_menu import MainWindow as PreferenceMenuWindow  # Menüyü açmak için

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Applications.ui", self)

        # Buton bağlantıları
        self.applications_buton_exit.clicked.connect(self.close)
        self.applications_buton_back_menu.clicked.connect(self.open_user_preference_menu)
        self.applications_buton_filtered_applications.clicked.connect(self.handle_google_sheet_upload)

        # Diğer butonlar pasif (isteğe bağlı etkinleştirilebilir)
        self.applications_buton_search.clicked.connect(self.not_implemented)
        self.applications_buton_all_aplications.clicked.connect(self.not_implemented)
        self.applications_buton_planned_meeting.clicked.connect(self.not_implemented)
        self.applications_buton_unscheduledmeeting.clicked.connect(self.not_implemented)
        self.applications_buton_previousvit.clicked.connect(self.not_implemented)
        self.applications_buton_repeated_registration.clicked.connect(self.not_implemented)
        self.applications_buton_different_registration.clicked.connect(self.not_implemented)

    def showEvent(self, event):
        """Pencere gösterildiğinde veriler otomatik olarak Google Sheet'ten yüklenir"""
        super().showEvent(event)
        self.handle_google_sheet_upload()

    def handle_google_sheet_upload(self):
        sheet_id = "1A_KFbc2FVwURc7PB18VfUiFiWlFX7Y_XR8XVoii-fCQ"  # Kendi sheet ID’in
        df = get_data_from_google_sheet(sheet_id)
        self.display_data_in_table(df)

    def display_data_in_table(self, df):
        try:
            self.applications_table.setRowCount(len(df))
            self.applications_table.setColumnCount(len(df.columns))
            self.applications_table.setHorizontalHeaderLabels(df.columns)

            for row in range(len(df)):
                for col in range(len(df.columns)):
                    item = str(df.iat[row, col])
                    self.applications_table.setItem(row, col, QTableWidgetItem(item))
        except Exception as e:
            print(f"Tabloya veri aktarım hatası: {e}")

    def open_user_preference_menu(self):
        self.preference_menu = PreferenceMenuWindow()
        self.preference_menu.show()
        self.close()

    def not_implemented(self):
        print("Bu buton henüz işlevsel değil.")

# Yardımcı fonksiyon: Google Sheet'ten veri alma
def get_data_from_google_sheet(sheet_id):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)
        worksheet = client.open_by_key(sheet_id).sheet1
        data = worksheet.get_all_values()
        return pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame()
    except Exception as e:
        print(f"Google Sheet veri çekme hatası: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
