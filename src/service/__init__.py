from injector import Module, singleton

from .clientes_service import ClientesService
from .empresa_service import EmpresaService
from .estados_service import EstadosService
from .facturaHasItem_service import FacturaHasItemService
from .informe_service import InformeService
from .items_service import ItemsService
from .mediopago_service import MediopagoService
from .metodopago_service import MetodopagoService
from .procesos_service import ProcesosService
from .usuarios_service import UsuariosService
from .ventas_service import VentasService

class ServiceModule(Module):
    def configure(self, binder):
        clientes_service = ClientesService()
        empresa_service = EmpresaService()
        estados_service = EstadosService()
        facturaHasItem_service = FacturaHasItemService()
        informe_service = InformeService()
        items_service = ItemsService()
        mediopago_service = MediopagoService()
        metodopago_service = MetodopagoService()
        procesos_service = ProcesosService()
        usuarios_service = UsuariosService()
        ventas_service = VentasService()

        binder.bind(ClientesService, to=clientes_service, scope=singleton)
        binder.bind(EmpresaService, to=empresa_service, scope=singleton)
        binder.bind(EstadosService, to=estados_service, scope=singleton)
        binder.bind(FacturaHasItemService, to=facturaHasItem_service, scope=singleton)
        binder.bind(InformeService, to=informe_service, scope=singleton)
        binder.bind(ItemsService, to=items_service, scope=singleton)
        binder.bind(MediopagoService, to=mediopago_service, scope=singleton)
        binder.bind(MetodopagoService, to=metodopago_service, scope=singleton)
        binder.bind(ProcesosService, to=procesos_service, scope=singleton)
        binder.bind(UsuariosService, to=usuarios_service, scope=singleton)
        binder.bind(VentasService, to=ventas_service, scope=singleton)
