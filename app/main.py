from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


class Request(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: datetime


app = FastAPI(title="Delivery Fee Calculator API")


@app.get("/")
async def home():
    return {"Welcome to": "FastAPI Delivery Fee Calculator"}


@app.post("/calculator")
async def calculator(request: Request):
    return request
