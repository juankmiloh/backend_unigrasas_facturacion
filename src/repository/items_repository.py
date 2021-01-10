from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class ItemsRepository:
    def __init__(self, db):
        self.db = db

    def get_items_bd(self):
        sql = '''
            SELECT * FROM ITEM ORDER BY NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def items_insert_bd(self, item):
        print('-------------------------------------')
        print('OBJ ITEM -> ', item)
        print('-------------------------------------')
        sql = '''
            INSERT INTO ITEM(COD_ITEM, NOMBRE, PRECIO, DESCRIPCION, F_REGISTRO)
            VALUES (:CODITEM_ARG, :NOMBRE_ARG, :PRECIO_ARG, :DESCRIPCION_ARG, CURRENT_TIMESTAMP);
        '''
        self.db.engine.execute(text(sql), CODITEM_ARG=item["id"], NOMBRE_ARG=item["label"], PRECIO_ARG=item["precio"], DESCRIPCION_ARG=item["descripcion"])

    def items_update_bd(self, item):
        print('-------------------------------------')
        print('* ITEM A ACTUALIZAR -> ', item)
        print('-------------------------------------')

        sql = '''
            UPDATE 
                ITEM
	        SET 
                COD_ITEM = :CODITEM_ARG,
                NOMBRE = :NOMBRE_ARG,
                PRECIO = :PRECIO_ARG,
                DESCRIPCION = :DESCRIPCION_ARG
	        WHERE IDITEM = :IDITEM_ARG;
        '''
        self.db.engine.execute(text(sql), IDITEM_ARG=item["value"], CODITEM_ARG=item["id"], NOMBRE_ARG=item["label"], PRECIO_ARG=item["precio"], DESCRIPCION_ARG=item["descripcion"])
            
                        
    def items_delete_bd(self, item):
        print('-------------------------------------')
        print('* ITEM A ELIMINAR -> ', item)
        print('-------------------------------------')
        sql = '''
            DELETE FROM ITEM
            WHERE IDITEM = :IDITEM_ARG;
        '''
        self.db.engine.execute(text(sql), IDITEM_ARG=item["value"])