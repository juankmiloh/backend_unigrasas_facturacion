import json
from flask import request
from ..controller import controller
from ..service import VentasService
from ..repository import VentasRepository
from ..util.constants import API_ROOT_PATH


# Obtener listado de anos de ventas
@controller.route(API_ROOT_PATH + 'ventas_lista_anos', methods=['GET'])
def anos(ventas_service: VentasService, ventas_repository: VentasRepository):
    return json.dumps(ventas_service.get_ventas_lista_anos(ventas_repository))

# Obtener listado de meses de ventas X ano
@controller.route(API_ROOT_PATH + 'ventas_lista_meses', methods=['POST'])
def meses(ventas_service: VentasService, ventas_repository: VentasRepository):
    # DATA
    datos = request.json
    print('--------------------------------')
    print('ANO -> ', datos)
    print('--------------------------------')
    return json.dumps(ventas_service.get_ventas_lista_meses(ventas_repository, datos))

# Obtener listado de clientes con ventas terminadas
@controller.route(API_ROOT_PATH + 'ventas_clientes', methods=['POST'])
def listclientes(ventas_service: VentasService, ventas_repository: VentasRepository):
    # DATA
    datos = request.json
    print('--------------------------------')
    print('DATA CLIENTES -> ', datos)
    print('--------------------------------')
    return json.dumps(ventas_service.get_ventas_clientes(ventas_repository, datos))

# Obtener listado de usuarios con ventas terminadas x cliente
@controller.route(API_ROOT_PATH + 'ventas_usuarios', methods=['POST'])
def listusuarios(ventas_service: VentasService, ventas_repository: VentasRepository):
    # DATA
    datos = request.json
    print('--------------------------------')
    print('DATA USUARIOS -> ', datos)
    print('--------------------------------')
    return json.dumps(ventas_service.get_ventas_usuarios(ventas_repository, datos))

# Obtener listado de productos en ventas terminadas x cliente x usuario x producto
@controller.route(API_ROOT_PATH + 'ventas_productos', methods=['POST'])
def listproductos(ventas_service: VentasService, ventas_repository: VentasRepository):
    # DATA
    datos = request.json
    print('--------------------------------')
    print('DATA PRODUCTOS -> ', datos)
    print('--------------------------------')
    return json.dumps(ventas_service.get_ventas_productos(ventas_repository, datos))

# Obtener total de ventas x ano
@controller.route(API_ROOT_PATH + 'ventas_ano', methods=['POST'])
def ventasano(ventas_service: VentasService, ventas_repository: VentasRepository):
    # DATA
    datos = request.json
    return json.dumps(ventas_service.get_ventas_ano(ventas_repository, datos))

# Obtener total de ventas x ano x mes
@controller.route(API_ROOT_PATH + 'ventas_ano_mes', methods=['POST'])
def ventasanomes(ventas_service: VentasService, ventas_repository: VentasRepository):
    # DATA
    datos = request.json
    return json.dumps(ventas_service.get_ventas_ano_mes(ventas_repository, datos))
