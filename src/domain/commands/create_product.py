import dataclasses

from .command import Command


@dataclasses.dataclass
class CreateProduct(Command):
    sku: str
    quantity: int