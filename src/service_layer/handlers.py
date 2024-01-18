from domain.commands.allocate import Allocate as CommandAllocate
from domain.models.product import Product
from domain.commands.allocate import Allocate as CommandAllocate
from service_layer import unit_of_work

def allocate(command:CommandAllocate, uow: unit_of_work.SQLModelProductRepository):
    
    with uow:
        product = Product(sku=command.sku, name=command.name, quantity=command.quantity)
        uow.add(product=product)
        uow.commit()

COMMAND_HANDLERS = {
CommandAllocate: allocate
}