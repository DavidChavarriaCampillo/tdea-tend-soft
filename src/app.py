from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

conexion = MySQL(app)

#Funcion listar cursos

@app.route('/cursos') #Ruta de la funcion
def listar_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo,nombre,creditos FROM cursos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {'codigo':fila[0],'nombre':fila[1],'creditos':fila[2]}
            cursos.append(curso)
        return jsonify({'cursos':cursos,'mensaje':'Estos son los cursos listados.'})
    except Exception as er:
        return jsonify({'mensaje':'Error al listar.'})