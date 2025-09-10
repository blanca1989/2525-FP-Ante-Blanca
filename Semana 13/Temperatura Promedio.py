def calcular_promedio_ciudad(datos_temperatura, nombre_ciudad):
    """
    Calcula la temperatura promedio de una ciudad específica
    a lo largo de todas las semanas y días registrados.

    Args:
        datos_temperatura (list): Una lista 3D que contiene los datos de temperatura.
                                   La estructura es: [ciudad][semana][día].
                                   Cada día es un diccionario con 'day' y 'temp'.
        nombre_ciudad (str): El nombre de la ciudad para la cual calcular el promedio.

    Returns:
        float: La temperatura promedio de la ciudad especificada, o None si la ciudad no se encuentra.
    """
    ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]  # Mapeo de índice a nombre de ciudad

    try:
        ciudad_idx = ciudades.index(nombre_ciudad)
    except ValueError:
        print(f"Error: La ciudad '{nombre_ciudad}' no se encontró en los datos.")
        return None

    ciudad_seleccionada = datos_temperatura[ciudad_idx]

    todas_las_temperaturas = []
    for semana in ciudad_seleccionada:
        for dia_datos in semana:
            todas_las_temperaturas.append(dia_datos["temp"])

    if not todas_las_temperaturas:  # Si no hay datos de temperatura para esa ciudad
        return 0.0

    promedio_total = sum(todas_las_temperaturas) / len(todas_las_temperaturas)
    return promedio_total


# Usando la matriz de temperaturas proporcionada
temperaturas = [
    [  # Ciudad 1
        [  # Semana 1
            {"day": "Lunes", "temp": 78}, {"day": "Martes", "temp": 80}, {"day": "Miércoles", "temp": 82},
            {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 85}, {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 76}, {"day": "Martes", "temp": 79}, {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 77}, {"day": "Martes", "temp": 81}, {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 82}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 95}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 75}, {"day": "Martes", "temp": 78}, {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 84}, {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [  # Ciudad 2
        [  # Semana 1
            {"day": "Lunes", "temp": 62}, {"day": "Martes", "temp": 64}, {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 73}, {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 63}, {"day": "Martes", "temp": 66}, {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72}, {"day": "Viernes", "temp": 75}, {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 61}, {"day": "Martes", "temp": 65}, {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 72}, {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 64}, {"day": "Martes", "temp": 67}, {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71}, {"day": "Viernes", "temp": 74}, {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"day": "Lunes", "temp": 90}, {"day": "Martes", "temp": 92}, {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 89}, {"day": "Martes", "temp": 91}, {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 91}, {"day": "Martes", "temp": 93}, {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 92}, {"day": "Viernes", "temp": 89}, {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 83}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 88}, {"day": "Martes", "temp": 90}, {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 89}, {"day": "Viernes", "temp": 86}, {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]

# Ejemplo de uso de la función:
promedio_ciudad1 = calcular_promedio_ciudad(temperaturas, "Ciudad 1")
if promedio_ciudad1 is not None:
    print(f"El promedio general de temperaturas para Ciudad 1 es: {promedio_ciudad1:.2f} grados.")

promedio_ciudad2 = calcular_promedio_ciudad(temperaturas, "Ciudad 2")
if promedio_ciudad2 is not None:
    print(f"El promedio general de temperaturas para Ciudad 2 es: {promedio_ciudad2:.2f} grados.")

promedio_ciudad3 = calcular_promedio_ciudad(temperaturas, "Ciudad 3")
if promedio_ciudad3 is not None:
    print(f"El promedio general de temperaturas para Ciudad 3 es: {promedio_ciudad3:.2f} grados.")

# Ejemplo con una ciudad que no existe
promedio_ciudad_inexistente = calcular_promedio_ciudad(temperaturas, "Ciudad 4")