# 🚀 TaskFlow - Flask Task Management App

TaskFlow is a simple task management application built with **Flask** and **SQLite** as part of my DevOps learning journey.

The project focuses on learning software development alongside DevOps best practices such as Git branching, Docker, CI/CD, security scanning, and Kubernetes.

---

# Features

- Add Tasks
- Delete Tasks
- Task Priority
- Task Status
    - 📋 To Do
    - 🟠 In Progress
    - ✅ Completed
- Health Check Endpoint
- SQLite Database
- Flask Blueprints
- SQLAlchemy ORM
- Flask-Migrate

---

# Tech Stack

- Python 3.12
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite
- HTML
- CSS

---

# Project Structure

```
taskflow/
│
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── config.py
│
├── instance/
│   └── taskflow.db
│
├── migrations/
│
├── run.py
├── requirements.txt
└── README.md
```

---

# Clone Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/taskflow.git

cd taskflow
```

---

# Create Virtual Environment

Linux

```bash
python3 -m venv .venv
```

Windows

```powershell
python -m venv .venv
```

Activate

Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python run.py
```

Application will be available at

```
http://localhost:5000
```

---

# Database

Initialize database

```bash
flask db upgrade
```

If starting fresh

```bash
flask db init
flask db migrate -m "Initial schema"
flask db upgrade
```

---

# Health Check

```
GET /health
```

Example

```
http://localhost:5000/health
```

Returns

```json
{
  "application": "TaskFlow",
  "status": "healthy"
}
```

---

# Git Workflow

Create a feature branch

```bash
git checkout -b feature/<feature-name>
```

Commit changes

```bash
git add .

git commit -m "feat: description"
```

Push

```bash
git push origin feature/<feature-name>
```

Merge into main after testing.

---

# Upcoming Milestones

- Multi-stage Dockerfile
- Docker Compose
- GitHub Actions CI
- Trivy Security Scanning
- SonarQube
- Kubernetes
- Helm
- Terraform
- AWS Deployment

---

# Contributing

Fork the repository.

Create your own feature branch.

Submit a Pull Request.

Suggestions and improvements are always welcome.

---

# License

MIT License
