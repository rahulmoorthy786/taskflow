# 🚀 TaskFlow

A simple Task Management application built with **Flask** to learn modern DevOps practices from development to production.

This project is part of my DevOps learning journey where I gradually implement:

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

- Create new tasks
- Update task status (To Do → In Progress → Completed)
- Delete tasks
- Task priority (Low, Medium, High)
- PostgreSQL database support
- Database migrations using Flask-Migrate (Alembic)
- Health check endpoint (`/health`)
- Docker support
- Docker Compose support

---

# Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | Flask 3.x |
| Language | Python 3.12 |
| Database | PostgreSQL |
| ORM | Flask-SQLAlchemy |
| Migrations | Flask-Migrate |
| Container | Docker |
| Orchestration | Docker Compose |
| Operating System | Ubuntu 24.04 LTS |

---

# Project Structure

```text
taskflow/
├── app/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── add_task.html
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
│
├── instance/
│
├── migrations/
│
├── requirements.txt
├── run.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Quick Start

## Clone Repository

```bash
git clone <repository-url>

cd taskflow
```

---

## Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Database Migration

```bash
flask db upgrade
```

---

## Run Application

```bash
python run.py
```

Application runs at

```
http://localhost:5000
```

---

# Run with Docker

Build Image

```bash
docker build -t taskflow .
```

Run Container

```bash
docker run -d \
  --name taskflow \
  -p 5000:5000 \
  taskflow
```

Application

```
http://localhost:5000
```

---

# Run with Docker Compose

Start services

```bash
docker compose up -d --build
```

Stop services

```bash
docker compose down
```

View logs

```bash
docker compose logs -f
```

---

# Dockerfiles Explained

## Dockerfile

Single-stage Docker build using **python:3.12-alpine**.

Features:

- Lightweight Alpine image
- Non-root user
- Dependency installation
- Production-ready structure
- Exposes port 5000

---

# Docker Compose

The application consists of two services.

### taskflow

- Flask application
- Built from local Dockerfile
- Exposes port 5000

### postgres

- PostgreSQL 16
- Persistent Docker volume
- Health checks enabled
- Automatically connected to the Flask application

---

# Database

Current database:

- PostgreSQL 16

Database migrations are managed using Flask-Migrate.

Useful commands:

```bash
flask db migrate -m "Migration name"

flask db upgrade

flask db downgrade
```

---

# Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| / | GET | Home page |
| /add | GET / POST | Create task |
| /status/<id> | GET | Update task status |
| /delete/<id> | GET | Delete task |
| /health | GET | Health check |

---
