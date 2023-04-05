#importamos las librerias que vamos a utilizar
#FastAPI es el framework que vamos a utilizar, Path y Query es para validar los parametros que se le pasan a las rutas
from fastapi import FastAPI,Path,Query,HTTPException
from routers import basic_concepts

#creamos la aplicacion de fastapi
app= FastAPI()
#le agregamos las rutas de la api

app.include_router(basic_concepts.router)

#le ponemos un titulo, descripcion y version a la api
app.title = "API DE RIFAS"
app.description = "a continuacion se muestran las rutas de la API"
app.version = "0.0.1"

