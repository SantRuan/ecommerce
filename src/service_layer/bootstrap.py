from service_layer import unit_of_work


def bootstrap(start_orm: bool = True,
              uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlModelProductUnityOfWork,
              ):

    if start_orm:
        from adapters.orm import orm
        orm.start_mappers()
