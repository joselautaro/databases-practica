import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="computadoras"
)

# print(conn)

# Con este comando empiezo a generar la base de datos
cursor = conn.cursor()

# Creamos tablas
# sql = """CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, nombres VARCHAR(255), direccion VARCHAR(255))"""
# cursor.execute(sql)
# conn.commit()
# sql = """CREATE TABLE empleados (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), puesto VARCHAR (100))"""

# Ingresamos datos
# sql = """INSERT INTO empleados (nombres, direccion) VALUES (%s, %s)"""

#Incorporo tres filas mas en la tabla clientes
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra1")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra10")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra5")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra77")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra14")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra414")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra1410")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra87417")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Estela", "Alexandra45471")"""
# sql = """INSERT INTO clientes (nombres, direccion) VALUE ("Micaela", "Rio de Janeiro")"""
#Incorporo tres filas mas en la tabla clientes
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "German", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Macarena", "Dueña")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Germangtg", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Germantgtg", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Germantgtg", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Germanfvfv", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Germanyhyhyh", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Germanhnhnhn", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Germanqqaqaq", "Gerente")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Macarena", "Dueña")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Macarena", "Dueña")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Macarena", "Dueña")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Macarena", "Dueña")"""
# sql = """INSERT INTO empleados (id, nombre, puesto) VALUE ("", "Macarena", "Dueña")"""
# valores = [
#     ("", "Miguel Zamora", "Cuidad de México"),
#     ("", "Macarena Rodriguez", "Buenos aires"),
#     ("", "Lautaro Montaña", "Buenos Aires"),
#     ("", "Lucia", "Pacchiano"),
#     ("", "Jorge", "Rodriguez"),
#     ("", "Jorge", "Rodriguez"),
#     ("", "Jorge", "Rodriguez"),
#     ("", "Jorge", "Rodriguez"),
# ]
# cursor.executemany(sql, valores)
# conn.commit()

# sql = """INSERT INTO clientes id AUTO_INCREMENT"""

#Seleccionamos datos y buscamos por clientes en su totalidad de los datos
# sql = """SELECT * FROM clientes"""

#Seleccionamos y filtramos por nombres puede ser de las dos maneras a continuacion, *el LIKE es decir parecido*, *tambien filtramos por palabras en la direccion que contengan la letra n y tambien la letra n al final*
# sql = """SELECT * FROM clientes WHERE nombres LIKE "Miguel%" """
# sql = """SELECT * FROM clientes WHERE nombres = "Miguel Zamora" """
# sql = """SELECT * FROM clientes WHERE direccion LIKE "%n%" """
# sql = """SELECT * FROM clientes WHERE direccion LIKE "%n" """
# sql = """SELECT * FROM clientes WHERE direccion LIKE "" """

#Maneras de ordenar
#Por nombres
# sql = """SELECT * FROM clientes ORDER BY nombres"""
#Por direccion
# sql = """SELECT * FROM clientes ORDER BY direccion"""
#Por id
# sql = """SELECT id, direccion FROM clientes ORDER BY direccion"""
#De manera descendiente // selecciona el nombre y la direccion de la tabla clientes ordenada de manera descendiente
# sql = """SELECT nombres, direccion FROM clientes ORDER BY nombres DESC"""
#De manera ascendente
# sql = """SELECT nombres, direccion FROM clientes ORDER BY nombres ASC"""

#como borrar datos
#eliminamos borrar de clientes donde la direccion sea igual a cuidad
# sql = """DELETE FROM clientes WHERE nombres = "Miguel Zamora" """
# cursor.execute(sql)
# conn.commit()
#Buscamos los nombres clientes con nombres que tengan letra a
# sql = """SELECT * FROM clientes WHERE nombres = "%a%" """


#como actualizar datos de una base de datos
#CRUD = CREATE READ UPDATE DELETE
#crear, leer, actualizar y borrar
#Actualizar la tabla clientes en la direccion va a ser "México" y la direccion antigua es "Rio de Janeiro" en este caso le estamos cambiando el nombre a todas las personas que viven en mexico
# sql = """UPDATE clientes SET nombres = "Tamara" WHERE direccion = "Mexico" """

#En este caso, cambiamos el lugar se recidencia, ubicando a la tabla por id en este caso el 2
# sql = """UPDATE empleados SET puesto = "sub dueña" WHERE id = 2"""
# cursor.execute(sql)
# conn.commit()


#Buscamos por nombre de los clientes
# sql = """SELECT nombres FROM clientes"""
# cursor.execute(sql)
#forma mas correcta de hacer es con fetchall y con fetchone traemos todos los datos de una tabla


#como limitar busquedas internas
# sql = """SELECT * FROM empleados LIMIT 7"""
#Que pasa si quiero que me traiga los dos registros a partir del campo numero 3
# sql = """SELECT * FROM empleados LIMIT 10 OFFSET 3"""
# cursor.execute(sql)
# conn.commit()
# clientes = cursor.fetchall()




#Como borrar tablas
# sql = """DROP TABLES clientes"""
sql = """SHOW TABLES"""
cursor.execute(sql)
# conn.commit()
empleados = cursor.fetchall()


#Declaro una lista de tuplas
# valores = [
#     ("Miguel Zamora", "Cuidad de México"),
#     ("Macarena Rodriguez", "Buenos aires"),
#     ("Lautaro Montaña", "Buenos Aires"),
# ]

# Pasamos valores de identificacion de los ultimos clientes iterando por medio de parámetros
# cursor.executemany(sql, valores)

#Cometemos los ingresos
# conn.commit()


#Imprimimos por id de lo ingresado
# print("se insertó el ID: ", cursor.lastrowid)

#Cerramos la base
# conn.close()

#Imprimo la cuenta del ultimo registro
# print(cursor.rowcount, "registro insertado")

# imprimir la cantidad de ultimos registros insertados
# print(cursor.rowcount, "registros insertados")

# mostrar las tablas
# cursor.execute("SHOW TABLES")


# Este comando ya no se usa porque ya está creada la base de datos arriba
# cursor.execute("CREATE DATABASE computadoras")


# con este comando genero la ejecucion y veo la base de datos
# cursor.execute("SHOW DATABASES")

# Recorro e imprimo las bases de datos que tengo
for empleado in empleados:
    print(empleados)

# cierro la base de datos
conn.close()
