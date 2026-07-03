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

    todo = len([t for t in tasks if t.status == "To Do"])

    progress = len([t for t in tasks if t.status == "In Progress"])

    completed = len([t for t in tasks if t.status == "Completed"])

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        todo=todo,
        progress=progress,
        completed=completed,
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
            status=request.form["status"],
        )

        db.session.add(task)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("add_task.html")


# ==========================
# Update Task Status
# ==========================
@main.route("/status/<int:task_id>")
def update_status(task_id):

    task = Task.query.get_or_404(task_id)

    if task.status == "To Do":

        task.status = "In Progress"

    elif task.status == "In Progress":

        task.status = "Completed"

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
