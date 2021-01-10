import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
from ..repository import FacturaHasItemRepository
from ..util.web_util import format_date
from ..util.web_util import add_wrapper

class FacturaHasItemService:

    def get_facturaHasItem(self, facturaHasItem_repository: FacturaHasItemRepository):
        facturaHasItem = []
        data = facturaHasItem_repository.get_facturaHasItem_bd()
        for result in data:
            facturaHasItem.append(
                {
                    'idfactura': result[0],
                    'iditem': result[1],
                    'cantidad': result[2],
                }
            )
        return facturaHasItem

    def get_facturaHasItem_proceso(self, facturaHasItem_repository: FacturaHasItemRepository, idproceso):
        facturaHasItems = []
        data = facturaHasItem_repository.get_facturaHasItem_proceso_bd(idproceso)
        for result in data:
                
            facturaHasItems.append(
                {
                    'idfactura': result[0],
                    'iditem': result[1],
                    'cantidad': result[2],
                    'precio': result[3],
                    'coditem': result[4],
                    'item': result[5],
                    'descripcion': result[6],
                }
            )
        return facturaHasItems

    def facturaHasItem_insert(self, facturaHasItem_repository: FacturaHasItemRepository, facturaHasItem):
        facturaHasItem_repository.facturaHasItem_insert_bd(facturaHasItem)
        return add_wrapper(['FacturaHasItem registrada con éxito!'])

    def facturaHasItem_update(self, facturaHasItem_repository: FacturaHasItemRepository, dataFacturaHasItem):
        facturaHasItem_repository.facturaHasItem_update_bd(dataFacturaHasItem)
        return add_wrapper(['FacturaHasItem actualizada con éxito!'])

    def facturaHasItem_delete(self, facturaHasItem_repository: FacturaHasItemRepository, facturaHasItem):
        facturaHasItem_repository.facturaHasItem_delete_bd(facturaHasItem)
        return add_wrapper(['FacturaHasItem borrada con éxito!'])