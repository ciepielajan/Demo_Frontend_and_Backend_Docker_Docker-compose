import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}

class Item(BaseModel):
    Hello: str

@app.post("/prediction")
def get_potability(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run("hello_world_fastapi:app")
