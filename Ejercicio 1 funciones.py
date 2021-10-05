""" => Ejercicio 1:
    Realiza una función separar(lista) que tome una lista de números enteros 
    y devuelva dos listas la primera con los números pares 
    y la segunda con los números impares.

    Ej:
        pares, impares = separar([6,5,2,1,7])
        print(pares)
        print(impares)

        >>> [2, 6]
        >>> [1, 5, 7]
 """

numeros_enteros = [1, 2, 3, 4, 5, 6, 7, 8]

# definicion de la funcion "separar"
def separar(lista):
    impares = list(filter(lambda x: x % 2 != 0, lista))
    pares = list(filter(lambda x: x % 2 == 0, lista))
    
    return (pares, impares)

pares, impares = separar(numeros_enteros)
print(pares)
print(impares)