from sqlalchemy.sql import text


class DecisionRepository:
    def __init__(self, db):
        self.db = db

    def get_decision_bd(self):
        sql = '''
            SELECT * FROM DESCISIONRECURSO;
        '''
        return self.db.engine.execute(text(sql)).fetchall()