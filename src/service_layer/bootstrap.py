import inspect
from service_layer import unit_of_work
from service_layer import handlers
from adapters.orm import orm
from service_layer import messagebus


def bootstrap(start_orm: bool = True,
              uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlModelProductUnityOfWork(),
              ) -> messagebus.MessageBus:

    if start_orm:

        orm.start_mappers()
        orm.create_tables()
    dependencies = {"uow": uow}
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }
    return messagebus.MessageBus(uow=uow, command_handlers=injected_command_handlers)


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)
