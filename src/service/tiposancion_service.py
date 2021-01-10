import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import TiposancionRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class TiposancionService:

    def get_tiposancion(self, tiposancion_repository: TiposancionRepository):
        tiposancion = []
        data = tiposancion_repository.get_tiposancion_bd()
        for result in data:
            tiposancion.append(
                {
                    'idtiposancion': result[0],
                    'nombre': result[1],
                }
            )
        return tiposancion