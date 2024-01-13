from abc import ABC, abstractmethod
from domain.models.product import Product


class AbstractRepository(ABC):

    @abstractmethod
    def _add(self, object):
        raise NotImplementedError

    @abstractmethod
    def _get(self, object):
        raise NotImplementedError


class SQLModelProductRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, product):
        self.session.add(product)

    def _get(self, sku):
        return self.session.query(Product).filter_by(sku=sku).first()
