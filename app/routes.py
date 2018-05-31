from app import app
from flask import jsonify

@app.route('/')
@app.route('/index')


def index():
    return jsonify({'message': 'maintenance tracker endpoints!'});
    

@app.route('/login')

def login():
    pass


@app.route('/signup')

def signup():
    pass

@app.route('/logout')

def logout():
    pass

@app.route('/getrequests')

def getrequests():
    pass
@app.route('/getrequest')

def getrequest():
    pass
@app.route('/editrequest')

def editrequest():
    pass

@app.route('/deleterequest')

def deleterequest():
    pass

@app.route('/modifyrequest')

def modifyrequest():
    pass
@app.route('/createrequest')

def createrequest():
    pass

