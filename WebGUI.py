__author__ = 'stew'
from flask import Flask
import SensorClass
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test/")
def test():
    return "Hello Test World!"

if __name__ == "__main__":
    app.run()