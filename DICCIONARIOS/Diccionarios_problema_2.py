def verificar_inclusion(dic1, dic2):
    for clave, valor in dic1.items():
        if clave not in dic2 or dic2[clave] != valor:
            return False
    return True

# Ejemplo:
d1 = {"a": 1, "b": 2}
d2 = {"a": 1, "b": 2, "c": 3}
print(verificar_inclusion(d1, d2))  # True
