import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/prediction")
def get_prediction(item: dict): # uwaga, fastapi wymusza typing. Bez tego front będzie zwracał błąd. Może być bardziej rozbudowany jako pydatic :)
    data = item["data"]
    data["age"] = 35
    return item


if __name__ == "__main__":
    uvicorn.run("hello_world_fastapi:app")
