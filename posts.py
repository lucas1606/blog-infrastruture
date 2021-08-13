from models import Post
from datetime import datetime

post1 = Post(
    data = datetime.today(),
    titulo = 'Ótimo Gnoch Vegano',
    texto = 'Gnoch vegano preperado a base de batata doce',
    imagem = '../static/images/gnoch.jpeg',
)

post2 = Post(
        data = datetime.today(),
        titulo = 'Carbonara Vegano',
        texto = 'Carbonara vgano a base de cogumelos e tofú defumado',
        imagem = '../static/images/carbonara.jpeg',
)
post_list = [post1, post2]
