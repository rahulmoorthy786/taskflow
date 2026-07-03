from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
)

from .models import db, Task

main = Blueprint("main", __name__)


# ==========================
# Home Page
# ==========================
@main.route("/")
def index():

    tasks = Task.query.order_by(Task.id.desc()).all()

    total = len(tasks)
    completed = len([t for t in tasks if t.completed])
    pending = total - completed

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
    )


# ==========================
# Add Task
# ==========================
@main.route("/add", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        task = Task(
            title=request.form["title"],
            description=request.form["description"],
            priority=request.form["priority"],
        )

        db.session.add(task)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("add_task.html")


# ==========================
# Complete / Undo Task
# ==========================
@main.route("/complete/<int:task_id>")
def complete_task(task_id):

    task = Task.query.get_or_404(task_id)

    # Toggle completion status
    task.completed = not task.completed

    db.session.commit()

    return redirect(url_for("main.index"))


# ==========================
# Delete Task
# ==========================
@main.route("/delete/<int:task_id>")
def delete_task(task_id):

    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("main.index"))


# ==========================
# Health Check
# ==========================
@main.route("/health")
def health():

    return jsonify(
        {
            "status": "healthy",
            "application": "TaskFlow",
        }
    )
