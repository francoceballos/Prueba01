"""Se almacena datos en Archivo CSV"""
from pathlib import Path

#Ejemplos
fileName = "store_book.txt"
fileObj = Path(fileName)


#Crear Archivo. Verificar que existe
if(fileObj.is_file()):
    print("Leyendo Base de datos CSV existente")
else:
    print("Creando Base de datos CSV")
    with open(fileName, "a") as fd_books:
        fd_books.write("Name,Author,Read\n")


def add_book(name, author):
    with open(fileName, "a") as fd_books:
        fd_books.write(f"{name.title()},{author.title()},NO\n")


def list_total_books():
    print(f"\nBook directory:\n")

    with open(fileName, "r") as fd_books:
        list_books = fd_books.readlines()

    for book in list_books[1:]:
        name, author, read = book.strip().split(',')
        print(f"Book Name: {name}")
        print(f"Author: {author}")
        print(f"Read: {read}\n")


def book_read(name_read):
    with open(fileName, "r") as fd_books:
        list_books = fd_books.readlines()

    aux=0
    list_key= list_books[0].strip().split(',')  #Strip elimina el caracter \n
    books = []

    for book in list_books[1:]:
        list = book.strip().split(',')

        if list[0].lower() == name_read.lower():
            list[2]='YES'
            aux=1

        books.append(dict(zip(list_key, list)))

    if aux==1:
        _save_new_list_books(books)
    else:
        print(f"Error, book name '{name_read}' not find")


def book_delete(name_delete):
    with open(fileName, "r") as fd_books:
        list_books = fd_books.readlines()

    aux=0
    list_key= list_books[0].strip().split(',')  #Strip elimina el caracter \n
    books = []

    for book in list_books[1:]:
        list = book.strip().split(',')

        if list[0].lower() == name_delete.lower():
            aux=1
        else:
            books.append(dict(zip(list_key, list)))

    if aux==1:
        _save_new_list_books(books)
    else:
        print(f"Error, book name '{name_delete}' not find")


#Las funciones con '_' al inicio son funciones internas de la libreria
def _save_new_list_books(New_book):
    with open(fileName, "w") as fd_books:
        fd_books.write("Name,Author,Read\n")

        for book in New_book:
            fd_books.write(f"{book['Name']},{book['Author']},{book['Read']}\n")