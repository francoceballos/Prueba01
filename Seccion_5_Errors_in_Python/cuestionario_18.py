def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)				# n solo existe en al ambito de try, Cuando sucede el error n no existe no se crea
    except ValueError:
        print('Your input was invalid.')
    finally:
        n_square = n ** 2			#Si try se ejecuta n existe. Si sale error n no existe. Por tanto ek error es n**2 que no existe 
        return n_square



def power_of_two2():
	user_input = input('Please enter a number: ')
	try:
		n = float(user_input)
	except ValueError:
		print('Your input was invalid. Using default value 0')
		n = 0
	else:
		n_square = n ** 2
		return n_square


def power_of_two3():
	user_input = input('Please enter a number: ')
	try:
		n = float(user_input)
	except ValueError:
		print('Your input was invalid. Using default value 0')
		n = 0
	else:
		n_square = n ** 2
	finally:	
		return n_square


def power_of_two4():
	user_input = input('Please enter a number: ')
	try:
		n = float(user_input)
	except ValueError:
		print('Your input was invalid. Using default value 0')
		return 0					#NO IMPORTA MENOR PRIORIDAD 
	else:
		n_square = n ** 2
	finally:	
		return n_square				#sIEMPRE SE EJECUTA NO IMPORTA RETURN ANTERIOR

prueba=power_of_two4()
print(f"{prueba}")
prueba2=power_of_two4()
print(f"{prueba2}")