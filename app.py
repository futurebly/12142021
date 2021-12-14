from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Home"

@app.route("/read/<id>/")
def read(id):
    return "Read"+id

@app.route("/create/")
def create():
    return "create"

app.run(debug=True,host="0.0.0.0",port="8000")
