class ClimaSemanal:
    """
    Clase para gestionar y calcular el promedio semanal de la temperatura.
    Aplica el concepto de Encapsulamiento.
    """

    def __init__(self, ciudad="Latacunga"):
        """
        Constructor de la clase. Inicializa los atributos.
        """
        self.ciudad = ciudad
        # Encapsulamiento: Se usa un atributo privado para almacenar las temperaturas
        self.__temperaturas = []

    def cargar_datos(self, datos_temperatura):
        """
        Método para ingresar los datos diarios de la temperatura.
        """
        if isinstance(datos_temperatura, list):
            self.__temperaturas = datos_temperatura
            print(f"✅ Datos cargados exitosamente para {self.ciudad}.")
        else:
            print("❌ Error: Los datos deben ser proporcionados como una lista de números.")

    def obtener_promedio(self):
        """
        Método para calcular el promedio semanal de las temperaturas.
        """
        if not self.__temperaturas:
            return 0.0  # Devuelve 0 si no hay datos

        # El cálculo es responsabilidad de este método dentro de la clase
        suma = sum(self.__temperaturas)
        cantidad_dias = len(self.__temperaturas)
        promedio = suma / cantidad_dias

        return promedio

    def mostrar_informe(self):
        """
        Método que muestra un resumen de los datos y el resultado.
        """
        promedio = self.obtener_promedio()

        print("\n--- 🌡️ INFORME DE CLIMA SEMANAL ---")
        print(f"Ciudad: **{self.ciudad}**")
        print(f"Temperaturas registradas (°C): {self.__temperaturas}")
        print(f"Total de días: {len(self.__temperaturas)}")
        print("-----------------------------------")
        print(f"**PROMEDIO SEMANAL: {promedio:.2f} °C**")
        print("-----------------------------------\n")


# --- Ejecución Principal ---

# 1. Definición de los datos reales para Latacunga
datos_latacunga = [12, 13, 14, 12, 11, 13, 14]

# 2. Creación de un Objeto (Instancia de la clase)
clima_latacunga = ClimaSemanal("Latacunga")

# 3. Utilizar métodos para cargar los datos en el objeto
clima_latacunga.cargar_datos(datos_latacunga)

# 4. Utilizar un método para obtener y mostrar el resultado
clima_latacunga.mostrar_informe()