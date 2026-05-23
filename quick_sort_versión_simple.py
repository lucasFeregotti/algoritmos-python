# Ordenamiento rápido - Quicksort - Versión simple

lista = [8, 12, 3, 11, 5, 9, 10, 4, 15, 7]  # Definimos una lista con números desordenados.
print(lista) # Imprimimos la lista original antes de ordenarla.
print()

# Definimos la función 'particionado' que divide la lista en dos sublistas según el pivote.
def particionado(lista): 
    pivote = lista[0]  # El primer elemento de la lista se toma como pivote.

    # Inicializamos dos listas vacías para los elementos menores y mayores que el pivote.
    menores = []
    mayores = []
    for i in range(1, len(lista)): # Recorremos la lista desde el segundo elemento hasta el final.
        if lista[i] < pivote:   # Si el elemento actual es menor que el pivote, lo agregamos a la lista de 'menores'.
            menores.append(lista[i])
        else:
            mayores.append(lista[i])  # Si el elemento es mayor o igual al pivote, lo agregamos a la lista de 'mayores'.
            
    return menores, pivote, mayores  # Retornamos las dos listas (menores y mayores) junto con el pivote
e
def quicksort(lista):
    if len(lista) < 2:  # Caso base: si la lista tiene menos de 2 elementos, ya está ordenada.
        return lista
    menores, pivote, mayores = particionado(lista)  # Llamamos a 'particionado' para obtener las sublistas menores, el pivote y las mayores.

    return quicksort(menores) + [pivote] + quicksort(mayores)   # Recursivamente ordenamos las sublistas menores y mayores, y las concatenamos con el pivote en el medio.
print(quicksort(lista)) # Imprimimos la lista ordenada llamando a la función 'quicksort' sobre la lista original.'''
