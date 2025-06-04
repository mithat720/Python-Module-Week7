import sys
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6 import uic
from user_preference_menu import MainWindow as PreferenceMenuWindow  # Menüyü açmak için
from PyQt6.QtCore import Qt

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Applications.ui", self)

        # Google Sheets dosya ID'si
        self.SHEET_ID = "11A_KFbc2FVwURc7PB18VfUiFiWlFX7Y_XR8XVoii-fCQ"

        try:
            self.df = get_data_from_google_sheet(self.SHEET_ID)
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Google Sheets verisi alınamadı:\n{e}")
            return

        # Buton bağlantıları
        self.applications_buton_exit.clicked.connect(self.close)
        self.applications_buton_back_menu.clicked.connect(self.open_user_preference_menu)
        self.applications_buton_filtered_applications.clicked.connect(self.handle_google_sheet_upload)

        # Diğer butonlar pasif (isteğe bağlı etkinleştirilebilir)
        self.applications_buton_search.clicked.connect(self.not_implemented)
        self.applications_buton_all_aplications.clicked.connect(self.load_google_sheet_into_table)
        self.applications_buton_planned_meeting.clicked.connect(self.not_implemented)
        self.applications_buton_unscheduledmeeting.clicked.connect(self.not_implemented)
        self.applications_buton_previousvit.clicked.connect(self.not_implemented)
        self.applications_buton_repeated_registration.clicked.connect(self.not_implemented)
        self.applications_buton_different_registration.clicked.connect(self.not_implemented)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint) #Frameless window


     # Arama tetikleyicileri
        self.applications_buton_search.clicked.connect(self.filter_table)
        self.applications_linedit_input.returnPressed.connect(self.filter_table)

    def load_google_sheet_into_table(self):
        sheet_id = "1A_KFbc2FVwURc7PB18VfUiFiWlFX7Y_XR8XVoii-fCQ"
        df = get_data_from_google_sheet(sheet_id)
        self.df = df  # Tüm veri bellekte tutulur
        self.update_table(df)

    def update_table(self, df):
        table = self.applications_table
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
        input_text = self.applications_linedit_input.text().strip().lower()
        if input_text and "Mentinin adi soyadi" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Mentinin adi soyadi"].str.lower().str.startswith(input_text)]

   
        self.update_table(filtered_df)

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
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
