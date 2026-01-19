from modelos.empleado import Empleado

class Administrativo(Empleado):
    def __init__(self, nombre, sueldo_base, bono_puntualidad):
        # Herencia: aprovechamos el constructor de la clase padre
        super().__init__(nombre, sueldo_base)
        self.bono_puntualidad = bono_puntualidad

    def calcular_ingresos_totales(self):
        # Polimorfismo: Suma el bono al sueldo base
        return self.get_sueldo_base() + self.bono_puntualidad