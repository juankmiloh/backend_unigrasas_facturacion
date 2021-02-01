from ..repository import EmpresaRepository
from ..util.web_util import add_wrapper

class EmpresaService:

    def get_empresas(self, empresa_repository: EmpresaRepository):
        empresas = []
        data = empresa_repository.get_empresas_bd()
        for result in data:
            empresas.append(
                {
                    'id_empresa': result[0],
                    'id_tipopersona': result[1],
                    'nit': result[2],
                    'dv': result[3],
                    'nombre': result[4],
                    'direccion': result[5],
                    'pais': result[6],
                    'ciudad': result[7],
                    'ciuu': result[8],
                    'matricula': result[9],
                }
            )
        return add_wrapper(empresas)