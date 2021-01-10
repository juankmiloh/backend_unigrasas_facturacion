from itertools import count
from sqlalchemy.sql import text
from sqlalchemy.sql.elements import Null


class ClientesRepository:
    def __init__(self, db):
        self.db = db

    def get_clientes_bd(self):
        sql = '''
            SELECT C.*, TP.NOMBRE FROM CLIENTE C, TIPO_PERSONA TP WHERE C.IDTIPO_PERSONA = TP.IDTIPO_PERSONA ORDER BY C.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def clientes_insert_bd(self, cliente):
        print('-------------------------------------')
        print('OBJ CLIENTE -> ', cliente)
        print('-------------------------------------')

        tipopersona = cliente["tipopersona"]
        if tipopersona == 'Persona jurídica':
            tipopersona = 2
        else:
            tipopersona = 1

        sql = '''
            INSERT INTO CLIENTE(IDTIPO_PERSONA, NIT, NOMBRE, DIRECCION, EMAIL, TELEFONO, F_REGISTRO)
            VALUES (:IDTIPOPERSONA_ARG, :NIT_ARG, :NOMBRE_ARG, :DIRECCION_ARG, :EMAIL_ARG, :TELEFONO_ARG, CURRENT_TIMESTAMP);
        '''
        self.db.engine.execute(text(sql), IDTIPOPERSONA_ARG=tipopersona, NIT_ARG=cliente["nit"], NOMBRE_ARG=cliente["nombre"], DIRECCION_ARG=cliente["direccion"], EMAIL_ARG=cliente["email"], TELEFONO_ARG=cliente["telefono"])

    def clientes_update_bd(self, cliente):
        print('-------------------------------------')
        print('* CLIENTE A ACTUALIZAR -> ', cliente)
        print('-------------------------------------')

        tipopersona = cliente["tipopersona"]
        if tipopersona == 'Persona jurídica':
            tipopersona = 2
        else:
            tipopersona = 1

        sql = '''
            UPDATE 
                CLIENTE
	        SET 
                IDTIPO_PERSONA = :IDTIPOPERSONA_ARG,
                NIT = :NIT_ARG,
                NOMBRE = :NOMBRE_ARG,
                DIRECCION = :DIRECCION_ARG,
                EMAIL = :EMAIL_ARG,
                TELEFONO = :TELEFONO_ARG
	        WHERE IDCLIENTE = :IDCLIENTE_ARG;
        '''
        self.db.engine.execute(text(sql), IDCLIENTE_ARG=cliente["idcliente"], IDTIPOPERSONA_ARG=tipopersona, NIT_ARG=cliente["nit"], NOMBRE_ARG=cliente["nombre"], DIRECCION_ARG=cliente["direccion"], EMAIL_ARG=cliente["email"], TELEFONO_ARG=cliente["telefono"])
            
                        
    def clientes_delete_bd(self, cliente):
        print('-------------------------------------')
        print('* CLIENTE A ELIMINAR -> ', cliente)
        print('-------------------------------------')
        sql = '''
            DELETE FROM CLIENTE
            WHERE IDCLIENTE = :IDCLIENTE_ARG;
        '''
        self.db.engine.execute(text(sql), IDCLIENTE_ARG=cliente["idcliente"])