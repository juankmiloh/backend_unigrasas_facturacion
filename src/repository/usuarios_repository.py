from sqlalchemy.sql import text


class UsuariosRepository:
    def __init__(self, db):
        self.db = db

    def autenticar_usuario(self, usuario):
        print('LOGIN USUARIO - >', usuario)
        sql = '''
            SELECT TOKEN FROM USUARIO
            WHERE 
                NICKNAME = :USER_ARG
            AND CONTRASENA = :PASS_ARG;
        '''
        return self.db.engine.execute(text(sql), USER_ARG=usuario["username"].lower(), PASS_ARG=usuario["password"]).fetchall()

    def getData_usuario(self, token):
        print('TOKEN USUARIO -> ', token)
        sql = '''
            SELECT 
                R.NOMBRE,
                U.DESCRIPCION,
                U.NICKNAME,
                CONCAT_WS(' ', U.NOMBRE, U.APELLIDO) AS USUARIO,
                U.IDUSUARIO,
                CASE WHEN (U.IDGENERO = 1 AND U.IDROL = 1) THEN 'Administrador'
                ELSE CASE WHEN (U.IDGENERO = 2 AND U.IDROL = 1) THEN 'Administradora'
                ELSE CASE WHEN (U.IDGENERO = 1 AND U.IDROL = 2) THEN 'Vendedor'
                ELSE CASE WHEN (U.IDGENERO = 2 AND U.IDROL = 2) THEN 'Vendedora'
                ELSE 'Consulta' END END END END AS PRIVILEGIO,
                U.AVATAR
            FROM USUARIO U, ROL R
            WHERE 
                U.IDROL = R.IDROL
                AND TOKEN = :TOKEN_ARG;
        '''
        return self.db.engine.execute(text(sql), TOKEN_ARG=token).fetchall()

    def get_usuarios_bd(self):
        sql = '''
            SELECT * FROM USUARIO WHERE IDROL <> 3 ORDER BY NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()

    def get_lista_usuarios_bd(self):
        sql = '''
            SELECT
                CASE WHEN (U.IDGENERO = 1 AND U.IDROL = 1) THEN 'Administrador'
                ELSE CASE WHEN (U.IDGENERO = 2 AND U.IDROL = 1) THEN 'Administradora'
                ELSE CASE WHEN (U.IDGENERO = 1 AND U.IDROL = 2) THEN 'Vendedor'
                ELSE CASE WHEN (U.IDGENERO = 2 AND U.IDROL = 2) THEN 'Vendedora'
                ELSE 'Consulta' END END END END AS PRIVILEGIO,
                U.*,
                G.NOMBRE
            FROM USUARIO U, ROL R, GENERO G
            WHERE 
                U.IDROL = R.IDROL
                AND U.IDGENERO = G.IDGENERO
            ORDER BY U.NOMBRE ASC;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_rol_bd(self):
        sql = '''
            SELECT * FROM ROL;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def get_nicknames_bd(self):
        sql = '''
            SELECT NOMBRE, APELLIDO, NICKNAME FROM USUARIO;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
    
    def usuarios_create_bd(self, usuario):
        sql = '''
            INSERT INTO USUARIO
            (NOMBRE, APELLIDO, IDGENERO, NICKNAME, DESCRIPCION, IDROL, AVATAR, CONTRASENA, TOKEN, IDEMPRESA) 
            VALUES (:NOMBRE_ARG, :APELLIDO_ARG, :GENERO_ARG, :NICKNAME_ARG, :DESCRIPCION_ARG, :ROL_ARG, :AVATAR_ARG, :CONTRASENA_ARG, :TOKEN_ARG, :EMPRESA_ARG);
        '''
        return self.db.engine.execute(text(sql), NOMBRE_ARG=usuario['nombre'], APELLIDO_ARG=usuario['apellido'], GENERO_ARG=usuario['genero'], NICKNAME_ARG=usuario['nickname'], DESCRIPCION_ARG=usuario['descripcion'], ROL_ARG=usuario['rol'], AVATAR_ARG=usuario['avatar'], CONTRASENA_ARG=usuario['contrasena'], TOKEN_ARG=usuario['token'], EMPRESA_ARG=1)
    
    def usuario_update_bd(self, usuario):
        print('-------------------------------------')
        print('* USUARIO A ACTUALIZAR -> ', usuario['contrasena'])
        print('-------------------------------------')
        if usuario['contrasena'] != '':    
            sql = '''
                UPDATE USUARIO SET
                    NOMBRE = :NOMBRE_ARG,
                    APELLIDO = :APELLIDO_ARG,
                    IDGENERO = :GENERO_ARG,
                    NICKNAME = :NICKNAME_ARG,
                    DESCRIPCION = :DESCRIPCION_ARG,
                    IDROL = :ROL_ARG,
                    AVATAR = :AVATAR_ARG,
                    CONTRASENA = :CONTRASENA_ARG,
                    TOKEN = :TOKEN_ARG
                WHERE IDUSUARIO = :IDUSUARIO_ARG;
            '''
        else:
            sql = '''
                UPDATE USUARIO SET
                    NOMBRE = :NOMBRE_ARG,
                    APELLIDO = :APELLIDO_ARG,
                    IDGENERO = :GENERO_ARG,
                    NICKNAME = :NICKNAME_ARG,
                    DESCRIPCION = :DESCRIPCION_ARG,
                    IDROL = :ROL_ARG,
                    AVATAR = :AVATAR_ARG,
                    TOKEN = :TOKEN_ARG
                WHERE IDUSUARIO = :IDUSUARIO_ARG;
            '''
            
        return self.db.engine.execute(text(sql), IDUSUARIO_ARG=usuario['idusuario'], NOMBRE_ARG=usuario['nombre'], APELLIDO_ARG=usuario['apellido'], GENERO_ARG=usuario['genero'], NICKNAME_ARG=usuario['nickname'], DESCRIPCION_ARG=usuario['descripcion'], ROL_ARG=usuario['rol'], AVATAR_ARG=usuario['avatar'], CONTRASENA_ARG=usuario['contrasena'], TOKEN_ARG=usuario['token'])

    def usuario_delete_bd(self, idusuario):
        print('-------------------------------------')
        print('* USUARIO A ELIMINAR -> ', idusuario)
        print('-------------------------------------')
        sql = '''
            DELETE FROM USUARIO
	        WHERE IDUSUARIO = :IDUSUARIO_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDUSUARIO_ARG=idusuario)

        return resultsql
