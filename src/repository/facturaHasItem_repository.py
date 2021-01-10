from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class FacturaHasItemRepository:
    def __init__(self, db):
        self.db = db

    def get_facturaHasItem_bd(self):
        sql = '''
            SELECT * FROM FACTURA_HAS_ITEM;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_facturaHasItem_proceso_bd(self, idProceso):
        print('---------- IDFACTURA ', idProceso, ' ----------------')
        sql = '''
            SELECT FHI.*, I.COD_ITEM, I.NOMBRE, I.DESCRIPCION FROM FACTURA_HAS_ITEM FHI, ITEM I
            WHERE 
            FHI.IDFACTURA = :IDPROCESO_ARG
            AND FHI.IDITEM = I.IDITEM;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def facturaHasItem_insert_bd(self, facturaHasItem):
        print('-------------------------------------')
        print('OBJ FACTURA_ITEM -> ', facturaHasItem)
        print('-------------------------------------')
        sql = '''
            INSERT INTO FACTURA_HAS_ITEM (IDFACTURA, IDITEM, CANTIDAD, PRECIO) VALUES (:IDFACTURA_ARG, :IDITEM_ARG, :CANTIDAD_ARG, :PRECIO_ARG);
        '''
        self.db.engine.execute(text(sql), IDFACTURA_ARG=facturaHasItem["idfactura"], IDITEM_ARG=facturaHasItem["iditem"], CANTIDAD_ARG=facturaHasItem["cantidad"], PRECIO_ARG=facturaHasItem["precio"])

    def facturaHasItem_update_bd(self, facturaHasItem):
        print('-------------------------------------')
        print('* FACTURA_ITEM A ACTUALIZAR -> ', facturaHasItem)
        print('-------------------------------------')
        sql = '''
            UPDATE
                FACTURA_HAS_ITEM
	        SET
                CANTIDAD = :CANTIDAD_ARG,
                PRECIO = :PRECIO_ARG
	        WHERE IDFACTURA = :IDFACTURA_ARG
            AND IDITEM = :IDITEM_ARG;
        '''
        self.db.engine.execute(text(sql), IDFACTURA_ARG=facturaHasItem["idfactura"], IDITEM_ARG=facturaHasItem["iditem"], CANTIDAD_ARG=facturaHasItem["cantidad"], PRECIO_ARG=facturaHasItem["precio"])
                        
    def facturaHasItem_delete_bd(self, facturaHasItem):
        print('-------------------------------------')
        print('* FACTURA_ITEM A ELIMINAR -> ', facturaHasItem)
        print('-------------------------------------')
        sql = '''
            DELETE FROM FACTURA_HAS_ITEM
            WHERE IDFACTURA = :IDFACTURA_ARG
            AND IDITEM = :IDITEM_ARG;
        '''
        self.db.engine.execute(text(sql), IDFACTURA_ARG=facturaHasItem["idfactura"], IDITEM_ARG=facturaHasItem["iditem"])