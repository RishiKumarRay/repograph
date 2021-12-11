from flask import render_template
import os, subprocess

class Data:

    def __init__(self, url):
        self.url:str = url

    def templateGenerator(self):
        graph:str = self.__getGraphFromUrl()
        graphArrayNewLine:str = []
        graphArrayNewLine = graph.splitlines()
        template:str = render_template("data.html", graphArrayNewLines = graphArrayNewLine)
        return template

    def __getGraphFromUrl(self): 
        repoName:str = self.url.split('/')[4].split('.')[0]
        os.chdir('./support')
        os.remove('dumbFile.txt')
        os.system('git clone ' + self.url)
        os.chdir('./' + repoName)
        response:str = subprocess.getoutput('git log --graph --all')
        os.chdir('../')
        os.system('rm -rf ' + repoName)
        os.system('touch dumbFile.txt')
        return response
            