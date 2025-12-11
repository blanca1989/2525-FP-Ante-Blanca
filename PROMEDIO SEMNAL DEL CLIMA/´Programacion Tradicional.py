# 1. Función para la entrada o definición de los datos diarios (temperaturas en °C)
def obtener_datos_diarios():
    """Define las temperaturas diarias de la semana para Latacunga."""
    # Los datos proporcionados son: 12, 13, 14, 12, 11, 13, 14 °C
    temperaturas = [12, 13, 14, 12, 11, 13, 14]
    return temperaturas

# 2. Función para el cálculo del promedio semanal
def calcular_promedio_semanal(temperaturas):
    """Calcula el promedio de una lista de temperaturas."""
    if not temperaturas:
        return 0  # Devuelve 0 si la lista está vacía para evitar división por cero

    suma_temperaturas = sum(temperaturas)
    cantidad_dias = len(temperaturas)

    # Fórmula del promedio: Suma de valores / Cantidad de valores
    promedio = suma_temperaturas / cantidad_dias
    return promedio

# 3. Función para mostrar el resultado
def mostrar_resultado(promedio):
    """Muestra el promedio semanal de la temperatura."""
    print("---")
    print(f"El promedio semanal de la temperatura en Latacunga es: **{promedio:.2f} °C**")
    print(f"(El resultado se muestra redondeado a dos decimales)")
    print("---")

# Ejecución principal del programa
if __name__ == "__main__":
    # A. Obtener las temperaturas
    temp_semanales = obtener_datos_diarios()

    # B. Calcular el promedio
    promedio_final = calcular_promedio_semanal(temp_semanales)

    # C. Mostrar el resultado
    mostrar_resultado(promedio_final)