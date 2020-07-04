# Define a PrimeGenerator class
class PrimeGenerator(object):
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.current = 1

    def __next__(self):
        while self.current <= self.stop:
            self.current += 1
            for x in range(2, self.current):
                if self.current % x == 0:  # if n is divisible by x, it means it's not a prime number.
                    break
            else:  # if n was not divisible by any x, it means it is a prime number.
                return self.current
        else:
            raise StopIteration()


#g = PrimeGenerator(17)


#Solucion ejercicio por Jose Salvatierra
class PrimeGenerator_alt:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:  # not prime
                    break
            else:  # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n  # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator


g = PrimeGenerator_alt(17)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
