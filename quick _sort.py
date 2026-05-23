# Ordenamiento rápido - Quicksort

def quick_sort(lista):
  if len(lista) <= 1:
    return lista
  menores,pivote, mayores = particionar(lista)
  return quick_sort(menores) + [pivote] + quick_sort(mayores)

def particionar(lista):  
  # Pivote el de la derecha
  pivote = lista[len(lista) // 2]
  menores = []
  mayores = []
  for elemento in lista:
    if elemento < pivote:
      menores.append(elemento)
    elif elemento > pivote:
      mayores.append(elemento)
  return menores, pivote, mayores

# Lista de ejemplo
lista = [4, 6, 2, 5, 8, 9, 5, 10]
print("Lista original:", lista)
print("Lista ordenada:", quick_sort(lista))