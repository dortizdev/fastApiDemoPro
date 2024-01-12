from fastapi import FastAPI
from redis_om import get_redis_connection

app = FastAPI()

redis = get_redis_connection(
    host=env.host,
    port=env.port,
    password=env.password,
    decode_responses=True
)

class Product():
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

@app.get('/products')
async def all():
    return []