from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 🔐 PROTEÇÃO DO ADMIN
@router.get("/admin")
def admin(request: Request):
    # se não estiver logado → manda pro login
    if not request.session.get("logado"):
        return RedirectResponse("/login", status_code=302)

    # se estiver logado → entra no admin
    return templates.TemplateResponse("admin.html", {
        "request": request
    })