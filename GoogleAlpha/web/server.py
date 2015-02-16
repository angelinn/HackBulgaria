from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    html = open('index.html', 'r')
    text = html.read()
    html.close()

    return text


@app.route("/<request>")
def search(request):
    return request

if __name__ == "__main__":
    app.run()
