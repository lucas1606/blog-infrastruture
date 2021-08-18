from flask_login import UserMixin, AnonymousUserMixin
class Post:
    def __init__(self, data, titulo, texto, imagem,  id = None):
       
        self.data = data
        self.titulo = titulo
        self.texto = texto
        self.imagem= imagem
        self.id = id

class Usuario(UserMixin):

    nome = None
    senha = None

    def __init__(self, id):
        self.id = id
     

