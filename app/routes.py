from app import app
from flask import request

users = ['nolan', 'annie']
from funcs import login
@app.route('/')
def helloFunction():
    return 'Hello'

@app.route('/create/<user>')
def createUser(user):
    users.append(user)
    return 'User added'
@app.route('/login/<user>', methods=['GET','POST'])
def loginPage(user):
    return login(user, users)
