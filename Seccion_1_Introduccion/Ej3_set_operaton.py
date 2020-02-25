#! /usr/bin/python3.7

#Ejercicio 3 manejo de conjuntos 'set'

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
name_input = input("Enter name best friend: ")

# Add the name to the empty set
user_friends.add(name_input)
print(f"Set user_friends " + " , ".join(user_friends))

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
set_intersection_friends = user_friends.intersection(nearby_people)
print(f"Intersection set_intersection_friends {set_intersection_friends}")




# Mejorar impresión de conjuntos. 
# Imagine you've got all your friends in a list, and you want to print it out.
friends = ["Rolf", "Anne", "Charlie"]
print(f"My friends are {friends}.")

# Not the prettiest, so instead you can join your friends using a ",":
friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")