import pandas as pd
import numpy as np
import datetime
from flask import abort
from ..repository import EmpresaRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class EmpresaService:

    def get_empresas(self, empresa_repository: EmpresaRepository, servicio):
        empresas = []
        data = empresa_repository.get_empresas_servicio_bd(servicio)
        for result in data:
            empresas.append(
                {
                    'id_empresa': result[0],
                    'nombre': result[1],
                    'nit': result[2],
                    'idservicio': result[3],
                    'servicio': result[4],
                }
            )
        return add_wrapper(empresas)