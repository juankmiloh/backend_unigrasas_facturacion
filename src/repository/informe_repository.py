from sqlalchemy.sql import text


class InformeRepository:
    def __init__(self, db):
        self.db = db

    def get_cantidad_procesos_bd(self, idservicio):
        sql = '''
            SELECT (CASE WHEN PROCESO_FASE.CANTIDAD IS NOT NULL THEN PROCESO_FASE.CANTIDAD ELSE 0 END) AS CANTIDAD, FASE.NOMBRE FROM
            (SELECT * FROM FASE) FASE
            LEFT JOIN
            (SELECT F.IDFASE, COUNT(*) AS CANTIDAD, F.NOMBRE FROM PROCESO P, FASE F WHERE P.FASE = F.IDFASE AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG) GROUP BY F.IDFASE, F.NOMBRE ORDER BY F.NOMBRE ASC) PROCESO_FASE
            ON FASE.IDFASE = PROCESO_FASE.IDFASE;
        '''
        return self.db.engine.execute(text(sql), IDSERVICIO_ARG=idservicio).fetchall()

    # DATOS EMPRESA
    
    def get_cantidad_procesos_empresa_bd(self, fase, idservicio):
        sql = '''
            SELECT COUNT(*), EMP.NOMBRE FROM PROCESO P, EMPRESA EMP
            WHERE 
                P.FASE = :FASE_ARG
                AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                AND P.EMPRESA = EMP.IDEMPRESA
                AND P.IDSERVICIO = EMP.SERVICIO
            GROUP BY EMP.NOMBRE;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()

    def get_procesos_empresa_bd(self, fase, idservicio):
        sql = '''
            SELECT P.IDPROCESO, P.RADICADOPROCESO, EMP.NOMBRE FROM PROCESO P, EMPRESA EMP
            WHERE 
                P.FASE = :FASE_ARG
                AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                AND P.EMPRESA = EMP.IDEMPRESA
                AND P.IDSERVICIO = EMP.SERVICIO;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()

    # DATOS CAUSAL
    
    def get_cantidad_procesos_causal_bd(self, fase, idservicio):
        sql = '''
            SELECT COUNT(*), C.NOMBRECAUSAL FROM PROCESO P, PROCESO_CAUSAL PC, CAUSAL C
            WHERE 
                P.FASE = :FASE_ARG
                AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                AND P.IDPROCESO = PC.IDPROCESO
                AND PC.IDCAUSAL = C.IDCAUSAL
            GROUP BY 
                PC.IDCAUSAL,
                C.NOMBRECAUSAL;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()

    def get_procesos_causal_bd(self, fase, idservicio):
        sql = '''
            SELECT P.IDPROCESO, P.RADICADOPROCESO, C.NOMBRECAUSAL FROM PROCESO P, PROCESO_CAUSAL PC, CAUSAL C
            WHERE 
                P.FASE = :FASE_ARG
                AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                AND P.IDPROCESO = PC.IDPROCESO
                AND PC.IDCAUSAL = C.IDCAUSAL;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()

    # DATOS USUARIO
    
    def get_cantidad_procesos_usuario_bd(self, fase, idservicio):
        sql = '''
            SELECT COUNT(*), U.NOMBRE||' '||U.APELLIDO FROM PROCESO P, USUARIOS U
            WHERE
                P.FASE = :FASE_ARG
                AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                AND P.USUARIOASIGNADO = U.IDUSUARIO
            GROUP BY U.NOMBRE||' '||U.APELLIDO;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()
    
    def get_procesos_usuario_bd(self, fase, idservicio):
        sql = '''
            SELECT P.IDPROCESO, P.RADICADOPROCESO, U.NOMBRE||' '||U.APELLIDO FROM PROCESO P, USUARIOS U
            WHERE
                P.FASE = :FASE_ARG
                AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                AND P.USUARIOASIGNADO = U.IDUSUARIO;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()

    # DATOS ESTADO
    
    def get_cantidad_procesos_estado_bd(self, fase, idservicio):
        sql = '''
            SELECT COUNT(*), ESTADO FROM
            (
                SELECT 
                    P.IDPROCESO,
                    P.RADICADOPROCESO AS EXPEDIENTE,
                    P.FECHACADUCIDAD AS CADUCIDAD,
                    EMP.NOMBRE AS EMPRESA,
                    ES.NOMBREESTADO AS ESTADO,
                    S.NOMBRE AS SERVICIO,
                    U.IDUSUARIO AS IDUSUARIO,
                    U.NOMBRE || ' ' || U.APELLIDO AS USUARIO,
                    EP.ETAPA
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES
                WHERE
                    P.FASE = :FASE_ARG
                    AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                    AND P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
            ) PROCESO,
            (
                SELECT 
                    P.IDPROCESO,
                    MIN(EP.ETAPA) AS IDETAPA
                FROM PROCESO P, ETAPA_PROCESO EP
                WHERE
                    P.IDPROCESO = EP.PROCESO
                GROUP BY P.IDPROCESO
            ) ETAPA
            WHERE
                PROCESO.IDPROCESO = ETAPA.IDPROCESO
                AND PROCESO.ETAPA = ETAPA.IDETAPA
            GROUP BY ESTADO;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()
    
    def get_procesos_estado_bd(self, fase, idservicio):
        sql = '''
            SELECT PROCESO.IDPROCESO, PROCESO.EXPEDIENTE, ESTADO FROM
            (
                SELECT 
                    P.IDPROCESO,
                    P.RADICADOPROCESO AS EXPEDIENTE,
                    P.FECHACADUCIDAD AS CADUCIDAD,
                    EMP.NOMBRE AS EMPRESA,
                    ES.NOMBREESTADO AS ESTADO,
                    S.NOMBRE AS SERVICIO,
                    U.IDUSUARIO AS IDUSUARIO,
                    U.NOMBRE || ' ' || U.APELLIDO AS USUARIO,
                    EP.ETAPA
                FROM
                    EMPRESA EMP, SERVICIO S, PROCESO P, USUARIOS U, ETAPA_PROCESO EP, ETAPA E, ESTADO ES
                WHERE
                    P.FASE = :FASE_ARG
                    AND (P.IDSERVICIO = :IDSERVICIO_ARG OR 0 = :IDSERVICIO_ARG)
                    AND P.IDPROCESO = EP.PROCESO
                    AND EP.ETAPA = E.IDETAPA
                    AND E.IDESTADO = ES.IDESTADO
                    AND P.EMPRESA = EMP.IDEMPRESA
                    AND EMP.SERVICIO = S.IDSERVICIO
                    AND P.IDSERVICIO = S.IDSERVICIO
                    AND P.USUARIOASIGNADO = U.IDUSUARIO
            ) PROCESO,
            (
                SELECT 
                    P.IDPROCESO,
                    MIN(EP.ETAPA) AS IDETAPA
                FROM PROCESO P, ETAPA_PROCESO EP
                WHERE
                    P.IDPROCESO = EP.PROCESO
                GROUP BY P.IDPROCESO
            ) ETAPA
            WHERE
                PROCESO.IDPROCESO = ETAPA.IDPROCESO
                AND PROCESO.ETAPA = ETAPA.IDETAPA;
        '''
        return self.db.engine.execute(text(sql), FASE_ARG=fase, IDSERVICIO_ARG=idservicio).fetchall()