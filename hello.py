from flask import flask
app = Flask(__name__)


@app.route('/')
def hello_world():
	retrun 'Hello, World'


if __name__ =='__main__'
	app.run()
