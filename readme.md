# 📝 Notes API – FastAPI + SQLite Backend

A RESTful Notes API built using **FastAPI + SQLAlchemy + SQLite** to understand real backend architecture and database integration.

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
│
└── app/
    ├── database.py
    ├── models.py
    ├── schemas.py
    │
    └── routes/
        └── notes.py
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

### 🔹 GET `/notes`

Returns all notes.

---

### 🔹 GET `/notes/find/{note_id}`

Returns a single note by ID.

---

### 🔹 GET `/notes/search?keyword=python`

Search notes by keyword.

---

### 🔹 POST `/notes/create`

Create a new note.

Example Request Body:

```json
{
  "title": "My Note",
  "content": "Some content"
}
```

---

### 🔹 PUT `/notes/update/{note_id}`

Update an existing note.

---

### 🔹 DELETE `/notes/delete/{note_id}`

Delete a note by ID.

---

# 🧠 What I Learned

- FastAPI routing & modular structure  
- Path & Query Parameters  
- Pydantic data validation  
- SQLAlchemy ORM basics  
- Persistent database vs in-memory storage  
- CRUD API design  
- Dependency injection (DB sessions)  
- Structuring backend projects professionally  

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
