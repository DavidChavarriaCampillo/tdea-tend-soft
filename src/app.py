from flask import Flask, jsonify, render_template, request, redirect
from flask_mysqldb import MySQL
from config import obtener_conexion
import Controlador

app = Flask(__name__)

conexion = MySQL(app)

#Funcion listar cursos

#Ruta principal carga el template Login
@app.route('/')
@app.route('/Login')
def Login():
    return render_template("Login.html")

#Ruta Home Recoge los datos puestos por el usuario en el inicio de sección
#llama a la base de datos y trae los usuarios y contraseñas guardándolos en un arreglo
#recorre el arreglo y compara cada usuario y contraseña de la base de datos con los datos escritos por el usuario
#en el inicio de sección, si los datos escritos por el usuario coinciden con los de la base de datos
# renderizara el témplate Home y mandara el nombre del usuario y una condición para mostrar el nadvar
#de lo contrario redireccionara a login
@app.route('/Home', methods = ["POST"])
def loguear():
    usuario = request.form["username"]
    contraceña = request.form["password"]
    usuarios = Controlador.logear()
    condi = False
    for usu in usuarios:
        if usu[0] == usuario and usu[1] == contraceña:
            usuari = usu[0]
            condi = True
    if condi :
        return render_template("Home.html", usuari = usuari, cond = True)
    else:
        return redirect("/Login")

#renderiza el témplate Registro y manda condición para que no se muestre el nadvar pero si se cargue el framework bootstrap
@app.route("/registro")
def registro():
    return render_template("Registro.html", cond = False)

#Recoje los datos ingresados por el usuario mediante método post valida con un condicional si las contraseñas son iguales
#en caso de ser iguales llama a la base de datos le manda los datos ingresados por el usuario ingresa los datos
#a la base de datos y redirecciona al login si no son iguales recarga el témplate registro y manda una variable
# para habilitar un mensaje
@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = request.form["nombre"]
    correo = request.form["email"]
    usuario = request.form["username"]
    password = request.form["password"]
    confirm = request.form["confirm"]
    if password == confirm:
        Controlador.registrar(nombre, correo, usuario, password, confirm)
        return redirect("/Login")
    else:
        return render_template("Registro.html", mensaje = True)

#cierra seccion y redirecciona al login
@app.route('/logout')
def Logout():
    return redirect("/Login")

# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)