#Busqueda de números primos
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:  # if n is divisible by x, it means it's not a prime number.
            #print(f"{n} equals {x} * {n//x}")
            break
    else:  # if n was not divisible by any x, it means it is a prime number.
        print(f"{n} is a prime number.")


"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""
def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:  # if n is divisible by x, it means it's not a prime number.
                break
        else:  # if n was not divisible by any x, it means it is a prime number.
            yield n


g = prime_generator(10)

print(f"prime_generator {next(g)} is a prime number.")
print(f"prime_generator {next(g)} is a prime number.")
print(f"prime_generator {next(g)} is a prime number.")
print(f"prime_generator {next(g)} is a prime number.")