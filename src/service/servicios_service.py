import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import ServiciosRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class ServiciosService:

    def get_servicios(self, servicios_repository: ServiciosRepository):
        servicios = []
        data = servicios_repository.get_servicios_bd()
        for result in data:
            servicios.append(
                {
                    'idservicio': result[0],
                    'servicio': result[1],
                }
            )
        return servicios