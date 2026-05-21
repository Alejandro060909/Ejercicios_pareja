from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/calcular/{a}/{operation}/{b}")
async def calculadora(request: Request, a: float, b:float, operation:str):
    if operation=="suma":
        resultado=a+b
    if operation=="resta":
        resultado=a-b
    if operation=="multiplicacion":
        resultado=a*b
    if operation=="division":
        if b==0:
            resultado="operacion invalida"
        else:
            resultado=a/b

    return  templates.TemplateResponse(request=request, name="calcular.html", context={"operation":operation, "resultado":resultado, "a":a, "b":b})


@app.get("/")
async def raiz(request: Request):
    return templates.TemplateResponse(request=request, name="base.html")

@app.get("/perfil")
def perfil(request: Request):
    persona = {"nombre": "Ana", "edad": 18 , "hobby": "Trotar" }
    
    return templates.TemplateResponse(request=request, name="perfil.html", context={"usuario": persona})

@app.get("/equipo")
async def calcular(request: Request):
    equipo_datos = [
        {"nombre": "Alex", "posicion": "portero", "goles": 0},
        {"nombre": "Matias", "posicion": "defensa", "goles": 1},
        {"nombre": "Duque", "posicion": "delantero", "goles": 4},
        {"nombre": "Aron", "posicion": "centro campo", "goles": 2},
        {"nombre": "Jesus", "posicion": "defensa", "goles": 0},
        {"nombre": "Alexis", "posicion": "centro campo", "goles": 1},
    ]
    

    total_goles = sum(jugador["goles"] for jugador in equipo_datos)
    
    return templates.TemplateResponse(request=request, name="equipo.html", context={"datos": equipo_datos, "total": total_goles})
