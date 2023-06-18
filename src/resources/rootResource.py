import json
from fastapi import APIRouter

resource = APIRouter()

@resource.get("/")
async def root():
    return {"message": "Hello World"}