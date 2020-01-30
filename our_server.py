import flask

app = flask.Flask(__name__)


@app.route("/")
def homepage():
    return "omg I created a server"


@app.route("/contact")
def contact(name):
    return "email me at info@google.com<br>I dare you"


@app.route("/create")
def create():
    with open("create.html", "r") as file:
        return file.read()

@app.route("/login")
def login():
    return ""



app.run(host="0.0.0.0", port=65535, debug=True)
