# Busqueda por Selección

import time
import random
start_time = time.time() # Tiempo de inicio

def seleccion(lista):
    for i in range(0, len(lista)):      
        minimo = i  
        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]: 
                minimo = j 
        aux = lista[i] 
        lista[i] = lista[minimo]
        lista[minimo] = aux     
lista = [random.randint(0, 1000000) for _ in range(50000)]  # Genera una lista de 500,000 números aleatorios   

seleccion(lista) # Ordena la lista
resultado = seleccion(lista)
end_time = time.time() # Registra el tiempo al final
print(f"Tiempo de inicio: {start_time}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

'''print (f"La lista desordenada:{lista}")         
lista_ordenada = seleccion(lista)               
print(f"La lista ordenada:{lista_ordenada}")'''