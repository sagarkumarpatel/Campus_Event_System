# 🎓 Campus Event System

A robust Django-based web application designed to streamline event management within a campus environment. It uses **MongoDB** as the backend database via **Djongo**, offering flexibility and scalability.

---

## 🚀 Features

- 📅 Create and manage campus events easily
- 🔐 Admin dashboard for managing users and events
- 📦 MongoDB-powered data storage
- 🛡️ Secure environment using virtual environments and environment variables

---

## 🖥️ Tech Stack

- **Backend:** Django 3.2
- **Database:** MongoDB (via Djongo)
- **Language:** Python 3.8+
- **ORM:** Djongo
- **Others:** Virtual Environment, PowerShell/Command Prompt (Windows)

---

## ⚙️ Project Setup (After System Reboot - Windows)

1. **Open Command Prompt or PowerShell**

2. **Navigate to Project Folder**
   ```bash
   cd C:\Projects\campus_event_system
   ```

3. **Activate the Virtual Environment**
   ```bash
   .\venv\Scripts\activate
   ```

4. **Start MongoDB Service**
   ```bash
   net start MongoDBServer
   ```

   > If MongoDB isn't registered as a service, start it manually by running `mongod` from its install directory.

5. **Run Django Server**
   ```bash
   python manage.py runserver
   ```

6. Open your browser:
   ```
   http://127.0.0.1:8000/
   ```

---

## 🧑‍💻 Setup on a New Windows Machine

### 🔧 Prerequisites

- [ ] Install Python 3.8 – 3.10  
  ➤ https://www.python.org/downloads/windows/  
  > ✅ **Check “Add Python to PATH” during installation**

- [ ] Install MongoDB  
  ➤ https://www.mongodb.com/try/download/community  
  > ✅ Recommended: Install as a Windows service

---

### 🛠️ Step-by-Step Setup

1. **Copy Project Folder** (including `manage.py`, `requirements.txt`)

2. **Open Command Prompt / PowerShell**

3. **Navigate to Project Directory**
   ```bash
   cd path\to\campus_event_system
   ```

4. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

5. **Activate Virtual Environment**
   ```bash
   .\venv\Scripts\activate
   ```

6. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

7. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

8. **(Optional) Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

9. **Start Django Server**
   ```bash
   python manage.py runserver
   ```

---

## ✅ Pre/Post VENV Checklist (Windows)

### Before Activating VENV:
- [ ] **Check Python Installation**
  ```bash
  python --version
  ```

- [ ] **Ensure MongoDB is Running**
  ```bash
  net start MongoDBServer
  ```

### After Activating VENV:
- [ ] **Ensure (venv) Prefix Appears**
- [ ] **Check Installed Packages**
  ```bash
  pip list
  ```

- [ ] **Run Migrations Without Error**
  ```bash
  python manage.py migrate
  ```

---

## 🎥 Demo Preparation

### ✅ Before Demo
- Start MongoDB:
  ```bash
  net start MongoDBServer
  ```
- Activate VENV and run server:
  ```bash
  .\venv\Scripts\activate
  python manage.py runserver
  ```
- Add sample events in:
  ```
  http://127.0.0.1:8000/admin/
  ```

### ❌ After Demo
- Stop server with `Ctrl + C`
- Optionally stop MongoDB:
  ```bash
  net stop MongoDBServer
  ```

---

## 💡 Pro Tips (Windows)

### 🔐 Use Environment Variables
Set sensitive data like your MongoDB URI and `SECRET_KEY` using environment variables or a `.env` file:

**.env Example:**
```env
SECRET_KEY=your_secret_key
MONGO_URI=mongodb://localhost:27017
```

**Load in `settings.py`:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
```

> ☑️ Add `.env` to `.gitignore`

---

### 💾 MongoDB Backup
```bash
mongodump --db campus_events_db --out C:\backups\
```

---

### 🛠️ One-Click Start Script

Create `start_dev.bat`:
```bat
@echo off
echo Activating virtual environment...
call venv\Scripts\activate
echo Starting MongoDB service...
net start MongoDBServer
echo Starting Django development server...
python manage.py runserver
pause
```

Double-click this file to launch your project quickly.

---

## 📦 Requirements

```txt
asgiref==3.8.1
dataclasses==0.6
Django==3.2.12
djongo==1.3.6
dnspython==2.7.0
pymongo==3.12.3
python-dateutil==2.9.0.post0
pytz==2025.2
six==1.17.0
sqlparse==0.2.4
typing_extensions==4.13.2
```

---

## 🙌 Contributing

Feel free to fork the repository and submit a pull request! Feedback and suggestions are welcome.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🌐 Live Preview (if applicable)

Coming soon...

---

## 📬 Contact

Created by [Sagar Kumar Patel] — feel free to reach out for feedback or collaboration!