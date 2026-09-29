from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Items API")


class Item(BaseModel):
    name: str
    description: str


items = {}
next_item_id = 1


@app.get("/items")
def list_items():
    """Return all items."""
    # TODO: Return the items collection.
    return []


@app.post("/items")
def create_item(item: Item):
    """Create an item and return it with its identifier."""
    global next_item_id

    # TODO: Store the item and increment next_item_id.
    return {"id": next_item_id, **item.model_dump()}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return one item by identifier."""
    # TODO: Look up the item and handle an unknown identifier.
    return {"id": item_id}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Replace an existing item."""
    # TODO: Update the item and handle an unknown identifier.
    return {"id": item_id, **item.model_dump()}


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item by identifier."""
    # TODO: Delete the item and handle an unknown identifier.
    return {"deleted": item_id}
