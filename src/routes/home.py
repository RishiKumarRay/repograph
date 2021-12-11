from flask import render_template

class Home:

    def __init__(self):
        pass
        
    def templateGenerator(self):
        template:str = render_template("index.html")
        return template