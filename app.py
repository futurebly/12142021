from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Home"

@app.route("/read/1/")
def read():
    return "Read"

@app.route("/read/2/")
def read2():
    return "Read2"

app.run(debug=True,host="0.0.0.0",port="8000")
