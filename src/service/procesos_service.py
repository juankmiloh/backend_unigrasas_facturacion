import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
from ..repository import ProcesosRepository
from ..util.web_util import format_date
from ..util.web_util import add_wrapper


class ProcesosService:

    def get_procesos(self, procesos_repository: ProcesosRepository):
        procesos = []
        data = procesos_repository.get_procesos_bd()
        for result in data:
            f_vencimiento = None
            # print('-------------------- f_vencimiento -----------------', result[2])

            if result[6]:
                f_vencimiento = str(result[6])

            procesos.append(
                {
                    'idfactura': result[0],
                    'cliente': result[1],
                    'f_emision': str(result[2]),
                    'total': result[3],
                    'idusuario': result[4],
                    'usuario': result[5],
                    'f_vencimiento': f_vencimiento
                }
            )
        return procesos

    def proceso_detalle_inicial(self, procesos_repository: ProcesosRepository, idProceso):
        proceso = []
        data = procesos_repository.get_proceso_inicial_bd(idProceso)
        for result in data:
            caducidad = None
            # print('-------------------- CADUCIDAD -----------------', result[2])

            if result[2]:
                caducidad = str(result[2])
    
            proceso.append(
                {
                    'idfactura': result[0],
                    'cliente': result[1],
                    'divisa': result[2],
                    'f_emision': str(result[3]),
                    'total': result[4],
                    'idusuario': result[5],
                    'usuario': result[6]
                }
            )
        return proceso
    
    def proceso_detalle(self, procesos_repository: ProcesosRepository, idProceso):
        proceso = []
        data = procesos_repository.get_proceso_bd(idProceso)
        for result in data:
            print('-------------------- DATA FACTURA -----------------', result)    
            proceso.append(
                {
                    'idfactura': result[0],
                    'cliente': result[1],
                    'metodopago': result[2],
                    'mediopago': result[3],
                    'idusuario': result[4],
                    'divisa': result[5],
                    'f_emision': str(result[6]),
                    'f_vencimiento': str(result[7]),
                    'f_pago': str(result[8]),
                    'total': result[9],
                    'descripcion': result[10],
                    'n_cliente': result[11],
                    'direccion': result[12],
                    'nit': result[13],
                    'telefono': result[14],
                    'email': result[15],
                    'negociacion': result[16],
                    'n_mediopago': result[17],
                    'vendedor': result[18],
                }
            )
        return proceso

    def proceso_insert(self, procesos_repository: ProcesosRepository, proceso):
        procesos_repository.proceso_insert_bd(proceso)
        return add_wrapper(['Expediente registrado con éxito!'])
    
    def proceso_usuario_update(self, procesos_repository: ProcesosRepository, dataProceso):
        procesos_repository.proceso_usuario_update_bd(dataProceso)
        return add_wrapper(['Expediente actualizado con éxito!'])

    def proceso_total_update(self, procesos_repository: ProcesosRepository, dataProceso):
        procesos_repository.proceso_total_update_bd(dataProceso)
        return add_wrapper(['Total actualizado con éxito!'])
    
    def proceso_update(self, procesos_repository: ProcesosRepository, dataProceso):
        procesos_repository.proceso_update_bd(dataProceso)
        return add_wrapper(['Expediente actualizado con éxito!'])

    def proceso_delete(self, procesos_repository: ProcesosRepository, proceso):
        procesos_repository.proceso_delete_bd(proceso)
        return add_wrapper(['Expediente borrado con éxito!'])
