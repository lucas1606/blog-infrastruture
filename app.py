from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "<h1>Blog infra structure</h1>"


@app.route("/login")
def login(user, password):

    pass


if __name__ == '__main__':   
    app.run(debug= True)
