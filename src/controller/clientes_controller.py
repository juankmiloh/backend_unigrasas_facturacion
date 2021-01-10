import json

from flask import request

from ..controller import controller
from ..service import ClientesService
from ..repository import ClientesRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'clientes', methods=['GET'])
def clientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    return json.dumps(clientes_service.get_clientes(clientes_repository))

# Crear un cliente
@controller.route(API_ROOT_PATH + 'clientes', methods=['POST'])
def createClientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    cliente = request.json
    return json.dumps(clientes_service.clientes_insert(clientes_repository, cliente))

# Actualizar cliente
@controller.route(API_ROOT_PATH + 'clientes', methods=['PUT'])
def updateClientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    # Datos clientes
    datacliente = request.json
    return json.dumps(clientes_service.clientes_update(clientes_repository, datacliente))

# Eliminar un cliente
@controller.route(API_ROOT_PATH + 'clientes', methods=['DELETE'])
def deleteClientes(clientes_service: ClientesService, clientes_repository: ClientesRepository):
    # Datos clientes
    datacliente = request.json
    return json.dumps(clientes_service.clientes_delete(clientes_repository, datacliente))