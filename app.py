from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <!DOCTYPE html>
    <head>
        <title>WEB</title>
    </head>
    <body>
        <h1><a href="/index.html">Web</a></h1>
        <ol>
            <li><a href="/1.html">html</a></li>
            <li><a href="/2.html">css</a></li>
            <li><a href="/3.html">js</a></li>
        </ol>
        <h2>Welcome!</h2>
        Hello, WEB
    </body>
    </html>
    """

@app.route("/read/<id>/")
def read(id):
    return "Read"+id

@app.route("/create/")
def create():
    return "create"

app.run(debug=True,host="0.0.0.0",port="8000")
