# 1. Crear el diccionario inicial con la información proporcionada
informacion_personal = {
    "nombre": "Blanca Cecilia Ante",
    "edad": 36,  # Usamos el número entero para la edad
    "ciudad": "Shushufindi",
    # La clave "profesion" se debe agregar después, pero la pondremos inicialmente para la estructura inicial requerida
    "profesion": "Tecnóloga"
}

print(f"Diccionario Inicial: {informacion_personal}")
print("-" * 30)

## Acceder y Modificar Valores:

# Acceder al valor asociado con la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual (Acceso): {ciudad_actual}")

# Modificar el valor de "ciudad" por una ciudad diferente (ej. "Quito")
informacion_personal["ciudad"] = "Quito"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")
print("-" * 30)

# La clave "profesion" ya existe por la creación inicial, pero si hubiese que agregarla:
# Agrega una nueva clave-valor para la "profesion" (Si no existiera)
# informacion_personal["profesion"] = "Tecnóloga"

## Verificar Existencia de Claves:

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número de teléfono ficticio
    informacion_personal["telefono"] = "0989611243"
    print("La clave 'telefono' no existía y fue agregada.")
else:
    print("La clave 'telefono' ya existía.")
print(f"Diccionario después de verificar/agregar 'telefono': {informacion_personal}")
print("-" * 30)

## Eliminar una Clave:

# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]
    print("Clave 'edad' eliminada.")
else:
    print("La clave 'edad' no se encontró para eliminar.")
print("-" * 30)

## Imprimir el Diccionario Final:

# Imprimir el diccionario resultante después de realizar todas las operaciones
print("✅ Diccionario Final después de todas las operaciones:")
print(informacion_personal)

