from fastapi import FastAPI
from app.request import Request
from app.calculator import Calculator

app = FastAPI(title="Delivery Fee Calculator API")


@app.get("/")
async def home():
    return {"Welcome to": "FastAPI Delivery Fee Calculator"}


@app.post("/calculator")
async def calculator(request: Request):
    calc = Calculator(request.cart_value, request.delivery_distance,
                      request.number_of_items, request.time)
    return calc.get_total_delivery_fee()
