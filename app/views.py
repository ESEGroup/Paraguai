from flask import render_template, flash, redirect, send_from_directory
from app import app

#Index
@app.route("/")
@app.route("/index")
def index():
    return render_template("pages/index.html")

# UC01 Buscar Recurso
@app.route("/buscar/recurso")
def buscar_recurso():
    return render_template("recursos/index.html")
    
@app.route("/detalhar/recurso")
def detalhar_recurso():
    return render_template("recursos/detalhes.html")

@app.route("/criar/recurso")
def criar_recurso():
    return render_template("recursos/form.html")

@app.route("/buscar/usuario")
def buscar_usuario():
    return render_template("usuarios/index.html")
    
@app.route("/detalhar/usuario")
def detalhar_usuario():
    return render_template("usuarios/detalhes.html") 
    
@app.route("/criar/usuario")
def criar_usuario():
    return render_template("usuarios/form.html")

@app.route("/css/<path>")
def serve_stylesheet(path):
    return send_from_directory("./css",path)

@app.route("/js/<path>")
def serve_script(path):
    return send_from_directory("./js",path)