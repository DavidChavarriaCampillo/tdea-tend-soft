from re import template
from flask import Flask, jsonify, render_template, request, redirect
from flask_mysqldb import MySQL
from config import obtener_conexion
import Controlador

app = Flask(__name__)

conexion = MySQL(app)

mensaje = False
logueado = False

#Funcion listar cursos

if logueado:
    @app.route('/')
    @app.route('/Home') #Ruta de la funcion
    def Home():
        return render_template("Home.html")

if logueado == False:
    @app.route('/')
    @app.route('/Login')
    def Login():
        return render_template("Login.html", logueado = False)

@app.route('/Home', methods = ["POST"])
def loguear():
    usuario = request.form["username"]
    contraceña = request.form["password"]
    usuarios = Controlador.logear()
    cond = False
    usuari = ""
    for usu in usuarios:
        if usu[0] == usuario and usu[1] == contraceña:
            usuari = usu[0]
            condi = True
    if condi :
        render_template("Login.html", logueado = True)
        return render_template("Home.html", usuari = usuari, cond = True)
    else:
        return redirect("/Login")

@app.route("/registro")
def registro():
    return render_template("Registro.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["nombre"]
    correo = request.form["email"]
    usuario = request.form["username"]
    password = request.form["password"]
    confirm = request.form["confirm"]
    if password == confirm:
        mesaje = False
        Controlador.registrar(nombre, correo, usuario, password, confirm)
        # De cualquier modo, y si todo fue bien, redireccionar
        return redirect("/Login")
    else:
        return render_template("Registro.html", mensaje = True)

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)