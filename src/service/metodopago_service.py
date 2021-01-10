import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import MetodopagoRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class MetodopagoService:

    def get_metodopago(self, metodopago_repository: MetodopagoRepository):
        metodopago = []
        data = metodopago_repository.get_metodopago_bd()
        for result in data:
            metodopago.append(
                {
                    'idmetodopago': result[0],
                    'nombre': result[1],
                }
            )
        return metodopago