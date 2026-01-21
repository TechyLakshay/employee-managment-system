# Employee Management System (FastAPI + MySQL)

A simple **Employee Management System** built using **FastAPI** and **MySQL** that supports basic **CRUD operations** (Create, Read, Update, Delete).

This project was developed as part of an **internship backend task** to understand:
- FastAPI application structure
- MySQL database integration
- API testing using FastAPI Docs and Postman
- Basic Git & GitHub workflow

---

## 🚀 Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** MySQL (local instance)
- **Validation:** Pydantic
- **Server:** Uvicorn
- **API Testing:** FastAPI Docs (Swagger) & Postman
- **Version Control:** Git & GitHub

---
 
## 📁 Project Structure

employee_app/
│
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── config/
│ │ └── db.py # MySQL database connection
│ ├── models/
│ │ └── employee.py # Employee Pydantic model
│ ├── routes/
│ │ └── employee.py # API routes (CRUD)
│ └── services/
│ └── employee_service.py # Database operations
│
├── myenv/ # Python virtual environment
├── requirements.txt
└── README.md
---
##🧑‍💼 Employee Data Model 

Each employee contains the following attributes:

employee_id (String, Unique – business identifier)

name (String)

age (Integer)

department (String)

manager_name (String)

email (String)

salary (Float, optional)

---



---

## 🧑‍💼 Employee Data Model

Each employee contains the following attributes:

- `employee_id` (String, Unique – business identifier)
- `name` (String)
- `age` (Integer)
- `department` (String)
- `manager_name` (String)
- `email` (String)
- `salary` (Float, optional)

---

## 🗄️ Database Schema (MySQL)

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(100) NOT NULL,
    manager_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    salary FLOAT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

