from domain.commands.create_product import CreateProduct
from domain.models.product import Product

from domain.commands.get_order import GetOrder
from service_layer import unit_of_work

def create_product(command:CreateProduct, uow: unit_of_work.SQLModelProductRepository):
    
    with uow:
        product = Product(sku=command.sku, quantity=command.quantity)
        uow.add(product=product)
        uow.commit()

def get_product_from_repository(command: GetOrder, uow: unit_of_work.SQLModelProductRepository):
    
    with uow:
        product = uow.get_by_id(command.orderid)
    return product
        
COMMAND_HANDLERS = {
    CreateProduct: create_product,
    GetOrder: get_product_from_repository   
}