def calcular_descuento(monto_total, porcentaje_descuento=0.10):
  """
  Calcula el descuento aplicando un porcentaje a un monto total de compra.

  Parámetros:
  - monto_total (float): El monto total de la compra.
  - porcentaje_descuento (float): El porcentaje de descuento a aplicar. Por defecto es 0.10 (10%).

  Retorna:
  - float: El monto del descuento calculado.
  """
  descuento = monto_total * porcentaje_descuento
  return descuento

# Llamada a la función con el porcentaje de descuento por defecto (10%)
monto_compra_1 = 200.0
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

print(f"Compra 1:")
print(f"Monto total: ${monto_compra_1:.2f}")
print(f"Descuento aplicado (10% por defecto): ${descuento_1:.2f}")
print(f"Monto final a pagar: ${monto_final_1:.2f}")

print("-" * 35)

# Llamada a la función con un porcentaje de descuento personalizado (25%)
monto_compra_2 = 500.0
porcentaje_personalizado = 0.25
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_personalizado)
monto_final_2 = monto_compra_2 - descuento_2

print(f"Compra 2:")
print(f"Monto total: ${monto_compra_2:.2f}")
print(f"Descuento aplicado (25%): ${descuento_2:.2f}")
print(f"Monto final a pagar: ${monto_final_2:.2f}")
