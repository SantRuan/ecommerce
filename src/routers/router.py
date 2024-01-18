from fastapi import APIRouter
from typing import Union
from schemas import products
from domain.commands.create_product import CreateProduct
from domain.commands.get_order import GetOrder
from service_layer import view
from service_layer import bootstrap
from schemas import products
import json
router = APIRouter()

bus = bootstrap.bootstrap()

@router.post("/create_product")
def create_product(product:products.Product):
   command = CreateProduct(sku=product.sku, quantity=product.quantity)
   bus.handle(command)

@router.get("/product/{id}")
def get_product(id: int):
   command = GetOrder(id)
   product = view.get_products(command,uow=bus.uow)
   return products.Product(sku=product.sku, quantity=product.quantity)