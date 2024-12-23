from database import session
from models import Todo
from schema import TodoType


class TodoQuery:
    def todos(self):
        return session.query(Todo).all()

    def get_todo(self, todo_id: int) -> TodoType | None:
        todo = session.query(Todo).get(todo_id)
        if not todo:
            raise Exception("Todo not found")
        return todo

