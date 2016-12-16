from flask import render_template, flash, redirect, send_from_directory
from app import app

#Index
@app.route("/")
@app.route("/index")
def index():
    return render_template("pages/index.html")

@app.route("/buscar/recurso")
def buscar_recurso():
    return render_template("recursos/index.html")

@app.route("/buscar/usuario")
def buscar_usuario():
    return render_template("usuarios/index.html")

@app.route("/css/<path>")
def serve_stylesheet(path):
    return send_from_directory("./css",path)

@app.route("/js/<path>")
def serve_script(path):
    return send_from_directory("./js",path)