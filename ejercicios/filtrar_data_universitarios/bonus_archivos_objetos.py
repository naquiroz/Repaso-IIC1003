"""Pequeño extra de archivos-objetosrepaso I2 de intro a la progra."""

__author__ = 'Daniel Leal'
__version__ = '1.0'

# Básicamente, en vez de leer el archivo en una lista de listas, lo leeremos
# en una lista de objetos

# Primero definimos un estudiante


class Student:  # pylint: disable=too-few-public-methods

    """Modela un estudiante."""

    # pylint: disable=R0913
    def __init__(self, name, last_name, age, career, university):
        self.name = name
        self.last_name = last_name
        self.age = int(age)
        self.career = career
        self.university = university

    def __str__(self):  # Al hacer str(Student) se retornará 'nombre apellido'
        return '{} {}'.format(self.name, self.last_name)


if __name__ == '__main__':
    # Ahora abrimos el archivo
    with open('archivo.csv', 'r') as file:  # Abrir archivo en modo de lectura
        DATA = file.readlines()  # Guardar las lineas en una lista

    DATA.pop(0)  # Eliminamos los 'Headers'

    for i, line in enumerate(DATA):
        DATA[i] = line.replace('\n', '')  # Sacar el \n de cada linea
        DATA[i] = DATA[i].split(',')  # Separar los datos
        # Recuperar información de la sub lista
        NAME = DATA[i][0]
        LAST_NAME = DATA[i][1]
        AGE = DATA[i][2]
        CAREER = DATA[i][3]
        UNIV = DATA[i][4]
        # Crear estudiante con información recuperada
        STUDENT = Student(NAME, LAST_NAME, AGE, CAREER, UNIV)
        # Reemplazar sub lista por objeto Estudiante
        DATA[i] = STUDENT
    # Ahora tengo una lista con objetos tipo estudiante. Para filtrarla
    # la idea es la misma de antes
    NEW_LIST = []
    for student in DATA:
        if student.career == 'ingeniería' or student.university == 'USACH':
            NEW_LIST.append(student)
    # Ahora tenemos la lista con los objetos útiles
    # Pero queremos solo los nombres y apellidos. Podemos usar el método
    # __str__ que definimos!!
    for i, student in enumerate(NEW_LIST):
        NEW_LIST[i] = str(student)  # Esto retorna 'nombre apellido'!!!
    # Ahora tenemos una lista con strings, donde cada string es un nombre y
    # un apellido separados por un espacio
    # Podemos usar join para estar casi listos!
    FINAL_STRING = '\n'.join(NEW_LIST)
    # Podemos ver que el string es lo que necesitamos!
    print('\n\nString final:\n')
    print(FINAL_STRING)
    # Ahora solo falta crear el archivo (crearemos un archivo con otro nombre)
    with open('alternate_filtered_data.txt', 'w') as new:
        new.write(FINAL_STRING)
