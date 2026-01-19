class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        # Encapsulación: Sueldo protegido con __
        self.__sueldo_base = sueldo_base

    def get_sueldo_base(self):
        return self.__sueldo_base

    def calcular_ingresos_totales(self):
        # Método base que será sobrescrito (Polimorfismo)
        return self.__sueldo_base

    def __str__(self):
        return f"Empleado: {self.nombre}"