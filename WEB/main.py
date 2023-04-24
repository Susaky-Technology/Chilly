from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2
import uvicorn

from Conectors.trabajadores import trabajadores
from Conectors.productos import productos

import os

# Configuramos FastAPi
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Configuramos el Conector
users = trabajadores()
produ = productos()

# Funcion de LogIng
@app.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def login_post(request: Request):
    data = await request.form()
    info = [
        data['usuario'],
        data['password']
    ]
    try:
        if users.login(info[0], info[1])=="admin":
            return RedirectResponse(url="/main")
    except:
        return ("""<script>
    alert("Usuario no Existe o contraseña incorrecta");
    window.location.href= "/login";
    </script>
    """)
# Funcion de Sign_Up
@app.get("/sign_up", response_class=HTMLResponse)
async def sign_up_get(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request})

@app.post("/sign_up")
async def sign_up_post(request: Request):
    data = await request.form()
    info = [
        data['nombre'], # Nombre
        "  ", # Apellidos
        data['password'], # Cedula
        data['correo'], # Correo 
        "", # Direccion
        10, # Telefono
        "admin", # área
        "", # foto
        data['password_repeat'],
        data['accept_terms']
    ]
    # Registrar a la persona
    try:
        if info[2]==info[8]:
            users.insertar(info)
            return {"Hola": info}
    except:
        return "Error has ocurred"

# Pagina principal despues del login
@app.route("/main", methods=['GET', 'POST'])
async def main(request: Request):
    response = produ.listar()
    return templates.TemplateResponse("productos.html", {
        "request": request,
        "response": response
    })

# Añadir Producto
@app.post("/productos")
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

# Listar Trabajadores
@app.route("/trabajadores", methods=['GET', 'POST'])
async def trabajadores_get(request: Request):
    response = users.listar()
    try:
        data = await request.form()
        if data['_method'] == "POST":
            print()
        if data['_method'] == 'PUT':
            print()
        if data['_method'] == "DELETE":
            print()
    except:
        return templates.TemplateResponse("trabajadores.html", {
            "request": request,
            "response": response
        })

if __name__ == '__main__':
    uvicorn.run(app, host= os.getenv('DB_URL'), port=8000)