from datetime import datetime
import dbinit

SQL_CREATE_DB = "CREATE DATABASE blog;"

SQL_CREATE_TABLE = '''
            CREATE TABLE post(
                id SERIAL PRIMARY KEY,
                data DATE DEFAULT CURRENT_DATE,
                titulo VARCHAR(100) NOT NULL,
                texto TEXT,
                imagem VARCHAR(100));
                '''
SQL_INSERT_POST = ''' INSERT INTO post(titulo, texto, imagem)
                    VALUES({},{},{});
                    '''

SQL_DELETE_POST = "DELETE FROM post WHERE id = {};"

SQL_SELECT_POST_BY_ID = "SELECT * FROM post WHERE id = {};"

SQL_UPDATE_POST = '''UPDATE post SET
                     titulo = {},
                     texto = {},
                     imagem = {},
                     WHERE id = {};
                     '''

today = datetime.today().strftime('%d/%m/%Y')
connection = dbinit.execute_db


class PostDao:

    data = today
    def __init__(self, titulo, texto, imagem):
        self.titulo = titulo
        self.texto = texto
        self.imagem= imagem

    def imprime_tudo(self):
        print(self.titulo,
        self.texto,
        self.data,
        self.imagem)

    def insert_post(self):
        connection(SQL_INSERT_POST.format(self.titulo, self.texto, self.imagem))
    
    def edit_post(self, id):
        connection(SQL_UPDATE_POST.format(self.titulo, self.texto, self.imagem ,id))
    
    def delete_post(self, id):
        connection(SQL_DELETE_POST.format(id))

        
