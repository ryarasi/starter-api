from fastapi import Depends, FastAPI, HTTPException, Request, Response
from starlette.graphql import GraphQLApp
import graphene
import uvicorn
from .database import SessionLocal, engine
import os

from sqlalchemy.orm import Session
from . import models
models.Base.metadata.create_all(bind=engine)

from .gqQueries import Query
from .gqMutations import Mutation
from .gqSubscriptions import Subscription

# Dependency
def get_db(request: Request):
    return request.state.db

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response



port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 0))
host = str(os.getenv('HOST','0.0.0.0'))

@app.get('/')
def Home():
    return "Service is Running..."

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation,
                         subscription=Subscription)))



if __name__ == "__main__":
    print('port => ', port)
    print('reload => ', reload)
    print('host => ', host)
    uvicorn.run('main:app', port=port, reload=reload, host=host)
