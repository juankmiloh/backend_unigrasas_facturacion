from ..repository import MediopagoRepository

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