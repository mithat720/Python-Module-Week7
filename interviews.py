import sys
import gspread
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6 import uic
from oauth2client.service_account import ServiceAccountCredentials

class MainWindow(QMainWindow):
    # parent_window parameter receives a reference to the calling window (can be None if run directly)
    def __init__(self, parent_window=None):
        super().__init__()
        uic.loadUi("interviews.ui", self)
        # We don't store parent_window if we always want to go back to a specific menu,
        # but keep it in __init__ signature for compatibility.
        self.parent_window = parent_window 

        # Google Sheets file ID
        self.SHEET_ID = "1llV1MYFuIQRBbIvzVx09Rk0--_Lc00vRHltdzk7_3i0"

        try:
            self.df = get_data_from_google_sheet(self.SHEET_ID)
            
            if "Adınız Soyadınız" in self.df.columns:
                self.df.loc[:, "Adınız Soyadınız"] = self.df["Adınız Soyadınız"].astype(str).str.strip().str.lower()
                self.df["Adınız Soyadınız"].fillna('', inplace=True)
            else:
                QMessageBox.critical(self, "Error", "'Adınız Soyadınız' column not found.")
                return

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load Google Sheet. Please check the console for details and ensure Google Sheet permissions are correctly set.\nDetails: {e}")
            print(f"ERROR: Google Sheet failed to load in interviews.py. Details: {e}")
            service_account_email = "unknown (check credentials.json)"
            try:
                creds_check = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', ['https://www.googleapis.com/auth/drive'])
                service_account_email = creds_check.client_email
            except Exception:
                pass 
            print(f"Ensure the Google Sheet with ID '{self.SHEET_ID}' has 'Editor' or 'Viewer' permission granted to '{service_account_email}'.")
            print("Also, confirm 'credentials.json' is correctly placed and not corrupted.")
            return

        # Buton bağlantıları
        self.interview_buton_search.clicked.connect(self.search_record)
        self.interview_buton_sub_poject.clicked.connect(self.filter_submitted_projects)
        self.interview_buton_arriv_project.clicked.connect(self.filter_arrived_projects)
        self.interview_buton_backmenu.clicked.connect(self.go_back_menu)
        self.interview_buton_exit.clicked.connect(self.close)

        # Table will now be empty initially.

        # PyQt6 compatible setSectionResizeMode usage
        self.interview_table_result.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Initialize table with correct columns but no rows (empty)
        # This makes sure headers are visible even when the table is empty.
        if hasattr(self, 'df') and not self.df.empty:
            self.interview_table_result.setColumnCount(len(self.df.columns))
            self.interview_table_result.setHorizontalHeaderLabels(self.df.columns.tolist())
        else:
            # Fallback if df couldn't be loaded at all or is empty
            self.interview_table_result.setColumnCount(0)


    def populate_table(self, df):
        table = self.interview_table_result
        table.setRowCount(0) # Clear existing rows

        if df.empty:
            # If the DataFrame is empty, ensure columns are set if self.df was loaded successfully
            if hasattr(self, 'df') and not self.df.empty:
                table.setColumnCount(len(self.df.columns))
                table.setHorizontalHeaderLabels(self.df.columns.tolist())
            else:
                table.setColumnCount(0) # If self.df also empty, no columns
            return 

        table.setColumnCount(len(df.columns))
        table.setHorizontalHeaderLabels(df.columns)
        
        table.setRowCount(len(df)) # Set the table's row count to the DataFrame's row count

        for row_idx in range(len(df)):
            for col_idx, column_name in enumerate(df.columns):
                value = df.iloc[row_idx, col_idx] # Safer access with .iloc
                item = QTableWidgetItem(str(value))
                table.setItem(row_idx, col_idx, item)

        table.viewport().update() # Notify Qt that the table has been updated


    def search_record(self):
        text = self.interview_linedit_input.text().strip().lower()
        if not text:
            # If search text is empty, show a warning and do nothing else
            QMessageBox.warning(self, "Warning", "Please enter a name to search.")
            return # Simply return without populating the table
        
        if "Adınız Soyadınız" not in self.df.columns:
            QMessageBox.critical(self, "Error", "'Adınız Soyadınız' column not found.")
            return

        result = self.df[self.df["Adınız Soyadınız"].str.contains(text, na=False)]
        
        if result.empty:
            QMessageBox.information(self, "Result", "No matching records found!")
            self.populate_table(pd.DataFrame(columns=self.df.columns)) # Clear table but keep headers if no match
        else:
            self.populate_table(result)

    def filter_submitted_projects(self):
        if "Proje gonderilis tarihi" not in self.df.columns:
            QMessageBox.critical(self, "Error", "'Proje gonderilis tarihi' column not found.")
            return

        result = self.df[self.df["Proje gonderilis tarihi"].notna() & \
                          (self.df["Proje gonderilis tarihi"].astype(str).str.strip() != "")]
        if result.empty:
            QMessageBox.information(self, "Result", "No submitted project records found.")
        self.populate_table(result)

    def filter_arrived_projects(self):
        if "Projenin gelis tarihi" not in self.df.columns:
            QMessageBox.critical(self, "Error", "'Projenin gelis tarihi' column not found.")
            return

        result = self.df[self.df["Projenin gelis tarihi"].notna() & \
                          (self.df["Projenin gelis tarihi"].astype(str).str.strip() != "")]
        if result.empty:
            QMessageBox.information(self, "Result", "No project arrival records found.")
        self.populate_table(result)

    def go_back_menu(self):
        # Import inside the function to minimize circular import issues
        # Make sure the file name and class name are correct for your admin menu
        try:
            from preferences_admin_menu import MainWindow as AdminMainWindow
            # Create a NEW instance of the Admin menu
            # WARNING: This creates a new window each time. If you want to return to an *existing* window,
            # you would need to pass its reference around, which goes against the "don't change other files" constraint.
            self.admin_menu = AdminMainWindow() 
            self.admin_menu.show()
            self.close() # Close the current (interviews) window
        except ImportError as e:
            QMessageBox.critical(self, "Error", f"Could not go back to Admin Menu. Check if preferences_admin_menu.py exists and is correctly structured. Details: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred while returning to Admin Menu: {e}")


# Function to get data from Google Sheet
def get_data_from_google_sheet(sheet_id):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_id).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())