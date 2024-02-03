from fastapi import APIRouter
from ..services.clientService import Client

router = APIRouter()

@router.get("/v1/clients")
def clients():
    clients = Client.getAll()
    return {"data": clients, "status_code": 200}