from flask import Flask
from flask.ext.hashing import Hashing
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!"
   
