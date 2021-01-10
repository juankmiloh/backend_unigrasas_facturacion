from sqlalchemy.sql import text


class MetodopagoRepository:
    def __init__(self, db):
        self.db = db

    def get_metodopago_bd(self):
        sql = '''
            SELECT * FROM METODO_PAGO;
        '''
        return self.db.engine.execute(text(sql)).fetchall()