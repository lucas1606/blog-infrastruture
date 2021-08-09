from flask import Flask, render_template
from posts import post_list

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html',post_list = post_list)

@app.route("post/<int:post_id>")
def show_post(post_id):
    
    return render_template('post.html', post = post_list[post_id])
        

@app.route("/login")
def login(user, password):

    pass


if __name__ == '__main__':   
    app.run(debug= True)

