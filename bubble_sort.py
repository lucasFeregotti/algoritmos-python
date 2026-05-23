# Ordenamiento por Burbuja

import time
import random
start_time = time.time() # Tiempo de inicio

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0,n-i-1):                            
            if lista[j] > lista[j+1]:                       
                lista[j],lista[j+1]=lista[j+1],lista[j]                                                  
lista = [random.randint(0, 1000000) for _ in range(500)]  # Genera una lista de 500,000 números aleatorios                                        

#lista_ordenada = bubble_sort(lista)                          
#print("lista ordenada:",lista_ordenada)   

bubble_sort(lista) # Ordena la lista
resultado = bubble_sort(lista)
end_time = time.time() # Registra el tiempo al final

print(f"Tiempo de inicio: {start_time}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")                                                     