def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = round((start + end)/ 2)

    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)

    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)

    else:
        return mid

"""
Ordenación por inserción que usa timsort si el tamaño del arreglo es pequeño o si el tamaño de la "carrera" es pequeño
"""
def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array

def merge(left, right):
    """
  Toma dos listas ordenadas y devuelve una sola lista ordenada comparando los
    elementos de uno en uno.
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def timsort(the_array):
    runs, sorted_runs = [], []
    length = len(the_array)
    new_run = [the_array[0]]

    # para cada i en el rango de 1 a la longitud del arreglo
    for i in range(1, length):
        # si i está al final de la lista
        if i == length - 1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        # si el i-ésimo elemento del arreglo es menor que el anterior
        if the_array[i] < the_array[i-1]:
            # si new_run se establece en Ninguno (NULL)
            if not new_run:
                runs.append([the_array[i]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        # de lo contrario si es igual o mayor 
        else:
            new_run.append(the_array[i])

    # para cada elemento en las ejecuciones, agrégalo usando la ordenación por inserción
    for item in runs:
        sorted_runs.append(insertion_sort(item))
    
    # por cada ejecución en sorted_runs, fusionarlos

    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    print(sorted_array)


timsort([2, 3, 1, 5, 6, 7, 50 , 100, 600, 6, 21])