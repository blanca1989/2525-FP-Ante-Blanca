"""
Funcionalidad: Este programa gestiona el registro básico de un producto en un inventario,
calculando el valor total del stock y verificando si requiere reabastecimiento.
"""

# --- Definición de Funciones (Uso de snake_case) ---
def calcular_valor_inventario(cantidad, precio_unitario):
    """
    Calcula el valor monetario total de las existencias de un producto. [cite: 101]
    """
    return cantidad * precio_unitario

def verificar_reabastecimiento(cantidad_actual, limite_minimo):
    """
    Determina si es necesario comprar más stock (retorna un valor Booleano). [cite: 35]
    """
    return cantidad_actual < limite_minimo

# --- Bloque Principal del Programa ---

# 1. Identificadores y Tipos de Datos Primitivos [cite: 24, 57]
nombre_producto = "Cámara DSLR"      # String: Secuencia de caracteres [cite: 29]
precio_por_unidad = 450.75           # Float: Número con decimales [cite: 32]
cantidad_en_stock = 8                # Integer: Número sin decimales [cite: 25]
es_producto_importado = True         # Boolean: Valor de verdad [cite: 35]

# 2. Identificadores Descriptivos para Constantes
STOCK_MINIMO_PERMITIDO = 10

# 3. Procesamiento de Datos
# Se calcula el valor total usando la función definida [cite: 84]
total_monetario = calcular_valor_inventario(cantidad_en_stock, precio_por_unidad)

# Se verifica el estado de reabastecimiento [cite: 101]
necesita_compra = verificar_reabastecimiento(cantidad_en_stock, STOCK_MINIMO_PERMITIDO)

# 4. Salida de Información (Uso de Identificadores Claros) [cite: 103, 104]
print(f"--- Ficha del Producto: {nombre_producto} ---")
print(f"Precio Unitario: ${precio_por_unidad}")
print(f"Cantidad Disponible: {cantidad_en_stock}")
print(f"¿Es Importado?: {es_producto_importado}")
print(f"Valor Total del Inventario: ${total_monetario}")
print(f"¿Requiere Reabastecimiento?: {necesita_compra}")

# Ejemplo de impacto de mala nomenclatura (evitado según diapositivas) [cite: 106, 107]
# En lugar de usar 'cnt' o 'p', usamos 'cantidad_en_stock' y 'precio_por_unidad'.