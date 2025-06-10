import sys
import gspread
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6 import uic
from PyQt6.QtCore import Qt
from oauth2client.service_account import ServiceAccountCredentials
from user_preference_menu import MainWindow as PreferenceMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("interviews.ui", self)

        # Google Sheets file ID
        self.SHEET_ID = "1rrxfZPTK6kPh3DGOEugtWbrtTfzaq6E9-4Zf1PK8XTE"
        # Try to load data from Google Sheets
        try:
            self.df = get_data_from_google_sheet(self.SHEET_ID)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch data from Google Sheets:\n{e}")
            return

        self.populate_table(self.df)

        self.interview_buton_search.clicked.connect(self.search_records)
        self.interview_buton_sub_poject.clicked.connect(self.filter_submitted_projects)
        self.interview_buton_arriv_project.clicked.connect(self.filter_arrived_projects)
        self.interview_buton_backmenu.clicked.connect(self.go_back_menu)
        self.interview_buton_exit.clicked.connect(self.close)

    def populate_table(self, df):
        """Populate the table with DataFrame content."""
        df = df.reset_index(drop=True)
        table = self.interview_table_result
        table.clear()
        table.setRowCount(len(df))
        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)

        for row_idx, row in df.iterrows():
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # center align text
                table.setItem(row_idx, col_idx, item)

        
        table.resizeColumnsToContents()

        # Makes the header stretch to fill the available space
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  
    def search_records(self):
        """Searches for records based on the input text in the 'Adınız Soyadınız' column."""
        search_text = self.interview_linedit_input.text().strip().lower()
        column = "Adınız Soyadınız"

        if not search_text:
            QMessageBox.warning(self, "Warning", "Please enter the searched text.")
            return

        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column is not found.")
            return

        filtered = self.df[self.df[column].notna()]
        filtered = filtered[filtered[column].str.strip().str.lower().str.startswith(search_text)]

        if filtered.empty:
            QMessageBox.information(self, "Search result", "No matching records.")
        else:
            self.populate_table(filtered.reset_index(drop=True))

    def filter_submitted_projects(self):
        """Shows sent projects ."""
        column = "Proje gonderilis tarihi"
        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column is not found.")
            return

        submitted = self.df[self.df[column].notna() & (self.df[column].astype(str).str.strip() != "")]
        submitted = submitted.reset_index(drop=True)
        if submitted.empty:
            QMessageBox.information(self, "Result", "No submitted project foound.")
        else:
            self.populate_table(submitted)

    def filter_arrived_projects(self):
        """ It shows columns where Prohenin gelis tarihi is not empty."""
        column = "Projenin gelis tarihi"
        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column is not found.")
            return

        arrived = self.df[self.df[column].notna() & (self.df[column].astype(str).str.strip() != "")]
        arrived = arrived.reset_index(drop=True)
        if arrived.empty:
            QMessageBox.information(self, "Result", "No macthing records for projects arrivals.")
        else:
            self.populate_table(arrived)

    def go_back_menu(self):
       
        self.pref_window = PreferenceMenu()
        self.pref_window.show()
        self.close()

def get_data_from_google_sheet(sheet_id):
    """Google Sheets'ten veri çeker ve DataFrame olarak döndürür."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    worksheet = client.open_by_key(sheet_id).sheet1
    data = worksheet.get_all_values()
    return pd.DataFrame(data[1:], columns=data[0]) if len(data) > 1 else pd.DataFrame()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
