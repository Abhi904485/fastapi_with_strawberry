from typing import List

import strawberry

from mutation import TodoMutation
from query import TodoQuery
from schema import TodoType


@strawberry.type
class Mutation:
    add_todo: TodoType = strawberry.mutation(resolver=TodoMutation.add_todo)
    delete_todo: str = strawberry.mutation(resolver=TodoMutation.delete_todo)


@strawberry.type
class Query:
    todos: List[TodoType] = strawberry.field(resolver=TodoQuery.todos)
    todo_by_id: TodoType = strawberry.field(resolver=TodoQuery.get_todo)
