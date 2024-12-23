import strawberry


@strawberry.type
class TodoType:
    id: int
    title: str
    description: str


@strawberry.input
class TodoInput:
    title: str
    description: str
