#! /usr/bin/python3.7

# En los bucles, puede agregar una sentencia `else`. Esto solo se ejecuta si el ciclo no encuentra un `break` o un error.
# Eso significa que, si el ciclo se completa con éxito, se ejecutará la parte `else`.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")
else:
    print("All cars built successfully. No faulty cars!")


# Remove the "faulty" and you'll see the `else` part starts running.
# Link: https://blog.tecladocode.com/python-snippet-1-more-uses-for-else/


#Busqueda de números primos

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # if n is divisible by x, it means it's not a prime number.
            print(f"{n} equals {x} * {n//x}")
            break
    else:  # if n was not divisible by any x, it means it is a prime number.
        print(f"{n} is a prime number.")



#Obtener porción de lista, se obtinen nueva lista parseada
		#	0		1			2		3		4
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
		#	-5			-4		-3		-2		-1

print(friends[2:4])		#No incluye dirección final  ['Anna', 'Bob']
print(friends[2:])		#Sin nada sì incluye final ['Anna', 'Bob', 'Jen']
print(friends[:4])		#['Rolf', 'Charlie', 'Anna', 'Bob']
print(friends[:])		#['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen']
print(friends[-3:])		#['Anna', 'Bob', 'Jen']
print(friends[:-2])		#['Rolf', 'Charlie', 'Anna']
print(friends[-3:-1])	#['Anna', 'Bob']
print(friends[-5:2])	#['Rolf', 'Charlie']

# You can slice with tuples and strings as well.
# More advanced content in our slices blog posts!

# https://blog.tecladocode.com/python-slices/
# https://blog.tecladocode.com/python-slices-part-2/