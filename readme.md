# 📝 Notes API – FastAPI + SQLite Backend

A RESTful Notes API built using **FastAPI + SQLAlchemy (SQLite) + JWT Authentication (python-jose)+ Password Hashing (passlib + bcrypt)** to understand real backend architecture and database integration.

This project is part of my journey toward becoming a **GenAI Full Stack Developer**.

---

## 🚀 Features

- ✅ Create Notes  
- ✅ Get All Notes  
- ✅ Get Note by ID  
- ✅ Search Notes using Query Params  
- ✅ Update Notes  
- ✅ Delete Notes  
- ✅ Persistent SQLite Database  
- ✅ SQLAlchemy ORM Integration  
- ✅ Automatic Validation using Pydantic  
- ✅ Interactive Swagger Docs  
- ✅ User Registration
- ✅ User Login (JWT Authentication)
- ✅ Password Hashing using bcrypt
- ✅ Protected Routes using OAuth2
- ✅ User-specific Notes (Multi-user support)
---

## 🛠 Tech Stack

- Python 3.10+  
- FastAPI  
- Pydantic  
- SQLAlchemy  
- SQLite  

---

## 📂 Project Structure

```
notes-api/
│── main.py
│── requirements.txt
│── README.md
└── app/
    ├── config.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── auth.py
    └── routes/
        ├── notes.py
        └── users.py
```

---

# ⚙️ Project Setup (Windows – PowerShell)

This guide explains how to set up and manage a local Python development environment on Windows using PowerShell.

---

## 1️⃣ Create the Virtual Environment

```powershell
python -m venv .venv
```

---

## 2️⃣ Set Execution Policy (If Required)

```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
```

> The `-Scope Process` flag ensures this change only applies to the current terminal session.

---

## 3️⃣ Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

You will know it is active when:

```
(.venv)
```

appears in your terminal prompt.

---

## 4️⃣ Install Dependencies

```powershell
pip install -r requirements.txt
```

Make sure your `requirements.txt` includes:

```
fastapi
sqlalchemy
pydantic
```

---

## 5️⃣ Run the Development Server

```powershell
fastapi dev main.py
```

Server will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## 6️⃣ Deactivate Environment

```powershell
deactivate
```

---

# 🗄 Database Information

- Uses **SQLite**
- Database file: `notes.db`
- Tables are automatically created using SQLAlchemy ORM

This means:

❌ Data is NOT temporary anymore  
✅ Data persists even after server restart  

This is important for building production-ready applications and AI systems later.

---

# 📌 API Endpoints

## 🔐 Authentication

### 🔹 POST `/register`
Register a new user.

### 🔹 POST `/login`
Login user and receive JWT access token.

---

## 📝 Notes (Protected Routes – Requires Authorization)

### 🔹 GET `/notes`
Get all notes of logged-in user.

### 🔹 GET `/notes/{note_id}`
Get specific note by ID.

### 🔹 GET `/notes/search?keyword=python`
Search notes by keyword (title-based).

### 🔹 POST `/notes`
Create a new note.

### 🔹 PUT `/notes/{note_id}`
Update a note.

### 🔹 DELETE `/notes/{note_id}`
Delete a note.

# 🔑 Authentication Flow

1. Register a user using `/register`
2. Login using `/login`
3. Receive JWT access token
4. Click **Authorize** button in Swagger
5. Enter username and password
6. Access protected routes

All notes are user-specific and secured using JWT.

# 🧠 What I Learned

- FastAPI routing & modular structure  
- Path & Query Parameters  
- Pydantic data validation  
- SQLAlchemy ORM basics  
- Persistent database vs in-memory storage  
- CRUD API design  
- Dependency injection (DB sessions)  
- Structuring backend projects professionally  
- JWT-based authentication
- OAuth2 password flow
- Password hashing with bcrypt
- User-based data protection
- Securing database queries per user

---

# 🔥 Future Improvements

- Add JWT Authentication  
- Add User-based Notes (Foreign Key relationships)  
- Switch to PostgreSQL  
- Integrate OpenAI API for Note Summarization  
- Convert into a RAG-based AI Notes Assistant  

---

## 🎯 Why This Project?

This project builds the foundation required for:

- AI-powered backend applications  
- GenAI tools  
- Production-ready API design  
- Backend freelancing & job roles  

---

## 👨‍💻 Author

Arshdeep Singh  
Aspiring GenAI Full Stack Developer 🚀  

---

⭐ If you found this helpful, feel free to star the repo!
