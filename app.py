from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Home"

@app.route("/read/1/")
def read():
    return "Read"

app.run(debug=True,host="0.0.0.0",port="8000")
