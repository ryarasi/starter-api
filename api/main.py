from fastapi import FastAPI
from starlette.graphql import GraphQLApp
import graphene
import uvicorn
import os

app = FastAPI()

port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 0))
host = str(os.getenv('HOST','0.0.0.0'))

class Query (graphene.ObjectType):
    hello = graphene.String(name=graphene.String
    (default_value=", World 🗺️!"))

    def resolve_hello(self, info, name):
        return "Hello " + name 

app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))


if __name__ == "__main__":
    print('port => ', port)
    print('reload => ', reload)
    print('host => ', host)
    uvicorn.run('main:app', port=port, reload=reload, host=host)
