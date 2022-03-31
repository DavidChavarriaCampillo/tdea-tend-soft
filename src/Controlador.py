from config import obtener_conexion

def registrar(nombre, correo, usuario, password, confirm):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(nombre,correo,usuario,contraceña,confirm) VALUES (%s,%s,%s,%s,%s)",(nombre,correo,usuario,password,confirm))
    conexion.commit()
    conexion.close()