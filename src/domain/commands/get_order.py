from dataclasses import dataclass
from .command import Command

@dataclass
class GetOrder(Command):
    orderid: int