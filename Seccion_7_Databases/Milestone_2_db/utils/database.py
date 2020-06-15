
from sqlite3 import DatabaseError
from utils.db_context_manager import ClassDBMetod
from pathlib import Path

#Ejemplos
fileName = "store_book.db"
fileObj = Path(fileName)


#Crear Archivo. Verificar que existe
if(fileObj.is_file()):
    pass
else:
    try:
        with ClassDBMetod(fileName) as fd_books:
            fd_books.execute("CREATE TABLE books (Title VARCHAR(100) PRIMARY KEY, Author VARCHAR(100), "
                             "Read INTEGER default 0)")
    except DatabaseError:
        print(f"Error DatabaseError {DatabaseError}")


def _readdbtodic():
    try:
        with ClassDBMetod(fileName) as fd_books:
            books_tuples=fd_books.execute("SELECT * FROM books").fetchall()
    except DatabaseError:
        print(f"Error DatabaseError {DatabaseError}")
        return 0

    keys = ("name", "author", "read")   #Claves para crear la lista de diccionarios
    books_list = []                     #Lista de diccionarios
    for book in books_tuples:
        dic = dict(zip(keys,book))
        books_list.append(dic)

    return books_list


def _find_book(name):
    list_books = _readdbtodic()
    ret = False
    for book in list_books:
        if name == book['name']:
            ret = True

    return ret


def add_book(name, author):
    try:
        with ClassDBMetod(fileName) as fd_books:
            fd_books.execute("insert INTO books (Title, Author) Values (?, ?)", (name.title(), author.title()))

    except DatabaseError:
        print(f"Error DatabaseError {DatabaseError}")


def list_total_books():
    print("\nBook directory in data base:")

    list_books = _readdbtodic()

    for book in list_books:
        print(f"Book Name: {book['name']}, Author: {book['author']}, Read: {'YES' if book['read'] else 'NO'}")


def book_read(name_read):
    try:
        if _find_book(name_read.title()) == True:
            with ClassDBMetod(fileName) as fd_books:
                fd_books.execute("UPDATE books SET Read = 1 WHERE Title = ?", (name_read.title(),))  #Debe ser una tupla
        else:
            print(f"ERROR No se encuentra titulo: {name_read.title()}")

    except DatabaseError:
        print(f"Error DatabaseError {DatabaseError}")


def book_delete(name_delete):
    try:
        if _find_book(name_delete.title()) == True:
            with ClassDBMetod(fileName) as fd_books:
                fd_books.execute("DELETE FROM books WHERE Title = ?", (name_delete.title(),))  #Debe ser una tupla
        else:
            print(f"ERROR No se encuentra titulo: {name_delete.title()}")

    except DatabaseError:
        print(f"Error DatabaseError {DatabaseError}")