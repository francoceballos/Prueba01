#! /usr/bin/python3.7

#Ejercicio 4 Loteria simple con diccionario y conjuntos.

lottery_numbers = {13, 21, 22, 5, 8}

print("Numbers lottery win: " + str(lottery_numbers))

"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [

	{"name": "Franco", "numbers":{7, 8, 17, 24, 25}},
	{"name": "Daniel", "numbers":{0, 13, 22, 27, 33}},
]

print("\nJugadores")
print("Nombre: " + players[0]["name"] + " " + str(players[0]["numbers"]))
print("Nombre: " + players[1]["name"] + " " + str(players[1]["numbers"]))

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

print("\nAcierto de Jugadores")

num_p1 = len(lottery_numbers.intersection(players[0]["numbers"]))
num_p2 = len(lottery_numbers.intersection(players[1]["numbers"]))

print (players[0]["name"] + " acertó " + str(num_p1) + " de los números ganadores")
print (players[1]["name"] + " acertó " + str(num_p2) + " de los números ganadores")