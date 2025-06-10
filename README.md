# CRM Project – Team 3

This is a Python-based CRM application developed for the **We'RHERE** organization as part of an IT training program.

The project allows users to manage and view application data that is stored in Google Sheets. It uses a GUI created with **PyQt6**, and integrates with **Google Drive** and **Google Calendar** APIs.

---

## 📌 Project Purpose

We'RHERE organization handles IT training programs and manages participant data using Google Sheets.

This project aims to provide a **user-friendly desktop application** that displays and interacts with this data easily, without requiring manual access to spreadsheets.

---

## 💻 Technologies Used

- Python 3.x
- PyQt6 & Qt Designer
- Google API Client (Drive & Calendar)
- JSON (for local data)
- Object-Oriented Programming
- UML Diagrams
- GitHub & Trello (Agile-Scrum)

---

## 🚀 How to Run

> **Note:** This project is currently in development. It is not yet packaged as an `.exe` file.

To run the application locally:

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/crm-project.git
cd crm-project/week7
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not yet generated, install manually:
```bash
pip install PyQt6 google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

4. **Make sure you have the correct `credentials.json` file for Google API access.**

5. **Run the application:**

```bash
python main.py
```

---

## 📁 Project Structure

```bash
week7/
├── main.py
├── login.py
├── Admin_Menu.py
├── Mentor_Menu.py
├── Applications.py
├── interviews.py
├── user_session.py
├── *.ui                 # UI design files (Qt Designer)
├── credentials.json     # Google API credentials
├── Icons/               # Images and icons used in UI
├── README.md
```

---

## 👥 Team & Responsibilities

- **Cafer** – UML diagrams, Login system, Applications page  
- **Ibrahim** – UI interface design, Mentor Menu  
- **Sumeyra** – Trello planning, Admin Menu, Google API integration  
- **Mithat** – Interviews page, README documentation, GitHub uploads  
- **All Members** – Testing and preparation of the final presentation

---

## 📌 Notes

- Google APIs require proper configuration and authentication. Replace `credentials.json` with your own authorized file.
- In the future, we plan to build a `.exe` version using PyInstaller or similar tools.

---

## 📷 Screenshots

> (You can add screenshots of your app here in future commits.)

---

## 📃 License

This project is for educational purposes. License to be added.
