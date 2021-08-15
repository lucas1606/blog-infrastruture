from flask import Flask, render_template, session, request, redirect
from flask.helpers import url_for
from postDao import PostDao
from models import Post
app = Flask(__name__)
user = 'admin'
password = 'admin'
postDao = PostDao()
#user routes

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
    if (request.form["user"] == user and request.form["psw"] == password):
        return redirect(url_for('admin_page'))
    else:
        return redirect(url_for('home_page'))



@app.route('/admin')
def admin_page():
    admin_page = []
    post_array= postDao.select_posts(3)
    for post in post_array:
        post = Post(post[1] ,post[2], post[3], post[4], post[0])
        admin_page.append(post)

    return render_template('admin_page.html', post_list = admin_page)

@app.route('/admin/<int:post_id>', methods=['POST', 'DELETE', 'UPDATE'])
def post_crud(post_id):
    if request.method == 'DELETE':
        postDao.delete_post(post_id)

    if request.method == 'UPDATE':
        




if __name__ == '__main__':   
    app.run(debug= True)

