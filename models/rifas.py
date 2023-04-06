#BaseModel es para crear las clases que se van a utilizar para crear las rifas
from pydantic import BaseModel, Field
#Optional es para que el atributo titulo sea opcional en los base model
from typing import Optional

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
