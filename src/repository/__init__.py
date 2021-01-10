from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .prueba_repository import PruebaRepository
from .empresa_repository import EmpresaRepository
from .procesos_repository import ProcesosRepository
from .servicios_repository import ServiciosRepository
from .usuarios_repository import UsuariosRepository
from .estados_repository import EstadosRepository
from .tiposancion_repository import TiposancionRepository
from .decision_repository import DecisionRepository
from .metodopago_repository import MetodopagoRepository
from .mediopago_repository import MediopagoRepository
from .facturaHasItem_repository import FacturaHasItemRepository
from .informe_repository import InformeRepository
from .clientes_repository import ClientesRepository
from .items_repository import ItemsRepository


class RepositoryModule(Module):
    def __init__(self, db):
        self.db = db

    def configure(self, binder):
        prueba_repository = PruebaRepository(self.db)
        empresa_repository = EmpresaRepository(self.db)
        procesos_repository = ProcesosRepository(self.db)
        servicios_repository = ServiciosRepository(self.db)
        usuarios_repository = UsuariosRepository(self.db)
        estados_repository = EstadosRepository(self.db)
        tiposancion_repository = TiposancionRepository(self.db)
        decision_repository = DecisionRepository(self.db)
        metodopago_repository = MetodopagoRepository(self.db)
        mediopago_repository = MediopagoRepository(self.db)
        facturaHasItem_repository = FacturaHasItemRepository(self.db)
        informe_repository = InformeRepository(self.db)
        clientes_repository = ClientesRepository(self.db)
        items_repository = ItemsRepository(self.db)

        binder.bind(PruebaRepository, to=prueba_repository, scope=singleton)
        binder.bind(EmpresaRepository, to=empresa_repository, scope=singleton)
        binder.bind(ProcesosRepository, to=procesos_repository, scope=singleton)
        binder.bind(ServiciosRepository, to=servicios_repository, scope=singleton)
        binder.bind(UsuariosRepository, to=usuarios_repository, scope=singleton)
        binder.bind(EstadosRepository, to=estados_repository, scope=singleton)
        binder.bind(TiposancionRepository, to=tiposancion_repository, scope=singleton)
        binder.bind(DecisionRepository, to=decision_repository, scope=singleton)
        binder.bind(MetodopagoRepository, to=metodopago_repository, scope=singleton)
        binder.bind(MediopagoRepository, to=mediopago_repository, scope=singleton)
        binder.bind(FacturaHasItemRepository, to=facturaHasItem_repository, scope=singleton)
        binder.bind(InformeRepository, to=informe_repository, scope=singleton)
        binder.bind(ClientesRepository, to=clientes_repository, scope=singleton)
        binder.bind(ItemsRepository, to=items_repository, scope=singleton)