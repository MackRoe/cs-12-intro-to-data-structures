from flask import flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Worms"


if __name__ == '__main__':
    app.run()