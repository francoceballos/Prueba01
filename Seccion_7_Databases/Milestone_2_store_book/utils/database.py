"""Lista de diccionarios - Se almacena datos en memoria
   Agregar opciones para guardar la lista creada y para leer la misma de un archivo JSON
"""
import json
from pathlib import Path

#Ejemplos
fileName = "json_book.json"
fileObj = Path(fileName)

books = []

#Crear Archivo. Verificar que existe
if(fileObj.is_file()):
    print("Leyendo Base de datos JSON existente")
    with open(fileName, 'r') as fd_json:
        books = json.load(fd_json)
else:
    print("No existe base de datos JSON")

def add_book(name, author):
    books.append({
        'name': name.title(),
        'author': author.title(),
        'read': False
    })


def list_total_books():
    print(f"\nTotal books {len(books)}. Book directory:\n")

    for book in books:
        read = 'YES' if book['read'] else 'NO' #Sentencia ternaria: resultado = valor_si if condicion else valor_no
        print(f"Name: {book['name']}")
        print(f"Author: {book['author']}")
        print(f"Read: {read}\n")


def list_name_books():

    print("\nList total book name:")
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"Book name: {book['name']} - read: {read}")


def book_read(name):

    for book in books:
        if name.lower() == book['name'].lower():
            book['read'] = True
            print(f"Book {name}, mark to read successfully")
            break
    else:
        print(f"Error, book name '{name}' not find")


def book_delete(name):

    global books #"""Le decimos al interprete que la variable books en la función es la variable global."""
                 #"""Evita crear una variable locar"""

    books = [book for book in books if book['name'].lower() != name.lower()]

    #"Mala practica" alterar lista a la vez que se esta recorriendo.
    #for book in books:
    #    if name == book['name']:
    #        books.remove(book)
    #        print("Book delete successfully")
    #        break
    #else:
    #    print(f"Error, book name '{name}' not find")

    list_name_books()


def save_json_file():
    if len(books) > 0:
        with open(fileName, 'w') as file:
            json.dump(books, file, indent=4)
    else:
        print("No hay datos para guardar")