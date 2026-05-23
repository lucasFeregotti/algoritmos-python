# Ordenamiento por Insercciòn

import time
import random
start_time = time.time() # Tiempo de inicio

def inserccion(lista):
    for j in range(1, len(lista)): 
        actual = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > actual:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = actual
    return lista                                
lista = [random.randint(0, 1000000) for _ in range(50000)]  # Genera una lista de 500,000 números aleatorios 

inserccion(lista) # Ordena la lista
resultado = inserccion(lista)
end_time = time.time() # Registra el tiempo al final
print(f"Tiempo de inicio: {start_time}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

#print (f"La lista desordenada:{lista}")         
#lista_ordenada = inserccion(lista)              
#print(f"La lista ordenada:{lista_ordenada}")                                      