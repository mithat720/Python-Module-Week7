import sys
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import uic
from user_preference_menu import MainWindow as PreferenceMenuWindow  

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Applications.ui", self)

        self.applications_buton_exit.clicked.connect(self.close)
        self.applications_buton_back_menu.clicked.connect(self.open_user_preference_menu)
        self.applications_buton_filtered_applications.clicked.connect(self.handle_google_sheet_upload)

        self.applications_buton_search.clicked.connect(self.filter_table)
        self.applications_buton_all_aplications.clicked.connect(self.handle_google_sheet_upload)
        self.applications_buton_planned_meeting.clicked.connect(self.show_planned_meetings)
        self.applications_buton_unscheduledmeeting.clicked.connect(self.show_unscheduled_meetings)
        self.applications_buton_previousvit.clicked.connect(self.not_implemented)
        self.applications_buton_repeated_registration.clicked.connect(self.not_implemented)
        self.applications_buton_different_registration.clicked.connect(self.not_implemented)
        self.applications_linedit_input.returnPressed.connect(self.filter_table)
        self.applications_linedit_input.textChanged.connect(self.filter_table)



    # def showEvent(self, event): #Automatic datas loading.
    #     super().showEvent(event)
    #     self.handle_google_sheet_upload()

    # def filter_table(self):
    #     if not hasattr(self, 'df'):
    #         return
    #     input_text = self.applications_linedit_input.text().strip().lower()
    #     filtered_df = self.df
    #     if input_text and "Adınız Soyadınız" in filtered_df.columns:
    #         filtered_df = filtered_df[filtered_df["Adınız Soyadınız"].str.lower().str.contains(input_text)]
    #     self.display_data_in_table(filtered_df)

    # def filter_table(self, df):
    #     table = self.applications_table
    #     table.setRowCount(0) # Clear existing rows

    #     if df.empty:
    #         # If the DataFrame is empty, ensure columns are set if self.df was loaded successfully
    #         if hasattr(self, 'df') and not self.df.empty:
    #             table.setColumnCount(len(self.df.columns))
    #             table.setHorizontalHeaderLabels(self.df.columns.tolist())
    #         else:
    #             table.setColumnCount(0) # If self.df also empty, no columns
    #         return 

    #     table.setColumnCount(len(df.columns))
    #     table.setHorizontalHeaderLabels(df.columns)
        
    #     table.setRowCount(len(df)) # Set the table's row count to the DataFrame's row count

    #     for row_idx in range(len(df)):
    #         for col_idx, column_name in enumerate(df.columns):
    #             value = df.iloc[row_idx, col_idx] # Safer access with .iloc
    #             item = QTableWidgetItem(str(value))
    #             table.setItem(row_idx, col_idx, item)

    #     table.viewport().update() # Notify Qt that the table has been updated

    def filter_table(self):
        if not hasattr(self, 'df'):
            return
        input_text = self.applications_linedit_input.text().strip().lower()
        filtered_df = self.df
        if input_text and "Adınız Soyadınız" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Adınız Soyadınız"].str.lower().str.contains(input_text)]
            self.display_data_in_table(filtered_df)


    def handle_google_sheet_upload(self):
        sheet_id = "1A_KFbc2FVwURc7PB18VfUiFiWlFX7Y_XR8XVoii-fCQ"  # Kendi sheet ID’in
        df = get_data_from_google_sheet(sheet_id)
        self.df = df
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

    def show_planned_meetings(self):
        if "Mentor gorusmesi" in self.df.columns:
            df = self.df[self.df["Mentor gorusmesi"] == "OK"]
            self.display_data_in_table(df)
            print("Sütunlar:", self.df.columns.tolist())


    def show_unscheduled_meetings(self):
        if "Mentor gorusmesi" in self.df.columns:
            df = self.df[self.df["Mentor gorusmesi"] != "ATANMADI"]
            self.display_data_in_table(df)



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
