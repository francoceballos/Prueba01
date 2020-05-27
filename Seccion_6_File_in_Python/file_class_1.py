print("Clase 1 Archivos en Python. Conceptos generales")

my_file = open('name.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('name.txt', 'a')
my_file_writing.write("\n")
my_file_writing.write(user_name)
my_file_writing.close()