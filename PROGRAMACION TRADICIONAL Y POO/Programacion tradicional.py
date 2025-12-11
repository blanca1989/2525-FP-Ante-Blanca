# --- Programación Tradicional: Clima Semanal ---

def obtener_temperaturas_diarias():
    """
    Solicita al usuario las temperaturas de 7 días.
    Retorna una lista de las temperaturas.
    """
    print("\n--- Modo: Programación Tradicional ---")
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias_semana:
        while True:
            try:
                # Se pide la temperatura en grados Celsius
                temp = float(input(f"Ingrese la temperatura del {dia} (°C): "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    return temperaturas


def calcular_promedio_semanal(datos_temperatura):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el valor promedio.
    """
    if not datos_temperatura:
        return 0

    suma = sum(datos_temperatura)
    promedio = suma / len(datos_temperatura)
    return promedio


def mostrar_resultado(temperaturas, promedio):
    """
    Muestra las temperaturas ingresadas y el promedio calculado.
    """
    print("\n--- Resumen Semanal (Tradicional) ---")
    print(f"Temperaturas registradas: {temperaturas}")
    print(f"El promedio semanal de la temperatura es: {promedio:.2f} °C")


# --- Lógica Principal (Estructura de la solución) ---
if __name__ == "__main__":
    temperaturas_semana = obtener_temperaturas_diarias()

    if temperaturas_semana:
        promedio_semanal = calcular_promedio_semanal(temperaturas_semana)
        mostrar_resultado(temperaturas_semana, promedio_semanal)