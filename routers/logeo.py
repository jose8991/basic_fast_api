from fastapi import APIRouter, Path, Query, HTTPException, Request
from models.usuario import Usuario
from tools.jwt_auntentication import create_token,validar_token,Autenticacion

router = APIRouter()

listaUsuarios = [
    Usuario(id=1, correo="jose@gmail.com", username="admin", full_name="admin", numero_telefonico=123456789, rol="administrador", contraseña="123456"),
    Usuario(id=2, correo="luis", username="vendedor", full_name="vendedor", numero_telefonico=123456789, rol="vendedor", contraseña="123456"),
    Usuario(id=3, correo="pepito", username="cliente", full_name="cliente", numero_telefonico=123456789, rol="cliente", contraseña="123456")
]

@router.post("/")
def login(user: Usuario):
    if user.correo == "jose@gmail.com" and user.contraseña == "123456" and user.rol == "administrador":
        token:str = create_token(user.dict())
        return {"token": token, "rol": user.rol}
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

