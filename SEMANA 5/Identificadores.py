"""
Funcionalidad: Este programa gestiona el registro de un producto en un inventario.
Utiliza identificadores descriptivos para representar el estado del stock
y calcular costos, cumpliendo con las convenciones de Python.
"""

# --- Funciones (Definidas con snake_case) ---
# Un buen identificador describe el propósito del elemento [cite: 61]
def calcular_costo_total_inventario(cantidad_unidades, precio_por_unidad):
    """Calcula el valor total multiplicando cantidad por precio."""
    return cantidad_unidades * precio_por_unidad

def evaluar_estado_disponibilidad(cantidad_actual):
    """Determina si hay existencias disponibles (Boolean)."""
    # Los identificadores deben ser descriptivos como 'longitud_lista' [cite: 101]
    existencia_minima = 1
    return cantidad_actual >= existencia_minima

# --- Bloque Principal ---

# 1. String (Cadena de texto): Secuencias de caracteres [cite: 29]
nombre_del_articulo = "Computadora Portátil"

# 2. Integer (Entero): Números sin decimales [cite: 25]
cantidad_en_bodega = 15

# 3. Float (Flotante): Números con decimales [cite: 32]
precio_venta_publico = 850.99

# 4. Boolean (Booleano): Valores de verdad [cite: 35]
es_producto_nuevo = True

# --- Procesamiento usando Identificadores Claros ---
# Evitamos nombres como 'cnt' o 'p' que llevan a confusión [cite: 106, 107]
costo_total_acumulado = calcular_costo_total_inventario(cantidad_en_bodega, precio_venta_publico)
esta_disponible_para_venta = evaluar_estado_disponibilidad(cantidad_en_bodega)

# --- Salida de Datos ---
print(f"Producto Registrado: {nombre_del_articulo}")
print(f"Cantidad en Stock: {cantidad_en_bodega}")
print(f"Precio Unitario: ${precio_venta_publico}")
print(f"¿El producto es nuevo?: {es_producto_nuevo}")
print(f"Valor Total del Stock: ${costo_total_acumulado}")
print(f"¿Disponible para despacho?: {esta_disponible_para_venta}")