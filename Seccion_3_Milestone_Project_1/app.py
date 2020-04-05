#Titulo inicial para el Proyecto 1
print("Project 1: 'Movie storage directory application'")

#Definición de string de opciones
MENU_PROMPT = """\nMovie storage directory application.\nEnter one option:\r
'a' to add a movie\r
'l' to see your movies\r
'f' to find a movie by title\r
'q' to quit\r
Your Choice: """

#Variable principal donde se almacenan, imprimen y buscan las peliculas.
movies = []

def add_movie():

    title = input("\nEnter the movie Title: ")
    director = input("Enter the movie Director: ")
    year = input("Enter the movie release Year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movie():

    print("\nMovie directory in format 'Title - Director - Year':")
    description = "{} - {} - {}."

    for movie in movies:
        print(description.format(movie["title"], movie["director"], movie["year"]))

    print("\n")


def find_movie():

    title_f = input("\nEnter the movie 'Title' to find in directory: ")

    for movie in movies:
        if(title_f == movie['title']):
            print(f"The movie finded correctly. Title: {movie['title']}, Director: {movie['director']} and Year: {movie['year']}")
            break
    else:
        print(f"The movie title {title_f} not found in directory")

    print("\n")

#Se podria hacer una unica función para imprimir los datos de algun modo particular.
#Así se usaria tal funcion en varios lugares

# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        add_movie()
    elif selection == "l":
        list_movie()
    elif selection == "f":
        find_movie()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)



#--- Otra forma de hacer menu --
#diccionario con oppciones - donde cada clave: valor es opcion: funcion
user_options = {
    "a": add_movie,
    "l": list_movie,
    "f": find_movie
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

menu()

