# Creando una matriz 3x3
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Accediendo a un elemento de la matriz (por ejemplo, el elemento en la fila 2, columna 3)
# Recuerda que los índices de las listas en Python comienzan en 0.
# El elemento en la fila 2 (índice 1) y columna 3 (índice 2) es 6.
fila = 1
columna = 2
elemento = matriz[fila][columna]
print(f"El elemento en la posición ({fila}, {columna}) es: {elemento}")

# Imprimiendo toda la matriz
print("\nLa matriz completa es:")
for fila in matriz:
    print(fila)

# Modificando un valor en la matriz (por ejemplo, el elemento en la posición 0,0)
matriz[0][0] = 10
print("\nLa matriz modificada es:")
for fila in matriz:
    print(fila)