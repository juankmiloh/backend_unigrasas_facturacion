import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import MediopagoRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class MediopagoService:

    def get_mediopago(self, mediopago_repository: MediopagoRepository):
        mediopago = []
        data = mediopago_repository.get_mediopago_bd()
        for result in data:
            mediopago.append(
                {
                    'idmediopago': result[0],
                    'nombre': result[1],
                }
            )
        return mediopago