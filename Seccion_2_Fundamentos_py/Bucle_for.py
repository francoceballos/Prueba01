#! /usr/bin/python3.7

#Bucle for en python 

# -- Repeat once for each element of an iterable --
friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)

# But Python comes with a function for that already, which is even more powerful than just doing that.
for index in range(10):     #rango de 1 a 10 contando de 1
    print(index)

for index in range(5, 10):  #rango de 5 a 10 contando de 1
    print(index)

for index in range(2, 20, 3): #rango de 2 a 20 contando de 3
    print(index)


# -- Using each value while you iterate --
students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:  # student is a variable used for iteration
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}.")

# When to use?
# When you want to repeat something a defined number of times.
# For example, once for each element of a list, or even just "10 times"



#Destructurar en Python: asignar valores de tuplas o listas a variables 

# Given a tuple or list:
currencies = 0.8, 1.2
usd, eur = currencies

# -- Destructuring in a loop --
# If you've got a list of lists, such as friend names and ages, you can destructure
# in a loop like this:
friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
for name, age in friends:  # for friend in friends first
    print(f"{name} is {age} years old.")


# -- Destructurar Diccionario: acceder al dic con bucle for y asignar a variables
friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name in friend_ages:
    print(name)

for age in friend_ages.values():
    print(age)

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")



#Sentencias "break and continue"  igual que en lenguaje c

# -- break --
# Exits out of the loop, so that no more iterations occur.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")

# -- continue --
# Terminates the current iteration and moves onto the next one.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue

    print(f"This car is {status}.")
    print("Shipping new car to customer!")