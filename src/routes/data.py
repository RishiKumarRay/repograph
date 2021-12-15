from flask import render_template
import os, subprocess, re

class Data:

    def __init__(self, url) -> None:
        self.url:str = url

    def templateGenerator(self) -> str:
        response:str = self.__getGraphFromUrl()
        #jsonResponse:dict = self.__getDictionaryFromString(response)
        template:str = render_template('data.html', response = response)
        return template

    def __getGraphFromUrl(self) -> str:
        repoName:str = self.url.split('/')[4].split('.')[0]
        os.chdir('./support')
        os.remove('dumbFile.txt')
        os.system('git clone ' + self.url)
        os.chdir('./' + repoName)
        command:str = "git log --pretty=format:'%n{%n%d%n  'CommitHash': '%H',%n  'Author': '%an',%n  'AuthorEmail': '%ae',%n  'Date': '%ad',%n  'Message': '%f'%n}'"
        response:str = subprocess.getoutput(command)
        os.chdir('../')
        os.system('rm -rf ' + repoName)
        os.system('touch dumbFile.txt')
        return response
    
    def __getDictionaryFromString(self, stringResponse:str) -> dict:
        #TO DO
        pass