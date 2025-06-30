# Función que imprime los valores de un diccionario en orden ascendente
def imprimir_valores_asc(dic):
    # Convierte los valores del diccionario en una lista
    valores = list(dic.values())

    # Ordena la lista de valores de menor a mayor
    valores.sort()

    # Imprime los valores ya ordenados
    print("Valores ordenados:", valores)

# Ejemplo de uso de la función
d = {"a": 4, "b": 2, "c": 7}  # Diccionario con claves y valores numéricos
imprimir_valores_asc(d)      # Llama a la función para imprimir los valores ordenados

