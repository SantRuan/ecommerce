from domain.commands import command
from service_layer.unit_of_work import AbstractUnitOfWork
from typing import Union, Dict, Type, Callable
import logging

logger = logging.getLogger(__name__)
Message = Union[Type[command.Command], None]


class MessageBus:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
        command_handlers: Dict[Type[command.Command], Callable],
    ):
        self.uow = uow
        self.command_handlers = command_handlers
    
    def handle(self, message:Message):
        self.queue=[message]
        while self.queue:
            message = self.queue.pop(0)
            if isinstance(message, command.Command):
                self.handle_command(message)
            else:
                raise Exception(f"{message} was not an Event or Command")
    
    def handle_command(self,command: command.Command):
        try:
            handler = self.command_handlers[type(command)]
            handler(command)
        except:
            logger.exception("Exception handling command %s", command)
            raise