from flask import Flask, request, redirect
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    print(rows)
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    return f"""
    <html>
    <body>
        <h1><a href="/">Web</a></h1>
        <ul>
            {liTag}
        </ul>
        <h2>Welcome!</h2>
        Hello, WEB

        <ul>
            <li><a href="/create">create</a></li>
        </ul>
    </body>
    </html>
    """

@app.route("/read/<id>/")
def read(id):
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'

    cursor.execute('SELECT * FROM topics WHERE id = ?', (id,))
    topic = cursor.fetchone()
    return f"""
    <html>
    <body>
        <h1><a href="/">Web</a></h1>
        <ul>
            {liTag}
        </ul>
        <h2>{topic[1]}</h2>
        {topic[2]}

        <ul>
            <li><a href="/create/">create</a></li>
            <li>
                <form action="/delete/{id}" method='post'>
                    <input type='submit' value='DELETE'>
                </form>
            </li>
        </ul>
    </body>
    </html>
    """

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    con = sqlite3.connect('data.db')
    cursor = con.cursor()    
    sql = 'DELETE FROM topics WHERE id = ?'
    cursor.execute(sql, [id])
    con.commit()
    return redirect(f'/')


@app.route('/create_process/', methods=['POST'])
def create_process():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()    
    title = request.form.get('title')
    body = request.form.get('body')
    sql = 'INSERT INTO topics (title, body) VALUES(?, ?)'
    cursor.execute(sql, [title, body])
    con.commit()
    return redirect(f'/read/{cursor.lastrowid}')

@app.route("/create/")
def create():
    con = sqlite3.connect('data.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM topics')
    rows = cursor.fetchall()
    print(rows)
    liTag = ''
    for row in rows:
        liTag = liTag + f'<li><a href="/read/{row[0]}">{row[1]}</a></li>'
    return f"""
    <html>
    <body>
        <h1><a href="/">Web</a></h1>
        <ul>
            {liTag}
        </ul>

        <form action="/create_process/" method='post'>
            <p><input type='text' placeholder='title' name='title'></p>
            <p><input type='text' placeholder='body' name='body'></p>
            <p><input type='submit' value='create'></p>
        </form>

        <ul>
            <li><a href="/create">create</a></li>
        </ul>
    </body>
    </html>
    """

app.run(debug=True,host="0.0.0.0",port="8000")
