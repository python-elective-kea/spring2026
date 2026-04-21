from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic model (request/response validation)
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = ""

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = ""

# Simpel "database"
items: List[Item] = [
    Item(id=1, name="Item 1", description="Description for Item 1"),
    Item(id=2, name="Item 2", description="Description for Item 2")
]

# Hjælpefunktion
def find_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return None

# READ all
@app.get("/items", response_model=List[Item])
def get_items():
    return items

# READ one
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# CREATE
@app.post("/items", response_model=Item, status_code=201)
def create_item(new_item: ItemCreate):
    item = Item(
        id=len(items) + 1,
        name=new_item.name,
        description=new_item.description
    )
    items.append(item)
    return item

# UPDATE
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_data: ItemCreate):
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item.name = updated_data.name
    item.description = updated_data.description
    return item

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    item = find_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    items = [i for i in items if i.id != item_id]
    return {"result": "Item deleted"}