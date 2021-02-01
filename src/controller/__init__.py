from flask import Blueprint
controller = Blueprint('controller', __name__, url_prefix='/')
# src.controller
from . import (
    front_controller,
    empresa_controller,
    procesos_controller,
    usuarios_controller,
    estados_controller,
    metodopago_controller,
    mediopago_controller,
    facturaHasItem_controller,
    informe_controller,
    clientes_controller,
    items_controller
)