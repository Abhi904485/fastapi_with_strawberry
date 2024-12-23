from database import session
from models import Todo
from schema import TodoInput


class TodoMutation:

    def add_todo(self, todo: TodoInput):
        todo = Todo(title=todo.title, description=todo.description)
        session.add(todo)
        session.commit()
        return todo

    def delete_todo(self, todo_id: int) -> str:
        todo = session.query(Todo).get(todo_id)
        if not todo:
            raise Exception(f"Todo with {todo_id} not Found ")
        session.delete(todo)
        session.commit()
        return f"Todo With ID {todo_id} deleted"
