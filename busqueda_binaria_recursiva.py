def busqueda_binaria_recursiva(lista, inicio, fin, valor):
    if inicio > fin:
        return -1 # Caso base: el valor no se encuentra
    
    medio = (inicio + fin) // 2  

    if lista[medio] == valor: #  valor encontrado
        return medio
    
    elif lista[medio] > valor:  #El valor buscado es menor que el elemento del medio, por lo tanto se descarta la mitad derecha y se busca en la izquierda 
    
        return busqueda_binaria_recursiva(lista, inicio, medio -1, valor)   # mitad izquierda
    else: 
        return busqueda_binaria_recursiva(lista, medio + 1, fin, valor)  # mitad derecha


''' la lista debe estar previamente ordenada '''    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
valor_a_buscar = 3
resultado = busqueda_binaria_recursiva(lista, 0, len(lista) - 1, valor_a_buscar)  

if resultado != -1:
    print(f"El valor {valor_a_buscar} se encuentra en el índice {resultado}.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la lista.")

'''
def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: multiplica la base por el resultado de la potencia con el exponente reducido en 1
    return base * potencia(base, exponente - 1)

# Ejemplo de uso
resultado = potencia(2, 3)  # Calcula 2^3
print(f"2 elevado a 3 es: {resultado}")
    '''