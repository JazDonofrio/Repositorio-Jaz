# Ejercicio 1

#   Escribir un programa que solicite:
#     - nombre
#     - apellido
#     - edad 
#     - numero de telefono
#     - email

#   Mostrarlos por consola. 

'''
nombre = input("Ingrese su nombre: ")
print("Su nombre es: " + nombre)

apellido = input("Ingrese su apellido: ")
print("Su apellido es: " + apellido)

edad = input("Ingrese su edad: ")
print("Edad: " + edad)

num_Tel = int(input("Ingrese su numero de telefono: "))
print("Su numero es: " + num_Tel)

email = input("Ingrese su email: ")
print("Su Email es: " + email) '''

#-----------------------------------------------------------------------------------------

# Ejercicio 2:

# Escribir un programa que solicite tres numeros y muestre por consola el promedio.

'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo numero: "))
num3 = int(input("Ingrese un tercer numero: "))

suma = num1 + num2 + num3
promedio = (suma/3)

print(promedio)
'''
#-----------------------------------------------------------------------------------------


# Ejercicio 3: 

#   - Crear un programa que le pida ingresar 4 colores. 
#   - Mostrarlos por consola.
#   - Agregarle un color desde el programa, mostrarle al usuario el nuevo color agregado. 
#   - imprimir la cantidad de colores. 
#   - Pedirle al usuario que ingrese un nuevo color e insertarlo en la posición 1. Imprimir el    listado de colores.
#   - Mostrale por consola al usuario el color que se encuentra en la posicion 3.
#   - Eliminar el ultimo color de la lista.
#   - Pedirle al usuario que ingrese un color para ver si existe en la lista, imprimir por consola True o False. 
#   - Limpiar la lista e imprimirla por consola.

col1 = input("Ingrese un color: ")
col2 = input("Ingrese otro color : ")
col3 = input("Ingrese un tercer color: ")

print(col1)
print(col2)
print(col3)

#-lista de los colores creada para poder insertar un elemento nuevo
colores = [col1, col2, col3]
print(colores)

#-Se agrega un color nuevo
colNuevo = input("Ingrese un nuevo color: ")
colores.append(colNuevo)
print(colores)

#-cantidad de elementos
print("La cantidad de colores es: ")
print(len(colores))

#- Pedirle al usuario que ingrese un nuevo color e insertarlo en la posición 1. Imprimir el    listado de colores.
colNuevo = input("Ingrese un nuevo color: ")
colores.insert(1, colNuevo) 
print(colores)

#- Mostrale por consola al usuario el color que se encuentra en la posicion 3.
print("El color en la 3ra posicion es: " + colores[3])

#- Eliminar el ultimo color de la lista.
colores.pop()
print(colores)

# Pedirle al usuario que ingrese un color para ver si existe en la lista, imprimir por consola True o False.
buscarColor = input("Color existente: ")
print(buscarColor in colores)

# Limpiar la lista e imprimirla por consola.
colores.clear()
print(colores)
    

