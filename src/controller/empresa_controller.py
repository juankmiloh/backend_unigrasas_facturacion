import json
from ..controller import controller
from ..repository import EmpresaRepository
from ..service import EmpresaService
from ..util.constants import API_ROOT_PATH

# Obtener lista de empresas
@controller.route(API_ROOT_PATH + 'empresa', methods=['GET'])
def empresas(empresa_service: EmpresaService, empresa_repository: EmpresaRepository):
    return json.dumps(empresa_service.get_empresas(empresa_repository))
