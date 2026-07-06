from app.models import Task, db


def test_create_task(app):
    with app.app_context():
        task = Task(
            title="Write Tests",
            description="Testing PostgreSQL",
            priority="High",
        )

        db.session.add(task)
        db.session.commit()

        saved_task = Task.query.first()

        assert saved_task is not None
        assert saved_task.title == "Write Tests"
        assert saved_task.priority == "High"
