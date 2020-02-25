#! /usr/bin/python3.7

#Listas en Python 

friends = ["Rolf", "Bob", "Anne"]

print(friends[0])  # This is called a subscript
print(friends[1])

# -- Length of a list --

friends = ["Rolf", "Anne"]
print(len(friends))  # 2

# -- Lists inside lists --
# As mentioned earlier, you can put anything inside a list—and that includes other lists.

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends[0][1])  # 24
print(friends[1][0])  # Bob

# -- Adding to a list --

friends = ["Rolf", "Bob", "Anne"]
friends.append("Jen")

print(friends)  # ["Rolf", "Bob", "Anne", "Jen"]

# -- Removing from a list --

friends.remove("Bob")

print(friends)  # ["Rolf", "Anne", "Jen"]

# Remember if you have a list of lists, for example, you still need the entire thing you want to remove:

friends = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]

friends.remove(["Bob", 30])


#Tuplas ; Tipo de lista fijas No pueden modificarse 
# -- Defining tuples --

short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")
not_a_tuple = "Rolf"

# -- Adding to a tuple --

friends = ("Rolf", "Bob", "Anne")
friends.append("Jen")  # ERROR!



#Conjuntos; listas Mutable, sin orden, no contiene duplicados.

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}
# -- Adding to a set --
art_friends.add("Jen")
print(art_friends)

# -- No duplicate items --
art_friends.add("Jen")
print(art_friends)  # Same as before, "Jen" was not added twice

# -- Removing from a set --
science_friends.remove("Charlie")
print(science_friends)

#Operaciones con conjuntos 

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

# -- Difference --
# Gives you members that are in one set but not the other.
art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)

# -- Symmetric difference --
# Gives you those members that aren't in both sets
# Order doesn't matter with symmetric_difference
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

# -- Intersection --
# Gives you members of both sets
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# -- Union --
# Gives you all members of all sets, but of course without duplicates
all_friends = art_friends.union(science_friends)
print(all_friends)