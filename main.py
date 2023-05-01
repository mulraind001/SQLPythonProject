from http.server import BaseHTTPRequestHandler, HTTPServer
import mysql.connector
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

mydb = mysql.connector.connect(
    # use the information that you used to set up your mysql.
    host='localhost',
    user='DBuckhana',
    password='@Comp320sql',
    port='3306',
    database='python_sql'
)
#This is a cursor that points to the database
myCursor = mydb.cursor()

#This is make sure the SQL Connection is working. It will show the table in the console
myCursor.execute('SELECT * FROM users')
#Fetch all from the table users.
users = myCursor.fetchall()
#Print out the table.
for user in users:
    print(user)

@app.route('/')
def homepage():
    return render_template("login.html")

@app.route('/login', methods = ['POST','GET'])
def login():
    #Check if account exists using MySQL
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        #Comment out the following code that you do not want to test. Be sure comment one or the other, not both.
        #Bad example with no input validation.  Here we pass the user's input raw.
        #myCursor.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")

        # Correct way using parameters.  Here we sanitize the user's input.
        myCursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))

        #Fetch one record and return result
        account = myCursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Redirect to home page
            return render_template('home.html', name=username)
        else:
            # Account doesn't exist or username/password incorrect
            return render_template('login.html', info='Incorrect Credentials')
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run()
