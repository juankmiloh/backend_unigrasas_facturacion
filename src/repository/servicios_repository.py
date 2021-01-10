from sqlalchemy.sql import text


class ServiciosRepository:
    def __init__(self, db):
        self.db = db

    def get_servicios_bd(self):
        sql = '''
            SELECT * FROM SERVICIO;
        '''
        return self.db.engine.execute(text(sql)).fetchall()