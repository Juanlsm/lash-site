from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import home
from routers import admin

app = FastAPI()

# templates
templates = Jinja2Templates(directory="templates")

# EXEMPLO (se não tiver ainda vindo do banco)
lista_servicos = [
    ("1", "Design de sobrancelha", 40),
    ("2", "Design com henna", 50),
]

# rota agendamento
@app.get("/agendamento")
def agendamento(request: Request, servico: str = None):
    return templates.TemplateResponse("agendamento.html", {
        "request": request,
        "servicos": lista_servicos,
        "servico_selecionado": servico
    })

# arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# rotas
app.include_router(home.router)
app.include_router(admin.router)