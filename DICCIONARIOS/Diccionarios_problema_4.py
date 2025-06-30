# Función que imprime los nombres y apellidos de personas dentro de un rango de edad
def imprimir_personas_por_edad(lista_personas, edad_min, edad_max):
    # Recorre cada diccionario (persona) dentro de la lista
    for persona in lista_personas:
        # Verifica si la edad está dentro del rango especificado (inclusive)
        if edad_min <= persona["edad"] <= edad_max:
            # Imprime el nombre y apellido de la persona si cumple con la condición
            print(persona["nombres"], persona["apellidos"])

# Ejemplo de uso:

# Lista de diccionarios, donde cada uno representa una persona
personas = [
    {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
    {"nombres": "Ana María", "apellidos": "Gómez Pérez", "edad": 25},
    {"nombres": "Luis Alberto", "apellidos": "Ramírez Díaz", "edad": 33}
]

# Llama la función para mostrar las personas entre 20 y 40 años
imprimir_personas_por_edad(personas, 20, 40)
