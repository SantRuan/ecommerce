from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry

mapper_registry = registry()

products = Table("products",
                 mapper_registry.metadata,
                 Column("id", Integer, primary_key=True, autoincrement=True),
                 Column("sku", String(255)),
                 Column("quantity", Integer, nullable=False),
                 )
