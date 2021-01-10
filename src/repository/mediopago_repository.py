from sqlalchemy.sql import text


class MediopagoRepository:
    def __init__(self, db):
        self.db = db

    def get_mediopago_bd(self):
        sql = '''
            SELECT * FROM MEDIO_PAGO;
        '''
        return self.db.engine.execute(text(sql)).fetchall()