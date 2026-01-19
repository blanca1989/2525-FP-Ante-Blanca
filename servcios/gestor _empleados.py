class CalculadorNomina:
    @staticmethod
    def imprimir_recibo(empleado):
        # Gracias al polimorfismo, no importa si es Vendedor o Administrativo,
        # ambos responden al método 'calcular_ingresos_totales'
        total = empleado.calcular_ingresos_totales()
        print(f"RECIBO DE PAGO")
        print(f"Personal: {empleado.nombre}")
        print(f"Total a Depositar: ${total:.2f}")
        print("-" * 20)