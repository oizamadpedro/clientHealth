from fastapi import FastAPI
from .v1.services.clientService import Client

app = FastAPI()

@app.get("/v1/clients")
def clients():
    clients = Client.get()
    return clients