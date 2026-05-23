# Merge Sort | Ordenamiento por mezcla.
# Diseño de divide y vencerás. Es un algoritmo recursivo que tiene una complejidad de O(n log(n)).

def MergeSort(left_arr, right_arr):
    arr_resultado = []
    
    # Mostrar las listas izquierda y derecha antes de fusionarlas
    print(f"Sublista Izquierda (left): {left_arr}")
    print(f"Sublista Derecha (right): {right_arr}")
    print()
    
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_resultado.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_resultado.append(left_arr[0])
            left_arr.pop(0)

    # Añadir los elementos restantes de 'left' (si los hay)
    while len(left_arr) > 0:
        arr_resultado.append(left_arr[0])
        left_arr.pop(0)

    # Añadir los elementos restantes de 'right' (si los hay)
    while len(right_arr) > 0:
        arr_resultado.append(right_arr[0])
        right_arr.pop(0)

    return arr_resultado

arr = [4, 6, 2, 5, 8, 9, 5, 10]
print(f"Arreglo original: {arr}\n")
# Dividimos el arreglo en dos partes ordenadas
left_arr = sorted(arr[:len(arr)//2])
right_arr = sorted(arr[len(arr)//2:])
arr_merge = MergeSort(left_arr, right_arr)
print(f"Lista fusionada: {arr_merge}")