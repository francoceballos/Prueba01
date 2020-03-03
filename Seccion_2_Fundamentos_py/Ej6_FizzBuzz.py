#! /usr/bin/python3.7

#Ejercicio 6.

# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

print("Ejercicio 6 FizzBuzz")

for x in range(1, 101):
	mul_3 = x%3
	mul_5 = x%5

	if( (mul_3 or mul_5) == 0):
		print("FizzBuzz")
	elif(mul_3 == 0):
		print("Fizz")
	elif(mul_5 == 0):
		print("Buzz")
	else:
		print(x)

print("Fin")