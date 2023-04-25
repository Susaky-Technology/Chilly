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

# Pagina principal despues del login
@router.route("/main", methods=['GET', 'POST'])
async def main(request: Request):
    response = produ.listar()
    return templates.TemplateResponse("productos.html", {
        "request": request,
        "response": response
    })

# Añadir Producto
@router.post("/productos")
async def productos_post(request: Request):
    data = await request.form()
    if data['_method'] == "POST":
        produ.insertar([
            data['nombre'],
            data['cantidad'],
            data['precio'],
            0,
            "",
        ])

    if data['_method'] == 'PUT':
        produ.editar(data['id'], [
            data['nombre'],
            data['cantidad'],
            data['precio'],
            0,
            "",
        ]) 
    if data['_method'] == "DELETE":
        produ.eliminar(data['id'])
    return RedirectResponse("/main")
