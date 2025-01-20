from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int

items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0),
    1: Item(name="Pliers", price=5.99, count=20, id=1),
    2: Item(name="Nails", price=1.99, count=100, id=2),
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def get_items() -> dict[str, dict[int, Item]]:
    return {"items": items}

@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise Exception(status_code=404, details=f"Item with {item_id} does not exist.")
    return items[item_id]