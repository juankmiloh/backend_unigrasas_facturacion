import pandas as pd
import numpy as np
import datetime
from flask import abort
from sqlalchemy.sql.elements import Null
from ..repository import ItemsRepository
from ..util.web_util import format_date
from ..util.web_util import add_wrapper

class ItemsService:

    def get_items(self, items_repository: ItemsRepository):
        items = []
        data = items_repository.get_items_bd()
        for result in data:
            items.append(
                {
                    'value': result[0],
                    'id': result[1],
                    'label': result[2],
                    'precio': result[3],
                    'descripcion': result[4],
                    'registro': str(result[5]),
                }
            )
        return items

    def items_insert(self, items_repository: ItemsRepository, dataitems):
        items_repository.items_insert_bd(dataitems)
        return add_wrapper(['item registrado con éxito!'])

    def items_update(self, items_repository: ItemsRepository, dataitems):
        items_repository.items_update_bd(dataitems)
        return add_wrapper(['item actualizado con éxito!'])

    def items_delete(self, items_repository: ItemsRepository, dataitems):
        items_repository.items_delete_bd(dataitems)
        return add_wrapper(['item borrado con éxito!'])