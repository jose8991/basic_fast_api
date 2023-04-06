#BaseModel es para crear las clases que se van a utilizar para crear las rifas
from pydantic import BaseModel, Field
#Optional es para que el atributo titulo sea opcional en los base model
from typing import Optional
from enum import Enum

#el usuario puede tener tres roles y dependiendo de rol va a tener ciertas acciones
class Rol(str, Enum):
    administrador = "administrador"
    vendedor = "vendedor"
    cliente = "cliente"

#la clase rifa es la que se va a utilizar para crear las rifas donde va a tener los atributos de la rifa que son
#id,estado,nombre de la persona a la quie se le asigno,precioTotal y titulo que es opcional
class Usuario(BaseModel):
    id: Optional[int]
    correo: Optional[str]
    username: Optional[str]
    full_name: Optional[str]
    numero_telefonico: Optional[int] 
    rol: Optional[Rol]
    contraseña: Optional[str] 
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "correo": "@gmail.com",
                "username": "pepito1998",
                "full_name": "Juan",
                "numero_telefonico": 123456789,
                "rol": "administrador",
                "contraseña": "123456"
            }
        }
