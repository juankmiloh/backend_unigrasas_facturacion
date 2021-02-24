import json
from flask import request
from ..controller import controller
from ..service import InformeService
from ..repository import InformeRepository
from ..util.constants import API_ROOT_PATH


@controller.route(API_ROOT_PATH + 'producto_cliente', methods=['POST'])
def productoCliente(informe_service: InformeService, informe_repository: InformeRepository):
    # DATA
    datos = request.json
    print('--------------------------------')
    print('DATA PRODUCTOS -> ', datos)
    print('--------------------------------')
    return json.dumps(informe_service.get_cliente_producto(informe_repository, datos))

@controller.route(API_ROOT_PATH + 'cliente_producto', methods=['POST'])
def clienteProducto(informe_service: InformeService, informe_repository: InformeRepository):
    # DATA
    datos = request.json
    print('--------------------------------')
    print('DATA CLIENTES -> ', datos)
    print('--------------------------------')
    return json.dumps(informe_service.get_producto_cliente(informe_repository, datos))

@controller.route(API_ROOT_PATH + 'vendedor_cliente', methods=['POST'])
def vendedorCliente(informe_service: InformeService, informe_repository: InformeRepository):
    # DATA
    datos = request.json
    print('--------------------------------')
    print('DATA VENDEDOR -> ', datos)
    print('--------------------------------')
    return json.dumps(informe_service.get_cliente_vendedor(informe_repository, datos))