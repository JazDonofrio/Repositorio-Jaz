# Ejercicio 2:

#   Crear un menu de usuario con las siguientes opciones:
#     - 1 mostrar un numero
#     - 2 mostrar una frase
#     - 3 mostrar opción seleccionada
#     - 4 salir del sistema
#   pista: utilizar while - if elif else

menuUsuario = """
    --Menu de Usuario--
    
    1-> mostrar un numero.
    2-> mostrar una frase.
    3-> mostrar opción seleccionada.
    4-> salir del sistema.
"""
print(menuUsuario)

opcion = 0
while opcion != 4:
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print(1)
        break
    
    elif opcion == 2:
        print("Holaa")
        break
    
    elif opcion == 3:
        print(f"Usted selecciono la opcion:4 {opcion}")
        break
    
    elif opcion == 4:
        print("Saliendo del sistema...")
        
    else:
        print("Opcion incorrecta.")