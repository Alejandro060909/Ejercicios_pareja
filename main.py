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

