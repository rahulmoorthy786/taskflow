# 🚀 TaskFlow

A simple Task Management application built with **Flask** for learning modern DevOps practices.

This project is part of my DevOps learning journey and will gradually evolve from a local Flask application into a production-ready application using:

- Docker
- Docker Compose
- PostgreSQL
- GitHub Actions
- SonarQube
- Trivy
- AWS
- Kubernetes

---

# Features

- Add Tasks
- Update Task Status
- Delete Tasks
- Task Priorities
- SQLite Database
- Health Check Endpoint

---

# Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Flask 3.x |
| Language | Python 3.12 |
| Database | SQLite (Current) |
| Future Database | PostgreSQL |
| ORM | Flask-SQLAlchemy |
| Migrations | Flask-Migrate |
| OS | Ubuntu 24.04 LTS |

---

# Project Structure

```text
taskflow/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
│
├── instance/
│   └── taskflow.db
│
├── migrations/
│
├── requirements.txt
├── run.py
├── .env.example
└── README.md
```

---

# Running Locally

Clone the repository

```bash
git clone <repo-url>
cd taskflow
```

Create a Python virtual environment

```bash
python3 -m venv .venv
```

Activate the virtual environment

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python run.py
```

Application URL

```
http://localhost:5000
```
