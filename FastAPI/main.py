from fastapi import FastAPI
from models import Item
# app is name in command, main is name of file in command
app = FastAPI()

@app.get("/") # other methods work as well, / is path, not endpoint
def read_root(): # path operation function
    return {"message": "Hello, World!"}

@app.get("/items/cola") # now this is working because it's above dynamic path below
def read_item_cola():
    return {"item": "cola"}

@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict:
    return {"item_id": item_id}

# curl -X GET 'http://127.0.0.1:8000/users?user_id=2'
@app.get("/users")
def read_user(user_id: int | None = None, admin: bool | None = False) -> dict:
    if user_id is None:
        return {"message": "No user id provided"}
    return {"user_id": f"user_{user_id}", "admin": admin}

@app.post("/items")
def create_item(item: Item) -> dict:
    return {"name": item.name, "description": item.description}
