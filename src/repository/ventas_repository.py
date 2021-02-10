from sqlalchemy.sql import text


class VentasRepository:
    def __init__(self, db):
        self.db = db

    def get_ventas_lista_anos_bd(self):
        sql = '''
            SELECT DATE_FORMAT(F_PAGO, '%Y') ANOS FROM FACTURA
            GROUP BY DATE_FORMAT(F_PAGO, '%Y');
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_ventas_lista_meses_bd(self, ano):
        sql = '''
            SELECT CONVERT((DATE_FORMAT(F_PAGO, '%m')), SIGNED INTEGER) MES FROM FACTURA
            WHERE DATE_FORMAT(F_PAGO, '%Y') = :ANO_ARG
            GROUP BY DATE_FORMAT(F_PAGO, '%m');
        '''
        return self.db.engine.execute(text(sql), ANO_ARG=ano).fetchall()
    
    def get_ventas_clientes_bd(self, ano, mes):
        sql = '''
            SELECT C.IDCLIENTE, C.NOMBRE FROM FACTURA F, CLIENTE C
            WHERE IDESTADO = 2
            AND F.IDCLIENTE = C.IDCLIENTE
            AND (DATE_FORMAT(F.F_PAGO, '%Y') = :ANO_ARG OR 0 = :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') = :MES_ARG OR 0 = :MES_ARG)
            GROUP BY C.IDCLIENTE, C.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), ANO_ARG=ano, MES_ARG=mes).fetchall()
    
    def get_ventas_usuarios_bd(self, cliente, ano, mes):
        sql = '''
            SELECT U.IDUSUARIO, U.NOMBRE FROM FACTURA F, USUARIO U
            WHERE IDESTADO = 2
            AND F.IDUSUARIO = U.IDUSUARIO
            AND (F.IDCLIENTE = :CLIENTE_ARG OR 0 = :CLIENTE_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') = :ANO_ARG OR 0 = :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') = :MES_ARG OR 0 = :MES_ARG)
            GROUP BY U.IDUSUARIO, U.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=cliente, ANO_ARG=ano, MES_ARG=mes).fetchall()
    
    def get_ventas_productos_bd(self, cliente, usuario, ano, mes, producto):
        sql = '''
            SELECT FI.IDITEM, I.NOMBRE, FI.CANTIDAD, FI.PRECIO, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE = :CLIENTE_ARG OR 0 = :CLIENTE_ARG)
            AND (F.IDUSUARIO = :USUARIO_ARG OR 0 = :USUARIO_ARG)
            AND (FI.IDITEM = :ITEM_ARG OR 0 = :ITEM_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') = :ANO_ARG OR 0 = :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') = :MES_ARG OR 0 = :MES_ARG)
            GROUP BY FI.IDITEM, I.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=cliente, USUARIO_ARG=usuario, ANO_ARG=ano, MES_ARG=mes, ITEM_ARG=producto).fetchall()

    def get_ventas_bd(self, cliente, usuario, ano, mes, producto):
        sql = '''
            SELECT DATE_FORMAT(F.F_PAGO, '%Y') ANO, DATE_FORMAT(F.F_PAGO, '%m') MES, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE = :CLIENTE_ARG OR 0 = :CLIENTE_ARG)
            AND (F.IDUSUARIO = :USUARIO_ARG OR 0 = :USUARIO_ARG)
            AND (FI.IDITEM = :ITEM_ARG OR 0 = :ITEM_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') = :ANO_ARG OR 0 = :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') = :MES_ARG OR 0 = :MES_ARG)
            GROUP BY DATE_FORMAT(F.F_PAGO, '%Y'), DATE_FORMAT(F.F_PAGO, '%m');
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=cliente, USUARIO_ARG=usuario, ANO_ARG=ano, MES_ARG=mes, ITEM_ARG=producto).fetchall()