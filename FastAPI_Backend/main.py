import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}


@app.post("/prediction")
def get_potability(data):
    # received = data.dict()

    return {"Prediction": data}


if __name__ == "__main__":
    uvicorn.run("hello_world_fastapi:app")