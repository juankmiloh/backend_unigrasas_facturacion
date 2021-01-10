from sqlalchemy.sql import text


class ProcesosRepository:
    def __init__(self, db):
        self.db = db

    def get_procesos_bd(self):
        sql = '''
            SELECT F.IDFACTURA, C.NOMBRE, F.F_EMISION, F.TOTAL, U.IDUSUARIO, CONCAT_WS(' ', U.NOMBRE, U.APELLIDO) AS USUARIO, F.F_VENCIMIENTO FROM FACTURA F, CLIENTE C, USUARIO U
            WHERE F.IDCLIENTE = C.IDCLIENTE
            AND F.IDUSUARIO = U.IDUSUARIO
            ORDER BY F.IDFACTURA DESC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_proceso_inicial_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT F.IDFACTURA, F.IDCLIENTE, F.DIVISA, F.F_EMISION, F.TOTAL, U.IDUSUARIO, CONCAT_WS(' ', U.NOMBRE, U.APELLIDO) AS USUARIO FROM FACTURA F, CLIENTE C, USUARIO U
            WHERE F.IDCLIENTE = C.IDCLIENTE
            AND F.IDUSUARIO = U.IDUSUARIO
            AND F.IDFACTURA = :IDPROCESO_ARG;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()
    
    def get_proceso_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            SELECT
                F.IDFACTURA,
                F.IDCLIENTE,
                F.IDMETODO_PAGO,
                F.IDMEDIO_PAGO,
                U.IDUSUARIO,
                F.DIVISA,
                F.F_EMISION,
                F.F_VENCIMIENTO,
                F.F_PAGO,
                F.TOTAL,
                F.DESCRIPCION,
                C.NOMBRE AS CLIENTE,
                C.DIRECCION,
                C.NIT,
                C.TELEFONO,
                C.EMAIL,
                METODOP.NOMBRE AS NEGOCIACION,
                MEDIOP.NOMBRE AS MEDIOPAGO,
                CONCAT(U.NOMBRE, ' ', U.APELLIDO) AS VENDEDOR
            FROM FACTURA F, CLIENTE C, USUARIO U, MEDIO_PAGO MEDIOP, METODO_PAGO METODOP 
            WHERE
            F.IDFACTURA = :IDPROCESO_ARG
            AND F.IDCLIENTE = C.IDCLIENTE
            AND F.IDUSUARIO = U.IDUSUARIO
            AND F.IDMETODO_PAGO = METODOP.IDMETODO_PAGO
            AND F.IDMEDIO_PAGO = MEDIOP.IDMEDIO_PAGO;
        '''
        return self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso).fetchall()

    def proceso_insert_bd(self, proceso):
        print('-------------------------------------')
        print('OBJ FACTURA -> ', proceso)
        print('-------------------------------------')
        sql = '''
            INSERT INTO FACTURA(IDCLIENTE, IDUSUARIO, IDESTADO, DIVISA, F_EMISION, TOTAL, F_REGISTRO)
            VALUES (:IDCLIENTE_ARG, :IDUSUARIO_ARG, :ESTADO_ARG, :DIVISA_ARG, STR_TO_DATE(:F_EMISION_ARG,'%Y/%m/%d %H:%i:%s'), :TOTAL_ARG, CURRENT_TIMESTAMP);
        '''
        resultsql = self.db.engine.execute(text(sql), IDCLIENTE_ARG=proceso["cliente"], IDUSUARIO_ARG=proceso["usuario"], ESTADO_ARG=1, DIVISA_ARG=proceso["divisa"], TOTAL_ARG=0, F_EMISION_ARG=proceso["f_emision"])

        return resultsql
    
    def proceso_usuario_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* FACTURA A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE FACTURA
            SET IDUSUARIO = :IDUSUARIO_ARG
            WHERE IDFACTURA = :IDFACTURA_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDFACTURA_ARG=dataProceso["idfactura"], IDUSUARIO_ARG=dataProceso["usuario"])

        return resultsql

    def proceso_total_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* FACTURA A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE FACTURA
            SET TOTAL = :TOTAL_ARG
            WHERE IDFACTURA = :IDFACTURA_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDFACTURA_ARG=dataProceso["idfactura"], TOTAL_ARG=dataProceso["total"])

        return resultsql

    def proceso_update_bd(self, dataProceso):
        print('-------------------------------------')
        print('* PROCESO A ACTUALIZAR -> ', dataProceso)
        print('-------------------------------------')

        # if dataProceso["caducidad"] == 'None':
        #     dataProceso["caducidad"] = None

        sql = '''
            UPDATE 
                FACTURA
	        SET 
                IDCLIENTE = :IDCLIENTE_ARG,
                IDMETODO_PAGO = :IDMETODO_PAGO_ARG,
                IDMEDIO_PAGO = :IDMEDIO_PAGO_ARG,
                IDUSUARIO = :IDUSUARIO_ARG,
                DIVISA = :DIVISA_ARG,
                F_EMISION = STR_TO_DATE(:FEMISION_ARG,'%Y/%m/%d %H:%i:%s'),
                F_VENCIMIENTO = STR_TO_DATE(:FVENCIMIENTO_ARG,'%Y/%m/%d %H:%i:%s'),
                F_PAGO = STR_TO_DATE(:FPAGO_ARG,'%Y/%m/%d %H:%i:%s'),
                TOTAL = :TOTAL_ARG,
                DESCRIPCION = :DESCRIPCION_ARG
	        WHERE
                IDFACTURA = :IDFACTURA_ARG;
        '''
        self.db.engine.execute(text(sql), IDFACTURA_ARG=dataProceso["idfactura"], IDCLIENTE_ARG=dataProceso["cliente"],
         IDMETODO_PAGO_ARG=dataProceso["metodopago"], IDMEDIO_PAGO_ARG=dataProceso["mediopago"], IDUSUARIO_ARG=dataProceso["idusuario"],
         DIVISA_ARG=dataProceso["divisa"], FEMISION_ARG=dataProceso["f_emision"], FVENCIMIENTO_ARG=dataProceso["f_vencimiento"], 
         FPAGO_ARG=dataProceso["f_pago"], TOTAL_ARG=dataProceso["total"], DESCRIPCION_ARG=dataProceso["descripcion"])
    
    def proceso_delete_bd(self, idProceso):
        print('-------------------------------------')
        print('* PROCESO A ELIMINAR -> ', idProceso)
        print('-------------------------------------')
        sql = '''
            UPDATE FACTURA
            SET IDESTADO = 3
            WHERE IDFACTURA = :IDPROCESO_ARG;
        '''
        self.db.engine.execute(text(sql), IDPROCESO_ARG=idProceso)