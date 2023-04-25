from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2

from Conectors.productos import productos

router = APIRouter()

# Configuramos el Conector
produ = productos()
templates = Jinja2Templates(directory="templates")

# Pagina principal de facturas
@router.route("/facturas", methods=['GET', 'POST'])
async def facturas(request: Request):
    return templates.TemplateResponse("facturas.html", {
        "request": request
    })
