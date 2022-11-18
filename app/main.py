from fastapi import FastAPI

app = FastAPI(title="Delivery Fee Calculator API")


@app.get("/")
async def home():
    return {"Welcome to": "FastAPI Delivery Fee Calculator"}

@app.post("/calculator")
async def calculator():
    return {"This will be the": "POST calculator"}
