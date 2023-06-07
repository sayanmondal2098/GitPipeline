from typing import Union
from fastapi.params import Body
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/")
def basic_post(payLoad : dict = Body(...)):
    print(payLoad)
    return {"message": f"successfull post request with data {payLoad} "}