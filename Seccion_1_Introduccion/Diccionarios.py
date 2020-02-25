#! /usr/bin/python3.7

#Diccionarios en Python
#d={key:valor} las claves son unicas  

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])  # 24
# friend_ages["Bob"]  ERROR

# -- Adding a new key to the dictionary --

friend_ages["Bob"] = 20
print(friend_ages)  # {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}

# -- Modifying existing keys --

friend_ages["Rolf"] = 25

print(friend_ages)  # {'Rolf': 25, 'Adam': 30, 'Anne': 27, 'Bob': 20}

# -- Lists of dictionaries --
# Imagine you have a program that stores information about your friends.
# This is the perfect place to use a list of dictionaries.
# That way you can store multiple pieces of data about each friend, all in a single variable.

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

description = "{} is {} years old."
print(description.format(friends[0]["name"], friends[0]["age"]))

add_dic = {"name": "Franco", "age": 28}

friends.append(add_dic)

print(friends)

# You can turn a list of lists or tuples into a dictionary:

friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)