from flask import render_template
import os, subprocess

class Data:

    def __init__(self, url) -> None:
        self.url:str = url

    def templateGenerator(self) -> str:
        graph:str = self.__getGraphFromUrl()
        graphArrayNewLine:list[str] = graph.splitlines()
        jsonResponse:dict = self.__getJsonResponseFromGraph(graphArrayNewLine)
        template:str = render_template("data.html", jsonResponse = jsonResponse.values())
        return template

    def __getGraphFromUrl(self) -> str: 
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
    
    def __getJsonResponseFromGraph(self, lines:list[str]) -> dict:
        separetedChunks:list[str] = []
        for line in lines:
            if 'commit' in line:
                separetedChunks.append('\n')
            separetedChunks.append(line)
        separetedChunks.pop(0)
        commits:list[str] = []
        support:str = ''
        for chunk in separetedChunks:
            if '\n' !=  chunk:
                support += chunk
            else:
                commits.append(support.replace('\\', '').replace('/', '').replace('|', '').replace('*', ''))
                support = ''
        json:dict = {}
        for i in range(len(commits)):
            json[i] = commits[i]
        return json