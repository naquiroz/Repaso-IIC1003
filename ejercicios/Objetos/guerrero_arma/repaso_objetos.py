"""Pequeño repaso de objetos para la I2 de introducción a la programación."""

__author__ = 'Daniel Leal'
__version__ = '1.0'

# Primero definimos al guerrero


class Warrior:

    """
    El guerrero 'nace' con un nombre, una estatura, un peso y una cantidad
    de fuerza, por lo que esas variables deben ir como argumentos del
    constructor de clase.
    """

    # Constructor de clase
    # Como las variables son mudas, las nombraré con nombres aleatorios
    # Lo importante aquí es el nombre con que queden definidos en la instancia
    # Orden: nombre, estatura, peso, fuerza
    def __init__(self, platano, corchete, elefante, australopitecus):
        self.name = platano
        self.height = float(corchete)  # Podría estar dada como 1.8 metros
        self.weight = int(elefante)  # El peso siemrpe será un entero
        self.strength = int(australopitecus)  # La fuerza siemrpe será entera
        # Una vez definido esto, nuestro guerrero puede ser instanciado. Sin
        # embargo, no tiene un espacio para su arma! Hay que ponerle un espacio
        # vacío para ponerle después una arma
        self.weapon = None  # Aquí irá su arma cuando se la equipe

    # El guerrero tiene que poder entrenar. Con cada entrenamiento, gana 2
    # puntos de fuerza. Para hacerlo, basta con lo siguiente

    def train(self):
        """Le agrega dos puntos a la fuerza."""
        self.strength += 2
        print('{} ha entrenado exitosamente!'.format(self.name))

    # El guerrero también debe ser capaz de equipar su arma! Para esto,
    # podemos definir un método que la añada e imprima un mensaje
    # Nuevamente, las variables son mudas, así que el nombre que usemos para
    # referirnos al arma equipada es irrelevante

    def equip(self, zapallo):
        """Equipa un arma e imprime un estatus de las armas equipadas."""
        if self.weapon is None:  # Solo si no había un arma antes equipada
            self.weapon = zapallo
            print('Se ha equipado el arma {}!'.format(zapallo.name))
            # En esta linea, se asume que el arma tiene un atributo 'name'
        else:
            # Primero decimos el arma a des-equipar
            print('Se ha des-equipado el arma {}!'.format(self.weapon.name))
            # En esta linea, se asume que el arma tiene un atributo 'name'
            self.weapon = zapallo
            print('Se ha equipado el arma {}!'.format(zapallo.name))
            # En esta linea, se asume que el arma tiene un atributo 'name'

    # Ya estamos casi con el guerrero! Tenemos que poder golpear con la arma
    # equipada, por lo que solamente nos falta ese método para el guerrero!

    def smash(self):
        """
        Imprime en pantalla el daño hecho por el guerrero. Le quita durabilidad
        al arma.
        """
        if self.weapon is not None:
            damage = self.strength + self.weapon.bonus_strength
            # El daño es equivalente a la fuerza del guerrero más la fuerza
            # extra añadida por el arma! Recordar que self.weapon es UN OBJETO,
            # por lo que tiene atributos y métodos
            print('El golpe ha hecho {} puntos de daño!'.format(damage))
            # Además hay que quitarle durabilidad al arma!
            durability_lost = int(0.1 * self.strength)
            self.weapon.lose_durability(durability_lost)  # El arma se gasta
            # Si la durabilidad llega a 0, el arma se deshace en el vacío!!
            if self.weapon.durability <= 0:
                self.weapon = None  # Le sacamos el arma al guerrero
        else:
            damage = 0
            print('El guerrero nórdico no tiene un arma para golpear!')
        return damage  # Solo por si acaso, retornamos el daño causado

# Con esto ya tenemos a nuestro guerrero listo!
# Ahora solo falta crear el arma!


class Weapon:  # pylint: disable=too-few-public-methods

    """
    El arma 'nace' con un nombre, una cantidad de fuerza bonus y una
    durabilidad, por lo que esas variables deben ir como argumentos del
    constructor de clase.
    """

    # Constructor de clase
    # Como las variables son mudas, las nombraré con nombres aleatorios
    # Lo importante aquí es el nombre con que queden definidos en la instancia
    # Orden: nombre, fuerza_bonus, durabilidad
    def __init__(self, eucarionte, jirafa, dijkstra):
        self.name = eucarionte
        self.bonus_strength = int(jirafa)  # La fuerza bonus siempre es entera
        self.durability = int(dijkstra)  # La durabilidad siempre es entera

    # Anteriormente llamamos un método que le quitaba durabilidad al arma,
    # por lo que hay que crearlo!

    # Como las variables son mudas, puedo poner el nombre que quiera

    def lose_durability(self, julijuimus):  # julijuimus = durab. perdida
        """Le quita durabilidad al arma e imprime el estado de ésta."""
        self.durability -= julijuimus
        # Se le quita la durabilidad al arma
        if self.durability > 0:  # Si aún le queda durabilidad, se expresa
            print('{} ha perdido {} de durabilidad, quedando en {}'.
                  format(self.name, julijuimus, self.durability))
        else:
            # Si la durabilidad se pasa para abajo de 0, entonces se setea
            # en cero y se expresa el fin de la durabilidad
            self.durability = 0
            print('{} ha perdido {} de durabilidad y se ha desvanecido!!'.
                  format(self.name, julijuimus))

# Como pueden ver, ya terminamos nuestro modelamiento. Ahora falta probar un
# poco nuestro juego


if __name__ == '__main__':
    # Orden de argumentos: nombre, estatura, peso, fuerza
    SOMEONE = Warrior('Thor', 1.93, 90, 30)
    # Supongamos que olvidamos su fuerza y la queremos ver
    print('La fuerza de {} es: {}'.format(SOMEONE.name, SOMEONE.strength))
    # Ahora Thor se fue a entrenar!
    SOMEONE.train()  # Ésto va a imprimir un status
    # Ahora queremos ver de nuevo su fuerza! Debería haber aumentado en 2...
    print('La fuerza de {} es: {}'.format(SOMEONE.name, SOMEONE.strength))
    # Evectivamente!
    # En este momento, Thor decide equiparse su martillo. Para esto,
    # debemos primero crear el martillo
    # Orden de argumentos: nombre, fuerza_bonus, durabilidad
    HAMMER = Weapon('Mighty-Hammer', 10, 5)
    # Ahora si podemos equiparle el arma
    print('\nAhora se equipará un arma:')
    SOMEONE.equip(HAMMER)  # Ésto va a imprimir un status
    # Thor se enojó mucho porque no terminaste tu tarea 1 de Introducción
    # a la Programación! Por la ira que lo llena, golpea violentamente
    # un árbol!
    print('\nGolpe de ira por tu tarea 1 incompleta:')
    SOMEONE.smash()  # Ésto entregará un status
    # Al enterarse de que no terminaste tu tarea 2 tampoco, Thor te golpea
    # en la cara!
    print('\nGolpe de ira por tu tarea 2 incompleta:')
    SOMEONE.smash()  # Al martillo se le acabará la durabilidad!
    # Como su martillo se esfumó, Thor se enfurece y trata de golpear algo,
    # pero es completamente incapaz
    print('\nGolpe de ira por la destrucción del martillo (no funcionará):')
    SOMEONE.smash()
