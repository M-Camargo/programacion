import random
numeros = "1234"
mensaje_error = "Por favor, ingrese un comando valido"
error_lista = "Sino genero una lista, debe generar una para poder continuar."
lista_aleatoria = None

def generar_lista_aleatoria():
    lista = [random.randint(1, 100) for i in range(50)]
    return lista

def ordenar_lista(lista, criterio="AS"):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if (criterio == "AS" and lista[j] > lista[j+1]) or (criterio == "DES" and lista[j] < lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def buscar_numero_rango(lista,rango_min,rango_max):
    resultado=[]
    for num in lista:
        if rango_min <= num <= rango_max:
            resultado += [num]
    return resultado
            