from flask import Flask, request
from routes.data import Data
from routes.home import Home

app:Flask = Flask(__name__, template_folder = '../templates')

@app.route('/', methods=['get'])
def home():
    x:Home = Home()
    return x.templateGenerator()

@app.route('/data', methods=['get'])
def data():
    x:Data = Data(url = request.args['url'])
    return x.templateGenerator()

app.run()