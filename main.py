from fastapi import FastAPI,Path,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional


app= FastAPI()
app.title = "API DE RIFAS"
app.description = "a continuacion se muestran las rutas de la API"
app.version = "0.0.1"


#la clase rifa es la que se va a utilizar para crear las rifas donde va a tener los atributos de la rifa que son
#id,estado,nombre de la persona a la quie se le asigno,precioTotal
class Rifa(BaseModel):
    id: int = Field(ge=1, le=9999, description="El id debe ser mayor a 0 y menor a 10000")
    estado: str
    nombre: str = Field( default="mi pelicula",min_length=3, max_length=5)
    #es opcional
    titulo: Optional[str] = None
    precioTotal: float = Field(ge=1, le=9999, description="El precio debe ser mayor a 10000 y menor a 1000000")
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "estado": "separada",
                "nombre": "Juan",
                "titulo": "Rifa de un auto",
                "precioTotal": 1000.0
            }
        }

    
listaRifas = [
    Rifa(id=1,estado="separada",nombre="Juan",titulo="Rifa de un auto",precioTotal=1000.0),
    Rifa(id=2,estado="separada",nombre="Pedro",titulo="Rifa de un auto",precioTotal=1000.0),
    Rifa(id=3,estado="separada",nombre="Maria",titulo="Rifa de un auto",precioTotal=1000.0),
    Rifa(id=4,estado="cancelada",nombre="Jose",titulo="Rifa de un auto",precioTotal=1000.0),
    Rifa(id=5,estado="cancelada",nombre="Luis",titulo="Rifa de un auto",precioTotal=1000.0),
    Rifa(id=6,estado="disponible",nombre="Ana",titulo="Rifa de un auto",precioTotal=1000.0),
]


#la ruta de la api que va a mostrar todas las rifas
@app.get("/rifas",tags=["Rifas"],response_model=list[Rifa])
async def getRifas():
    return listaRifas

#la ruta de la api que va a mostrar una rifa en especifico
@app.get("/rifa/{id}",tags=["Rifas"],response_model=Rifa)
async def getRifa(id: int = Path(ge=1, le=9999)):
    for rifa in listaRifas:
        if (rifa.id == id):
            return rifa
    return {"error": "Rifa no encontrada"}

@app.get("/rifa",tags=["Rifas"])
async def getRifa(id: int = Query(ge=1, le=9999)):
    print("entro a la ruta")
    for rifa in listaRifas:
        if (rifa.id == id):
            return rifa
    return {"error": "Rifa no encontrada"}



@app.post("/rifa",tags=["Rifas"])
async def postRifa(rifa: Rifa):
    if(rifa.id in [rifa.id for rifa in listaRifas]):
        return {"error": "Rifa ya existe"}
    listaRifas.append(rifa)
    return rifa

@app.put("/rifa/{id}",tags=["Rifas"])
async def putRifa(id: int, rifa: Rifa):
    for i in range(len(listaRifas)):
        if (listaRifas[i].id == id):
            listaRifas[i] = rifa
            return rifa
    return {"error": "Rifa no encontrada"}

@app.delete("/rifa/{id}",tags=["Rifas"])
async def deleteRifa(id: int):
    for i in range(len(listaRifas)):
        if (listaRifas[i].id == id):
            listaRifas.pop(i)
            return {"mensaje": "Rifa eliminada"}
    return {"error": "Rifa no encontrada"}








