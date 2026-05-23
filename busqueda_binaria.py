# Ordenamiento por Busqueda Binaria

import time
import random
start_time = time.time() # Tiempo de inicio

def busqueda_binaria(lista, objetivo):         
    inicio = 0                          
    final = len(lista)-1                
    while inicio <= final:              
        medio = (inicio + final) //2    
        if lista[medio] == objetivo:    
            return "está en la lista"                     
        elif lista[medio] < objetivo:   
            inicio = medio + 1          
        elif lista[medio] > objetivo:   
            final = medio - 1           
    return "no está en la lista"        
lista = [random.randint(0, 100) for _ in range(50000)]  # Genera una lista de 500,000 números aleatorios                 

  
objetivo = -1
lista.sort()  

resultado = busqueda_binaria(lista, objetivo)
end_time = time.time() # Registra el tiempo al final

print(f"Elemento encontrado en la posición: {resultado}")
print(f"Tiempo de inicio: {start_time}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")


'''lista = [54,26,93,17,77,31,44,55,20]                        
objetivo = 21                                                  
lista.sort()                                                                                                  
print("El número", objetivo, busqueda_binaria(lista, objetivo))   '''                                              