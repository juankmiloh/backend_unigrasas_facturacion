from sqlalchemy.sql import text


class EmpresaRepository:
    def __init__(self, db):
        self.db = db

    def get_empresas_bd(self):
        sql = '''
            SELECT * FROM EMPRESA;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
