def imprimir_personas_por_edad(lista_personas, edad_min, edad_max):
    for persona in lista_personas:
        if edad_min <= persona["edad"] <= edad_max:
            print(persona["nombres"], persona["apellidos"])

# Ejemplo:
personas = [
    {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
    {"nombres": "Ana María", "apellidos": "Gómez Pérez", "edad": 25},
    {"nombres": "Luis Alberto", "apellidos": "Ramírez Díaz", "edad": 33}
]

imprimir_personas_por_edad(personas, 20, 40)
