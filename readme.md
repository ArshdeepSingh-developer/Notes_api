# 📝 Notes API – FastAPI Backend Project

A simple RESTful Notes API built using **FastAPI** to understand backend fundamentals like:

* Path Parameters
* Query Parameters
* Request Body Handling
* Pydantic Validation
* CRUD Operations
* Automatic API Documentation (Swagger)

This project is part of my journey toward becoming a **GenAI Backend Developer**.

---

## 🚀 Features

* ✅ Create Notes
* ✅ Get All Notes
* ✅ Get Note by ID
* ✅ Search Notes using Query Params
* ✅ Update Notes
* ✅ Delete Notes
* ✅ Automatic Validation using Pydantic
* ✅ Interactive Swagger Docs

---

## 🛠 Tech Stack

* Python 3.10+
* FastAPI
* Pydantic

---

## 📂 Project Structure

```
notes-api/
│── main.py
│── requirements.txt
│── README.md
│── .venv/
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

# 📌 API Endpoints

### 🔹 GET `/notes`

Returns all notes.

### 🔹 GET `/notes/{note_id}`

Returns a single note by ID.

### 🔹 GET `/search?keyword=python`

Search notes by keyword.

### 🔹 POST `/notes`

Create a new note.

Request Body:

```json
{
  "title": "Learn FastAPI",
  "content": "FastAPI is powerful"
}
```

### 🔹 PUT `/notes/{note_id}`

Update an existing note.

### 🔹 DELETE `/notes/{note_id}`

Delete a note by ID.

---

# 🧠 What I Learned

* FastAPI automatic validation using type hints
* Pydantic data modeling
* CRUD API design
* HTTP methods (GET, POST, PUT, DELETE)
* API testing using Swagger UI
* Structuring backend projects professionally

---

# 🔥 Future Improvements

* Add PostgreSQL database
* Add JWT Authentication
* Add User-based Notes
* Integrate OpenAI API for Note Summarization
* Convert into a RAG-based AI Notes Assistant

---

## 🎯 Why This Project?

This project builds the foundation required for:

* AI-powered applications
* Backend for GenAI tools
* Production-ready API design
* Backend projects

---

## 👨‍💻 Author

Arshdeep Singh
Aspiring GenAI Backend Developer 🚀

---

⭐ If you found this helpful, feel free to star the repo!

