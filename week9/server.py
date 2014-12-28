from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    html = open('index.html', 'r').read()
    return html


@app.route("/about/")
def about():
    return """
    <h1>Abou!</h1>t
    <a href="/">Main!</a
    """


@app.route("/user/<username>")
def user(username):
    return username

if __name__ == "__main__":
    app.run()
