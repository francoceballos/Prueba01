"""
Iterator: Un objeto tipo iterator es un objeto que representa un flujo de datos, el cual puede ser recorrido en un
proceso iterativo, como un bucle for, dentro de una función map o filter, en la creación de una list comprehension o
generador, o en una comparación in.
Todo objeto iterator contiene implementado un método next que es llamado en cada iteración devolviendo los
sucesivos elementos del flujo de datos cada vez. El flujo de datos del objeto no tiene por qué estar guardado en memoria,
sino que puede ser generado en tiempo real en cada iteración.
El objeto iterator guarda un estado interno para saber cuál fue el último elemento obtenido.
Así, en la siguiente llamada a __next__(), se obtendrá el siguiente elemento correcto.
Cuando ya no quedan más elementos en el flujo de datos del iterator, la función __next__() lanza StopIteration.
El estado interno no se reinicia automáticamente al llegar al final del flujo o al empezar a recorrerlo de nuevo.
Es decir, sólo se puede recorrer una vez.
Además, tiene implementado el método __iter__() que devuelve el propio objeto iterator.
"""
"""
Iterable: Un objeto iterable es un tipo de objeto que devuelve sus elementos de uno en uno cada vez.
 Tiene implementado alguno de estos dos métodos:

    __iter__() que devuelve un objeto iterator a partir de este objeto iterable.
    __getitem__() que accede a cada uno de los elementos para índices empezando desde 0.

Un objeto iterable no tiene por qué tener definido el método __next__(), 
En cambio, al tener la obligación de implementar el método __iter__() o __getitem__(), 
puede ser utilizado como argumento para la función iter() y así recorrer el iterator resultante.
"""
"""
Los generadores son una forma sencilla y potente de iterador. Un generador es una función especial que produce secuencias
 completas de resultados en lugar de ofrecer un único valor. En apariencia es como una función típica pero en lugar de 
 devolver los valores con return lo hace con la declaración yield. Hay que precisar que el término generador define tanto 
 a la propia función como al resultado que produce.
"""

"""
The below is class which implements `__next__`as if it was a function using the `yield` keyword:
"""


class FirstHundredGenerator(object):
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


gen = FirstHundredGenerator()
next(gen)  # 0
next(gen)  # 1

"""
Notice how the object, with its property, remembers what the value of `self.number` is at all points in time.

This object is called in Python a generator because every time the next number is available not because 
it’s in a sequence, but because it is generated from its current state (in this case, by adding 1 to `self.number`).

All objects that have this `__next__` method are called iterators. All generators are iterators, but not the other way round.

For example, you could have an iterator on which you can call `next()`, but that doesn’t generate its values. Instead, 
it could take them from a list or from a database.

*Important*: iterators are objects which have a `__next__` method.

Here’s an example of an iterator which is not a generator:
"""


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current
        else:
            raise StopIteration()


"""
As you can see it’s returning numbers that are not being generated; instead they’re being returned from a list.

If we run this code though, we will get an error:

"""

#sum(FirstHundredGenerator())  # comment this line out to run the rest of the file.

"""
Similarly if we run this code:
"""

#for i in FirstHundredGenerator():
#    print(i)

"""
And that’s because in Python, an `iterator` and an `iterable` are different things. You can iterate over an `iterable`.
The iterator is used to get the next value (either from a sequence or generated values).

> You can iterate over iterables, not over iterators.
"""