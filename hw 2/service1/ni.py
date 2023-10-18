import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def ni_hao():
    return "Ni "

if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')

