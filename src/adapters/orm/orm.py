
import logging

from adapters.orm.product import products
from domain.models.product import Product
from sqlalchemy.orm import registry


logger = logging.getLogger(__name__)

mapper_registry = registry()

def start_mappers():
    logger.info("Starting Mapper")

    product_mapper = mapper_registry.map_imperatively(Product, products)
