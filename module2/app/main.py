from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI(title="Highload Shop API", version="0.2.0")

@app.get("/")
async def root():
    return {
        "service": "highload-shop",
        "instance": socket.gethostname(),   # ← Кто обработал запрос
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "instance": socket.gethostname()}

@app.get("/products")
async def list_products():
    return {
        "instance": socket.gethostname(),
        "products": [
            {"id": 1, "name": "Ноутбук", "price": 89990},
            {"id": 2, "name": "Смартфон", "price": 49990},
            {"id": 3, "name": "Наушники", "price": 12990}
        ],
        "total": 3
    }