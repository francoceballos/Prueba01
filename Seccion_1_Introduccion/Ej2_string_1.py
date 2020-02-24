#! /usr/bin/python3.7

#Pruebas debug manejo de strings python 3.6
multiline = """Hello, world.
My name is Franco.
Welcome to my program.
"""
print(multiline)

friend_name = "Rolf"
goodbye = "hello, {name2} - Goodbye, {name}!"
goodbye_rolf = goodbye.format(name2="Franco", name="Fran")
print(goodbye_rolf)



description = "{} is {} years old.{}, {age}"
print(description.format("Bob", 30,"franco", age=29))

name = input("Introdusca su nombre: ")
print("Hola, " + name)


meses = int(input("Introdusca su edad en años: ")) * 12
print(f"Su edad en meses es: {meses}")


#Ejercicio 2: Comunicacion con el usuario por consola

# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!
name = input("Introdusca su nombre: ")
print("Hello, " + name)

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
meses = int(input("Introdusca su edad en años: ")) * 12
print("Su edad en meses es: " + str(meses))
