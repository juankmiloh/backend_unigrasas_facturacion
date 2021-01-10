import json

from flask import request

from ..controller import controller
from ..service import MediopagoService
from ..repository import MediopagoRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'mediopago', methods=['GET'])
def mediopago(mediopago_service: MediopagoService, mediopago_repository: MediopagoRepository):
    return json.dumps(mediopago_service.get_mediopago(mediopago_repository))
