from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from routers import home
from routers import admin

app = FastAPI()

# sessão (login)
app.add_middleware(SessionMiddleware, secret_key="senha_super_secreta")

# templates
templates = Jinja2Templates(directory="templates")

# exemplo de serviços
lista_servicos = [
    ("1", "Design de sobrancelha", 40),
    ("2", "Design com henna", 50),
]

# AGENDAMENTO
@app.get("/agendamento")
def agendamento(request: Request, servico: str = None):
    return templates.TemplateResponse("agendamento.html", {
        "request": request,
        "servicos": lista_servicos,
        "servico_selecionado": servico
    })

# LOGIN PAGE
@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# LOGIN POST
@app.post("/login")
def login(request: Request, senha: str = Form(...)):
    if senha == "1234":
        request.session["logado"] = True
        return RedirectResponse("/admin", status_code=302)

    return templates.TemplateResponse("login.html", {
        "request": request,
        "erro": "Senha incorreta"
    })

# LOGOUT (opcional mas top)
@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=302)

# arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# rotas
app.include_router(home.router)
app.include_router(admin.router)