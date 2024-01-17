import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from dotenv import load_dotenv
from starlette.requests import Request

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)

# Should be a different database
redis = get_redis_connection(
    host=os.getenv("host"),
    port=os.getenv("port"),
    password=os.getenv("password"),
    decode_responses=True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str

    class Meta:
        database = redis

@app.post('/orders')
async def create(request: Request):
    body = await request.json()