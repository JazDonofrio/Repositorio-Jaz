# Ejercicio 3:

#   Pedirle al usuario que ingrese tres numeros.
#   Mostrarle por consola segun corresponda 
#   - los tres numeros son iguales 
#   - dos de los numeros son iguales 
#   - los tres numeros son distintos



# Solucion 1 facil


# numero1 = int(input("Ingrese un numero: "))
# numero2 = int(input("Ingrese un segundo numero: "))
# numero3 = int(input("Ingrese un tercer numero: "))

# if numero1 == numero2 == numero3:
#     print("Los tres numeros son iguales")
    
# elif numero1 == numero2:
#     print("Dos de los numeros son iguales")
    
# elif numero2 == numero3:
#     print("Dos de los numeros son iguales")
    
# elif numero1 == numero3:
#     print("Dos de los numeros son iguales")
    
# else:
#     print("Los tres numeros son distintos")



# Solucion 2
#Se crea una lista para no crear 3 variables distintas con el mismo contenido
lista = [input("Ingrese el primer número: "), input("Ingrese un segundo número: "), input("Ingrese un tercer número: ")]


numeros = set(lista)
#set colección que no posee órden

if len(numeros) == 1:
    print("Todos sus elementos son iguales")
elif len(numeros) == 2:
    print("2 elementos son iguales")
else:
    print("Todos los elementos son distintos")