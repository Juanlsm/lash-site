from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import sqlite3

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 🔐 senha admin
SENHA_ADMIN = "1234"


def conectar():
    return sqlite3.connect("database.db")


# 🏠 HOME
@router.get("/", response_class=HTMLResponse)
def home(request: Request):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, preco, foto FROM servicos")
    servicos = cursor.fetchall()

    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "servicos": servicos}
    )


# 📅 AGENDAMENTO
@router.get("/agendamento", response_class=HTMLResponse)
def agendamento(request: Request):

    servico_selecionado = request.query_params.get("servico")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nome, preco FROM servicos")
    servicos = cursor.fetchall()

    cursor.execute("SELECT data FROM agendamentos")
    datas_ocupadas = [row[0] for row in cursor.fetchall()]

    conn.close()

    return templates.TemplateResponse(
        "agendamento.html",
        {
            "request": request,
            "servicos": servicos,
            "servico_selecionado": servico_selecionado,
            "datas_ocupadas": datas_ocupadas
        }
    )


# 💾 SALVAR AGENDAMENTO
@router.post("/agendar")
def salvar_agendamento(
    nome: str = Form(...),
    telefone: str = Form(...),
    servico: str = Form(...),
    data: str = Form(...)
):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM agendamentos WHERE data = ?", (data,))
    existente = cursor.fetchone()

    if existente:
        conn.close()
        return RedirectResponse(url="/agendamento", status_code=303)

    cursor.execute("""
        INSERT INTO agendamentos (nome, telefone, servico, data)
        VALUES (?, ?, ?, ?)
    """, (nome, telefone, servico, data))

    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=303)


# 🔐 LOGIN
@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login(senha: str = Form(...)):

    if senha == SENHA_ADMIN:
        response = RedirectResponse(url="/admin", status_code=303)
        response.set_cookie(key="admin", value="logado")
        return response

    return RedirectResponse(url="/login", status_code=303)


# 👩‍💼 ADMIN (PROTEGIDO)
@router.get("/admin", response_class=HTMLResponse)
def admin(request: Request):

    if request.cookies.get("admin") != "logado":
        return RedirectResponse(url="/login", status_code=303)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM agendamentos ORDER BY id DESC")
    agendamentos = cursor.fetchall()

    conn.close()

    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            "agendamentos": agendamentos
        }
    )


# ❌ DELETAR
@router.get("/deletar/{id}")
def deletar_agendamento(id: int):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM agendamentos WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return RedirectResponse(url="/admin", status_code=303)