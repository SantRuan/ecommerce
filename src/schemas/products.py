

from pydantic import BaseModel


class Product(BaseModel):
    sku: str
    quantity: int