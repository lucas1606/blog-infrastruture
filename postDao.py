from datetime import datetime
import dbinit

SQL_INSERT_POST = "INSERT INTO post(titulo, texto, imagem) VALUES('{}', '{}', '{}');"
                 
SQL_DELETE_POST = "DELETE FROM post WHERE id = {};"

SQL_SELECT_POST_BY_ID = "SELECT * FROM post WHERE id = {};"

SQL_SELECT_POSTS = "SELECT * FROM post;"

SQL_UPDATE_POST = '''UPDATE post SET
                     titulo = '{}',
                     texto = '{}',
                     imagem = '{}',
                     WHERE id = {};
                     '''


today = datetime.today().strftime('%d/%m/%Y')
connection = dbinit.execute_db

class PostDao:

    def insert_post(self,titulo, texto, imagem):
        connection(SQL_INSERT_POST.format(titulo, texto, imagem))
    
    def edit_post(self,titulo, texto, imagem, id):
        connection(SQL_UPDATE_POST.format(titulo, texto, imagem ,id))  
    
    def delete_post(self,id):
        try:
            connection(SQL_DELETE_POST.format(id))
            return 'Post {} excluido com sucesso'.format(id)
        except:
            return 'Ocorreu um erro ao deletar o post {}'.format(id)
    
    def select_post_by_id(self,id):
        return list(connection(SQL_SELECT_POST_BY_ID.format(id), 1))

    def select_posts(self,n_posts):
        return list(connection(SQL_SELECT_POSTS, query_posts = n_posts))

try:
    dbinit.check_if_db_exists()
finally:
    pass
