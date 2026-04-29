from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Product Service")


class Product(BaseModel):
    id: str
    name: str
    price: float
    available: bool


PRODUCTS: dict[str, Product] = {
    "1": Product(id="1", name="Laptop", price=1200.0, available=True),
    "2": Product(id="2", name="Keyboard", price=75.5, available=True),
    "3": Product(id="3", name="Monitor", price=320.0, available=False),
}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "product-service"}


@app.get("/products", response_model=list[Product])
def list_products() -> list[Product]:
    return list(PRODUCTS.values())


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str) -> Product:
    product = PRODUCTS.get(product_id)
    if product is None:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )
    return product
