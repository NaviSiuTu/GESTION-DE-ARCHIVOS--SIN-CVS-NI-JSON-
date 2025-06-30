# Función que verifica si todos los pares clave-valor de dic1 están contenidos en dic2
def verificar_inclusion(dic1, dic2):
    # Recorre cada clave y valor del primer diccionario
    for clave, valor in dic1.items():
        # Si la clave no está en dic2 o el valor no coincide, retorna False
        if clave not in dic2 or dic2[clave] != valor:
            return False
    # Si pasa todas las verificaciones, retorna True
    return True

# Ejemplo de uso:
d1 = {"a": 1, "b": 2}           # Primer diccionario
d2 = {"a": 1, "b": 2, "c": 3}   # Segundo diccionario (contiene a d1)
print(verificar_inclusion(d1, d2))  # True porque todos los pares de d1 están en d2

