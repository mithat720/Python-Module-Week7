# 📌 We'RHERE CRM Application

## 🧭 Project Overview

This is a desktop CRM application developed in Python using PyQt6 and Google APIs. The application allows We’RHERE to manage their IT training application process by accessing and filtering data stored in multiple Google Sheets.

The software includes login-based access (admin and user roles), page-specific filtering options, and automated interaction with Google Calendar for managing events and sending notification emails.

---

## ⚙️ Technologies Used

- Python 3.x
- PyQt6 & Qt Designer
- Google Drive API
- Google Calendar API
- pandas
- JSON (for local configuration)
- GitHub for version control

---

## 🚀 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/crm-project.git
   cd crm-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure your `credentials.json` file for Google API access is in the root directory.

4. Run the program:
   ```bash
   python main.py
   ```

5. (Optional) To create an executable:
   Use `pyinstaller` or `auto-py-to-exe`.

---

## 🖥️ Application Pages Summary

- **Login Page**: Allows users to log in with credentials stored in Google Sheets. Redirects based on user role.
- **Preferences Menu (User/Admin)**: Main navigation page. Admins have additional options.
- **Applications Page**: Filter, search, and view candidate applications with various options.
- **Mentor Meetings Page**: View mentor feedback and filter via ComboBox.
- **Interviews Page**: View submitted or received project data.
- **Admin Menu**: Fetch events from Google Calendar and send automated emails.

---

## 📌 Usage Scenarios

### 1. Login Screen
- User enters their username and password.
- Admin is redirected to the Admin Preferences Menu.
- User is redirected to the User Preferences Menu.

### 2. Preferences Menu (User)
- Buttons:
  - `Applications` opens the Applications page.
  - `Mentor Meetings` opens the Mentor page.
  - `Interviews` opens the Interview page.
- Back button available on each subpage.

### 3. Preferences Menu (Admin)
- Buttons:
  - Access `Applications`, `Mentor Meetings`, `Interviews`, and `Admin Menu`.
- A "Back to Admin Menu" button is provided on each page.

### 4. Applications Page
- Actions:
  - Search by name.
  - View all applications.
  - Filter by mentor assignment.
  - View duplicate entries.
  - Compare VIT1/VIT2 data.
  - Filter unique entries.
  - Navigate back with Back button.

### 5. Mentor Page
- Actions:
  - Search by name.
  - View all mentor meeting records.
  - Filter by evaluation result (via ComboBox).
  - Navigate back to Preferences Menu.

### 6. Interviews Page
- Actions:
  - Search by name.
  - View candidates with submitted projects.
  - View candidates whose projects were received.
  - Navigate back to Preferences Menu.

### 7. Admin Menu Page
- Actions:
  - Click `Activity Control` to fetch Google Calendar data.
  - Click `Send Mail` to notify selected users.
  - View events in a table.
  - Navigate back to Admin Preferences.

---

## 📂 Project Structure

```
crm-project/
│
├── src/                # Python source files
├── ui/                 # Qt Designer .ui files
├── credentials.json    # Google API credentials
├── requirements.txt
├── README.md
└── main.py             # Entry point
```

---

## 📝 Notes

- Internet connection is required to interact with Google Sheets and Calendar.
- Ensure your Google Sheets files are shared with the email address from your `credentials.json`.

---
