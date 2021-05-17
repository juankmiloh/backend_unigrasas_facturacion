from sqlalchemy.sql import text


class InformeRepository:
    def __init__(self, db):
        self.db = db

    def get_cantidad_procesos_bd(self, idservicio):
        sql = '''
            SELECT (CASE WHEN FACTURA_ESTADO.CANTIDAD IS NOT NULL THEN FACTURA_ESTADO.CANTIDAD ELSE 0 END) AS CANTIDAD, ESTADO.NOMBRE FROM
            (SELECT * FROM ESTADO) ESTADO
            LEFT JOIN
            (SELECT F.IDESTADO, COUNT(*) AS CANTIDAD, E.NOMBRE FROM FACTURA F, ESTADO E
            WHERE F.IDESTADO = E.IDESTADO AND (F.IDCLIENTE = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG) 
            GROUP BY F.IDESTADO, E.NOMBRE ORDER BY E.NOMBRE ASC) FACTURA_ESTADO
            ON ESTADO.IDESTADO = FACTURA_ESTADO.IDESTADO;
        '''
        return self.db.engine.execute(text(sql), IDSERVICIO_ARG=idservicio).fetchall()

    # DATOS VENTAS X PRODUCTO
    
    def get_cantidad_cliente_producto(self, datos):
        sql = '''
            SELECT SUM(FI.CANTIDAD) AS CANTIDAD, C.NOMBRE FROM FACTURA F, CLIENTE C, FACTURA_HAS_ITEM FI
            WHERE F.IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND F.IDCLIENTE = C.IDCLIENTE
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY C.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), ITEM_ARG=tuple(datos['producto']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()

    def get_cliente_producto_bd(self, datos):
        sql = '''
            SELECT F.IDFACTURA, I.NOMBRE, C.NOMBRE, FI.CANTIDAD, FI.PRECIO, (FI.CANTIDAD * FI.PRECIO) AS TOTAL, TO_CHAR(F.F_EMISION, 'YYYY-Mon') AS FECHA
            FROM FACTURA F, CLIENTE C, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND F.IDCLIENTE = C.IDCLIENTE
            AND FI.IDITEM = I.IDITEM
            AND (FI.IDITEM IN :ITEM_ARG OR 0 IN :ITEM_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            ORDER BY I.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql), ITEM_ARG=tuple(datos['producto']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()

    # DATOS VENTAS X CLIENTE
    
    def get_cantidad_producto_cliente(self, datos):
        sql = '''
            SELECT SUM(FI.CANTIDAD) AS CANTIDAD, I.NOMBRE FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I
            WHERE F.IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY I.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=tuple(datos['cliente']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()

    def get_producto_cliente_bd(self, datos):
        sql = '''
            SELECT F.IDFACTURA, C.NOMBRE, I.NOMBRE, FI.CANTIDAD, FI.PRECIO, (FI.CANTIDAD * FI.PRECIO) AS TOTAL, TO_CHAR(F.F_EMISION, 'YYYY-Mon') AS FECHA 
            FROM FACTURA F, FACTURA_HAS_ITEM FI, ITEM I, CLIENTE C
            WHERE F.IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND FI.IDITEM = I.IDITEM
            AND F.IDCLIENTE = C.IDCLIENTE
            AND (F.IDCLIENTE IN :CLIENTE_ARG OR 0 IN :CLIENTE_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            ORDER BY C.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql), CLIENTE_ARG=tuple(datos['cliente']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()
    
    # DATOS VENTAS X VENDEDOR
    
    def get_cantidad_cliente_vendedor(self, datos):
        sql = '''
            SELECT SUM(FI.CANTIDAD) AS CANTIDAD, C.NOMBRE FROM FACTURA F, CLIENTE C, FACTURA_HAS_ITEM FI
            WHERE F.IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND F.IDCLIENTE = C.IDCLIENTE
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY C.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), USUARIO_ARG=tuple(datos['usuario']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()

    def get_cliente_vendedor_bd(self, datos):
        sql = '''
            SELECT F.IDFACTURA, U.NOMBRE, C.NOMBRE, SUM(FI.CANTIDAD), SUM(FI.CANTIDAD * FI.PRECIO) AS TOTAL, TO_CHAR(F.F_EMISION, 'YYYY-Mon') AS FECHA 
            FROM FACTURA F, CLIENTE C, USUARIO U, FACTURA_HAS_ITEM FI
            WHERE F.IDESTADO = 2
            AND F.IDFACTURA = FI.IDFACTURA
            AND F.IDCLIENTE = C.IDCLIENTE
            AND F.IDUSUARIO = U.IDUSUARIO
            AND (F.IDUSUARIO IN :USUARIO_ARG OR 0 IN :USUARIO_ARG)
            AND (CAST(TO_CHAR(F_EMISION, 'YYYY') AS INTEGER) IN :ANO_ARG OR 0 IN :ANO_ARG)
            AND (CAST((EXTRACT(MONTH FROM F_EMISION)) AS INTEGER) IN :MES_ARG OR 0 IN :MES_ARG)
            GROUP BY F.IDFACTURA, U.NOMBRE, C.NOMBRE, TO_CHAR(F.F_EMISION, 'YYYY-Mon')
            ORDER BY U.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), USUARIO_ARG=tuple(datos['usuario']), ANO_ARG=tuple(datos['ano']), MES_ARG=tuple(datos['mes'])).fetchall()