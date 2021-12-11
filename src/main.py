from flask import Flask, request, render_template
import os, subprocess

from flask.wrappers import Response

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
    graphArrayNewLine:str = []
    graphArrayNewLine = graph.splitlines()
    template:str = render_template("data.html", graphArrayNewLines = graphArrayNewLine)
    return template

def getGraphFromUrl(url:str): 
    repoName:str = url.split('/')[4].split('.')[0]
    os.chdir('./support')
    os.remove('dumbFile.txt')
    os.system('git clone ' + url)
    os.chdir('./' + repoName)
    response:str = subprocess.getoutput('git log --graph --all')
    os.chdir('../')
    os.system('rm -rf ' + repoName)
    os.system('touch dumbFile.txt')
    return response

########## end ##########

app.run()