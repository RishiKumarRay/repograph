from flask import Flask, request
from routes.data import Data
from routes.home import Home

app:Flask = Flask(__name__, template_folder = '../templates')

@app.route('/', methods=['get'])
def home():
    home:Home = Home()
    return home.templateGenerator()

@app.route('/data', methods=['get'])
def data():
    data:Data = Data(url = request.args['url'])
    return data.templateGenerator()

app.run()