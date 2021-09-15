from flask import Flask
import hashlib

app = Flask(__name__)

@app.route('/hello/<sname>')
def hello(sname):
    #return "Hello, here " + str(sname)
    return "hello, " + hashlib.sha256(sname.encode('utf-8')).hexdigest()
   
