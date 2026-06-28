# Event Registration System

A Django-based Event Registration System developed as part of the **CodeAlpha Internship**. This application allows users to browse available events, register for events, view their registrations, and cancel registrations. It also includes a Django Admin Panel for managing events and registrations.

---

## Features

* View all available events
* View event details
* Register for an event
* View all registrations
* Cancel a registration
* Django Admin Panel for managing events and registrations
* Responsive user interface
* SQLite database integration

---

## Tech Stack

* Django
* Python
* SQLite
* HTML
* CSS
* Jazzmin (Admin Panel Theme)

---

## Project Structure

```text
CodeAlpha_EventRegistrationSystem/
│
├── eventApp/
├── eventSystem/
├── templates/
│   ├── index.html
│   ├── details.html
│   └── registrations.html
│
├── static/
│   └── style.css
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd CodeAlpha_EventRegistrationSystem
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create an admin user:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

---

## Usage

* User Website:

```
http://127.0.0.1:8000/
```

* Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

## Database

SQLite (`db.sqlite3`) is used to store:

* Events
* User Registrations

---

## Author

**Dhineshkumar I**

CodeAlpha Internship Project
