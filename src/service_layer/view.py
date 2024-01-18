
from domain.commands import get_order
from service_layer import unit_of_work
from .handlers import get_product_from_repository

def get_products(command:get_order.GetOrder, uow: unit_of_work.SqlModelProductUnityOfWork):
    return get_product_from_repository(command,uow)
    