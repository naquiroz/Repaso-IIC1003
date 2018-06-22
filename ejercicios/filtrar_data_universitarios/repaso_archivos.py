"""Pequeño repaso de archivos para la I2 de introducción a la programación."""

__author__ = 'Daniel Leal'
__version__ = '1.0'

with open('archivo.csv', 'r') as file:  # Abrir archivo en modo 'r' (lectura)
    DATA = file.readlines()  # Guardar las lineas en una lista

# TAMBIÉN SE PUEDE USAR LO SIGUIENTE:

# file = open('archivo.csv', 'r')
# DATA = file.readlines()
# file.close()

# Ahora hay dejar la lista en un formato que nos sirva
for i, line in enumerate(DATA):
    # A cada elemento de DATA (a cada linea) se le aplica lo siguiente
    DATA[i] = line.replace('\n', '')  # Sacar el \n de cada linea
    DATA[i] = DATA[i].split(',')  # Separar el string en una lista de cosas
    # Luego de este último paso, queda una lista con listas de datos
    # Cada elemento de la lista grande corresponde a una lista que contiene
    # la información de una linea del archivo
    # Cada sublista tiene nombre como elemento 0, apellido como elemento 1,
    # edad como elemento 2, carrera como elemento 3 y universidad
    # como elemento 4

# FIJARSE que este archivo tenía "headers" (una linea indicando qué info
# contendría cada espacio separado por comas)

print('\nLista sin eliminar "Headers":\n')
for elem in DATA:
    print(elem)

# Podemos querer deshacernos de estos "headers". Por suerte, solamente son
# un elemento de la lista grande, así que es simple eliminarlo para quedar
# con una lista tal como la queremos de la siguiente manera

DATA.pop(0)

print('\n\nLista con "Headers" eliminados:\n')
for elem in DATA:
    print(elem)

# NO OLVIDAR que ahora tenemos una lista con las listas previamente mostradas

# Ahora queremos crear un archivo que contenga solamente el nombre y apellido
# de los estudiantes de ingeniería o de la USACH (independiente de la carrera),
# el nombre separado del apellido por un espacio y cada nombre en una línea
# nueva. Notar que se pide crear un archivo nuevo, no modificar el existente.
# Ponerle de nombre "filtered_data.txt"

# Lo primero que hay que hacer es crear una lista que solamente tenga a los
# estudiantes que cumplan con los requisitos previamente estipulados,
# Para esto, poodemos crear un lista vacía e irle agregando los elementos
# útiles para el ejercicio

NEW_LIST = []
for student in DATA:
    # Para cada estudiante, revisamos si su elemento 3 (carrera) es la deseada
    # o si su elemento 4 (universidad) es el deseado
    if student[3] == 'ingeniería' or student[4] == 'USACH':
        NEW_LIST.append(student)

# Como podemos ver, NEW_LIST ahora tiene todos los estudiantes que queríamos

print('\n\nLos estudiantes seleccionados son los siguientes:\n')
for stud in NEW_LIST:
    print(stud)

# Ahora solo queda añadirlos al archivo pedido. Para esto, lo más fácil parece
# ser crear un string largo y agregar ese string al archivo. No hay que
# olvidarse de agregarle los saltos de linea!!

FINAL_STRING = ''

# Le iremos agregando los nombres al string uno por uno

for student in NEW_LIST:
    FINAL_STRING += student[0]  # Agregar el nombre
    FINAL_STRING += ' '  # Agregar el espacio entre el nombre y el apellido
    FINAL_STRING += student[1]  # Agregar el apellido
    FINAL_STRING += '\n'  # IMPORTANTE: AGREGAR EL SALTO DE LINEA!!!
FINAL_STRING = FINAL_STRING[:-1]  # Podemos eliminar el último salto de linea

# Chequeamos que el string final es lo que queremos agregar al archivo

print('\n\nString final:\n')
print(FINAL_STRING)

# HAY UNA FORMA MUCHO MÁS ELEGANTE DE HACER ESTO!
# Quizás les puede servir saber hacerlo

# Primero, queremos tener una lista con los estudiantes útiles, donde cada
# elemento sea una lista que contenga solamente el nombre y el apellido

for i in range(len(NEW_LIST)):
    NEW_LIST[i].pop(-1)  # Sacamos la universidad
    NEW_LIST[i].pop(-1)  # Sacamos la carrera
    NEW_LIST[i].pop(-1)  # Sacamos la la edad
    # Solamente queda el nombre y el apellido!
    # Ahora podemos usar el comando join para transformar esta sub lista en
    # un string
    NEW_LIST[i] = ' '.join(NEW_LIST[i])

# Ahora tenemos una lista de strings donde los nombres y apellidos están
# separados por un espacio. Ahora solamente falta agregar los saltos de linea!

ALTERNATIVE_FINAL_STRING = '\n'.join(NEW_LIST)

# Chequeamos si nos sirve

print('\n\nString final alternativo:\n')
print(ALTERNATIVE_FINAL_STRING)

# Incluso podemos comparar directamente

if FINAL_STRING == ALTERNATIVE_FINAL_STRING:
    print('\n\nLos strings son perfectamente iguales!')
else:
    print('Mal ahí, los strings son distintos')

# Ahora solo nos queda agregar este string al archivo deseado. Como los dos
# son iguales, da lo mismo cual se le agregue

# Abrimos el archivo nuevo en modo 'w' (de escritura)
with open('filtered_data.txt', 'w') as new:
    new.write(ALTERNATIVE_FINAL_STRING)
    # Con esto le escribimos el string al archivo

# TAMBIÉN SE PUEDE USAR LO SIGUIENTE:

# new = open('filtered_data.txt', 'w')
# new.write(ALTERNATIVE_FINAL_STRING)
# new.close()"""
