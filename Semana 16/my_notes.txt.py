
# Nombre del archivo que vamos a manipular
file_name = "my_notes.txt"

# ----------------------------------------------------
# 1. ESCRITURA DE ARCHIVO DE TEXTO usando write()
# ----------------------------------------------------

print(f"--- 1. Escribiendo notas personales en '{file_name}' ---")

# Usamos 'with open(..., 'w')' para abrir el archivo en modo escritura.
# El modo 'w' crea el archivo si no existe, o lo sobrescribe si ya existe.
# La instrucción 'with' se encarga de llamar automáticamente a close() al final.
try:
    with open(file_name, 'w', encoding='utf-8') as file:
        # Usamos write() para escribir cada línea. Es crucial incluir '\n' al final
        # de cada cadena para asegurar un salto de línea real en el archivo.
        # --- NUEVAS NOTAS AGREGADAS ---
        file.write("Nota 1: Cuando termines de almorzar me lavas los platos\n")
        file.write("Nota 2: Te deje la cena en el horno\n")
        file.write("Nota 3: Me llamas cuando llegues de viaje\n")
        print("✅ Escritura completada. Tres líneas de notas han sido guardadas.")
    # El archivo se cierra automáticamente aquí.

except IOError as e:
    print(f"❌ Error al escribir el archivo: {e}")


# ----------------------------------------------------
# 2. LECTURA DE ARCHIVO DE TEXTO línea por línea usando readline()
# ----------------------------------------------------

print(f"\n--- 2. Leyendo el contenido de '{file_name}' ---")

# Usamos 'with open(..., 'r')' para abrir el archivo en modo lectura.
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        line_count = 1
        while True:
            # readline() lee una sola línea del archivo, incluyendo el carácter '\n'.
            line = file.readline()

            # Si readline() devuelve una cadena vacía (''), hemos llegado al final del archivo (EOF).
            if not line:
                break

            # Muestra la línea en la consola. Usamos .strip() para eliminar el salto de línea
            # y cualquier espacio en blanco extra que pueda tener al principio o final.
            print(f"Línea {line_count}: {line.strip()}")
            line_count += 1

    print("✅ Lectura completada. Todas las líneas han sido mostradas.")
    # El archivo se cierra automáticamente aquí.

except FileNotFoundError:
    print(f"❌ Error: El archivo '{file_name}' no se encontró antes de la lectura.")
except IOError as e:
    print(f"❌ Error al leer el archivo: {e}")

# ----------------------------------------------------
# 3. LIMPIEZA (Opcional, pero útil para evitar archivos residuales)
# ----------------------------------------------------

# Puedes descomentar las siguientes líneas si deseas eliminar el archivo después de usarlo.
# try:
#     os.remove(file_name)
#     print(f"\nArchivo '{file_name}' eliminado.")
# except OSError as e:
#     print(f"\nError al eliminar el archivo: {e}")