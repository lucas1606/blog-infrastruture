from flask import Flask, render_template, session, request, redirect, flash, abort
from flask.helpers import url_for
from flask.wrappers import Request
from flask_login.utils import login_required
from postDao import PostDao
from userDao import UsuarioDao
from models import Post, Usuario
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.secret_key = '{}'.format(os.urandom(20))
postDao = PostDao()
usuarioDao = UsuarioDao()
login_manager = LoginManager()
login_manager.init_app(app)



#user routes
@login_manager.user_loader
def load_user(user_id):
    return Usuario(user_id)
@app.route('/')
def home_page():
    home_page_posts = []
    post_array= postDao.select_posts(2)
    for post in post_array:
        post = Post(post[1] ,post[2], post[3], post[4], post[0])
        home_page_posts.append(post)

    return render_template('home.html',post_list = home_page_posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = postDao.select_post_by_id(post_id)
    post = Post(post[1] ,post[2], post[3], post[4], post[0])
    return render_template('post.html', post = post)

 #admin routes   

@app.route('/login', methods=['POST', 'GET'])
def login():
    nome = request.form["user"]
    senha = request.form["psw"]
    user_id = usuarioDao.select_user_id(nome)
    if user_id:
        print('tem usuário')
        if usuarioDao.select_password_from_user(nome) == senha:
            print("senha é correta")
            user = Usuario(user_id)
            user.nome = nome
            user.senha = senha
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('admin_page', user = user))
    return redirect(url_for('home_page'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_page'))

@app.route('/admin')
@login_required
def admin_page():
    admin_page = []
    post_array= postDao.select_posts(3)
    for post in post_array:
        post = Post(post[1] ,post[2], post[3], post[4], post[0])
        admin_page.append(post)

    return render_template('admin_page.html', post_list = admin_page, user = current_user)

@app.route('/admin/<string:action>/<int:post_id>', methods=['POST', 'GET'])
@login_required
def post_crud(action=None ,post_id=None):
    if action == 'delete':
        post = postDao.select_post_by_id(post_id)
        os.remove(post[4][1:])
        postDao.delete_post(post_id)
        return redirect(url_for('admin_page'))
    if action == 'new':
        return redirect(url_for('post_editor'))
    if action == 'edit':
        return redirect(url_for('post_editor', post_id = post_id))


@app.route('/admin/editor/', methods=['POST', 'GET'])
@app.route('/admin/editor/<int:post_id>',  methods=['POST', 'GET'])
@login_required
def post_editor(post_id = None):
    if request.method == 'GET':
        if post_id == None:
            return render_template('post_editor.html',post = None)
        elif post_id:
            post = postDao.select_post_by_id(post_id)
            post = Post(post[1] ,post[2], post[3], post[4], post[0])
            return render_template('post_editor.html', post = post)
    elif request.method == 'POST':
        if post_id == None:
            titulo= request.form["titulo"]
            imagem= request.files["imagem"]
            texto= request.form["texto"]
            img_path = f'../static/images/{secure_filename(imagem.filename)}'
            imagem.save(img_path[1:])
            postDao.insert_post(titulo, texto, img_path)
            return redirect(url_for('admin_page'))
        elif post_id:
            titulo= request.form["titulo"]
            imagem= request.files["imagem"]
            texto= request.form["texto"]
            img_path = f'../static/images/{secure_filename(imagem.filename)}'
            imagem.save(img_path[1:])
            postDao.edit_post(titulo, texto, img_path, post_id)
            return redirect(url_for('admin_page'))

if __name__ == '__main__':   
    app.run(debug= True)

