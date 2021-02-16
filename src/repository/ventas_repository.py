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
            WHERE (DATE_FORMAT(F_PAGO, '%Y') IN :ANO_ARG OR 0 IN :ANO_ARG)
            GROUP BY CONVERT((DATE_FORMAT(F_PAGO, '%m')), SIGNED INTEGER);
        '''
        return self.db.engine.execute(text(sql), ANO_ARG=ano).fetchall()
    
    def get_ventas_clientes_bd(self, datos):
        sql = '''
            SELECT C.IDCLIENTE, C.NOMBRE FROM FACTURA F, CLIENTE C
            WHERE IDESTADO = 2
            AND F.IDCLIENTE = C.IDCLIENTE
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY C.IDCLIENTE, C.NOMBRE
            ORDER BY C.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), USUARIO_ARG=datos['usuario'], ANO_ARG=datos['ano'], MES_ARG=datos['mes']).fetchall()
    
    def get_ventas_usuarios_bd(self, datos):
        sql = '''
            SELECT U.IDUSUARIO, U.NOMBRE FROM FACTURA F, USUARIO U
            WHERE IDESTADO = 2
            AND F.IDUSUARIO = U.IDUSUARIO
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY U.IDUSUARIO, U.NOMBRE
            ORDER BY U.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=datos['cliente'], ANO_ARG=datos['ano'], MES_ARG=datos['mes']).fetchall()
    
    def get_ventas_productos_bd(self, datos):
        sql = '''
            SELECT FI.IDITEM, I.NOMBRE, SUM(FI.CANTIDAD) CANTIDAD, AVG(FI.PRECIO) PRECIO_PROM, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY FI.IDITEM, I.NOMBRE
            ORDER BY I.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=datos['cliente'], ANO_ARG=datos['ano'], MES_ARG=datos['mes'], USUARIO_ARG=datos['usuario'], ITEM_ARG=datos['producto']).fetchall()

    def get_ventas_ano_bd(self, datos):
        sql = '''
            SELECT DATE_FORMAT(F.F_PAGO, '%Y') ANO, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY DATE_FORMAT(F.F_PAGO, '%Y');
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=datos['cliente'], ANO_ARG=datos['ano'], MES_ARG=datos['mes'], USUARIO_ARG=datos['usuario'], ITEM_ARG=datos['producto']).fetchall()
    
    def get_ventas_ano_mes_bd(self, datos):
        sql = '''
            SELECT DATE_FORMAT(F.F_PAGO, '%Y') ANO, DATE_FORMAT(F.F_PAGO, '%m') MES, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%Y') IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (DATE_FORMAT(F.F_PAGO, '%m') IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY DATE_FORMAT(F.F_PAGO, '%Y'), DATE_FORMAT(F.F_PAGO, '%m');
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=datos['cliente'], ANO_ARG=datos['ano'], MES_ARG=datos['mes'], USUARIO_ARG=datos['usuario'], ITEM_ARG=datos['producto']).fetchall()