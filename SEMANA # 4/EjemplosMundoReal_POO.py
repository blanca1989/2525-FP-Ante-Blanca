# --- CLASE PRODUCTO (Tu código original) ---
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregar_cantidad(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"📚 INGRESO: Se han recibido {cantidad} copias de '{self.nombre}'.")
        else:
            print("La cantidad a agregar debe ser mayor que 0.")

    def eliminar_cantidad(self, cantidad):
        if cantidad > 0 and self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"📖 VENTA: Se han vendido {cantidad} copias de '{self.nombre}'.")
        elif cantidad <= 0:
            print("La cantidad a eliminar debe ser mayor que 0.")
        else:
            print(f"⚠️ AGOTADO: No hay suficientes copias de '{self.nombre}' para vender {cantidad}.")

    def mostrar_informacion(self):
        print(f"Título: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.cantidad}")

# --- EJECUCIÓN CON EJEMPLO DE LIBRERÍA ---

# 1. Creamos los libros (Instancias)
libro1 = Producto("Cien años de soledad", 25.50, 5)
libro2 = Producto("Don Quijote de la Mancha", 18.00, 3)
libro3 = Producto("El Principito", 12.99, 20)

print("--- REGISTRO DE MOVIMIENTOS ---")

# Llega un nuevo pedido para reponer el Quijote
libro2.agregar_cantidad(7)

# Vendemos 2 copias de Cien años de soledad
libro1.eliminar_cantidad(2)

# Intentamos vender 25 copias de El Principito (Supera el stock)
libro3.eliminar_cantidad(25)

print("\n--- INVENTARIO ACTUALIZADO ---")
# Mostramos la información de todos los libros
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro3.mostrar_informacion()