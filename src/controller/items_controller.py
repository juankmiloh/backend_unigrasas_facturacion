import json

from flask import request

from ..controller import controller
from ..service import ItemsService
from ..repository import ItemsRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'items', methods=['GET'])
def items(items_service: ItemsService, items_repository: ItemsRepository):
    return json.dumps(items_service.get_items(items_repository))

# Crear un item
@controller.route(API_ROOT_PATH + 'items', methods=['POST'])
def createItems(items_service: ItemsService, items_repository: ItemsRepository):
    dataitems = request.json
    return json.dumps(items_service.items_insert(items_repository, dataitems))

# Actualizar item
@controller.route(API_ROOT_PATH + 'items', methods=['PUT'])
def updateItems(items_service: ItemsService, items_repository: ItemsRepository):
    # Datos items
    dataitems = request.json
    return json.dumps(items_service.items_update(items_repository, dataitems))

# Eliminar un item
@controller.route(API_ROOT_PATH + 'items', methods=['DELETE'])
def deleteItems(items_service: ItemsService, items_repository: ItemsRepository):
    # Datos items
    dataitems = request.json
    return json.dumps(items_service.items_delete(items_repository, dataitems))