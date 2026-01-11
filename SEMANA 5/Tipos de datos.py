"""
Funcionalidad: Este programa gestiona el registro de un producto, calculando
el valor total del stock y verificando si cumple con el mínimo requerido.
"""

# --- Constantes (Convención: MAYÚSCULAS) ---
STOCK_MINIMO = 5  # [cite: 87]

# --- Funciones (Convención: snake_case) ---
def calcular_total_stock(cantidad, precio): # [cite: 83, 84, 99]
    """Calcula el valor monetario total del inventario."""
    return cantidad * precio

# --- Variables y Tipos de Datos (Identificadores Descriptivos) ---

# 1. String (Cadena de Texto): Secuencias de caracteres [cite: 29, 46]
nombre_producto = "Monitor Gamer 24"

# 2. Integer (Entero): Números sin decimales [cite: 25]
cantidad_disponible = 12

# 3. Float (Flotante): Números con decimales [cite: 32]
precio_unitario = 185.50

# 4. Boolean (Booleano): Valores de verdad (True/False) [cite: 35, 38]
esta_en_oferta = False

# --- Procesamiento de Datos ---

# Uso de identificadores para claridad del código [cite: 60, 61, 103]
valor_total_inventario = calcular_total_stock(cantidad_disponible, precio_unitario)

# Verificación lógica (Tipo Booleano)
necesita_pedido = cantidad_disponible < STOCK_MINIMO

# --- Salida de Resultados ---
print(f"--- REGISTRO DE PRODUCTO ---")
print(f"Producto: {nombre_producto}")
print(f"Stock actual: {cantidad_disponible} unidades")
print(f"Precio: ${precio_unitario}")
print(f"¿Tiene descuento activo?: {esta_en_oferta}")
print(f"Valor total en almacén: ${valor_total_inventario}")
print(f"¿Se debe realizar pedido?: {necesita_pedido}")