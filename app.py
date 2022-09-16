from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL


app = Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password2005'
app.config['MYSQL_DB'] = 'saad'

mysql = MySQL(app)



@app.route("/")
def hello_world():
    
    return render_template('index.html')

@app.route("/people")
def people():
    cursor = mysql.connection.cursor()
    cursor.execute('''select * from Info;''')
    data = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('people.html', data=data)

@app.route("/form")
def form():
    return render_template('form.html')


@app.route("/login", methods = ['post'])
def login():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute(""" INSERT INTO Info VALUES (%s,%s ,%s) """, (name, number, email))
    mysql.connection.commit()
    cursor.close()
    return """yay! User added successfully
    <p>to view entries press <a href="/people">here</a>
        """


#deleting
@app.route("/delete", methods = ['post'])
def delete():
    number = request.form['deletenum']
    cursor = mysql.connection.cursor()
    cursor.execute("""Delete from Info where number=%s;""",(number,))
    mysql.connection.commit()
    cursor.close()
    return """yay! deletion completed successfully
    <p>to view entries press <a href="/people">here</a>
        """


