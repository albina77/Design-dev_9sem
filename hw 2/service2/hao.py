import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_hello_world():
    response = requests.get("http://service-one:8080/")
    if response.status_code == 200:
        return response.text + "Hao!"
    else:
        return "Error getting response from Hello service"

if __name__ == '__main__':
    app.run(port=8081, host='0.0.0.0')