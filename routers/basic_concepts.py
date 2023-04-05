#importamos las librerias que vamos a utilizar
#FastAPI es el framework que vamos a utilizar, Path y Query es para validar los parametros que se le pasan a las rutas
from fastapi import APIRouter,Path,Query,HTTPException
#BaseModel es para crear las clases que se van a utilizar para crear las rifas
from pydantic import BaseModel, Field
#Optional es para que el atributo titulo sea opcional en los base model
from typing import Optional

#creamos la aplicacion de fastapi
router= APIRouter(prefix="/rifa",tags=["Rifas"])


#la clase rifa es la que se va a utilizar para crear las rifas donde va a tener los atributos de la rifa que son
#id,estado,nombre de la persona a la quie se le asigno,precioTotal y titulo que es opcional
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
@router.get("/total",response_model=list[Rifa])
async def getRifas():
    return listaRifas

#la ruta de la api que va a mostrar una rifa en especifico
@router.get("/{id}",response_model=Rifa)
async def getRifa(id: int = Path(ge=1, le=9999),status_code=200):
    for rifa in listaRifas:
        if (rifa.id == id):
            return rifa
    raise HTTPException(status_code=404, detail="Rifa no encontrada")

@router.get("/")
async def getRifa(id: int = Query(ge=1, le=9999)):
    print("entro a la ruta")
    for rifa in listaRifas:
        if (rifa.id == id):
            return rifa
    return {"error": "Rifa no encontrada"}



@router.post("/",tags=["Rifas"])
async def postRifa(rifa: Rifa):
    if(rifa.id in [rifa.id for rifa in listaRifas]):
        return {"error": "Rifa ya existe"}
    listaRifas.append(rifa)
    return rifa

@router.put("/{id}",tags=["Rifas"])
async def putRifa(id: int, rifa: Rifa):
    for i in range(len(listaRifas)):
        if (listaRifas[i].id == id):
            listaRifas[i] = rifa
            return rifa
    return {"error": "Rifa no encontrada"}

@router.delete("/",tags=["Rifas"])
async def deleteRifa(id: int):
    for i in range(len(listaRifas)):
        if (listaRifas[i].id == id):
            listaRifas.pop(i)
            return {"mensaje": "Rifa eliminada"}
    return {"error": "Rifa no encontrada"}





