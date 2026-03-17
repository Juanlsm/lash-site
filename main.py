from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import home
from routers import admin

app = FastAPI()

# arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# rotas
app.include_router(home.router)
app.include_router(admin.router)