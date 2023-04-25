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

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM users')

users = mycursor.fetchall()

for user in users:
    print(user)

@app.route('/')
def hello_world():
    return render_template("login.html")
database={'admin': '123'}


@app.route('/login', methods = ['POST','GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1] != pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name1)


if __name__ == '__main__':
    app.run()

#queryResults = mycursor.execute('SELECT * FROM users WHERE username = "' + name1 + '"')
    #
    # if queryResults != 1: print("fail")
    # else: print("pass")



# # Create a custom request handler
# class MyRequestHandler(BaseHTTPRequestHandler):
#
#     # Handle GET requests
#     def do_GET(self):
#         # Send response status code
#         self.send_response(200)
#
#         # Send headers
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#
#         # Send HTML response
#         html = """
#         <!DOCTYPE html>
#         <html>
#         <head>
#             <title>Username and Password Credentials</title>
#         </head>
#         <body>
#             <h1>Username and Password Credentials</h1>
#             <form>
#                 <label for="username">Username:</label>
#                 <input type="text" id="username" name="username" value="Aggies23"><br><br>
#                 <label for="password">Password:</label>
#                 <input type="password" id="password" name="password" value="AggiePride23"><br><br>
#                 <input type="submit" value="Submit">
#             </form>
#         </body>
#         </html>
#         """
#         self.wfile.write(html.encode())
#
#
# # Create the web server and listen on port 8080
# server_address = ('', 8080)
# httpd = HTTPServer(server_address, MyRequestHandler)
# print('Server running at http://localhost:8080')
#
# # Start the server
# httpd.serve_forever()
