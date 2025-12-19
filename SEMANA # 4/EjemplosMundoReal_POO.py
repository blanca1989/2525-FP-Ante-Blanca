# Usamos la misma estructura de clase que definiste
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregar_cantidad(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"📦 STOCK: Se han recibido {cantidad} unidades de '{self.nombre}'.")
        else:
            print("⚠️ Error: La cantidad a agregar debe ser mayor a 0.")

    def eliminar_cantidad(self, cantidad):
        if cantidad > 0 and self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"🛒 VENTA: Se han retirado {cantidad} unidades de '{self.nombre}'.")
        elif cantidad <= 0:
            print("⚠️ Error: La cantidad a eliminar debe ser mayor a 0.")
        else:
            print(f"❌ ERROR: Stock insuficiente de '{self.nombre}'. Solo quedan {self.cantidad}.")

    def mostrar_informacion(self):
        print("-" * 30)
        print(f"PRODUCTO: {self.nombre}")
        print(f"PRECIO:   ${self.precio:,.2f}")
        print(f"STOCK:    {self.cantidad} unidades")
        print("-" * 30)

# --- NUEVO EJEMPLO: TIENDA DE TECNOLOGÍA ---

# 1. Creamos los nuevos objetos (Instancias)
laptop = Producto("Laptop Gamer Pro", 1200.00, 5)
smartphone = Producto("iPhone 15", 999.00, 10)
audifonos = Producto("Sony WH-1000XM5", 350.50, 8)

# 2. Realizamos operaciones
print("--- INICIO DE OPERACIONES ---")

# Reponemos stock de laptops
laptop.agregar_cantidad(2)

# Vendemos varios iPhones
smartphone.eliminar_cantidad(4)

# Intentamos vender más audífonos de los que hay (esto probará tu validación)
audifonos.eliminar_cantidad(15)

# 3. Mostramos el estado final de los productos
print("\n--- RESUMEN DE INVENTARIO FINAL ---")
laptop.mostrar_informacion()
smartphone.mostrar_informacion()
audifonos.mostrar_informacion()