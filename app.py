import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from core import Query, Mutation

app = FastAPI()
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema=schema)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def ping():
    return {"ping": "pong"}
