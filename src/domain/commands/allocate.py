import dataclasses

from .command import Command


@dataclasses.dataclass
class Allocate(Command):
    sku: str
    name: str
    quantity: int