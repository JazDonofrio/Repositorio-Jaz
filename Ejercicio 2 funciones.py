""" => Ejercicio 2:
    Realiza una función que tome como parametro una frase y devuelva una 
    lista de palabras en mayuscula. 

      Ej: 
        mi_frase = "Este sabado tenemos el ultimo encuentro online"

        palabras = convertir(mi_frase)

        print(palabras)

        >>> ["ESTE", "SABADO", "TENEMOS", "EL", "ULTIMO", "ENCUENTRO", "ONLINE"]

   """
    
def frase_mayuscula(frase):
    frase = "Hola mundo"
    palabras = list(frase.upper())
  
    return list(palabras)
  
palabras, frase = frase_mayuscula()

print(palabras)