#from utils import database - Opcion archivo JSON
#MAL - se debe generar un archivo book.json con extensi{on. Debe inicializarce con  json.dump([], file, indent=4)
from utils import database

#Definición de string de opciones
MENU_PROMPT = """\nBook storage directory application.\nEnter one option:\r
-'a' to add a new book\r
-'l' to list all books\r
-'r' to mark a book as read\r
-'d' to delete a book\r
-'s' to save store books in database
-'q' to quit\r

Your Choice: """


def prompt_add_book():
    name = input("\nEnter the book Name-Title: ")
    author = input("Enter the book author: ")

    database.add_book(name, author)


def list_books():
    database.list_total_books()


def prompt_read_book():
    database.list_name_books()
    name_read = input("\nEnter the book name to mark as read: ")
    database.book_read(name_read)


def prompt_delete_book():
    database.list_name_books()
    name_delete = input("\nEnter the book name to delete: ")
    database.book_delete(name_delete)


def save_store_file():
    database.save_json_file()


#diccionario con oppciones - donde cada clave: valor es opcion: funcion
user_options = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book,
    's': save_store_file
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection] #hace una variable igual a una funcion
            selected_function()                         #llama a la funcion con los parentesis
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


if __name__ == '__main__':
    menu()