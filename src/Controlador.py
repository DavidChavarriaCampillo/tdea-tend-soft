from config import obtener_conexion

def registrar(nombre, correo, usuario, password, confirm):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(nombre,correo,usuario,contraceña,confirm) VALUES (%s,%s,%s,%s,%s)",(nombre,correo,usuario,password,confirm))
    conexion.commit()
    conexion.close()

def logear():
    conexion = obtener_conexion()
    usuarios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT usuario, contraceña FROM usuario")
        usuarios = cursor.fetchall()
    conexion.close()
    return usuarios