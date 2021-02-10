from flask import Blueprint
controller = Blueprint('controller', __name__, url_prefix='/')
# src.controller
from . import (
    clientes_controller,
    empresa_controller,
    estados_controller,
    facturaHasItem_controller,
    front_controller,
    informe_controller,
    items_controller,
    mediopago_controller,
    metodopago_controller,
    procesos_controller,
    usuarios_controller,
    ventas_controller,
)