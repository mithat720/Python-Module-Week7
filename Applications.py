import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import pandas as pd
from PyQt6.QtWidgets import QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Applications.ui", self) # Load the UI file
        
        # Buton bağlantıları
        self.applications_buton_exit.clicked.connect(self.close)
        self.applications_buton_back_menu.clicked.connect(self.open_user_preference_menu)
        self.applications_buton_search.clicked.connect(self.open_search_menu)
        self.applications_buton_all_aplications.clicked.connect(self.open_all_applications_menu)
        self.applications_buton_planned_meeting.clicked.connect(self.open_planned_meetings_menu)
        self.applications_buton_unscheduledmeeting.clicked.connect(self.open_unscheduled_meetings_menu)
        self.applications_buton_previousvit.clicked.connect(self.open_previous_vit_menu)
        self.applications_buton_repeated_registration.clicked.connect(self.open_repeated_registration_menu)
        self.applications_buton_different_registration.clicked.connect(self.open_different_registration_menu)
        self.applications_buton_filtered_applications.clicked.connect(self.handle_excel_upload)
    
    def showEvent(self, event):
        """Pencere gösterildiğinde otomatik olarak verileri yükle"""
        super().showEvent(event)
        self.load_applications_from_excel("Basvurular.xlsx")
    
    
    def open_filtered_applications_menu(self):
        pass

    def open_different_registration_menu(self):
        pass
        
    def open_repeated_registration_menu(self):
        pass

    def open_previous_vit_menu(self):
        pass

    def open_unscheduled_meetings_menu(self):
        pass

    def open_planned_meetings_menu(self):
        pass

    def open_all_applications_menu(self):
        pass

    def open_search_menu(self):
        pass

    def open_user_preference_menu(self):
        from user_preference_menu import MainWindow
        self.preference_menu = MainWindow()
        self.preference_menu.show()
        self.close()

    def handle_excel_upload(self):
        self.load_applications_from_excel("Basvurular.xlsx")

    def load_applications_from_excel(self, file_path):
        try:
            df = pd.read_excel(file_path)
            print(df.head())

            self.applications_table.setRowCount(len(df))
            self.applications_table.setColumnCount(len(df.columns))
            self.applications_table.setHorizontalHeaderLabels(df.columns)

            for row in range(len(df)):
                for col in range(len(df.columns)):
                    item = str(df.iat[row, col])
                    self.applications_table.setItem(row, col, QTableWidgetItem(item))
        except Exception as e:
            print(f"Excel yükleme hatası: {e}")
        # Kullanıcıya hata mesajı gösterebilirsiniz

    
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
