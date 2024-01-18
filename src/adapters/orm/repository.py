from abc import ABC, abstractmethod
from domain.models.product import Product
from adapters.orm.tables import products

class AbstractRepository(ABC):

    @abstractmethod
    def add(self, object):
        raise NotImplementedError

    @abstractmethod
    def get(self, object):
        raise NotImplementedError


class SQLModelProductRepository(AbstractRepository):
    
    def __init__(self, session):
        self.session = session

    def add(self, product):
        self.session.add(product)

    def get(self, sku):
        return self.session.query(Product).filter_by(sku=sku).first()

    def get_by_id(self, id):
        return self.session.query(products).filter_by(id).first()