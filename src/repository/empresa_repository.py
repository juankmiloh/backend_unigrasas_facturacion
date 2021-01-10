from sqlalchemy.sql import text


class EmpresaRepository:
    def __init__(self, db):
        self.db = db

    def get_empresas_bd(self):
        sql = '''
            SELECT E.IDEMPRESA, E.NOMBRE, E.NIT, S.NOMBRE AS SERVICIO FROM EMPRESA E, SERVICIO S
            WHERE E.SERVICIO = S.idservicio
            AND S.IDSERVICIO IN (1, 2, 3);
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def get_empresas_servicio_bd(self, servicio):
        sql = '''
            SELECT
                E.IDEMPRESA,
                E.NOMBRE,
                E.NIT,
                S.IDSERVICIO,
                S.NOMBRE AS SERVICIO 
            FROM EMPRESA E, SERVICIO S
            WHERE
                E.SERVICIO = S.idservicio
                AND (S.IDSERVICIO = :SERVICIO_ARG OR 0 = :SERVICIO_ARG)
            ORDER BY E.NOMBRE ASC;
        '''

        return self.db.engine.execute(text(sql), SERVICIO_ARG=servicio).fetchall()
