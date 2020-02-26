#! /usr/bin/python3.7

# Condicional if,elif y else
# Loop while

friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
else:
    print("Hello, stranger!")

# -- Checking whether the if statement will run --
print(bool(user_name == friend))  # if this is True, the if statement will run

# -- Using the `in` keyword --
friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")



# Principio ciclos while

user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")

print("We stopped running.")
# When to use?
# When you want to repeat something an undefined number of times.
# For example, until a user tells you to stop or some other condition becomes False.


# Ejercicio 5 Crear menu 
print("\n\nEjercicio 5 Menu.\n")
# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.
choose_user = input("choose one of two options p/q: ")

# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = ...

while choose_user != "q":
	
	if choose_user == "p":
		print("Hello")

	choose_user = input("choose one of two options p/q: ")

print("Fin")
# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
# Inside the loop, have an if statement that checks if the user typed 'p'.
#    If they did, print "Hello"
# Still inside the loop, ask the user again
# user_input = ...