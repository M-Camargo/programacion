from Fun_parcial import *

while True:
    print("MENU DE OPCIONES: ")
    print("1: Generar una lista de numeros aleatorios")
    print("2: Ordenar la lista de numeros generados")
    print("3: Obtener el numero maximo y minimo")
    print("4: Para salir del programa")
        
    opcion = input("Ingrese una opcion a realizar: ")
    if opcion not in numeros:
        print(f"ERROR!! {opcion} es un comando invalido. {mensaje_error}")
        continue
        
    if opcion == "1":
            lista_aleatoria = generar_lista_aleatoria()
            print(f"La lista generada aleatoriamente es:{lista_aleatoria}")
        
    elif opcion == "2":
        if lista_aleatoria == None:
            print(error_lista)
            continue
        
        if lista_aleatoria:
            criterio = input("Ingrese la manera que desea ordenar la lista AS (Ascendente) o DES (Descendente): ").upper()
            if criterio != "AS" and criterio != "DES":
                print(mensaje_error)
            else:
                lista_aleatoria_ordenada = ordenar_lista(lista_aleatoria, criterio=criterio)
                print(f"La lista ordenada es: {lista_aleatoria_ordenada}")
        else:
            print(error_lista)
    
    elif opcion == "3":
        if lista_aleatoria == None:
            print(error_lista)
            continue
        
        if lista_aleatoria:
            rango_min = int(input("Ingrese el valor mínimo del rango: "))
            rango_max = int(input("Ingrese el valor máximo del rango: "))
            numeros_en_rango = buscar_numero_rango(lista_aleatoria, rango_min, rango_max)
            if numeros_en_rango:
                print(f"NUMERO MAXIMO ENCONTRADO: {max(numeros_en_rango)}")
                print(f"NUMERO MINIMO ENCONTRADO: {min(numeros_en_rango)}")
            else:
                print(f"No hay números dentro del rango [{rango_min}-{rango_max}]")
        else:
            print(error_lista)
        
    elif opcion == "4":
        print("Saliendo del programa...")
        break
   