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

        # Google Sheets file ID
        self.SHEET_ID = "1rrxfZPTK6kPh3DGOEugtWbrtTfzaq6E9-4Zf1PK8XTE"

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
                table.setItem(row_idx, col_idx, item)

    def search_records(self):
        """Search records in the 'Adınız Soyadınız' column that start with the entered text."""
        search_text = self.interview_linedit_input.text().strip().lower()
        if not search_text:
            QMessageBox.warning(self, "Warning", "Please enter a name to search.")
            return

        if "Adınız Soyadınız" not in self.df.columns:
            QMessageBox.critical(self, "Error", "'Adınız Soyadınız' column not found.")
            return

        filtered = self.df.dropna(subset=["Adınız Soyadınız"])
        filtered = filtered[filtered["Adınız Soyadınız"].apply(lambda x: x.strip().lower().startswith(search_text))]
        filtered = filtered.reset_index(drop=True)

        if filtered.empty:
            QMessageBox.information(self, "Search Result", "No matching record found.")
        else:
            self.populate_table(filtered)

    def filter_submitted_projects(self):
        """Display records where the 'Proje gonderilis tarihi' column is not empty."""
        column = "Proje gonderilis tarihi"
        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column not found.")
            return

        submitted = self.df[self.df[column].notna() & (self.df[column].astype(str).str.strip() != "")]
        submitted = submitted.reset_index(drop=True)
        if submitted.empty:
            QMessageBox.information(self, "Result", "No submitted project record found.")
        else:
            self.populate_table(submitted)

    def filter_arrived_projects(self):
        """Display records where the 'Projenin gelis tarihi' column is not empty."""
        column = "Projenin gelis tarihi"
        if column not in self.df.columns:
            QMessageBox.critical(self, "Error", f"'{column}' column not found.")
            return

        arrived = self.df[self.df[column].notna() & (self.df[column].astype(str).str.strip() != "")]
        arrived = arrived.reset_index(drop=True)
        if arrived.empty:
            QMessageBox.information(self, "Result", "No project arrival record found.")
        else:
            self.populate_table(arrived)

    def go_back_menu(self):
        """Return to the user preference menu."""
        self.pref_window = PreferenceMenu()
        self.pref_window.show()
        self.close()

def get_data_from_google_sheet(sheet_id):
    """Fetch data from Google Sheets and return it as a DataFrame."""
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

