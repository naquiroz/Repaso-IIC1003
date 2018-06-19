# Resumen IIC-1103

***Por: Nicolás Quiroz***

----

## Listas

Las listas son una forma de guardar un conjunto de valores python.

*Ejemplo*:

```python
lista_supermercado = ['Huevos', 'Leche', 'Cereal', 'Harina']
```

Lo anterior corresponde a un conjunto de `strings` en una lista de supermercado.

#### ¿ Puedo guardar un *conjunto* de listas?

Si ! Y es bastante facil. Supongamos tienes una generacion de un colegio, con distintos alumnos, por curso:

```python
generacion_2017 = [['Nicolas Quiroz', 'Benil Wakas', 'Jorge Muñoz'],
                   ['Ignacio Sanchez','Claudio Rivera', 'Daniel Vidal'],
                  ['Cristian Ruz', 'Marcos Sepúlveda' , 'Daniel Leal']]
```

Como ven, para guardar listas dentro de listas, solo basta escribirlas separadas por una coma. Una forma que la gente suele ver las listas de listas, es como una matriz donde cada fila es una lista y cada columna es un elemento de cada lista.



***Tip*** : **Las listas pueden guardar muchos tipos de cosas a a la vez!  (strings, listas, ints en una misma lista)**

####¿ Qué puedo hacer con las listas (y, por ende, listas de listas)?

Muchas cosas, asi que resumiremos las mas esenciales.

1.  Agregar elementos

   ```python
   lista_supermercado.append('manjar')
   ```

2. Borrar elementos

   ```python
   lista_supermercado.remove('huevos')
   ```

3. Sacar y retornar elementos

   ```python
   curso_a = generacion_2017.pop(1) # Si no pongo un numero, por defecto es 0 asi que puedo poner otras cosas!
   ```

4. Sumar listas

   ``` python
   abuelos_paternos = ['Jose Manuel', 'Antonia']
   abuelos_maternos = ['Alfonso', 'Florencia']
   abuelos = abuelos_paternos + abuelos_maternos 
   # ['Jose Manuel', 'Antonia', 'Alfonso', 'Florencia']
   
   ```

5. Recorrerlas

   ```python
   def comprar(producto):
       print(producto, "comprado!")
   # Ciclos while
   while lista_super_mercado: # Equivalente a decir while len(lista_supermercado) > 0
       comprar(lista_supermercado.pop()) # Sacando los ultimos de la lista primero
   # Ciclos for
   for producto in lista_supermercado:
       comprar(producto)
       # Aqui no los saco de la lista, por lo que sigue igual. Y saco los primeros
       # de la lista primero.
       
   ```

6. Ordenarlas:

   ```python
   # Ordenamos por cantidad de alumnos, mayor cantidad primero
   generacion_2017.sort(key=len, reverse=True) # No es necesario poner ninguna de esas dos opciones, pero suele ser util.
   ```

7. Insertar Elementos

   ```python
   posicion = 3
   lista_supermercado.insert(posicion, "queso")
   ```

8. Slicing!

   Esto se refiere a extraer un pedazo en particular de la lista, sin alterarla.

   ```python
   a_y_b = generacion_2017[0:1]
   
   """
   Otros utiles:
   [a:-1] -> todos menos el ultimo
   [:5] -> desde el comienzo hasta el 5
   [6:] -> desde el 6 hasta el final
   [:] -> todo
   [::-1] -> todo invertido.
   """
   ```

   

