
from abc import ABC, abstractmethod
from adapters.orm.repository import AbstractRepository, SQLModelProductRepository
from sqlmodel import create_engine, SQLModel, Session
from scripts import create_database
import config


class AbstractUnitOfWork(ABC):
    repository: AbstractRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def add():
        raise NotImplementedError
        

    def collect_new_events(self):
        for product in self.products.seen:
            while product.events:
                yield product.events.pop(0)

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


create_database.create_database()
engine = create_engine(config.get_postgres_uri())
sql_model_session = SQLModel.metadata.create_all(engine)


class SqlModelProductUnityOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=Session(engine)) -> None:
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory
        self.product = SQLModelProductRepository(self.session)
        return self 

    def __exit__(self, *args):
        self.session.close()

    def commit(self):
        self.session.commit()

    def add(self, product):
        repository_instance = SQLModelProductRepository(self.session)
        repository_instance.add(product=product)
        
    def rollback(self):
        self.session.rollback()

