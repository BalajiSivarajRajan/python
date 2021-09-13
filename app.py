from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    import haslib
    #print (hashlib.algorithms_available)
    return "Hello, World!!!"
   
