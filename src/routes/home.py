from flask import render_template

class Home:

    def __init__(self) -> None:
        pass
        
    def templateGenerator(self) -> str:
        template:str = render_template("index.html")
        return template