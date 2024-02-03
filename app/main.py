from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .v1.routes import clientRoute

app = FastAPI()

origins = [
    "http://localhost:3000",  # Adicione os domínios permitidos aqui
    "https://seu-outro-dominio.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique os métodos permitidos
    allow_headers=["*"],  # ou especifique os cabeçalhos permitidos
)

app.include_router(clientRoute.router, tags=["products"])