from fastapi import FastAPI
from routers import todo, auth
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(todo.router)
app.include_router(auth.router)