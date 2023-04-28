from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2
import uvicorn
import os

# Configuramos las routas de los diferentes modulos
from routes.productos import router as productos 
from routes.trabajadores import router as trabajadores
from routes.facturas import router as facturas 

# Configuramos FastAPi
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rutas en modulos externos
app.include_router(productos)
app.include_router(trabajadores)
app.include_router(facturas)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/camara", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("camara.html", {"request": request})



if __name__ == '__main__':
    db_url = os.getenv('DB_URL')
    uvicorn.run(app, host=db_url, port=8000)
