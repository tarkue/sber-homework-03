from fastapi import FastAPI

from .routes import index_router

app = FastAPI()
app.add_route("/", index_router)