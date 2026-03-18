# 📝 Notes API – Production-Ready FastAPI Backend

A production-grade RESTful Notes API built using:

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy ORM**
- **JWT Authentication (python-jose)**
- **Password Hashing (passlib + bcrypt)**
- **Service Layer Architecture**

This project is part of my journey toward becoming a **GenAI Full Stack Developer**, focusing on scalable backend systems designed for AI integration.

---

# 🚀 Features

## 🔐 Authentication & Security
- ✅ User Registration  
- ✅ User Login (JWT Authentication)  
- ✅ OAuth2 Password Flow  
- ✅ Password Hashing using bcrypt  
- ✅ Protected Routes  
- ✅ User-specific Notes (Multi-user support)  
- ✅ Owner-based data filtering  

## 📝 Notes Management
- ✅ Create Notes  
- ✅ Get All Notes  
- ✅ Get Note by ID  
- ✅ Search Notes using Query Parameters  
- ✅ Update Notes  
- ✅ Delete Notes  

## 🏗 Architecture
- ✅ PostgreSQL (Production-grade database)  
- ✅ SQLAlchemy ORM  
- ✅ Service Layer pattern  
- ✅ Dependency Injection (DB sessions & auth)  
- ✅ Clean separation of concerns  
- ✅ RESTful status codes  
- ✅ Structured error handling  
- ✅ Interactive Swagger & ReDoc documentation  

---

# 🛠 Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- python-jose (JWT)
- passlib (bcrypt)
- psycopg2-binary
- python-dotenv

---

# 🏗 Architecture Overview

The backend follows a **layered architecture**:

Route Layer → Service Layer → Database Layer

### 🔹 Route Layer
- Handles HTTP requests
- Performs dependency injection
- Validates request data
- Calls service layer

### 🔹 Service Layer
- Contains business logic
- Performs database queries
- Handles ownership validation
- Raises business-related exceptions

### 🔹 Database Layer
- SQLAlchemy models
- PostgreSQL connection
- Session lifecycle management

This structure ensures:

- Maintainability  
- Scalability  
- Clean code practices  
- AI-readiness  

---

# 📂 Project Structure

notes-api/
│── main.py
│── requirements.txt
│── README.md
└── app/
    ├── core/
    │   ├── security.py
    │   ├── exception.py
    │   └── config.py
    │
    ├── db/
    │   ├── database.py
    │   └── models.py
    │
    ├── schema/
    │   ├── users.py
    │   └── notes.py
    │
    ├── routes/
    │   ├── users.py
    │   └── notes.py
    │
    └── services/
        ├── user_service.py
        └── note_service.py

---

# 🗄 Database

This project uses **PostgreSQL**.

### Why PostgreSQL?

- Better concurrency handling  
- Production-ready performance  
- Required for real deployments  
- Scalable for AI workloads  

The application connects via SQLAlchemy using:

postgresql://user:password@host:port/db_name

Database sessions are managed using FastAPI dependency injection.

---

# ⚙️ Environment Variables

Sensitive values are stored in a `.env` file:

DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=

Secrets are never hardcoded.

---

# ⚙️ Local Setup

## 1️⃣ Create Virtual Environment

```powershell
python3 -m venv .venv
```

## 2️⃣ Activate Environment

**macOS / Linux**  
```powershell
source .venv/bin/activate
```

**Windows (PowerShell)**

> If required, set the execution policy first:
```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
```

Then activate:
```powershell
.\.venv\Scripts\Activate.ps1
```
---

## 3️⃣ Install Dependencies

```powershell
pip install -r requirements.txt
```

Make sure `requirements.txt` includes:

fastapi  
uvicorn  
sqlalchemy  
psycopg2-binary  
python-jose  
passlib[bcrypt]  
pydantic  
python-dotenv  

---

## 4️⃣ Run Development Server

```powershell
fastapi dev main.py
```

Server:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

---

# 📌 API Endpoints

## 🔐 Authentication

POST `/api/v1/auth/register`  
Register a new user.

POST `/api/v1/auth/login`  
Login user and receive JWT access token.

---

## 📝 Notes (Protected Routes – Requires Bearer Token)

GET `/api/v1/notes`  
Get all notes of logged-in user.

GET `/api/v1/notes/{note_id}`  
Get specific note by ID.

GET `/api/v1/notes/search?keyword=python`  
Search notes by title (case-insensitive).

POST `/api/v1/notes`  
Create a new note.

PUT `/api/v1/notes/{note_id}`  
Update a note.

DELETE `/api/v1/notes/{note_id}`  
Delete a note.

---

# 🔑 Authentication Flow

1. Register user  
2. Login to receive JWT token  
3. Click **Authorize** in Swagger  
4. Enter credentials  
5. Access protected routes  

All note queries are filtered using:

owner_id == current_user_id

Ensuring user-level data isolation.

---

# ⚠️ Error Handling Strategy

- Schema validation → handled automatically by FastAPI  
- Business logic errors → raised inside service layer  
- REST status codes:
  - 400 → Bad Request  
  - 401 → Unauthorized  
  - 404 → Not Found  
  - 500 → Internal Server Error  

---

# 🧠 What This Project Demonstrates

- Production-ready FastAPI backend structure  
- PostgreSQL integration  
- SQLAlchemy session lifecycle  
- JWT authentication & OAuth2  
- Service Layer architecture  
- Dependency injection patterns  
- User-level data protection  
- Clean code & scalability principles  

---

# 🔮 Future Roadmap

- Convert to async endpoints for AI APIs  
- Background tasks for AI processing  
- Vector database integration  
- OpenAI API integration  
- Embedding generation  
- RAG-based AI Notes Assistant  
- Dockerization & deployment  

---

# 🎯 Why This Project?

This backend is designed as a foundation for:

- AI-powered applications  
- GenAI tools  
- Scalable SaaS systems  
- Backend freelancing  
- Production deployments  

---

# 👨‍💻 Author

**Arshdeep Singh**  
GenAI Backend Developer in Progress 🚀  

---

⭐ If you found this helpful, feel free to star the repo!