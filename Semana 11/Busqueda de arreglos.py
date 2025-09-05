def buscar_valor_en_matriz(matriz, valor_a_buscar):
    """
    Busca un valor específico dentro de una matriz bidimensional.

    Args:
        matriz (list): La matriz bidimensional donde buscar.
        valor_a_buscar: El valor que se desea encontrar.

    Returns:
        tuple or None: Una tupla (fila, columna) si el valor se encuentra,
                       o None si el valor no está en la matriz.
    """
    for fila_indice, fila in enumerate(matriz):
        for columna_indice, valor in enumerate(fila):
            if valor == valor_a_buscar:
                return (fila_indice, columna_indice)
    return None

# Definimos una matriz bidimensional de 3x3
mi_matriz = [
    [1, 5, 3],
    [8, 2, 7],
    [4, 9, 6]
]

# Valor que queremos buscar
valor_buscado = 7

# Llamamos a la función de búsqueda
posicion = buscar_valor_en_matriz(mi_matriz, valor_buscado)

# Mostramos el resultado
print(f"Matriz:")
for fila in mi_matriz:
    print(fila)
print("-" * 20) # Separador para mayor claridad

if posicion:
    fila_encontrada, columna_encontrada = posicion
    print(f"¡El valor {valor_buscado} se encontró en la matriz!")
    print(f"Está en la fila {fila_encontrada} y la columna {columna_encontrada}.")
else:
    print(f"El valor {valor_buscado} NO se encontró en la matriz.")

# Probamos con un valor que no está en la matriz
valor_no_existente = 10
posicion_no_existente = buscar_valor_en_matriz(mi_matriz, valor_no_existente)

print("-" * 20) # Separador

if posicion_no_existente:
    fila_encontrada, columna_encontrada = posicion_no_existente
    print(f"¡El valor {valor_no_existente} se encontró en la matriz!")
    print(f"Está en la fila {fila_encontrada} y la columna {columna_encontrada}.")
else:
    print(f"El valor {valor_no_existente} NO se encontró en la matriz.")