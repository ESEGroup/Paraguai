from flask import Flask
App = Flask(__name__)

@App.route("/")
def hello():
    return "Sistema de Agendamento"
