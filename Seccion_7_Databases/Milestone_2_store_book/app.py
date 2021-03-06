#from utils import database
from utils import databasefile

#Definición de string de opciones
MENU_PROMPT = """\nBook storage directory application.\nEnter one option:\r
-'a' to add a new book\r
-'l' to list all books\r
-'r' to mark a book as read\r
-'d' to delete a book\r
-'q' to quit\r

Your Choice: """


def prompt_add_book():
    name = input("\nEnter the book Name-Title: ")
    author = input("Enter the book author: ")

    #database.add_book(name, author)
    databasefile.add_book(name, author)


def list_books():
    databasefile.list_total_books()


def prompt_read_book():
    #database.list_name_books()
    name_read = input("\nEnter the book name to mark as read: ")
    #database.book_read(name_read)
    databasefile.book_read(name_read)


def prompt_delete_book():
    #database.list_name_books()
    name_delete = input("\nEnter the book name to delete: ")
    #database.book_delete(name_delete)
    databasefile.book_delete(name_delete)


#diccionario con oppciones - donde cada clave: valor es opcion: funcion
user_options = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book
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
