import json

from flask import request

from ..controller import controller
from ..service import DecisionService
from ..repository import DecisionRepository
from ..util.constants import API_ROOT_PATH

@controller.route(API_ROOT_PATH + 'decision', methods=['GET'])
def decision(decision_service: DecisionService, decision_repository: DecisionRepository):
    return json.dumps(decision_service.get_decision(decision_repository))
