from abc import ABC, abstractmethod
from domain.models.product import Product


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
