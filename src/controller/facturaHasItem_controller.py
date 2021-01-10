import json

from flask import request

from ..controller import controller
from ..service import FacturaHasItemService
from ..repository import FacturaHasItemRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'facturaHasItems', methods=['GET'])
def facturaHasItem(facturaHasItem_service: FacturaHasItemService, facturaHasItem_repository: FacturaHasItemRepository):
    return json.dumps(facturaHasItem_service.get_facturaHasItem(facturaHasItem_repository))

# Obtener detalle de las facturaHasItems de un proceso
@controller.route(API_ROOT_PATH + 'facturaHasItems/detalle', methods=['GET'])
def getFacturaHasItem(facturaHasItem_service: FacturaHasItemService, facturaHasItem_repository: FacturaHasItemRepository):
    # Id proceso
    idProceso = request.args.get('idproceso', default='', type=int)
    return json.dumps(facturaHasItem_service.get_facturaHasItem_proceso(facturaHasItem_repository, idProceso))

# Crear una facturaHasItem
@controller.route(API_ROOT_PATH + 'facturaHasItems', methods=['POST'])
def createFacturaHasItem(facturaHasItem_service: FacturaHasItemService, facturaHasItem_repository: FacturaHasItemRepository):
    facturaHasItem = request.json
    return json.dumps(facturaHasItem_service.facturaHasItem_insert(facturaHasItem_repository, facturaHasItem))

# Actualizar facturaHasItem
@controller.route(API_ROOT_PATH + 'facturaHasItems/update', methods=['PUT'])
def updateFacturaHasItem(facturaHasItem_service: FacturaHasItemService, facturaHasItem_repository: FacturaHasItemRepository):
    # Datos facturaHasItem
    dataFacturaHasItem = request.json
    return json.dumps(facturaHasItem_service.facturaHasItem_update(facturaHasItem_repository, dataFacturaHasItem))

# Eliminar una facturaHasItem
@controller.route(API_ROOT_PATH + 'facturaHasItems', methods=['DELETE'])
def deleteFacturaHasItem(facturaHasItem_service: FacturaHasItemService, facturaHasItem_repository: FacturaHasItemRepository):
    # Datos facturaHasItem
    dataFacturaHasItem = request.json
    return json.dumps(facturaHasItem_service.facturaHasItem_delete(facturaHasItem_repository, dataFacturaHasItem))