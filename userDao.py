import dbinit

SQL_INSERT_USER = "INSERT INTO usuario(nome, senha) VALUES('{}', '{}');"

SQL_EDIT_USER_PASSWORD = '''UPDATE usuario SET senha = {} WHERE nome = {};'''

SQL_SELECT_USER_AND_PASSWORD = '''SELECT senha FROM usuario WHERE nome = '{}'; '''

SQL_SELECT_USER_ID = "SELECT id FROM usuario WHERE nome = '{}';" 

connection = dbinit.execute_db


class UsuarioDao:

    def select_user_id(self, nome):
        try:
            id = connection(SQL_SELECT_USER_ID.format(nome),1)[0]
            return id
        except:
            return False
    def select_password_from_user(self, nome):
        try:
             return connection(SQL_SELECT_USER_AND_PASSWORD.format(nome), 1)[0]
        except:
            return NameError
    def insert_user(self, nome, senha):
        try:
            connection(SQL_INSERT_USER.format(nome, senha))
        except:
            return NameError