import json

from flask import request

from ..controller import controller
from ..service import MetodopagoService
from ..repository import MetodopagoRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'metodopago', methods=['GET'])
def metodopago(metodopago_service: MetodopagoService, metodopago_repository: MetodopagoRepository):
    return json.dumps(metodopago_service.get_metodopago(metodopago_repository))
