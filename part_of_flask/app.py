import flask

app = flask.Flask(__name__)

@app.route('/flask/opo')
def opo():
    return 'hello from flask'

if __name__ == '__main__':
    app.run(debug=True, port=5000)