from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from pymysql import NULL


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
    rollno = request.form['rollno']
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    cursor = mysql.connection.cursor()
    cursor.execute(""" INSERT INTO Info (rollno, Name, Number, Email) VALUES (%s,%s,%s ,%s) """, (rollno, name, number, email))
    mysql.connection.commit()
    cursor.close()
    return """yay! User added successfully
    <p>to view entries press <a href="/people">here</a>
        """


#deleting
@app.route("/delete", methods = ['post'])
def delete():
    rollno = request.form['deleteroll']
    cursor = mysql.connection.cursor()
    cursor.execute("""Delete from Info where rollno=%s;""",(rollno,))
    mysql.connection.commit()
    cursor.close()
    return """yay! deletion completed successfully
    <p>to view entries press <a href="/people">here</a>
        """


@app.route("/update", methods = ['post'])
def update():
    rollno = request.form['rollno']
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    if name != '' :
        cursor = mysql.connection.cursor()
        cursor.execute("""update Info set name = %s where rollno = %s;""", (name,rollno))
        mysql.connection.commit()
        cursor.close()
    if email != '':
        cursor = mysql.connection.cursor()
        cursor.execute("""update Info set email = %s where rollno = %s;""", (email,rollno))
        mysql.connection.commit()
        cursor.close()
    if number != '':
        cursor = mysql.connection.cursor()
        cursor.execute("""update Info set number = %s where rollno = %s;""", (number,rollno))
        mysql.connection.commit()
        cursor.close()
       
    
    
    return """ yay! update completed successfully
    <p>to view entries press <a href="/people">here</a> """