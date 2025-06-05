import sys
import datetime
import smtplib  #Send email via Gmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem

from googleapiclient.discovery import build  #Used to connect with the Google Calendar API and retrieve events
from google.oauth2 import service_account

# --- Google API Info ---
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'credentials.json'
CALENDAR_ID = 'vitcrmproject@gmail.com'  # Your gmail calendar ID

# --- Gmail SMTP Settings ---
GMAIL_USER = 'vitcrmproject@gmail.com'
GMAIL_PASSWORD = 'wtke vxea sxdy clom'  # Gmail App Password

class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("admin_menu.ui", self)

        self.admin_menu_buton_activity_control.clicked.connect(self.get_events_from_calendar)
        self.admin_menu_buton_sendmail.clicked.connect(self.send_emails)
        self.admin_menu_buton_prefencemenu.clicked.connect(self.open_preferences_admin_menu)
        self.admin_menu_buton_exit.clicked.connect(self.close)

    def get_events_from_calendar(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)  #Authenticate for Google API access
            service = build('calendar', 'v3', credentials=credentials)  #Start the Google Calendar service

            now = (datetime.datetime.utcnow() - datetime.timedelta(days=30)).isoformat() + 'Z' #Get events starting from 30 days ago
            events_result = service.events().list(
                calendarId=CALENDAR_ID,
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy='startTime'
            ).execute()  #Events are retrieved and come as an items list.

            events = events_result.get('items', [])
            self.admin_menu_table_result.setRowCount(0)

            for i, event in enumerate(events):
                summary = event.get('summary', 'No Title')
                start = event['start'].get('dateTime', event['start'].get('date', ''))
                attendees = ", ".join([att.get('email', '') for att in event.get('attendees', [])])
                organizer = event.get('organizer', {}).get('email', '')

                self.admin_menu_table_result.insertRow(i)
                self.admin_menu_table_result.setItem(i, 0, QTableWidgetItem(summary))
                self.admin_menu_table_result.setItem(i, 1, QTableWidgetItem(start))
                self.admin_menu_table_result.setItem(i, 2, QTableWidgetItem(attendees))
                self.admin_menu_table_result.setItem(i, 3, QTableWidgetItem(organizer))

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch events:\n{str(e)}")

    def send_emails(self):
        row_count = self.admin_menu_table_result.rowCount()
        if row_count == 0:
            QMessageBox.warning(self, "Warning", "No events to show.")
            return

        sent_emails = []
        for i in range(row_count):
            emails_raw = self.admin_menu_table_result.item(i, 2).text()
            subject = "Event Notification"
            body = f"""Dear Participant,

        You're invited to {self.admin_menu_table_result.item(i, 0).text()}.
        🕒 Start Time: {self.admin_menu_table_result.item(i, 1).text()}

        Best regards,  
        CRM Project Team 3"""

            for email in emails_raw.split(","):
                email = email.strip()
                if email:
                    success = self.send_email(email, subject, body)
                    if success:
                        sent_emails.append(email)

        if sent_emails:
            QMessageBox.information(self, "Email Sent", f"Emails were successfully sent to:\n{', '.join(sent_emails)}")
        else:
            QMessageBox.warning(self, "Email Error", "No emails could be sent.")

    def send_email(self, to_email, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = GMAIL_USER
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Error sending email to {to_email}: {e}")
            return False

    def open_preferences_admin_menu(self):
        from preferences_admin_menu import MainWindow
        self.preferences_admin_menu = MainWindow()
        self.preferences_admin_menu.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    window = AdminMenu()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
