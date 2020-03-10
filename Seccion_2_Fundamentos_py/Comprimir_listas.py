#! /usr/bin/python3.7

#Comprimir listas 

numbers = [0, 1, 2, 3, 4]
doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num * 2)

print(doubled_numbers)

# -- List comprehension --

numbers = [0, 1, 2, 3, 4]  # list(range(5)) is better
doubled_numbers = [num * 2 for num in numbers]  # num*2 variable a cargar en cada posición de la lista 
												# for recorre ciclos para generar la cantidad de indices en la lista  
# [num * 2 for num in range(5)] would be even better.

print(doubled_numbers)
# -- You can add anything to the new list --

numbers_five = [5 for _ in numbers]  # [5, 5, 5, 5, 5]  varibale ḿás ciclo para definir indice




friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]

print(age_strings)


# -- This includes things like --
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]

# That is particularly useful for working with user input.
# By turning everything to lowercase, it's less likely we'll miss a match.

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"I know {friend}!")


friends_upper = friend.upper()   #Método que transforma en mayusculas todas las letras de un string
print(friends_upper)

friends_title = friend.title()	#Método que trcapitalizeansforma cada primer letra de una cadena string
print(friends_title)





#Compresión de listas Cndicional; Incluir sentencia if dentro de la compresión

ages = [22, 35, 27, 21, 20]
odds = [n for n in ages if n % 2 == 1]

# -- with strings --

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "CharLIe", "michael"]

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.capitalize() for name in guests if name.lower() in friends_lower
]

print(present_friends)

# -- nested list comprehensions --
# Don't do this, because it's almost completely unreadable.
# Splitting things out into variables is better.

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

present_friends = [
    name.capitalize() for name in guests if name.lower() in [f.lower() for f in friends]
]



#Compresión de conjuntos 

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.capitalize() for name in present_friends}

present_friends = {name.capitalize() for name in friends_lower & guests_lower} #Condicional for; & debe estar en los dos conjuntos 

print(present_friends)

# Transforming data for easier consumption and processing is a very common task.
# Working with homogeneous data is really nice, but often you can't (e.g. when working with user input!).

# -- Dictionary comprehension --
# Works just like set comprehension, but you need to do key-value pairs.

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)


#Función zip, combina en tuplas los elementos de 2 o más vectores(listas o tuplas).
#La función zip debe ir acompañada de la conversión a tipo de dato que se quiere (list, dict)
#Siempre combina con la cantidad de datos(indices) de la menor lista. 

# While that is extremely useful when we have conditionals, sometimes we
# just want to create a dictionary out of two lists or tuples.
# That's when `zip` comes in handy!

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

# Remember how we can turn a list of lists or tuples into a dictionary?
# `zip(friends, time_since_seen)` returns something like [("Rolf", 3), ("Bob", 7)...]
# We then use `dict()` on that to get a dictionary.

friends_last_seen = dict(zip(friends, time_since_seen))
print(friends_last_seen)