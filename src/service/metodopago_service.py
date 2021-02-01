from ..repository import MetodopagoRepository

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