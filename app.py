from flask import Flask
app = Flask(__name__)
import haslib

@app.route("/")
def hello():
    #print (hashlib.algorithms_available)
    return "Hello, World!!!"
   
