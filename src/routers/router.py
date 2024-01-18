from fastapi import APIRouter
from typing import Union
from schemas.products import Product
from domain.commands.allocate import Allocate as CommandAloccate
from service_layer import bootstrap
router = APIRouter()

bus = bootstrap.bootstrap()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/allocate")
def allocate_product(product:Product):
   command = CommandAloccate(sku=product.sku,name=product.name, quantity=product.quantity)
   bus.handle(command)