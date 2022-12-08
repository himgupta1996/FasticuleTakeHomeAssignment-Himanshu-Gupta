from typing import Union
from fastapi import FastAPI

service = FastAPI()

@service.get("/")
def read_root():
    return {"Hello": "World"}


@service.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
