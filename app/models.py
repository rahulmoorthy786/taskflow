from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    title = db.Column(
        db.String(200),
        nullable=False,
    )

    description = db.Column(
        db.Text,
        nullable=True,
    )

    priority = db.Column(
        db.String(20),
        nullable=False,
        default="Medium",
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="To Do",
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    def __repr__(self):
        return f"<Task {self.title}>"
