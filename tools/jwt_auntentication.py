from fastapi import Request, HTTPException
from jwt import encode,decode
import os
from dotenv import load_dotenv
from fastapi.security import HTTPBearer
load_dotenv()
SECRET = os.getenv("SECRET")
ALGORITMO = os.getenv("ALGORITMO")
def create_token(data: dict, secret: str = SECRET, algorithm: str =ALGORITMO) -> str:
    return encode(data, secret, algorithm=algorithm)
    
def validar_token(token: str) -> dict:
    data: dict = decode(token, SECRET, algorithms=ALGORITMO)
    return data

class Autenticacion(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if auth.credentials:
            try:
                data = validar_token(auth.credentials)
                return data
            except:
                raise HTTPException(status_code=401, detail="Token invalido")
        raise HTTPException(status_code=401, detail="Token invalido")
