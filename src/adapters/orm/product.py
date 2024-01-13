
from sqlmodel import Table, MetaData, Column, String, Integer
metadata = MetaData()


products = Table("products",
                 metadata,
                 Column("id", Integer, primary_key=True, autoincrement=True),
                 Column("sku", String(255)),
                 Column("qty", Integer, nullable=False),
                 Column("orderid", String(255)),
                 )
