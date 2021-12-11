from re import template
from flask import Flask, request, render_template
import os
import subprocess

app:Flask = Flask(__name__, template_folder = '../templates')

########## / ##########
@app.route('/', methods=['get'])
def home():
    template:str = render_template("index.html")
    return template
########## end ##########

########## /data ##########
@app.route('/data', methods=['get'])
def data():
    url:str = request.args['url']
    graph:str = getGraphFromUrl(url)
    template:str = render_template("data.html", graph = graph)
    return template

def getGraphFromUrl(url:str): #'https://github.com/matiassingers/awesome-readme.git'
    repoName:str = url.split('/')[4].split('.')[0]
    os.chdir('./support')
    os.system('git clone ' + url)
    os.chdir('./' + repoName)
    response:str = subprocess.getoutput('git log --graph --all')
    os.chdir('../')
    os.system('rm -rf ' + repoName)
    return response
########## end ##########

app.run()