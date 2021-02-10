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
@controller.route(API_ROOT_PATH + 'ventas_lista_meses', methods=['GET'])
def meses(ventas_service: VentasService, ventas_repository: VentasRepository):
    # ano
    ano = request.args.get('ano', default='', type=int)
    return json.dumps(ventas_service.get_ventas_lista_meses(ventas_repository, ano))

# Obtener listado de clientes con ventas terminadas
@controller.route(API_ROOT_PATH + 'ventas_clientes', methods=['GET'])
def listclientes(ventas_service: VentasService, ventas_repository: VentasRepository):
    # ano
    ano = request.args.get('ano', default='', type=int)
    # mes
    mes = request.args.get('mes', default='', type=int)
    return json.dumps(ventas_service.get_ventas_clientes(ventas_repository, ano, mes))

# Obtener listado de usuarios con ventas terminadas x cliente
@controller.route(API_ROOT_PATH + 'ventas_usuarios', methods=['GET'])
def listusuarios(ventas_service: VentasService, ventas_repository: VentasRepository):
    # cliente
    cliente = request.args.get('cliente', default='', type=int)
    # ano
    ano = request.args.get('ano', default='', type=int)
    # mes
    mes = request.args.get('mes', default='', type=int)
    return json.dumps(ventas_service.get_ventas_usuarios(ventas_repository, cliente, ano, mes))

# Obtener listado de productos en ventas terminadas x cliente x usuario x producto
@controller.route(API_ROOT_PATH + 'ventas_productos', methods=['GET'])
def listproductos(ventas_service: VentasService, ventas_repository: VentasRepository):
    # cliente
    cliente = request.args.get('cliente', default='', type=int)
    # usuario
    usuario = request.args.get('usuario', default='', type=int)
    # ano
    ano = request.args.get('ano', default='', type=int)
    # mes
    mes = request.args.get('mes', default='', type=int)
    # producto
    producto = request.args.get('producto', default='', type=int)
    return json.dumps(ventas_service.get_ventas_productos(ventas_repository, cliente, usuario, ano, mes, producto))

# Obtener total de ventas x ano x mes
@controller.route(API_ROOT_PATH + 'ventas', methods=['GET'])
def ventas(ventas_service: VentasService, ventas_repository: VentasRepository):
    # cliente
    cliente = request.args.get('cliente', default='', type=int)
    # usuario
    usuario = request.args.get('usuario', default='', type=int)
    # ano
    ano = request.args.get('ano', default='', type=int)
    # mes
    mes = request.args.get('mes', default='', type=int)
    # producto
    producto = request.args.get('producto', default='', type=int)
    return json.dumps(ventas_service.get_ventas(ventas_repository, cliente, usuario, ano, mes, producto))
