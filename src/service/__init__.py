from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from .prueba_service import PruebaService
from .empresa_service import EmpresaService
from .procesos_service import ProcesosService
from .servicios_service import ServiciosService
from .usuarios_service import UsuariosService
from .estados_service import EstadosService
from .tiposancion_service import TiposancionService
from .decision_service import DecisionService
from .metodopago_service import MetodopagoService
from .mediopago_service import MediopagoService
from .facturaHasItem_service import FacturaHasItemService
from .informe_service import InformeService
from .clientes_service import ClientesService
from .items_service import ItemsService

class ServiceModule(Module):
    def configure(self, binder):
        prueba_service = PruebaService()
        empresa_service = EmpresaService()
        procesos_service = ProcesosService()
        servicios_service = ServiciosService()
        usuarios_service = UsuariosService()
        estados_service = EstadosService()
        tiposancion_service = TiposancionService()
        decision_service = DecisionService()
        metodopago_service = MetodopagoService()
        mediopago_service = MediopagoService()
        facturaHasItem_service = FacturaHasItemService()
        informe_service = InformeService()
        clientes_service = ClientesService()
        items_service = ItemsService()

        binder.bind(PruebaService, to=prueba_service, scope=singleton)
        binder.bind(EmpresaService, to=empresa_service, scope=singleton)
        binder.bind(ProcesosService, to=procesos_service, scope=singleton)
        binder.bind(ServiciosService, to=servicios_service, scope=singleton)
        binder.bind(UsuariosService, to=usuarios_service, scope=singleton)
        binder.bind(EstadosService, to=estados_service, scope=singleton)
        binder.bind(TiposancionService, to=tiposancion_service, scope=singleton)
        binder.bind(DecisionService, to=decision_service, scope=singleton)
        binder.bind(MetodopagoService, to=metodopago_service, scope=singleton)
        binder.bind(MediopagoService, to=mediopago_service, scope=singleton)
        binder.bind(FacturaHasItemService, to=facturaHasItem_service, scope=singleton)
        binder.bind(InformeService, to=informe_service, scope=singleton)
        binder.bind(ClientesService, to=clientes_service, scope=singleton)
        binder.bind(ItemsService, to=items_service, scope=singleton)
