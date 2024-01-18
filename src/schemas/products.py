

from pydantic import BaseModel


class Product(BaseModel):
    sku: str
    name: str
    quantity: int