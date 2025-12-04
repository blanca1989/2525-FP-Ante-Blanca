from abc import ABC, abstractmethod


# La clase ABC (Abstract Base Class) permite definir clases abstractas
class CuentaBancaria(ABC):
    """Clase base abstracta para cualquier cuenta bancaria."""

    def __init__(self, numero_cuenta, titular):
        # Inicializa las propiedades esenciales (el detalle interno del saldo se mantiene oculto)
        self._numero_cuenta = numero_cuenta
        self._titular = titular
        self._saldo = 0.0  # Saldo inicial

    def depositar(self, cantidad):
        """Método concreto: Permite depositar dinero en la cuenta."""
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de ${cantidad:.2f} realizado.")
        else:
            print("Error: La cantidad a depositar debe ser positiva.")

    @abstractmethod
    def retirar(self, cantidad):
        """Método abstracto: Debe ser implementado por las subclases."""
        pass

    # Método para obtener el saldo (esencial para el usuario)
    def obtener_saldo(self):
        """Muestra el saldo actual de la cuenta."""
        print(f"Saldo actual en la cuenta {self._numero_cuenta}: ${self._saldo:.2f}")
        return self._saldo

# Ejemplo de Abstracción: El usuario solo ve los métodos públicos: depositar, retirar y obtener_saldo.
# [Image of a black box with two labeled inputs (Deposit, Withdraw) and one labeled output (Current Balance),
# symbolizing the abstraction principle where internal complexity is hidden.]


# Continuando con el ejemplo:
class CuentaCorriente(CuentaBancaria):
    """Implementación de una Cuenta Corriente."""

    def __init__(self, numero_cuenta, titular, limite_sobregiro=100.0):
        super().__init__(numero_cuenta, titular)
        self._limite_sobregiro = limite_sobregiro

    def retirar(self, cantidad):
        """Implementación del método abstracto 'retirar'."""
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser positiva.")
            return

        # Encapsulación: El acceso a _saldo solo se realiza a través de este método.
        # Esto asegura que se apliquen reglas de negocio (como el límite de sobregiro).
        if self._saldo - cantidad >= -self._limite_sobregiro:
            self._saldo -= cantidad
            print(f"Retiro de ${cantidad:.2f} realizado.")
        else:
            print("Error: Fondos insuficientes y límite de sobregiro excedido.")


# Ejemplo de Encapsulación:
print("--- Demostración de Encapsulación ---")
cuenta_c = CuentaCorriente("CC001", "Ana García")
cuenta_c.depositar(200.0)
# Intentar acceder al saldo directamente (Python lo permite, pero es una mala práctica):
print(f"Acceso 'directo' (desaconsejado) a _saldo: {cuenta_c._saldo}")
# Modificación controlada a través del método 'retirar':
cuenta_c.retirar(250.0)
cuenta_c.obtener_saldo()


# Continuando con el ejemplo:
class CuentaAhorro(CuentaBancaria):  # Hereda de CuentaBancaria
    """Implementación de una Cuenta de Ahorro."""

    def __init__(self, numero_cuenta, titular, tasa_interes):
        super().__init__(numero_cuenta, titular)  # Llamada al constructor del padre
        self._tasa_interes = tasa_interes

    def calcular_intereses(self):
        """Método propio: Calcula y deposita intereses."""
        intereses = self._saldo * self._tasa_interes
        self.depositar(intereses)  # Reutiliza el método depositar del padre
        print(f"Intereses de ${intereses:.2f} calculados y añadidos.")

    def retirar(self, cantidad):
        """Implementación del método abstracto 'retirar' (específica para Ahorro)."""
        if cantidad <= 0:
            print("Error: La cantidad a retirar debe ser positiva.")
            return

        # Regla de Ahorro: No permite sobregiro.
        if self._saldo >= cantidad:
            self._saldo -= cantidad
            print(f"Retiro de ${cantidad:.2f} realizado de la cuenta de ahorro.")
        else:
            print("Error: Fondos insuficientes en la cuenta de ahorro.")


# Ejemplo de Herencia:
print("\n--- Demostración de Herencia ---")
cuenta_a = CuentaAhorro("AH100", "Javier Pérez", 0.05)
cuenta_a.depositar(500.0)  # Método heredado de CuentaBancaria
cuenta_a.calcular_intereses()  # Método propio de CuentaAhorro
cuenta_a.obtener_saldo()

# Continuación del ejemplo con Polimorfismo:

def realizar_retiro(cuenta, monto):
    """Función que acepta cualquier objeto que sea una CuentaBancaria."""
    print(f"\nProcesando retiro de ${monto:.2f}...")
    # Polimorfismo en acción: Se llama al método 'retirar' del objeto,
    # el cual puede ser de tipo CuentaCorriente o CuentaAhorro.
    cuenta.retirar(monto)
    cuenta.obtener_saldo()

# 1. Crear instancias de las diferentes clases
c_corriente = CuentaCorriente("CC002", "Elena Ruiz", 50.0)
c_ahorro = CuentaAhorro("AH101", "Pedro López", 0.02)

c_corriente.depositar(100.0)
c_ahorro.depositar(100.0)

print("\n--- Demostración de Polimorfismo ---")

# 2. Llamar a la misma función con diferentes objetos
# El objeto de CuentaCorriente (c_corriente) usa su propia lógica de 'retirar' (con sobregiro)
realizar_retiro(c_corriente, 120.0)

# El objeto de CuentaAhorro (c_ahorro) usa su propia lógica de 'retirar' (sin sobregiro)
realizar_retiro(c_ahorro, 120.0)

# La diferencia en el resultado demuestra el polimorfismo.