from fastapi import APIRouter, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import conectar
import shutil

from database import conectar

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/admin", response_class=HTMLResponse)
def admin(request: Request):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM servicos")

    servicos = cursor.fetchall()

    conn.close()

    return templates.TemplateResponse(
        "admin.html",
        {"request": request, "servicos": servicos}
    )


@router.post("/upload-foto")
async def upload_foto(
    servico_id: int = Form(...),
    foto: UploadFile = File(...)
):

    import shutil

    caminho = f"static/imagens/{foto.filename}"

    with open(caminho, "wb") as buffer:
        shutil.copyfileobj(foto.file, buffer)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE servicos SET foto = ? WHERE id = ?",
        (foto.filename, servico_id)
    )

    conn.commit()
    conn.close()

    return RedirectResponse("/admin", status_code=303)