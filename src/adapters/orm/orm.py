
import logging

from adapters.orm.tables import products, mapper_registry
from domain.models.product import Product
from sqlalchemy import create_engine

import config

logger = logging.getLogger(__name__)



def start_mappers():
    logger.info("Starting Mapper")
    
    mapper_registry.map_imperatively(Product, products)

def create_tables():
    mapper_registry.metadata.create_all(bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    ))    