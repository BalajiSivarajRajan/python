from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!"
    hs = hashlib.sha256(get_some_string().encode('utf-8')).hexdigest()
    return hs
