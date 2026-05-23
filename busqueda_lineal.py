# Busqueda Lineal (Secuencial)

'''import random
import time
start_time = time.time()  # Tiempo de inicio

def busqueda_lineal(lista,objetivo):       # O(1)
    for i in range (len(lista)):           # O(n)
        if lista[i]== objetivo:            # O(n)
            return i                       # O(n)
    return "no esta en la lista"           # O(1) 
    |                                      # 3n + 2 = O(n)
lista = [random.randint(0, 1000000) for _ in range(50000)]  # Genera una lista de 500,000 números aleatorios                 

objetivo = -1
resultado = busqueda_lineal(lista, objetivo)
end_time = time.time() # Registra el tiempo al final

print(f"Tiempo de inicio: {start_time}")
print(f"Elemento encontrado en la posición: {resultado}")
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

objetivo = 4                                   
#resultado = busqueda_lineal(lista,objetivo) 
#print("Indice del objetivo:", resultado)  '''

def suma_numeros(lista):          # O(1)
      total = 0                   # O(1)
      for numero in lista:        # O(n)
            total += numero                    # O(n)
      return total                                  # O(1)
			 # 2n + 3 = O(n)