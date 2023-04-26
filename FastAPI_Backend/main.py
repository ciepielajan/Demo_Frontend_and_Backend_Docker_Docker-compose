import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Union, Any

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}

class Item(BaseModel):
    data: Dict[str, Any]

@app.post("/prediction")
def get_potability(item: Item):
    data = item.data
    data["age"] = 34
    return item


if __name__ == "__main__":
    uvicorn.run("hello_world_fastapi:app")
