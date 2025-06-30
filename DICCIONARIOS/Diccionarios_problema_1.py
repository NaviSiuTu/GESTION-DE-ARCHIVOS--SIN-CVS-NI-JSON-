def imprimir_valores_asc(dic):
    valores = list(dic.values())
    valores.sort()
    print("Valores ordenados:", valores)

# Ejemplo:
d = {"a": 4, "b": 2, "c": 7}
imprimir_valores_asc(d)
