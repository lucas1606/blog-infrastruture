from flask import Flask, render_template, session, request, redirect
from flask.helpers import url_for
from posts import post_list

app = Flask(__name__)
user = 'admin'
password = 'admin'
log = False

#user routes

@app.route('/')
def home_page():
    return render_template('home.html',post_list = post_list)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return render_template('post.html', post = post_list[post_id])

 #admin routes   

@app.route('/login', methods=['POST', 'GET'])
def login():
    if (request.form["user"] == user and request.form["psw"] == password):
        return admin_page()
    else:
        return redirect(url_for('home_page'))



@app.route('/admin', methods=['POST', 'GET', 'DELETE', 'UPDATE'])
def admin_page():
        return render_template('admin_page.html', post_list = post_list)
    

if __name__ == '__main__':   
    app.run(debug= True)

