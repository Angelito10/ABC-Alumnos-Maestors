import sys
sys.path.append('..')
from db import get_connection

def comprobarConexion():
    try:
         connection = get_connection()
         connection.commit()
         print('CONEXION EXITOSA')
         connection.close()    
    except Exception as ex:
        print('Fallo la conexion :(')
        print(ex)

def agregar_maestros(nombre,apaterno,amaterno,matricula):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call agregar_maestros(%s,%s,%s,%s)',(nombre,apaterno,amaterno,matricula))
        connection.commit()
        connection.close()    
    except Exception as ex:
        print(ex)

def modificar_maestros(nombre,apaterno,amaterno,id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call actualizar_maestros(%s,%s,%s,%s)',(nombre,apaterno,amaterno,id))

            connection.commit()
            connection.close()
    except Exception as ex:
        print(ex)

def eliminar_maestros(id):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call eliminar_maestos(%s)',(id))
        connection.commit()
        connection.close()
    except Exception as ex:
        print(ex)
        
        
def getAllMaestros():
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('SELECT * FROM maestros')
        maestros = curso.fetchall()
        print(maestros)
        connection.close()
        return maestros
    except Exception as ex:
        print(ex)
        
def getAllMestroById(matricula):
    try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call consultar_maestro(%s)',(matricula))
            maestro = curso.fetchall()
            m = maestro[0]
        connection.close()
        return m
    except Exception as ex:
        print(ex)


comprobarConexion()