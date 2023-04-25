from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2

from Conectors.facturas import facturas 
import json

router = APIRouter()

# Configuramos el Conector
fac = facturas()
templates = Jinja2Templates(directory="templates")

# Pagina principal de facturas
@router.route("/facturas", methods=['GET', 'POST'])
async def facturas(request: Request):

    out = fac.listar()
    response = []
    for key in out:
        compras = key['compras']
        compras = bytes(compras['data']).decode('utf-8')
        compras = json.loads(compras)

        response.append(
            {
            'id': key['id'],
            'nombres': key['nombres'], 
            'apellidos': key['apellidos'],
            'fecha': key['fecha'],
            'ciudad': key['ciudad'],
            'compras': compras,
            'subtotal': key['subtotal'],
            'descuento': key['descuento'],
            'iva': key['iva'],
            'total': key['iva']
            }
        )
    
    return templates.TemplateResponse("facturas.html", {
        "request": request,
        "response": response
    })
