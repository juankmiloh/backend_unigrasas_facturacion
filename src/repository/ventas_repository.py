from sqlalchemy.sql import text


class VentasRepository:
    def __init__(self, db):
        self.db = db

    def get_ventas_lista_anos_bd(self):
        sql = '''
            SELECT TO_CHAR(F_EMISION, 'YYYY') ANOS FROM FACTURA
            GROUP BY TO_CHAR(F_EMISION, 'YYYY');
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_ventas_lista_meses_bd(self, ano):
        sql = '''
            SELECT CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) MES FROM FACTURA
            WHERE CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG
            GROUP BY (EXTRACT(MONTH FROM F_EMISION));
        '''
        return self.db.engine.execute(text(sql), ANO_ARG=ano).fetchall()
    
    def get_ventas_clientes_bd(self, datos):
        sql = '''
            SELECT C.IDCLIENTE, C.NOMBRE, SUM(FI.CANTIDAD) CANTIDAD, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL
            FROM FACTURA F, CLIENTE C, FACTURA_HAS_ITEM FI
            WHERE IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND F.IDCLIENTE = C.IDCLIENTE
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY C.IDCLIENTE, C.NOMBRE
            ORDER BY C.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=tuple(datos['cliente']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()
    
    def get_ventas_usuarios_bd(self, datos):
        sql = '''
            SELECT U.IDUSUARIO, U.NOMBRE, SUM(FI.CANTIDAD) CANTIDAD, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL
            FROM FACTURA F, USUARIO U, FACTURA_HAS_ITEM FI
            WHERE IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND F.IDUSUARIO = U.IDUSUARIO
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY U.IDUSUARIO, U.NOMBRE
            ORDER BY U.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql), USUARIO_ARG=tuple(datos['usuario']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()
    
    def get_ventas_productos_bd(self, datos):
        sql = '''
            SELECT FI.IDITEM, I.NOMBRE, SUM(FI.CANTIDAD) CANTIDAD, AVG(FI.PRECIO) PRECIO_PROM, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY FI.IDITEM, I.NOMBRE
            ORDER BY I.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=tuple(datos['cliente']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes']), USUARIO_ARG=tuple(datos['usuario']), ITEM_ARG=tuple(datos['producto'])).fetchall()

    def get_ventas_ano_bd(self, datos):
        sql = '''
            SELECT TO_CHAR(F.F_EMISION, 'YYYY') ANO, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY TO_CHAR(F.F_EMISION, 'YYYY')
            ORDER BY TO_CHAR(F.F_EMISION, 'YYYY') ASC;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=tuple(datos['cliente']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes']), USUARIO_ARG=tuple(datos['usuario']), ITEM_ARG=tuple(datos['producto'])).fetchall()
    
    def get_ventas_ano_mes_bd(self, datos):
        sql = '''
            SELECT TO_CHAR(F.F_EMISION, 'YYYY') ANO, CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) MES, SUM(FI.CANTIDAD * FI.PRECIO) TOTAL FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY TO_CHAR(F.F_EMISION, 'YYYY'), CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER);
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=tuple(datos['cliente']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes']), USUARIO_ARG=tuple(datos['usuario']), ITEM_ARG=tuple(datos['producto'])).fetchall()