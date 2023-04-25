from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2

from Conectors.trabajadores import trabajadores

router = APIRouter()

# Configuramos el Conector
users = trabajadores()
templates = Jinja2Templates(directory="templates")

# Funcion de LogIng
@router.get("/login", response_class=HTMLResponse)
async def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
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
@router.get("/sign_up", response_class=HTMLResponse)
async def sign_up_get(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request})

@router.post("/sign_up")
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
            return RedirectResponse(url="/main")
    except:
        return {"message": "Contraseñas no coincide o no aceptaste los terminos"}

# Listar Trabajadores
@router.route("/trabajadores", methods=['GET', 'POST'])
async def trabajadores_get(request: Request):
    response = users.listar()
    return templates.TemplateResponse("trabajadores.html", {
        "request": request,
        "response": response
    })

# Insertar Trabajadores
@router.post("/trabajadores_add")
async def trabajadores_add(request: Request):
    data = await request.form()
    try:
        info = [
            data['nombre'],
            data['apellidos'],
            data['cedula'],
            data['correo'],
            data['direccion'],
            data['telefono'],
            data['area'],
            data['foto']
        ]
 
        if data['_method'] == "POST":
            users.insertar(info)

        return RedirectResponse(url="/trabajadores")
    except:
        return {"data": data}

# Editar Trabajadores
@router.post("/trabajadores_update")
async def trabajadores_update(request: Request):
    data = await request.form()
    info = [
        data['nombre'],
        data['apellidos'],
        data['cedula'],
        data['correo'],
        data['direccion'],
        data['telefono'],
        data['area'],
        data['foto']
    ]
    try:
        if data['_method'] == 'PUT':
            print("This: ", users.editar(data['id'], info))

        return RedirectResponse(url="/trabajadores")
    except:
        return {"data": info}

# Eliminar Trabajadores
@router.post("/trabajadores_delete")
async def trabajadores_delete(request: Request):
    data = await request.form()
    try:
        if data['_method'] == "DELETE":
            users.eliminar(data['id'])

        return RedirectResponse(url="/trabajadores")
    except:
        return {"data": data}
