from datetime import datetime

today = datetime.today().strftime('%d/%m/%Y')
class BlogPost:

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

post1 = BlogPost(
    titulo = 'Ótimo Gnoch Vegano',
    texto = 'Gnoch vegano preperado a base de batata doce',
    imagem = '../static/images/gnoch.jpeg',
)

post2 = BlogPost(
        titulo = 'Carbonara Vegano',
        texto = 'Carbonara vgano a base de cogumelos e tofú defumado',
        imagem = '../static/images/carbonara.jpeg',
)
post_list = [post1, post2]

post1.imprime_tudo()
post2.imprime_tudo()